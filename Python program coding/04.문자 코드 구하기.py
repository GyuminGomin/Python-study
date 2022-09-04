# 조건
"""
1. 문자를 커맨드 창에서 입력받는다.
2. 입력은 "문자 1개를 입력하세요 : "로 한다.
3. 결과는 아래와 같이 화면에 프린트한다.
문자 : c          코드값 : 99[0x63]
cf. 파일실행은 디렉터리에서 cmd를 검색해 뜨는 커맨드창 위치에서 python "04.문자 코드 구하기.py"로 실행
"""

import sys
while True :
    result = input("문자 1개를 입력하세요 : ")
    if len(result) == 1 :
        print("문자 : {0}         코드값 : {1}[{2}]".format(result, ord(result), hex(ord(result))))
        break
    else :
        continue
