# Time 모듈
"""
time 모듈은 epoch time(Unix time, POSIX time)을 다룰 때 사용한다.
epoch time은 UTC(GMT+0) 기준으로 1970년 1월 1일 0시 0분 0초부터의 경과시간을 나타내는데 timestamp라고 불린다.
"""
# struct_time 객체
"""
tm_year 연
tm_mon 달
tm_mday 일
tm_hour 시
tm_min 분
tm_sec 초
tm_wday 요일 / 범위 : 0~6 (0: 월요일)
tm_yday 연중 경과일 / 범위 : 1~366
tm_isdst 일광절약타임 / 적용여부 0:미적용 1:적용 -1:모름
"""
import time
now = time.time()
print(time.localtime(now)) # 현지 시간대 기준 struct_time 타입으로 반환
print(time.localtime()) # now 안붙여도 적용
time.gmtime(now) # GMT+0 시간대 기준 struct_time 타입으로 반환
time.gmtime() # now 안붙여도 적용

print()
print(time.ctime()) # 요일 월 일 시:분:초 년 포멧으로 반환

print()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # datetime모듈과 같은 포맷의 문자열 반환방식 전환이지만, timestamp가 아닌 struct_time 객체를 받음
print(time.strftime('%Y-%m-%d %I:%M:%S %p',time.localtime()))
"""
%I 는 12진법 시간을 나타냄
%p 는 현재가 AM인지 PM인지를 나타냄
%a 는 요일을 나타냄
"""

print()
now_s = time.strftime('%Y-%m-%d %I:%M:%S %p',time.localtime())
print(time.strptime(now_s, '%Y-%m-%d %I:%M:%S %p')) # strftime과 반대

print()
# time.sleep() # 일정시간 지연 sec를 매개변수로 받음