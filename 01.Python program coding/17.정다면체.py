# 정다면체
"""
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이
높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

출력설명
첫 번째 줄에 답을 출력합니다.

입력예제 1
4 6

출력예제 1
5 6 7
"""
from collections import Counter
import re

while True :
    re_polyhedron = input("""원하는 N다면체,M다면체를 입력하세요.
N과 M은 4, 6, 8, 12, 20 중의 하나
N M (스페이스로 구분) : """)
    p = re.match("[4|6|8|12|20]{1,2}\s{1}[4|6|8|12|20]{1,2}$", re_polyhedron)
    if not p :
        print("입력을 잘못하셨습니다.")
        continue
    else :
        print("정답은")
        break
N, M = map(int, re_polyhedron.split(" "))
if N > M :
    tmp = N
    N = M
    M = tmp
# N < M 무조건
result = []
dic = {}
for i in range(1, N+1) :
    for j in range(1+i-1, M+1) :
        result.extend([i+j])
        dic['i+j'] = 1
        counter = Counter(result)
for i in counter.keys() :
    if counter[i] == max(counter.values()) :
        print(i, end=" ")
"""
cf. 내가 풀이한 방식은.. 주사위 2개가 (1,2), (2,1) 처럼 중복되는 건 빼서 구해 정답과 다름
"""
# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = -2147000000
for i in range(1, n+1) :
    for j in range(1, m+1) :
        cnt[i+j] += 1
for i in range(n+m+1) :
    if cnt[i] > max :
        max = cnt[i]
for i in range(n+m+1) :
    if cnt[i] == max :
        print(i, end = ' ')
"""
