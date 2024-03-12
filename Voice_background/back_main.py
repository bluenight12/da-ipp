import back_recognize_text_module
import back_translate_korean_to_english
from text2background_image_fin import TextToImageGenerator

back_recognize_text_module.back_recognize_and_save_text()
back_translate_korean_to_english.back_translate_korean_to_english("back.txt", "bck_eng.txt")

generator = TextToImageGenerator()
generator.generate_image()

