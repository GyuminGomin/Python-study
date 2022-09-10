# Copy
import copy

list_A = ['ABC']
list_B = list_A
print(id(list_A) == id(list_B))\

# Shallow Copy 얕은 복사
list_C = list_A.copy()
list_D = list_A[:]

print(id(list_A) == id(list_C))
print(id(list_A) == id(list_D))

"""
문제점
if list_A = ['ABC',['BCD','CDE']] 라면
list_A안에 변형객체인 리스트가 또 존재하는데 이것의 특성을 그대로 가져와
list_C를 얕은복사를 했더라도 변형객체는 list_A와 list_C 둘다 바뀌게 된다.
"""

# Deep Copy 깊은 복사
"""
객체의 변형성에 따라, 불변형 객체는 그대로 가져오고 변형 객체는 새로운 공간에 값을 복사하여
가져오게 된다.
즉, 두 객체는 같은 값을 가진 완전히 다른 객체가 됨
    단점
    완벽한 복사를 할 수 있지만, 새로운 곳에 생성하는 것 때문에 시간이 오래걸리고 메모리 또한
    많이 낭비한다. 따라서 항상 deepcopy를 이용하는 것이 아니라 상황에 따라 shallow copy도 같이 사용
"""
list_E = copy.deepcopy(list_A)
print(id(list_A) == id(list_E))