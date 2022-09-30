# 곳감(모래시계)

"""
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으로 이루
어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 각자의 행을 기준으로
왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령입니다.
[ 10 13 10 12 15 ]              [ 10 13 10 12 15 ]
[ 12 39 30 23 11 ] -          - [ 23 11 12 39 30 ] -
[ 11 25 50 53 15 ]      ->      [ 11 25 50 53 15 ]
[ 19 27 29 37 27 ]              [ 19 27 29 37 27 ]
[ 19 13 30 13 19 ]              [ 19 13 30 13 19 ]
첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전
하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감이 총 몇 개가
있는지 출력하는 프로그램을 작성하세요.
[ 10 13 10 12 15 ]
[    11 12 39    ]
[       50       ]
[    27 29 37    ]
[ 19 13 30 13 19 ]

입력설명
첫 줄에 자연수 N(3<=N<=20) 이 주어지며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보
가 M줄에 걸쳐 주어집니다.

출력설명
총 감의 개수를 출력합니다.

입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4

출력예제 1
362
"""
import copy
import re
import numpy as np

while True :
    try :
        N = int(input("3<=N<=20 의 자연수를 입력하세요.(홀수) : "))
        if N < 3 or N > 20 or N%2 == 0:
            print("N은 3이상 20이하의 홀수 입니다.")
            continue
    except ValueError :
        print("자연수만 입력해 주세요.")
        continue
    else : break

seq_list = [[0]*N]*N
for i in range(N) :
    while True :
        inp = input("N개의 자연수를 입력하세요. : ")
        p = re.match("(\d{1,2}\s{1})+\d{1,2}$", inp)
        if not p :
            print("숫자 또는 스페이스 오류입니다.")
            print("또는 자연수는 100을 초과할 수 없습니다.")
            continue
        if len(inp.split(" ")) != N :
            print("개수를 N개로 맞춰주세요.")
            continue
        if p :
            seq_list[i] = list(map(int, inp.split(" ")))
            break

while True :
    try :
        M = int(input("1<=M<=10 의 자연수를 입력하세요. : "))
        if M < 1 or M > 10 :
            print("M은 1이상 10이하의 자연수 입니다.")
            continue
    except ValueError :
        print("자연수만 입력해 주세요.")
        continue
    else : break

for i in range(M) :
    while True :
        cSeq_list = copy.deepcopy(seq_list)
        inp = input("행 방향(0,1) 횟수 를 입력해주세요. : ")
        p = re.match("\d+\s{1}[0-1]\s{1}\d+$", inp)
        if not p :
            print("숫자 또는 스페이스 또는 방향 또는 개수 오류 입니다.")
            continue
        if p :
            l, d, c = map(int,inp.split(" "))
            if d == 1 : # 오른쪽
                for j in range(c) :
                    cSeq_list = copy.deepcopy(seq_list)
                    for i in range(N) :
                        if i == N-1 :
                            seq_list[l-1][0] = cSeq_list[l-1][i]
                        else :
                            seq_list[l-1][i+1] = cSeq_list[l-1][i]
            elif d == 0 : # 왼쪽
                for j in range(c) :
                    cSeq_list = copy.deepcopy(seq_list)
                    for i in range(N) :
                        if i == 0 :
                            seq_list[l-1][N-1] = cSeq_list[l-1][i]
                        else :
                            seq_list[l-1][i-1] = cSeq_list[l-1][i]
            break

tot = 0
for i in range(N//2+1) :
    tot += np.sum(seq_list[i])
    for j in range(i) :
        tot -= seq_list[i][0+j]
        tot -= seq_list[i][N-1-j]
for i in range(N//2+1, N) :
    for j in range(i-N//2+1) :
        if j == 0 :
            tot += seq_list[i][N//2]
        else :
            tot += seq_list[i][N//2 + j]
            tot += seq_list[i][N//2 - j]

print(tot)

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m) :
    h, t, k = map(int, input().split())
    if t == 0 :
        for _ in range(k) :
            a[h-1].append(a[h-1].pop(0))
    else :
        for _ in range(k) :
            a[h-1].insert(0, a[h-1].pop())
res = 0
s = 0
e = n-1
for i in range(n) :
    for j in range(s, e+1) :
        res += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1
print(res)
"""