import speech_recognition as sr

def back_recognize_and_save_text():
    """
    사용자의 음성을 인식하고 인식된 텍스트를 파일에 저장합니다.
    """
    # 음성 인식기 객체 생성
    recognizer = sr.Recognizer()

    while True:
        # 마이크로 음성 입력 받기
        with sr.Microphone() as source:
            print("말씀해주세요...")
            recognizer.adjust_for_ambient_noise(source)  # 배경 소음에 대한 자동 조절
            audio = recognizer.listen(source, timeout=1)  # 마이크에서 음성 입력을 듣기

        # 음성을 텍스트로 변환
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("음성 인식 결과:", text)

            # 인식된 텍스트를 text.txt 파일에 저장
            with open("back.txt", "w") as file:
                file.write(text)
            print("인식된 단어를 text.txt 파일에 저장했습니다.")
            break  # 정상적으로 음성을 인식하면 루프를 종료합니다.

        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다. 다시 시도해주세요.")
        except sr.RequestError as e:
            print("Google Speech Recognition 서비스에 접근할 수 없습니다; {0}".format(e))

# 모듈로 사용할 때는 직접 실행하지 않고 함수를 호출할 수 있도록 합니다.
if __name__ == "__main__":
    back_recognize_and_save_text()