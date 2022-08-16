sub = {'국어' : 80, '수학' : 55 ,'영어' : 75}
a = sub['국어']
b = sub['수학']
c = sub['영어']

print(len(sub))
print((a+b+c)/len(sub))

# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법

if (13 % 2) == 1 :
    print ('odd')
else :
    print('even')

# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력

add = '881120-1068234'
head = '19'+add[:6]
tail = add[7:]
print (head)
print (tail)

# 주민번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881120-1068234"
print(pin[7])

# 다음과 같은 문자열 a:b:c:D가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 ㅊㄹ력해보자.
a = 'a:b:c:d'
print(a.replace(':', '#'))

# [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
list2 = [1,3,5,4,2]
list2.sort(reverse=True)
print(list2)

# 이것 말고도 list2.sort() 한 후, list2.reverse()를 해서 뒤집으면 된다.

# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
list1 = ['Life', 'is', 'too', 'short']
" ".join(list1)
print(list1)
print ('Life is too short')

# (1,2,3) 튜플에 값 4 를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
tu = (1,2,3)
tu = list(tu)
tu.append(4)
tu = tuple(tu)
print(tu)

# 이렇게 복잡하게 말고 tu = (1,2,3)에 tu += (4,) 만 넣으면 된다.

# 다음과 같은 딕셔너리 a 가 있다.
a = dict()
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명
""" 1. a['name'] = 'python'
    2. a[('a',)] = 'python'
    3. a[[1]] = 'python'   --> key값은 immutable이라 리스트가 들어올 수 없다.
    4. a[250] = 'python'
"""

# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A' : 90, 'B' : 80, 'C' : 70}
# 참고로 pop함수를 사용해 보며 적용
b = list(a.values())
b.pop()
print(b.pop())

# 이렇게 말고 a.pop('B')를 사용하면 된다.

# a 리스트에서 중복 숫자를 제거해 보자.
a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a,b 변수를 선언한 후 a의 두 번째
# 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
a = b = [1,2,3]
a[1] = 4
print(b)
# 예상 : id 값을 공유하고 있기 때문에 a가 바뀌면 b도 바뀐다.
