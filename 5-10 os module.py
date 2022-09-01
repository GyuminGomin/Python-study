# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# C:\doit 디렉터리로 이동한다.
# dir 명령을 실행하고 그 결과를 변수에 담는다.
# dir 명령의 결과를 출력한다.

import os
os.chdir("C:\\Users\\a6351\\PycharmProjects\\pythonProject\\파이썬 공부 2022-08-14 이후") # 디렉터리로 이동
result = os.popen("dir") # system이랑 같은 함수인 것 같애
print(result.read())
# a = os.system("dir") # 프롬프트 명령어를 실행하는 함수
# print(a)