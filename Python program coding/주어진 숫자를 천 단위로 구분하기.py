# 조건
"""
1. 사용자로부터 숫자를 입력받아 천 단위 마다 콤마를 구분하여 숫자를 출력
2. 입력 받는 숫자를 변수 num에 저장한다.
3. 입력받은 정보가 숫자로만 되어 있는지 확인한다.
"""
while True :
    try :
        user = int(input("숫자를 입력하시오. : "))
    except ValueError :
        continue
    else :
        num = user
        break
print(format(num, ','))
print('{:0,.1f}'.format(num))
print(num)

