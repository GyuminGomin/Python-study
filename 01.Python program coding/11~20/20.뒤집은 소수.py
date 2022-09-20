# 뒤집은 소수
"""
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로
그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다.
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터 연속된 0은 무시한다. 뒤집는 함수인
def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍
한다.

입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.

출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

입력예제 1
5
32 55 62 3700 250

출력예제 1
23 73
"""

import re

def reverse(x) : # x에는 뒤집기를 원하는 리스트 넣기
    for i in x :
        r_list = list(reversed(list(i)))
        return int(''.join(r_list))

def isPrime(x) : # 뒤집어진 리스트를 넣기
    for i in x :
        isP = True
        if i % 2 == 0 :
            continue
        for j in range(3,i,2) :
            if i % j == 0 :
                isP = False
                break
        if isP == False :
            continue
        elif isP == True :
           return i

while True :
    try :
        N = int(input("알아보고 싶은 숫자 개수를 입력하세요(N) : "))
        if N < 3 or N > 100000 :
            print("N의 범위는 3이상 10만 이하입니다.")
            continue
    except ValueError :
        print("숫자만 입력해 주세요.")
        continue
    else: break
while True :
    N_inp = input("N개의 숫자를 입력하세요(스페이스로 구분) : ")
    p = re.match("(\d+\s{1})+\d+$", N_inp)
    if not p :
        print("문자가 입력 되었거나, 갯수가 맞지 않습니다.")
        continue
    N_list = N_inp.split(" ")
    if len(N_list) != N :
        print("N의 갯수가 맞지 않습니다.")
        continue
    if p :
        break
rev_list = []
result = []

rev_list.extend([reverse(N_list)])
result.extend([isPrime(rev_list)])
print(result)

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")

def reverse(x) :
    res = 0
    while x > 0 :
        t = x % 10
        res = res * 10 + t
        x = x//10
    return res
def isPrime(x) :
    if x == 1 :
        return False
    for i in range(2, x//2 +1)
        if x%i == 0 :
            return False
    else :
        return True
        
n = int(input())
a = list(map(int, input().split()))
for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end = ' ')
"""