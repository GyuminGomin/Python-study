# 대표값
"""
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높은
점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수가
주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림
합니다.

입력예제 1
10
45 73 66 87 92 67 75 79 75 80

출력예제 1
74 7

예제설명)
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가
높은 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.
"""

import numpy as np

while True :
    try :
        stu_numbers = int(input("학생의 수를 입력하세요 : "))
        if stu_numbers < 5 or stu_numbers > 100 :
            print("학생들의 수를 5이상 100이하로 설정해주세요.")
            continue
    except ValueError :
        print("숫자만 입력해주세요.")
        continue
    else:
        break
while True :
    try :
        stu_points = input("N명의 점수를 번호에 맞게 입력하세요.(스페이스로 구분) : ")
        if len(stu_points.split(" ")) != stu_numbers :
            print("학생들의 수에 맞도록 다시 작성해주세요. 또는 스페이스 에러입니다.")
            continue
        points_list = list(map(int,stu_points.split(" ")))
        if max(points_list) > 100 :
            print("학생들의 점수는 100점을 넘을 수 없습니다.")
            continue
    except ValueError :
        print("숫자만 입력해주세요. 또는 스페이스 에러입니다.")
        continue
    else :
        break
k_mean_diff = 101 # 차이를 통해서 최솟값 구하기
k_mean_num = 0 # 숫자 저장
index = 0 # 인덱스
mean = round(np.mean(points_list)) # 평균
for i in range(stu_numbers) :
    if k_mean_diff >= abs(points_list[i]-mean) :
        if k_mean_diff == abs(points_list[i]-mean) and k_mean_num == points_list[i] :
            continue
        k_mean_diff = abs(mean-points_list[i])
        k_mean_num = points_list[i]
        index = i+1
print("평균",mean)
print("학생점수",k_mean_num,"순서", index)


# 최솟값 구하기
"""
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 파이썬에서 가장 큰 수 무한대 값을 의미함.
for i in range(len(arr)) : # for x in arr :
if arr[i] < arrMin :       #     if x < arrMin :
    arrMin=arr[i]          #         arrMin = x
print(arrMin)              # print(arrMIn)
"""

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a) :
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :
        if x > score :
            score = x
            res = idx + 1
print(ave, res)
"""
        
