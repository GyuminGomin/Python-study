# 다음 코드의 결과값은 무엇일까?

a = "Life is too short, you need python"

if "wife" in a : print('wife')
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else : print("none")

# 결과값은 shirt

# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

number = 0
total = 0
while number <= 1000 :
    number += 1
    if number % 3 != 0 :
        continue
    else :
        total += number
print(total)

# while 문을 사용하여 별을 표시하는 프로그램을 작성해보자.
limit = 5
number = 0
while number < limit :
    number += 1
    print('*' * number)

# for문을 사용하여 1부터 100까지의 숫자를 출력해보자.
for i in range(1,101) :
    print(i, end=' ')
print('')

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70,60,55,75,95,90,80,85,100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
stu = [70,60,55,75,95,90,80,85,100]
mean = 0
for i in stu :
    mean += i
print(mean/len(stu))

# 리스트 중 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1,2,3,4,5]
result = []
for n in numbers :
    if n % 2 == 1 :
        result.append(n*2)
print (result)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
result = [n*2 for n in numbers if n % 2 == 1]
print (result)