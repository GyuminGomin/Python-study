# K번째 큰 수
"""
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장
있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다.
3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을
작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값은
22 입니다.

입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.

출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

입력예제 1
10 3
13 15 34 23 45 65 33 11 26 42

출력예제 1
143
"""

import re

while True :
    print("#1")
    s_input = input("N(3<=N<=100) K(1<=K<=50) : ")
    p = re.match("\d+\s{1}\d+$",s_input)
    if not p :
        print("다시 입력하세요.(숫자 또는 스페이스 또는 갯수 오류)")
        continue
    N, K = map(int,s_input.split(" "))
    if N < 3 or N > 100 :
        print("N을 3이상 100이하로 설정해주세요.")
        continue
    if K < 1 or K > 50 :
        print("K를 1이상 50이하로 설정해주세요.")
        continue
    if K > N*(N-1)*(N-2)/6 :
        print("K가 나올 수 있는 경우의 수보다 큽니다.")
        continue
    if p :
        print("#2")
        break
while True :
    N_input = input("N개의 숫자를 입력하세요. (스페이스로 구분) : ")
    p = re.match("(\d+\s{1})+\d+$",N_input)
    if not p :
        print("다시 입력하세요.(숫자 또는 스페이스 또는 갯수 오류)")
        continue
    N_list = list(map(int,N_input.split(" ")))
    if p :
        break
n_list = [] # 뽑은 숫자를 저장하는 곳
for i, i_nums in enumerate(N_list) :
    for j, j_nums in enumerate(N_list) :
        if i <= j :
            continue
        for k, k_nums in enumerate(N_list) :
            if i <= k or j <= k :
                continue
            else :
                n_list.extend([i_nums + j_nums + k_nums])
n_list.sort(reverse=True)
for i, nums in enumerate(n_list) :
    if i == len(n_list)-1 :
        break
    if n_list[i] == n_list[i+1] :
        n_list.remove(nums)
print(n_list[K-1])

# 정답
"""
import sys
sys.stdin = open("input.txt", "rt")
n ,k = map(int, input().split())
a = list(map(int, input().split())
res = set()
for i in range(n) :
    for j in range(i+1, n) :
        for m in range(j+1, n) :
        res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
"""

