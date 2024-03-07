from googletrans import Translator

def translate_korean_to_english(input_file, output_file):
    """
    한국어 문장을 영어로 번역하여 결과를 파일에 저장합니다.

    Args:
    input_file (str): 한국어 문장이 있는 파일 경로.
    output_file (str): 번역된 영어 문장을 저장할 파일 경로.
    """
    # Google 번역기 객체 생성
    translator = Translator()

    # 한국어 문장을 읽어와서 영어로 번역하여 저장
    with open(input_file, 'r', encoding='utf-8') as f_input, open(output_file, 'w', encoding='utf-8') as f_output:
        for line in f_input:
            korean_sentence = line.strip()
            english_translation = translator.translate(korean_sentence, src='ko', dest='en').text
            f_output.write(english_translation + '\n')
            print(f"번역 결과: {english_translation}")

# 모듈로 사용할 때는 직접 실행하지 않고 함수를 호출할 수 있도록 합니다.
if __name__ == "__main__":
    translate_korean_to_english("text.txt", "english.txt")
