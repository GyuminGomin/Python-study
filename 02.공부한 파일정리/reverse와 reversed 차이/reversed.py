# reversed
"""
내장함수로, list에서 제공하는 함수가 아님
딕셔너리와 셋은 시퀀셜한 타입이 아니므로 지원하지 않고
튜플과 리스트에서 지원한다.

reverse함수는 'reversed'한 객체를 반환해준다.(id)

a = ['a','b','c']
b = ('a','b','c')
c = 'abc'
reversed(a) # listreverseiterator object at id
reversed(b) # reversed object at id
reversed(c) # reversed object ad id

list(reversed(a)) # ['c','b','a']
tuple(reversed(b)) # ('c','b','a')
"""
