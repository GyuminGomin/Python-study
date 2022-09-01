#11 glob 모듈을 사용하여 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.

# glob은 디렉터리의 원하는 파일들을 찾아주는 기능 *은 모든, ?는 한문자, recursive = True하고 **은 모든 하위 디렉토리까지 찾아줌
import glob
import time
import random

a = glob.glob("C:\\Users\\a6351\\PycharmProjects\\pythonProject\\파이썬 공부 2022-08-14 이후\\*.py")
print(a)

#12 time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32

print(time.time()) # time.time은 1970년 1월1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려줌
print(time.localtime(time.time())) # time.time이 돌려준 실수 값을 사용해 연,월,일,시,분,초,...의 형태로 바꾸어 줌
print(time.asctime(time.localtime(time.time()))) # time.localtime에 의해 변환된 튜플 형태의 값을 인수로 받아 알아보기 쉬운 형태로 돌려줌
print(time.ctime()) # 위의 문장을 간편하게 다른점은 현재 시간만 돌려줌
print(time.strftime('%c', time.localtime(time.time()))) # %c형태말고도 다른형태가 많음
# time.sleep(1) 1초간 딜레이
print(time.strftime("%Y/%m/%d %H:%M:%S"))

#13 random 모듈을 사용하여 로또 번호(1~45 사이의 수자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안됨).
# random.random() 0~1사이의 난수
# random.randint(1, 11) 1~11사이의 정수중 난수 값
data = []
lotto_n = []
for i in range(1,46) :
    data += [i]
for i in range(0,6) :
    number = random.randint(0, len(data) - 1)
    lotto_n += [data.pop(number)]
print(lotto_n)

# result = []
# while len(result) < 6:
#     num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
#     if num not in result:
#         result.append(num)
# 
# print(result)