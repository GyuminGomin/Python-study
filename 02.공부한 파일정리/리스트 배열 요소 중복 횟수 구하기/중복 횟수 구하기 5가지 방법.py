# 1.collections 모듈의 Counter
"""
from collections import Counter
array = ["1", "1", "1", "1", "2", "3", "4", "5"]

counter = Counter(array)

print(array)
print(counter)
print(dict(counter))
"""

# 2. for,try-except
"""
array = ["1", "1", "1", "1", "2", "3", "4", "5"]
counter = {}
for value in array :
    try : counter[value] += 1
    except : counter[value] = 1
print(array)
print(counter)
"""

# 3. for,in 사용하는 방법
"""
array = ["1", "1", "1", "1", "2", "3", "4", "5"]

counter = {}
for value in array :
    if value in counter :
        counter[value] += 1
    else :
        counter[value] = 1
print(array)
print(counter)
"""

# 4. List.count() 사용
"""
array = ["1", "1", "1", "1", "2", "3", "4", "5"]

print(array)
print("요소 '1' 갯수 : ", array.count('1'))
"""

# 5. 모든 요소들의 중복되는 횟수를 담은 dict에서 찾기
"""
array = ["1", "1", "1", "1", "2", "3", "4", "5"]

counter = {}
for value in array :
    try : counter[value] += 1
    except : counter[value] = 1
print(array)
print("요소 '1' 갯수 : ", counter['1'])
"""