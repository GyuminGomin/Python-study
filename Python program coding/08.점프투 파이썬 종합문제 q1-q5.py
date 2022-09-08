# Q1. 문자열 바꾸기
"""
다음과 같은 문자열이 있다.
a:b:c:d
문자열의 split와 join함수를 사용하여 위 문자열을 다음과 같이 고치시오.
a#b#c#d
"""

string_a = 'a:b:c:d'
string_b = string_a.split(':')
string_a = '#'.join(string_b)
print(string_a)

# Q2. 딕셔너리 값 추출하기
"""
다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
    >>> a = {'A':90, 'B':80}
    >>> a['C']
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    KeyError: 'C'
a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다. 'C'에 해당하는 key값이 
없을 경우 오류 대신 70을 얻을 수 있도록 수정하시오.
"""
try :
    a = {'A':90,'B':80}
    a['C']
except KeyError :
    print(70)

# Q3. 리스트의 더하기와 extend 함수
"""
다음과 같은 리스트 a 가 있다.
    >>> a = [1, 2, 3]
리스트 a에 [4,5]를 +기호를 사용하여 더한 결과는 다음과 같다.
    >>> a = [1, 2, 3]
    >>> a = a + [4,5]
    >>> a
    [1, 2, 3, 4, 5]
리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.
    >>> a = [1, 2, 3]
    >>> a.extend([4, 5])
    >>> a
    [1, 2, 3, 4, 5]
+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.
"""
# 정답
"""
리스트에 +기호를 사용해 리스트를 더하면 새로운 id값에 저장이 된다.
리스트에 extend함수를 사용해 리스트를 더하면 그대로인 id값에 저장이 된다.
"""

# Q4. 리스트 총합 구하기
"""
다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
"""
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
for i in A :
    if i >= 50 :
        result += i
    else :
        continue
print(result)

# Q5. 피보나치 함수
"""
첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을
더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
0, 1, 1, 2, 3, 5, 8, 13, ...
입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
"""
def fibo_num(numbers) : # numbers가 5보다 작거나 같을때는 성립이 안된다.
    Fibonacci_Numbers = []
    start = 1
    init = 0
    number = 0
    for i in range(1, numbers+1) :
        if i == 1 :
            Fibonacci_Numbers += [init] # [0]
            number = init + start # 1,0,1
            init += start # 1,1,1
        if i % 2 == 0 :
            Fibonacci_Numbers += [init] # [0,1] [0,1,1,2] [0,1,1,2,3,5]
            init += number # 1,2,1 - 1,5,3 - 1,13,8
            if number > numbers : # 이렇게 해야만 하는 이유를 설명을 못하겠다. 만족스러울 정도로..
                break
        if i % 2 == 1 and i != 1 :
            Fibonacci_Numbers += [number] # [0,1,1] [0,1,1,2,3]
            number += init # 1,2,3 - 1,5,8
            if init > numbers :
                break
    print(Fibonacci_Numbers)
# 피보나치 수열 Fibonacci numbers의 원리 하지만 numbers = 1,2,3,4,5일때는 for반복횟수가 적어 성립되지 않는다.
# 위 함수에서 브레이크를 없애면, 원하는 수열의 반복횟수를 정하는 피보나치 수열이다.
def fibo_num2(numbers) :
    if numbers == 1 :
        fibo_num(3)
    elif numbers == 2 :
        fibo_num(4)
    elif numbers == 3 or numbers == 4 :
        fibo_num(5)
    elif numbers == 5 :
        fibo_num(6)
    else :
        fibo_num(numbers)
# 피보나치 수열이 성립되지 않을 때, 적용하는 함수를 새로 다시 만들어 재 정립하였다.

# 정답
"""
재귀 호출을 사용하면 피보나치 함수를 다음과 같이 간단하게 작성할 수 있다.
하지만 이거슨 위 Fibonacci_Number 함수의 break만 제거하면 똑같다.
"""


def fib(n) :
    if n == 0 : return 0 # n이 0일 때는 0을 반환
    if n == 1 : return 1 # n이 1일 때는 1을 반환
    return  fib(n-2) + fib(n-1) # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

def fib2(n) :
    fibo = []
    for i in range(n) :
        fibo += [fib(i)]
    print(fibo)

fib2(8)