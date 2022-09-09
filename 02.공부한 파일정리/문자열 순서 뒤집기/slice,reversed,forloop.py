string = 'Hello Python'

# slice
"""
slice는 [start : stop : step]을 의미
"""
reversed_str = string[::-1]
print(f'Origin: {string}')
print(f'reversed: {reversed_str}')

# reversed()로 문자열 순서 뒤집기
"""
반대방향으로 순회하는 iterator를 리턴함
join()으로 리턴된 iterator의 데이터를 하나의 string으로 만들면, 뒤집어진 문자열 가능
join함수내에서만 사용할 수 있음!!
"""
reversed_str = "".join(reversed(string))
print(f'Origin: {string}')
print(f'reversed: {reversed_str}')

# for loop로 문자열 순서 뒤집기
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str
print(f'Original: {string}')
print(f'reversed: {reversed_str}')