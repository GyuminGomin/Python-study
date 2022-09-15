# Q11. 모듈 사용
"""
C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서
파이썬 셀을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
(즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)
    > import mymod
    >
"""
# 정답
"""
1. sys 모듈 사용하기
sys.path에 C:\doit 이라는 디렉터리를 추가하면 C:\doit 디렉토리에 있는 mymod 모듈 사용 가능
    >>> import sys
    >>> sys.path.append("c:/doit")
    >>> import mymod
2. PYTHONPATH 환경 변수 사용하기
PYTHONPATH 환경 변수에 C:\doit 디렉토리를 지정하면 C:\doit 디렉토리에 있는 mymod 모듈 사용 가능
    C:\Users\home>set PYTHONPATH=c:\doit
    C:\Users\home>python
    >>> import mymod
3. 현재 디렉토리 사용하기
파이썬 셀을 mymod.py가 있는 위치로 이동하여 실행해도 mymod 모듈을 사용할 수 있음
왜냐하면 sys.path 에는 현재 디렉토리인 . 이 항상 포함되어 있기 때문이다.
"""

# Q12. 오류와 예외 처리
"""
다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
    result = 0
    
    try:
        [1, 2, 3][3]
        "a"+1
        4 / 0
    except TypeError:
        result += 1
    except ZeroDivisionError:
        result += 2
    except IndexError:
        result += 3
    finally:
        result += 4
    
    print(result)
"""
# 정답
"""
7
try 문에서 오류가 발생하면 다음구문은 실행되지 않고 바로 except로 넘어간 후 실행이 끝난다.
그리고 "a"+1 에서 1이 자동으로 string으로 변환된다고 생각했는데 아니었고,
Type Error가 뜬다.
"""

# Q13. DashInsert 함수
"""
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수
사이에 -를 추가하고, 짝수가 연속되면*를 추가하는 기능을 갖고 있다. DashInsert함수를 완성하시오.
    입력 예시: 4546793
    출력 예시: 454*67-9-3
"""
def DashInsert() :
    def dashInsert(numbers) :
        num_list = list(map(int, list(numbers))) # map(int, list(numbers)) 만 하면 주소가 반환된다.
        num_list_clone = num_list.copy() # 미리 데이터를 다 복사해서 힘들었다..
        run_num = 0 # insert를 수행한 횟수를 표시
        for i in range(len(numbers)-1) :
            if num_list[i] % 2 == 0 and num_list[i+1] % 2 == 0 :
                num_list_clone.insert(i+1+run_num,'*')
                run_num += 1
            elif num_list[i] % 2 == 1 and num_list[i+1] % 2 == 1 :
                num_list_clone.insert(i+1+run_num,'-')
                run_num += 1
            else :
                continue
        num_list_clone = list(map(str,num_list_clone))
        result = ''.join(num_list_clone)
        print('출력 : {}'.format(result))
    while True :
        try :
            inp = input("입력 (숫자만): ")
            dashInsert(inp)
        except ValueError :
            continue
        else :
            break
# DashInsert()
# 정답
"""
    data = "4546793"
    numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
    result = []
    
    for i, num in enumerate(numbers): # 인덱스를 지정할 수 있는 함수
        result.append(str(num)) # 데이터 값 복사
        if i < len(numbers)-1:                   # 다음 수가 있다면
            is_odd = num % 2 == 1                # 현재 수가 홀수
            is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
            if is_odd and is_next_odd:           # 연속 홀수
                result.append("-")
            elif not is_odd and not is_next_odd: # 연속 짝수
                result.append("*")
    
    print("".join(result))
"""


# Q14. 문자열 압축하기
"""
문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을
압축하여 표시하시오.
    입력 예시: aaabbcccccca
    출력 예시: a3b2c6a1
"""

def RepeatInsert() :
    def repeatInsert(strings):
        str_list = list(strings)
        str_list_clone = str_list.copy()
        repeat_num = 1 # 반복되는 숫자 개수
        odd_num = 1 # 1,3,5,7,9에 숫자를 넣기위함
        for i in range(len(strings) - 1):
            if str_list[i] == str_list[i + 1] :
                alpa = str_list[i]
                str_list_clone.remove(alpa) # 알파벳 하나를 제거
                repeat_num += 1
            else:
                str_list_clone.insert(odd_num, str(repeat_num)) # a4b aaaabb
                odd_num += 2
                repeat_num = 1 # 1로 계속 초기화를 해줘야 함
                continue
        str_list_clone.insert(odd_num+2, str(repeat_num)) # 맨마지막 수를 넣어주기 위함
        result = ''.join(str_list_clone)
        print('출력 : {}'.format(result))

    inp = input("입력 (갯수 변환기): ")
    repeatInsert(inp)
# RepeatInsert()
# 정답
"""
    def compress_string(s):
        _c = ""
        cnt = 0
        result = ""
        for c in s:
            if c!=_c:
                _c = c
                if cnt: result += str(cnt)
                result += c
                cnt = 1
            else:
                cnt +=1
        if cnt: result += str(cnt)
        return result
    
    print(compress_string("aaabbcccccca"))  # a3b2c6a1 출력
"""

# Q15. Duplicate Numbers
"""
0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지
확인하는 함수를 작성하시오.
    입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
    출력 예시: True False False True False
"""
def dupli_nums() :
    inp = input("숫자를 입력하시오.(스페이스로 숫자 여러개 확인 가능) ex.1234 3456 : ")
    inp_list = inp.split(" ") # 분리된 리스트 갯수
    for i in range(len(inp_list)) :
        globals()["num_list{}".format(i)] = list(map(int, inp_list[i])) # global함수로 for문과 함께 변수 여러개 만들기
    # 선언 방식은 globals()['num_list0']

    for i in range(len(inp_list)) :
        for j in range(10) :
            if globals()['num_list{}'.format(i)].count(j) != 1 :
                print(False, end=" ")
                break
            else :
                if j == 9 :
                    print(True, end=" ")
                continue
# dupli_nums()

# 정답
"""
    def chkDupNum(s):
        result = []
        for num in s:
            if num not in result:
                result.append(num)
            else:
                return False
        return len(result) == 10
        
    print(chkDupNum("0123456789"))      # True 리턴
    print(chkDupNum("01234"))           # False 리턴
    print(chkDupNum("01234567890"))     # False 리턴
    print(chkDupNum("6789012345"))      # True 리턴
    print(chkDupNum("012322456789"))    # False 리턴
"""