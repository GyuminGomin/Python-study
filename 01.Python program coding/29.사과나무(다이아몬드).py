# 사과나무(다이아몬드)

"""
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어져 있다.
N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할
때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 수확을 한다.
[10 13 [] 12 15 ]
[12 [] [] [] 11 ]
[[] [] [] [] [] ]
[19 [] [] [] 27 ]
[19 13 [] 13 19 ]
현수가 수확하는 사과의 총 개수를 출력하세요.

입력설명
첫 줄에 자연수 N(홀수)이 주어진다. (3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.

출력설명
수확한 사과의 총 개수를 출력한다.

입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

출력예제 1
379
"""

import re
import numpy as np

while True :
    try :
        N = int(input("원하는 홀수 N을 입력하시오. : "))
        if N < 3 or N > 20 or N % 2 == 0:
            print("N은 3이상 20이하 홀수입니다.")
            continue
    except ValueError :
        print("숫자만 입력해주세요.")
    else: break

seq = [[0]*N]*N

for i in range(N) :
    while True :
        v_inp = input("N개의 숫자를 입력하세요. : ")
        p = re.match("(\d+\s{1})+\d+", v_inp)
        if not p :
            print("숫자 또는 스페이스 오류 또는 개수를 N개로 해 주십시오.")
            continue
        if p :
            seq_list = list(map(int,v_inp.split(" ")))
            seq[i] = seq_list
            break
tot = 0
sub = 0
for i in range(0, N//2+1) :
    for j in range(i+1) :
        tot += seq[i][(N//2)-j]
    for j in range(i+1) :
        if j == 0 :
            continue
        tot += seq[i][(N//2)+j]

for i in range(N-1, N//2, -1) :
    tot += np.sum(seq[i])
    for j in range(i-N//2) :
        sub += seq[i][j]
    for j in range(i-N//2) :
        sub += seq[i][N-1-j]


print(tot - sub)


# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n) :
    for j in range(s, e+1) :
        res +=a[i][j]
    if i < n//2 :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1
print(res)
# 와 이 방법은 상상도 못했다... ㄹㅇ
"""