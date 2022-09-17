# 자릿수의 합
"""
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는
프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성
해서 프로그래밍 하세요.

입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를
출력합니다.

입력예제 1
3
125 15232 97

출력예제 1
97
"""
import numpy as np
import re

def digit_num(x) : # 각 자릿수의 합을 구하는 함수
    while True :
        flag = False
        N_input = input("N개의 자연수를 입력하세요.(스페이스로 구분) : ")
        p = re.match("(\d+\s{1})+\d+$", N_input)
        if not p :
            print("숫자만 입력하세요. 또는 스페이스 오류입니다.")
            continue
        N_input_list = N_input.split(" ")
        if len(N_input_list) != x :
            print("숫자 개수를 맞춰주세요.")
            continue
        for i in N_input_list :
            if 10000000 < int(i) :
                flag = True
                print("자연수를 천만이하로 설정해주세요.")
                continue
        if flag == True :
            continue
        else : break
    total = 0 # 최댓값을 구하기 위한 변수

    for i in range(len(N_input_list)) :
        a = list(map(int,list(N_input_list[i])))
        if total < np.sum(a) :
            total = np.sum(a)
            index = N_input_list[i]
    print(index)

digit_num(3)

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x) :
    sum = 0
    while x > 0 :      #for i in str(x) :
        sum += x%10    #    sum += int(i)
        x = x//10      #return sum
    return sum
max = -2147000000
for x in a :
    tot = digit_sum(x)
    if tot > max :
        max = tot
        res = x
print(res)
"""