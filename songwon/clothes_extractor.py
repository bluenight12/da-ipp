def extract_clothes(input_file_path, output_file_path):
    """
    english.txt 파일에서 'yellow', 'black', 'blue', 't-shirt', 'cote'와 같은 단어를 찾아 
    clothes.txt 파일에 한 줄에 나열하여 저장하는 함수
    """
    # 'input_file_path' 파일 읽기
    with open(input_file_path, 'r') as english_file:
        # 'output_file_path' 파일 열기 (없으면 생성)
        with open(output_file_path, 'w') as clothes_file:
            # 'input_file_path' 파일의 각 줄을 확인
            for line in english_file:
                # 단어 단위로 분리
                words = line.split()
                # 'output_file_path' 파일에 발견된 단어들을 한 줄에 나열하여 저장
                clothes_file.write(' '.join([word for word in words if word in ['yellow', 'black', 'blue', 't-shirt', 'cote']]) + '\n')
