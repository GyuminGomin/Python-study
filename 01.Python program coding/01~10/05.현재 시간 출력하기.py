# 조건
"""
1. 현재 시간을 년-월-일 시:분:초 로 출력하기
2. 파이썬의 time 모듈을 사용하여 출력
3. test.log 파일을 만들고 파일에 정보 저장하기
4. 함수를 만들어 사용하기
5. 파일 생성시 print를 사용하여 화면에 출력하기
6. localtime()과 strftime() 내장 함수를 이용하기
"""

import time
def cureent_time() :
    now = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', now)

with open("05.test.log", "w") as f : # encoding = "cp949"
    f.write(cureent_time())
    print("파일이 생성되었습니다.")