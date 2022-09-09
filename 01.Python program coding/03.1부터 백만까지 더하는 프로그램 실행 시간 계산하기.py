# 조건
"""
1. 프로그램 실행 시간을 1/1000초 단위로 계산하기 # ms로 계산하라는 의미
2. datetime 모듈을 사용하기
3. datetime 모듈의 datetime 객체를 임포트하여 사용하기
4. ret 변수에 1부터 백만까지 더한 결과를 담을 변수로 사용한다.
5. 1부터 백만까지의 더하는 루틴은 for 문을 사용한다.
6. 1에서부터 백만까지 더한 결과를 화면에 print를 통해 출력한다.
7. 결과
    1부터 백만까지 더합니다.
    1부터 백만까지 더한 결과 : 499999500000 # 백만까지 더한게 아니라 99만9999까지 더한 값
    총 계산 시간 : 0:00:00.124968
    총 계산 시간 : 124ms
"""

from datetime import datetime

ret = 0

for i in range(1,1000000) :
    if i == 1 :
        print("1부터 백만까지 더합니다.")
        start = datetime.now()
    ret += i
    if i == 999999 :
        end = datetime.now() - start
        print("1부터 백만까지 더한 결과 : {}".format(ret))
        print("총 계산 시간 : {}".format(end))
        print("총 계산 시간 : {}ms".format(round(end.microseconds*0.001)))