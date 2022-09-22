# 점수계산
"""
OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다. 여러 개의 OX 문제로 만들어진 시험
에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기로 하였다.
1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음
문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째
문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계산한다.
예를 들어, 아래와 같이 10개의 OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경우
에는 0으로 표시하였을 때, 점수 계산은 아래 표와 같이 계산되어, 총 점수는 1+1+2+3+1+2=10점
이다.
채점 [ 1 0 1 1 1 0 0 1 1 0 ]
점수 [ 1 0 1 2 3 0 0 1 2 0 ]
시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오.

입력설명
첫째 줄에 문제의 개수 N (1 <= N <= 100)이 주어진다. 둘째 줄에는 N개 문제의 채점 결과를
나타내는 0 혹은 1이 빈칸을 사이에 두고 주어진다. 0은 문제의 답이 틀린 경우이고, 1은 문제의
답이 맞는 경우이다.

출력설명
첫째 줄에 입력에서 주어진 채점 결과에 대하여 가산점을 고려한 총 점수를 출력한다.

입력예제 1
10
1 0 1 1 1 0 0 1 1 0

출력예제 1
10
"""
import re

while True :
    try :
        pro_num = int(input("나온 문제의 개수를 입력하시오 : "))
        if pro_num < 1 or pro_num > 100 :
            print("N은 1이상 100이하로 설정해주세요.")
            continue
    except ValueError :
        print("숫자만 입력해주세요.")
        continue
    else: break
while True :
    checking_score = input("채점을 한 결과를 적으시오.\n0(틀린),1(맞은)(스페이스로 구분) : ")
    p = re.match("([0-1]\s{1})+[0-1]$", checking_score)
    if not p :
        print("0또는 1만 입력해주세요.")
        continue
    check_list = list(map(int,checking_score.split(" ")))
    if len(check_list) != pro_num :
        print("개수가 맞지 않습니다.")
        continue
    if p :
        break
score = 0
for i in range(len(check_list)) :
    if check_list[i] == 0 :
        score += 0
    if check_list[i] == 1 :
        score += 1
        for j in range(i+1, len(check_list)) :
            if check_list[j] == 1 :
                score += 1
            if check_list[j] == 0 :
                break
print(score)

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a :
    if x == 1 :
        cnt += 1
        sum += cnt
    else :
        cnt = 0
print(sum)
"""