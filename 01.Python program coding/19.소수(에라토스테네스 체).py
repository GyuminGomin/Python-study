# 소수(에라토스테네스 체)
"""
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

출력설명
첫 줄에 소수의 개수를 출력합니다.

입력예제 1
20

출력예제 1
8
"""
while True :
    try :
        N = int(input("자연수 N을 입력하세요. : "))
        if N < 2 or N > 200000 :
            print("N을 2 이상 20만 이하로 설정해 주세요.")
            continue
    except ValueError :
        print("N은 자연수입니다.")
    else:
        break
decimal_list = []
for i in range(2, N+1) :
    decimal_list.extend([i])

for i in range(2, N+1) :
    for j in range(1, int(N/2+1)) :
        try:
            decimal_list.remove(i*(j+1))
        except ValueError :
            continue
print(decimal_list)
print(len(decimal_list))

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1) :
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i) :
            ch[j] = 1
print(cnt)
"""