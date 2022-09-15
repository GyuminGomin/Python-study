# Q6. 숫자의 총합 구하기
"""
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오.(단 숫자는 콤마로 구분하여 입력한다.)
65,45,2,3,45,8
"""
def totalsum() :
    def total_sum(nums) :
        sum = 0
        for i in nums :
            sum += int(i)
        print(sum)
    while True :
        try :
            numbers = input("숫자를 입력하시오. (여러숫자는 콤마로 구분) : ")
            numbers = numbers.split(',')
            total_sum(numbers)
        except ValueError :
            continue
        else :
            break
# totalsum()


# Q7. 한 줄 구구단
"""
사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.
    실행 예)
    구구단을 출력할 숫자를 입력하세요(2~9): 2
    2 4 6 8 10 12 14 16 18
"""
def gugu_dan() :
    def gugudan(number):
        for i in range(1, 10):
            print(number * i, end= " ")

    while True :
        try :
            gugu = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
            if gugu < 2 or gugu > 9 :
                continue
            elif type(gugu) != int :
                continue
        except ValueError :
            continue
        else :
            break
    gugudan(gugu)
# gugu_dan()


# Q8. 역순 저장
"""
다음과 같은 내용의 파일 09.Q8-abc.txt가 있다.
    AAA
    BBB
    CCC
    DDD
    EEE
이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
    EEE
    DDD
    CCC
    BBB
    AAA
"""
def reverse_load() :
    with open('09.Q8-abc.txt', 'r') as f :
        data = f.read()
        data = ''.join(reversed(data))
    with open('09.Q8-abc.txt', 'w') as f :
        f.write(data)
        print(data)
# reverse_load()


# Q9. 평균값 구하기
"""
다음과 같이 총 10줄로 이루어진 09.Q9-sample.txt 파일이 있다. sample.txt 파일의 숫자값을
모두 읽어 총합과 평균 값을 구한 후 평균 값을 09.Q9-result.txt 파일에 쓰는 프로그램을 작성하시오.
    70
    60
    55
    75
    95
    90
    80
    80
    85
    100
"""
import numpy as np
def cal() :
    with open ('09.Q9-sample.txt', 'r') as f :
        data = []
        lines = f.readlines()
        for line in lines :
            data += [int(line)]
    with open('09.Q9-result.txt', 'w', encoding='UTF-8') as f :
        total = np.sum(data)
        mean = np.mean(data)
        f.write("총합 : {}, 평균 : {}".format(total,mean))
        print(f'실행이 완료되었습니다.')
# cal()


# Q10. 사칙연산 계산기
"""
다음과 같이 동작하는 클래스 Calculator를 작성하시오.
    >>> cal1 = Calculator([1,2,3,4,5])
    >>> cal1.sum() # 합계
    15
    >>> cal1.avg() # 평균
    3.0
    >>> cal2 = Calculator([6,7,8,9,10])
    >>> cal2.sum() # 합계
    40
    >>> cal2.avg() # 평균
    8.0
"""
import numpy as np
class Calculator :
    def __init__(self, args = [5,3]) : # 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다.
        self.numbers = args
    def setdata(self, *args) :
        self.numbers = args
    def sum(self, *args):
        print(np.sum(self.numbers))
    def avg(self, *args) :
        print(np.mean(self.numbers))
    def __del__(self): # 괜히 쓸데없이 메모리 낭비하는 것을 방지하기 위함
        print("객체가 소멸하였습니다.")

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
del cal1
cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()
del cal2
cal3 = Calculator()
cal3.sum()
cal3.avg()