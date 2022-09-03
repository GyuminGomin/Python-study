from datetime import timedelta
"""
1. timedelta 클래스는 기간을 표현하기 위해 사용한다.
2. timedelta 클래스의 생성자는 주,일,시,분,초,밀리 초,마이크로 초를 인자로 받음
3. date, datetime 클래스들을 계산하고 받는 타입이다.
    ex. a = datetime.now(), b = datetime.strptime("20220902","%Y%m%d")
    a - b를 하면 datetime.timedelta 타입을 갖게 된다.
4. datetime 클래스는 days, microseconds, seconds라는 함수를 가지고 있다.
"""
#from datetime import datetime
#a = datetime.now()
#b = datetime.strptime('2022/09/02','%Y/%m/%d')
#print(type(a-b))
#print((a-b).seconds)
#print((a-b).microseconds)
#print()

#import time # datetime의 라이브러리랑 다름
#import math
#start = time.time()
#math.factorial(1000000)
#end = time.time()
#print(f"{end-start:.5f} sec")

print(timedelta(weeks=5, days=3, hours=17, minutes=30, seconds=30, milliseconds=30, microseconds=30))
# 타입은 datatime.timedelta
print()
print()
""""""""""""""""""""""""""""""""""""
from datetime import date
"""
date 클래스의 생성자는 연,월,일 데이터를 인자로 받음
그리고 timedelta 클래스와 연산이 가능
"""
print(date(2019,12,25))
print(date.fromisoformat('2019-12-25')) # YYYY-MM-DD형태의 문자열을 date객체로 반환
today = date.today()
print(today.year, today.month, today.day) # 하나씩 받아올 수 있음
print(today.weekday(), today.isoweekday()) # 무슨 요일인지 weekday는 0 = 월요일, isoweekday는 1 = 월요일
print(today.replace(year=2019), today)

#today = date.today()
#print(today) # type은 datetime.date # + 연산이 적용가능

#one_week = timedelta(weeks=1)
#print(today + one_week)

#two_weeks = one_week * 2
#print(two_weeks)
#print(one_week < two_weeks)
print()
print()

""""""""""""""""""""""""""""""""""""
from datetime import timezone
"""
timedelta 객체를 인자로 받아 timezone 객체를 생성
"""
print(timezone(timedelta(hours=9)))
print(timezone.utc)
print()
print()

""""""""""""""""""""""""""""""""""""
from datetime import time
"""
time 클래스의 생성자는 시,분,초,마이크로 초,시간대를 인자로 받음 생략할경우 0으로 default
timedelta 클래스와 연산이 불가능
"""
print(time(13,42,35))
t = time(13,42,35)
# print(time.isoformat('13:42:35.000000')) # 문자열을 time객체로 변환해주는 것.. 근데 문자열을 어떻게 써야할지 모르겠다.
print(t.replace(hour=14), t)

print()
print()

""""""""""""""""""""""""""""""""""""
from datetime import datetime
"""
datetime클래스의 생성자는 연,월,일,시,분,초,마이크로 초,시간대를 인자로 받음
시간이후의 인자는 필수가 아니며 default로는 0
"""
d = date(2020, 7, 18)
t = time(13, 26, 23)
dt = datetime.combine(d,t)
print(dt)
print(datetime.now())
print()
print(datetime.now().strftime('%Y/%m/%d')) # 년월일
print(datetime.now().strftime('%H:%M:%S')) # 시분초
print(datetime.now().strptime('2020-07-18', '%Y-%m-%d')) # 문자열을 datetime객체로 변환
print()
print(int(datetime.now().timestamp()*1000)) # datetime 문자열인 현재시간을 ms단위로 가져오는법