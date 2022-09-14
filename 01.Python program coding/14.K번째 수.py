# K번째 수
"""
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

입력 설명
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
두 번째 줄에 N개의 숫자가 차례로 주어진다.

출력 설명
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.

입력 예제 1
2 # test case
6 2 5 3 # N, s, e, k
5 2 7 3 8 9 # N 개의 숫자가 차례로 주어진다.
15 3 10 3 # N, s, e, k
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15 # N 개의 숫자가 차례로 주어진다.

출력 예제 1
#1 7
#2 6

입력예제1 해설 :
case 1 : 2 7 3 8의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 7이다.
case 2 : 8 16 6 6 17 3 10 11의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 6이다.
"""

import re

def case_line() :
    while True :
        case_format = input("N(5<=N<=500) s(시작) e(끝) k(순서) : ")
        p = re.match("\d+\s{1}\d+\s{1}\d+\s{1}\d+", case_format)
        c_list = case_format.split()
        if not p:
            print("다시 입력하세요.")
            continue
        if len(c_list) != 4 :
            print("4개의 수만 입력해 주세요.")
            continue
        else :
            N, s, e, k = list(map(int, c_list))
            if N<5 or N>500 :
                print("N의 개수를 5이상 500미만으로 설정해주세요.")
                continue
            if k > abs(e-s)+1 or k > abs(s-e)+1 :
                print("k를 인덱스 범위에 맞도록 설정해주세요.")
                continue
            if s > N or e > N :
                print("s 또는 e를 N보다 작게 설정해주세요.")
                continue
            if s <= 0 or e <= 0 or k <= 0 :
                print("설정 값을 0보다 작게 설정할수 없습니다.")
                continue
            break
    while True :
        case = input("입력 N개 (스페이스로 구분) : ")
        p = re.match("(\d+\s{1})+\d+", case)
        case_list = case.split(" ")
        if not p :
            print("다시 입력하세요.")
            continue
        if len(case_list) != N:
            print("수를 맞춰주세요")
            continue
        else :
            break
    if e > s :
        case_list_order = case_list[s-1:e] # s부터 e까지의 수를 다른 리스트에 저장
    elif s > e :
        case_list_order = case_list[e-1:s]
    case_list_order.sort()
    return case_list_order[k-1]

while True :
    try :
        T = int(input("Test Case 1<=T<=10까지중 테스트할 갯수를 정하시오 : "))
        if T<1 or T>10 :
            print("T를 1이상 10이하로 설정해 주세요.")
            continue
    except ValueError :
        print("다시 입력해주세요.")
        continue
    else:
        break

dic = {} # 딕셔너리에 값 저장
for i in range(T) :
    dic['#{}'.format(i+1)] = case_line()
    if i == T-1 :
        break
for item in dic.items() :
    print(item[0], item[1])


# 정답
"""
import sys
sys.stdin=open("input.txt", "rt")
T=int(input()) # sys모듈로 파이썬 내장함수 input()을 사용하면, 파일안에 있는 문장을 가져옴
for t in range(T) : # T는 현재 \n으로 나누어진 문장의 갯수를 의미한다.
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
"""