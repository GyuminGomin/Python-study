# 회문 문자열 검사
"""
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다.
각 단어의 길이는 100을 넘지 않는다.

출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

입력예제 1
5
level
moon
abcba
soon
gooG

출력예제 1
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
"""
while True :
    try :
        N = int(input("N을 입력하세요.(원하는 입력 단어 갯수) : "))
    except ValueError :
        print("숫자만 입력해주세요.")
        continue
    else : break
w_list = [] # 단어 모으는 곳
c = 0
while True :
    if c == N :
        break
    words = input("단어를 입력하세요. : ")
    if len(list(words)) >= 100 :
        print("단어의 길이는 100을 넘으면 안됩니다.")
        continue
    rev_words = list(words).copy()
    rev_words.reverse()
    if words.upper() == ''.join(rev_words).upper() :
        c += 1
        w_list.extend(["YES"])
    else :
        c += 1
        w_list.extend(["NO"])

for i, ok in enumerate(w_list) :
    print("#{0} {1}".format(i+1, ok))

# 정답
"""
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
for i in range(n) :                     
    s = input()
    s = s.upper()
    size = len(s)                       if s == s[::-1] :
    for j in range(size//2) :               print("#d YES" %(i+1))
        if s[j] != s[-1-j] :            else :
            print("#%d NO" %(i+1))          print("%d NO" %(i+1))
            break
        else :
            print("#%d YES" %(i+1))
"""