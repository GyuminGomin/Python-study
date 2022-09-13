# K 번째 약수 -> 출처 : 한국정보올림피아드
"""
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
6을 예로 들면
    6 / 1 = 6 ... 0
    6 / 2 = 3 ... 0
    6 / 3 = 2 ... 0
    6 / 4 = 1 ... 2
    6 / 5 = 1 ... 1
    6 / 6 = 1 ... 0
그래서 6의 약수는 1, 2, 3, 6 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성

입력
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상
N 이하이다.

출력
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개숙 K개보다 적어서
K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.

입력 예제
6 3
출력 예제
3
"""
import re
while True :
    try :
        inp = input("원하는 숫자의 K번째 약수를 입력하시오. (입력 예시 : 6 3) -> (출력 : 3) : ")
        variable_list = []
        p = re.match('\d+\s{1}\d+', inp)
        if not p :
            print("다시 입력하시오.")
            print("-------------")
            continue
        inp_list = inp.split(' ')
        inp_list = list(map(int, inp_list))

        for i in range(1, inp_list[0]+1) :
            if inp_list[0] % i == 0 :
                variable_list.extend([i])
            else :
                continue
        print(variable_list)
        print(variable_list[inp_list[1] - 1])
    except IndexError :
        print(-1)
        break
    else :
        break

# 정답
"""
    실행 파일
    import sys
    sys.stdin = open("input.txt", "rt"
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1, n+1)
        if n%1 == 0 :
            cnt += 1
        if cnt == k :
            print(i)
            break
    else :
        print(-1)
    프로그램 파일 (input.txt)
    6 3
"""