# 수들의 합
"""
N개의 수로 된 수열 A[1], A[2], ..., A[N]이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력설명
첫째 줄에 N(1<=N<=10,000), M(1<=M<=300,000,000)이 주어진다. 다음 줄에는 A[1], A[2],
...,A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력설명
첫째 줄에 경우의 수를 출력한다.

입력예제 1
8 3
1 2 1 3 1 1 1 2

출력예제 1
5
"""
import re
import numpy as np

while True :
    inp = input("N개의 수와 원하는 M을 적으시오. : ")
    p = re.match("(\d+\s{1}){1}\d+$", inp)
    if not p :
        print("숫자 또는 스페이스 오류입니다.")
        continue
    if p :
        N,M = map(int,inp.split(" "))
        break
while True :
    seq = input("N개의 수를 입력하세요.(스페이스로 구분) : ")
    p = re.match("(\d+\s{1})+\d+", seq)
    if not p :
        print("숫자 또는 스페이스 오류입니다.")
        continue
    seq_list = list(map(int,seq.split(" ")))
    if len(seq_list) != N :
        print("N개의 수만 입력 해 주세요.")
        continue
    if p :
        break

cnt = 0
for i in range(N) :
    for j in range(i, N) :
        if np.sum(seq_list[i:j+1]) == M :
            cnt += 1
print(cnt)

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True :
    if tot < m :
        if rt < n :
            tot += a[rt]
            rt += 1
        else :
            break
    elif tot == m :
        cnt += 1
        tot -= a[lt]
        lt += 1
    else :
        tot -= a[lt]
        lt += 1
print(cnt)
"""