# 주사위 게임
"""
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이
있다.

규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게
된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금
으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을
작성하시오.

입력설명
첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람들이
주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력설명
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

입력예제 1
3
3 3 6
2 2 2
6 2 5

출력예제 1
12000
"""
import numpy as np
import re

while True :
    try :
        N = int(input("게임에 참가하는 사람의 수를 적으세요. : "))
        if N < 2 or N > 1000 :
            print("N은 2이상 1000이하로만 설정 가능합니다.")
            continue
    except ValueError :
        print("숫자를 적어주세요.")
        continue
    else :
        break
N_list = [] # 딴 돈을 적는다.
while N :
    dice_n = input("나온 3개의 주사위 눈금을 적으세요.(스페이스로 구분) :")
    p = re.match("(\d+\s{1}){2}\d+$",dice_n)
    if not p :
        print("문자를 입력했거나 스페이스 오류입니다.")
        continue
    int_diceList = list(map(int,dice_n.split(" ")))
    # if len(int_diceList) != 3 : # 안 넣어도 되는 이유를 이해하게 되었다!
    #     print("3개만 입력해 주세요.") # 숫자 하나만 더 넣으려면 스페이스를 붙여야
    #     continue # 하기 때문
    f, s, t = map(int,dice_n.split(" "))
    if f == s == t :
        N_list.extend([10000+(f*1000)])
    if f == s or f == t :
        N_list.extend([1000+(f*100)])
    if s == t :
        N_list.extend([1000+(s*100)])
    else :
        N_list.extend([np.max(int_diceList)*100])
    N -= 1

print(np.max(N_list))

# 정답
"""
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
res = 0
for i in range(n) :
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c :
        money = 10000+a*1000
    elif a == b or a == c :
        money = 1000+(a*100)
    else :
        money = c*100
    if money > res :
        res = money
print(res)
"""