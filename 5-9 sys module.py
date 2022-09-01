#9 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해 보자.
# C:\> cd doit
# C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
# 55
# 외장함수 sys.argv를 사용해 보자.

import sys
result = 0
for argu in sys.argv :
    if argu == sys.argv[0] :
        continue
    else :
        result += int(argu)
print(result)

# numbers = sys.argv[1:] 파일 이름을 제외한 명령 행의 모든 입력
