# 조건
"""
1. 남자와 여자의 조건은 다음과 같다.
male = ['수퍼맨','배트맨','아쿠아맨','아이언맨','스파이더맨']
female = ['원더우먼','캡틴마블','블랙윈도우','배트걸','수퍼걸']
2. 결과는 랜덤하게 아래와 같이 화면에 프린트되게 한다.
커플 1 : [수퍼맨]-[수퍼걸]
커플 2 : [배트맨]-[배트걸]
커플 3 : ...
"""

import random as rd
male = ['수퍼맨','배트맨','아쿠아맨','아이언맨','스파이더맨']
female = ['원더우먼','캡틴마블','블랙윈도우','배트걸','수퍼걸']

for i in range(len(male)) :
    m = rd.choice(male) # male 추첨
    f = rd.choice(female) # female 추첨
    print("커플 {0} : [{1}] - [{2}]".format(i+1,m,f))
    del male[male.index(m)]
    del female[female.index(f)]