# 2중 for문으로 2중 리스트 선언

array = [[0 for col in range(11)] for row in range(10)]

print(array) # 이것이 11열 10행 10x11 array

# 연산자와 for문으로 리스트 선언

array = [[0]*11 for i in range(10)]

print(array) # 10x11 array

# 연산자로 2중 리스트 선언

array = [[0]*11]*10

print(array)

# 2중 리스트의 인덱스
array[3][1] = '@'
print(array)

# 2중 리스트 출력
for i in array :
    for j in i :
        print(j, end=" ")
    print()