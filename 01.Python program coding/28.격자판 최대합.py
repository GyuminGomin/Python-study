# 격자판 최대합

"""
5*5 격자판에 아래와 같이 숫자가 적혀있습니다.
[10, 13, 10, 12, 15]
[12, 39, 30, 23, 11]
[11, 25, 50, 53, 15]
[19, 27, 29, 37, 27]
[19, 13, 30, 13, 19]
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

출력설명
최대합을 출력합니다.

입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

출력예제 1
155
"""
import numpy as np
import re

while True :
    try :
        N = int(input("N*N격자판을 만들기 위해 N을 입력하세요 : "))
        if N > 50 or N < 1:
            print("N의 범위는 1이상 50이하입니다.")
            continue
    except ValueError :
        print("숫자만 입력해주세요.")
        continue
    else: break
grid_list = [[0]*N]*N
for i in range(N) :
    while True :
        grid = input("N개의 숫자를 입력하세요. : ")
        p = re.match("(\d{1,2}\s{1})+\d{1,2}$", grid)
        if not p :
            print("숫자또는 스페이스 오류입니다.")
            print("또는 숫자를 100미만으로 입력해주세요.")
            continue
        if len(grid.split(" ")) != N :
            print("숫자의 개수를 맞춰주세요.")
            continue
        if p :
            break
    grid_list[i] = list(map(int,grid.split(" ")))

m = 0
diagonal = 0
diagonal2 = 0

for i in grid_list : # 행을 더하는 값
    tot = np.sum(i)
    if tot > m :
        m = tot

for i in range(N) : # \대각선을 더하는 값
    diagonal += grid_list[i][i]
    tot = diagonal
    if tot > m and i == N-1:
        m = tot

for i in range(N) : # / 대각선을 더하는 값
    diagonal2 += grid_list[i][N-(i+1)]
    tot = diagonal2
    if tot > m and i == N-1:
        m = tot

for i in range(N) : # 열을 더하는 값
    column = 0
    for j in range(N) :
        column += grid_list[i][j]
        tot = column
        if tot > m and j == N-1 :
            m = tot

print(m)

# 정답
"""
import sys
sys.stdin = open("input.txt","r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n) :
    sum1=sum2=0
    for j in range(n) :
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
sum1=sum2=0
for i in range(n) :
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest :
    largest = sum1
if sum2 > largest :
    largest = sum2
print(largest)
"""