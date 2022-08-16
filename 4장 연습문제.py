# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd(num) :
    if num % 2 == 0 :
        print("짝수입니다!")
    else: print("홀수입니다!")
is_odd(4)

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. ( 단 입력으로 들어오는 수의 개수는 정해져 있지 않다. )
def cal_mean(*nums) :
    total = 0
    for num in nums :
        total += num
    print( total / len(nums) )

cal_mean(5,3,3,3)

# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

# 이 프로그램을 수행해 보자.

# 첫번째 숫자를 입력하세요:3
# 두번째 숫자를 입력하세요:6
# 두 수의 합은 36 입니다

# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# 다음 중 출력 결과가 다른 것 한 개를 골라 보자.

# print("you" "need" "python") # youneedpython
# print("you"+"need"+"python") # youneedpython
# print("you", "need", "python") # you need python
# print("".join(["you", "need", "python"])) # youneedpython