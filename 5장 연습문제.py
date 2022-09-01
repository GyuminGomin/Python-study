#1 다음은 Calculator 클래스이다.
class Calculator :
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해보자.
# 즉 다음과 같이동작하는 클래스를 만들어야 한다.

class UpgradeCalculator(Calculator) :
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

#2 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
# 즉 다음과 같이 동작해야 한다.
class MaxLimitCalculator(Calculator) :
    def add(self, val):
        self.value += val
        if self.value > 100 :
            self.value = 100
cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력
# 단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다. (위의 calculator 클래스)

#3 다음 결과를 예측해 보자.
# 하나.
print(all([1, 2, abs(-3)-3])) # False
# 둘.
print(chr(ord('a')) == 'a') # True --> ord는 유니코드 값을 돌려주는 내장 함수

#4 filter와 lambda를 사용하여 리스트[1,-2,3,-5,8,-3]에서 음수를 모두 제거해 보자.
# filter은 첫번째 인자로 함수를 두번째 인자로 반복가능한 자료형을 받아 함수의 출력값이 True인 두번째 인자의 요소만 가져온다.
print(list(filter(lambda x: x>0,[1,-2,3,-5,8,-3])))

#5 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
hex(234)
# 이번에는 반대로 16진수의 문자열 0xea를 10진수로 변경해 보자.
print(0xea) # 이렇게 말고 int('0xea', 16)을 해도 됨

#6 map과 lambda를 사용하여 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어 보자.
# map은 filter와 비슷하지만 filter는 True,False에서 True만 가져온다면, map은 그 입력값에 해당하는 산수를 해서 출력한다.
print(list(map(lambda x : x*3, [1,2,3,4])))

#7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
l = [-8,2,7,5,-3,5,0,1]
print(max(l) + min(l))

#8 17/3의 결과는 다음과 같다. 5.666666666
# 위와 같은 결괏값 5.6666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
print(round(17/3,4))




