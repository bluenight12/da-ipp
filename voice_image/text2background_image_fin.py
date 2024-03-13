# 필요한 라이브러리 및 모듈 임포트
import gc
from pathlib import Path
import torch
import openvino as ov
import numpy as np
from transformers import CLIPTokenizer
from diffusers.schedulers import DDIMScheduler, LMSDiscreteScheduler, PNDMScheduler
from openvino.runtime import Model
import PIL
from PIL import Image
import cv2
import inspect
from typing import List, Optional, Union, Dict
from diffusers.pipelines.pipeline_utils import DiffusionPipeline
from diffusers import StableDiffusionPipeline
from pathlib import Path
import ipywidgets as widgets
from IPython.display import display
import random

class ModelConverter:
    def __init__(self):
        self.dtype_mapping = {
            torch.float32: ov.Type.f32,
            torch.float64: ov.Type.f64
        }
        pipe = StableDiffusionPipeline.from_pretrained("prompthero/openjourney").to("cpu")
        self.text_encoder = pipe.text_encoder
        
    def cleanup_torchscript_cache(self):                         # Pytorch의 JIT 컴파일러 캐시 정리
        torch._C._jit_clear_class_registry()
        torch.jit._recursive.concrete_type_store = torch.jit._recursive.ConcreteTypeStore()
        torch.jit._state._clear_class_state()

    def cleanup_memory(self, model):
        del model              # 모델의 메모리 삭제
        gc.collect()           # 더 이상 사용되지 않을 객체의 메모리 삭제

    def convert_model_to_ov(self, model: torch.nn.Module, ir_path:Path, input_info: List[tuple]):     # 실제 모델 변환 수행
        model.eval()                      # 모델을 추론 모드로 변경                            
        with torch.no_grad():             # 메모리 사용량 감소를 위한 그래디언트 계산 비활성화                       
            ov_model = ov.convert_model(model, ir_path, input_info)     # 모델을 OpenVINO의 IR 형식으로 변환
        ov.save_model(ov_model, ir_path) #변환된 IR 모델을 지정된 경로에 저장
        del ov_model                     # 메모리에서 IR 모델을 삭제
        self.cleanup_torchscript_cache()      # PyTorch JIT 컴파일러 캐시를 정리
        print(f'Text Encoder successfully converted to IR and saved to {ir_path}')    # 변환 및 저장이 완료됨을 출력

    def convert_text_encoder(self, text_encoder: torch.nn.Module, ir_path: Path):
        self.text_encoder = text_encoder
        input_ids = torch.ones((1,77), dtype=torch.long)
        input_info = [(1,77)]
        self.text_encoder.eval()
        self.convert_model_to_ov(text_encoder, ir_path, input_info)

    def convert_unet(self, unet: torch.nn.Module, ir_path:Path, input_info: List[tuple]):     # 실제 unet 모델 변환 수행
        # input_info
        latents_shape = (2, 4, 512 // 8, 512 // 8)
        latents = torch.randn(latents_shape)
        t = torch.from_numpy(np.array(1, dtype=float))
        encoder_hidden_state = torch.ones((2, 77, 768))
        dummy_inputs = (latents, t, encoder_hidden_state)
        input_info =[(ov.PartialShape(tuple(input_tensor.shape)), self.dtype_mapping[input_tensor.dtype]) for
                      input_tensor in dummy_inputs]   
        unet.eval()
        self.convert_model_to_ov(unet, ir_path, input_info)

    def convert_model_load(self, model, model_ov_path, convert_func):
        # 변환된 모델이 존재하지 않는 경우에만 모델을 변환하고 저장 
        if not model_ov_path.exists():
            convert_func(model, model_ov_path)
            self.cleanup_memory(model)
        # 변환된 모델이 이미 존재한다면 로딩
        else:
            print(f"Model will be loaded from {model_ov_path}")
        
# VAE 모델은 인코더, 디코더의 두 부분이 있음
# 인코더 : 이미지를 낮은 차원의 잠재적 표현으로 변환, U-net 모델에 대한 입력 역할
# 디코더 : 잠재적 표현을 다시 이미지로 변환
# vae_encoder_ov_path = Path("vae_encoder.xml")
# vae_decorder_ov_path = Path("vae_decoder.xml")
class Encoder:
    def __init__(self):
        self.ov_cache = {}
    
    def convert_vae_encoder(self, vae: torch.nn.Module, ir_path: Path):
        class VAEEncoderWrapper(torch.nn.Module):
            def __init__(self, vae):
                super().__init__()
                self.vae = vae
            def forward(self, image):
                return self.vae.encode(x=image)["latent_dist"].sample()

        vae_encoder = VAEEncoderWrapper(vae)
        vae_encoder.eval()
        image = torch.zeros((1, 3, 512, 512))
        with torch.no_grad():
            ov_model = ov.convert_model(vae_encoder, example_input=image, input=[((1,3,512,512),)])
        ov.save_model(ov_model, ir_path)
        del ov_model
        print(f'VAE encoder successfully converted to IR and saved to {ir_path}')
        
        torch.jit.clear_autodetected_analyzers()

    vae_encoder_ov_path = Path("vae_encoder.xml")
    if not vae_encoder_ov_path.exists():
        convert_vae_encoder(vae, vae_encoder_ov_path)
    else:
        print(f"VAE encoder will be loaded from {vae_encoder_ov_path}")

class Decorder:
    def __init__(self):
        self.ov_cache = {}

    def convert_vae_decoder(self, vae: torch.nn.Module, ir_path: Path):
        class VAEDecoderWrapper(torch.nn.Module):
            def __init__(self, vae):
                super().__init__()
                self.vae = vae
            def forward(self, latents):
                return self.vae.decode(latents)
    
        vae_decoder = VAEDecoderWrapper(vae)
        latents = torch.zeros((1, 4, 64, 64))

        vae_decoder.eval()
        with torch.no_grad():
            ov_model = ov.convert_model(vae_decoder, example_input=latents, input=[((1,4,64,64),)])
        ov.save_model(ov_model, ir_path)
        del ov_model
        print(f'VAE decoder successfully converted to IR and saved to {ir_path}')
        
        torch.jit.clear_autodetected_analyzers()
    vae_decorder_ov_path = Path("vae_decoder.xml")
    if not vae_decorder_ov_path.exists():
        convert_vae_decoder(vae, vae_decorder_ov_path)
        gc.collect()
    else:
        print(f"VAE decoder will be loaded from {vae_decorder_ov_path}")

class ImageSize:
    # 주어진 이미지 출력창 크기 조정 (원본 image -> 조정 dst)
    def scale_fit_to_window(self, dst_width:int, dst_height:int, image_width:int, image_height:int):
        im_scale = min(dst_height / image_height, dst_width / image_width)     # 원본과 목표 크기 간의 비율 유지
        return int(im_scale * image_width), int(im_scale * image_height)       # 이미지의 새로운 크기값 반환
    
    # 이미지 전처리 수행, 주어진 이미지를 입력받아 처리한 후 처리된 이미지와 추가 정보 반환
    def preprocess(image: PIL.Image.Image):
        src_width, src_height = image.size
        dst_width, dst_height = scale_fit_to_window(512, 512, src_width, src_height)
        image = np.array(image.resize((dst_width, dst_height),
                        resample=PIL.Image.Resampling.LANCZOS))[None, :]
        pad_width = 512 - dst_width
        pad_height = 512 - dst_height
        pad = ((0, 0), (0, pad_height), (0, pad_width), (0, 0))
        image = np.pad(image, pad, mode="constant")
        image = image.astype(np.float32) / 255.0
        image = 2.0 * image - 1.0
        image = image.transpose(0, 3, 1, 2)
        return image, {"padding": pad, "src_width": src_width, "src_height": src_height}


class OVStableDiffusionPipeline(DiffusionPipeline):
    def __init__(
        self,
        vae_decoder: Model,
        text_encoder: Model,
        tokenizer: CLIPTokenizer,
        unet: Model,
        scheduler: Union[DDIMScheduler, PNDMScheduler, LMSDiscreteScheduler],
        vae_encoder: Model = None,
    ):
        super().__init__()
        self.scheduler = scheduler
        self.vae_decoder = vae_decoder
        self.vae_encoder = vae_encoder
        self.text_encoder = text_encoder
        self.unet = unet
        self._text_encoder_output = text_encoder.output(0)
        self._unet_output = unet.output(0)
        self._vae_d_output = vae_decoder.output(0)
        self._vae_e_output = vae_encoder.output(0) if vae_encoder is not None else None
        self.height = 512
        self.width = 512
        self.tokenizer = tokenizer

    def __call__(
        self,
        prompt: Union[str, List[str]],
        image: PIL.Image.Image = None,
        num_inference_steps: Optional[int] = 50,
        negative_prompt: Union[str, List[str]] = None,
        guidance_scale: Optional[float] = 7.5,
        eta: Optional[float] = 0.0,
        output_type: Optional[str] = "pil",
        seed: Optional[int] = None,
        strength: float = 1.0,
        gif: Optional[bool] = False,
        **kwargs,
    ):
        if seed is not None:
            np.random.seed(seed)

        img_buffer = []
        do_classifier_free_guidance = guidance_scale > 1.0
        # get prompt text embeddings
        text_embeddings = self._encode_prompt(prompt, do_classifier_free_guidance=do_classifier_free_guidance, negative_prompt=negative_prompt)
        
        # set timesteps
        accepts_offset = "offset" in set(inspect.signature(self.scheduler.set_timesteps).parameters.keys())
        extra_set_kwargs = {}
        if accepts_offset:
            extra_set_kwargs["offset"] = 1

        self.scheduler.set_timesteps(num_inference_steps, **extra_set_kwargs)
        timesteps, num_inference_steps = self.get_timesteps(num_inference_steps, strength)
        latent_timestep = timesteps[:1]

        # get the initial random noise unless the user supplied it
        latents, meta = self.prepare_latents(image, latent_timestep)

        # prepare extra kwargs for the scheduler step, since not all schedulers have the same signature
        # eta (η) is only used with the DDIMScheduler, it will be ignored for other schedulers.
        # eta corresponds to η in DDIM paper: https://arxiv.org/abs/2010.02502
        # and should be between [0, 1]
        accepts_eta = "eta" in set(inspect.signature(self.scheduler.step).parameters.keys())
        extra_step_kwargs = {}
        if accepts_eta:
            extra_step_kwargs["eta"] = eta

        for i, t in enumerate(self.progress_bar(timesteps)):
            # expand the latents if you are doing classifier free guidance
            latent_model_input = np.concatenate([latents] * 2) if do_classifier_free_guidance else latents
            latent_model_input = self.scheduler.scale_model_input(latent_model_input, t)

            # predict the noise residual
            noise_pred = self.unet([latent_model_input, t, text_embeddings])[self._unet_output]
            # perform guidance
            if do_classifier_free_guidance:
                noise_pred_uncond, noise_pred_text = noise_pred[0], noise_pred[1]
                noise_pred = noise_pred_uncond + guidance_scale * (noise_pred_text - noise_pred_uncond)

            # compute the previous noisy sample x_t -> x_t-1
            latents = self.scheduler.step(torch.from_numpy(noise_pred), t, torch.from_numpy(latents), **extra_step_kwargs)["prev_sample"].numpy()
            if gif:
                image = self.vae_decoder(latents * (1 / 0.18215))[self._vae_d_output]
                image = self.postprocess_image(image, meta, output_type)
                img_buffer.extend(image)

        # scale and decode the image latents with vae
        image = self.vae_decoder(latents * (1 / 0.18215))[self._vae_d_output]

        image = self.postprocess_image(image, meta, output_type)
        return {"sample": image, 'iterations': img_buffer}
    
    def _encode_prompt(self, prompt:Union[str, List[str]], num_images_per_prompt:int = 1, do_classifier_free_guidance:bool = True, negative_prompt:Union[str, List[str]] = None):
        batch_size = len(prompt) if isinstance(prompt, list) else 1

        # tokenize input prompts
        text_inputs = self.tokenizer(
            prompt,
            padding="max_length",
            max_length=self.tokenizer.model_max_length,
            truncation=True,
            return_tensors="np",
        )
        text_input_ids = text_inputs.input_ids

        text_embeddings = self.text_encoder(
            text_input_ids)[self._text_encoder_output]

        # duplicate text embeddings for each generation per prompt
        if num_images_per_prompt != 1:
            bs_embed, seq_len, _ = text_embeddings.shape
            text_embeddings = np.tile(
                text_embeddings, (1, num_images_per_prompt, 1))
            text_embeddings = np.reshape(
                text_embeddings, (bs_embed * num_images_per_prompt, seq_len, -1))

        # get unconditional embeddings for classifier free guidance
        if do_classifier_free_guidance:
            uncond_tokens: List[str]
            max_length = text_input_ids.shape[-1]
            if negative_prompt is None:
                uncond_tokens = [""] * batch_size
            elif isinstance(negative_prompt, str):
                uncond_tokens = [negative_prompt]
            else:
                uncond_tokens = negative_prompt
            uncond_input = self.tokenizer(
                uncond_tokens,
                padding="max_length",
                max_length=max_length,
                truncation=True,
                return_tensors="np",
            )

            uncond_embeddings = self.text_encoder(uncond_input.input_ids)[self._text_encoder_output]

            # duplicate unconditional embeddings for each generation per prompt, using mps friendly method
            seq_len = uncond_embeddings.shape[1]
            uncond_embeddings = np.tile(uncond_embeddings, (1, num_images_per_prompt, 1))
            uncond_embeddings = np.reshape(uncond_embeddings, (batch_size * num_images_per_prompt, seq_len, -1))

            # For classifier free guidance, we need to do two forward passes.
            # Here we concatenate the unconditional and text embeddings into a single batch
            # to avoid doing two forward passes
            text_embeddings = np.concatenate([uncond_embeddings, text_embeddings])

        return text_embeddings


    def prepare_latents(self, image: PIL.Image.Image = None, latent_timestep:torch.Tensor = None):

        latents_shape = (1, 4, self.height // 8, self.width // 8)
        noise = np.random.randn(*latents_shape).astype(np.float32)
        if image is None:
            # if you use LMSDiscreteScheduler, let's make sure latents are multiplied by sigmas
            if isinstance(self.scheduler, LMSDiscreteScheduler):
                noise = noise * self.scheduler.sigmas[0].numpy()
                return noise, {}
        new_image_size = ImageSize()  # ImageSize 클래스의 인스턴스 생성
        input_image, meta = new_image_size.preprocess(image)
        latents = self.vae_encoder(input_image)[self._vae_e_output] * 0.18215
        latents = self.scheduler.add_noise(torch.from_numpy(latents), torch.from_numpy(noise), latent_timestep).numpy()
        return latents, meta

    def postprocess_image(self, image:np.ndarray, meta:Dict, output_type:str = "pil"):
        if "padding" in meta:
            pad = meta["padding"]
            (_, end_h), (_, end_w) = pad[1:3]
            h, w = image.shape[2:]
            unpad_h = h - end_h
            unpad_w = w - end_w
            image = image[:, :, :unpad_h, :unpad_w]
        image = np.clip(image / 2 + 0.5, 0, 1)
        image = np.transpose(image, (0, 2, 3, 1))
        # 9. Convert to PIL
        if output_type == "pil":
            image = self.numpy_to_pil(image)
            if "src_height" in meta:
                orig_height, orig_width = meta["src_height"], meta["src_width"]
                image = [img.resize((orig_width, orig_height),
                                    PIL.Image.Resampling.LANCZOS) for img in image]
        else:
            if "src_height" in meta:
                orig_height, orig_width = meta["src_height"], meta["src_width"]
                image = [cv2.resize(img, (orig_width, orig_width))
                         for img in image]
        return image

    def get_timesteps(self, num_inference_steps:int, strength:float):
        # get the original timestep using init_timestep
        init_timestep = min(int(num_inference_steps * strength), num_inference_steps)

        t_start = max(num_inference_steps - init_timestep, 0)
        timesteps = self.scheduler.timesteps[t_start:]

        return timesteps, num_inference_steps - t_start 

       
class TextToImageGenerator:
    def __init__(self):
        self.core = ov.Core()

    def compile_model(self, model_path, device='CPU', config=None):
        return self.core.compile_model(model_path, device, config)

    def create_ov_pipe(self):
        TEXT_ENCODER_OV_PATH = Path("text_encoder.xml")
        UNET_OV_PATH = Path('unet.xml')
        VAE_ENCODER_OV_PATH = Path("vae_encoder.xml")
        VAE_DECODER_OV_PATH = Path('vae_decoder.xml')

        tokenizer = CLIPTokenizer.from_pretrained('openai/clip-vit-large-patch14')
        lms = LMSDiscreteScheduler(
            beta_start=0.00085,
            beta_end=0.012,
            beta_schedule="scaled_linear"
        )

        pipe = StableDiffusionPipeline.from_pretrained("prompthero/openjourney").to("cpu")
        text_encoder = pipe.text_encoder
        text_encoder.eval()
        unet = pipe.unet
        unet.eval()
        vae = pipe.vae
        vae.eval()

        del pipe
        gc.collect()

        text_enc = self.compile_model(TEXT_ENCODER_OV_PATH, 'CPU')
        unet_model = self.compile_model(UNET_OV_PATH, 'CPU')
        ov_config = {"INFERENCE_PRECISION_HINT": "f32"} if 'CPU' != "CPU" else {}
        vae_decoder = self.compile_model(VAE_DECODER_OV_PATH, 'CPU', ov_config)
        vae_encoder = self.compile_model(VAE_ENCODER_OV_PATH, 'CPU', ov_config)

        return OVStableDiffusionPipeline(
            tokenizer=tokenizer,
            text_encoder=text_enc,
            unet=unet_model,
            vae_encoder=vae_encoder,
            vae_decoder=vae_decoder,
            scheduler=lms
        )

    def generate_image(self, text_data, steps=20, seed=20):
        f = open(text_data)  # 생성형 이미지를 만들기 위한 txt파일 경로 입력
        text_data = f.read()
        text_input = widgets.Text(value=text_data, description='your text')
        seed_input = widgets.IntText(min=0, max=10000000, description='seed: ', value=seed)
        steps_input = widgets.IntText(min=1, max=50, value=steps, description='steps:')

        ov_pipe = self.create_ov_pipe()
        result = ov_pipe(text_input.value, num_inference_steps=steps_input.value, seed=seed_input.value)

        new_background = random.choice(result['sample'])
        new_background.save('new_background.jpg')
        new_background.show()
