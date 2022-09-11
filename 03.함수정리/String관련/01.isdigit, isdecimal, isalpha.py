# isdigit()
"""
string 클래스에 있는 메서드
문자열이 '숫자'로만 이루어져있는지 확인하는 함수
문자열이 '단 하나'라도 있다면 False를 반환
모든 문자열이 '숫자'로만 이루어져 있으면 True를 반환

사용법
    str.isdigit(문자열)
    문자열.isdigit()
"""
a = "BlockDMask"  # 문자로만 이루어짐
b = "1234Blog"    # 문자 + 숫자
c = "131231"      # 숫자
d = "-234"        # 음수
e = "1.23"        # 소수점
f = "3²"          # 3의 2제곱 기호 숫자
g = "⅔"           # 수학 기호 숫자 2/3
h = "0"           # 0
i = "0123"        # 0 으로 시작한 숫자

# str.isdigit("문자열")
print(f"str.isdigit('{a}') : {str.isdigit(a)}")
print(f"str.isdigit('{b}') : {str.isdigit(b)}")
print(f"str.isdigit('{c}') : {str.isdigit(c)}")
print(f"str.isdigit('{d}') : {str.isdigit(d)}")
print(f"str.isdigit('{e}') : {str.isdigit(e)}")
print(f"str.isdigit('{f}') : {str.isdigit(f)}")
print(f"str.isdigit('{g}') : {str.isdigit(g)}")
print(f"str.isdigit('{h}') : {str.isdigit(h)}")
print(f"str.isdigit('{i}') : {str.isdigit(i)}")

print()

# "문자열".isdigit()
print(f"'{a}'.isdigit() : {a.isdigit()}")
print(f"'{b}'.isdigit() : {b.isdigit()}")
print(f"'{c}'.isdigit() : {c.isdigit()}")
print(f"'{d}'.isdigit() : {d.isdigit()}")
print(f"'{e}'.isdigit() : {e.isdigit()}")
print(f"'{f}'.isdigit() : {f.isdigit()}")
print(f"'{g}'.isdigit() : {g.isdigit()}")
print(f"'{h}'.isdigit() : {h.isdigit()}")
print(f"'{i}'.isdigit() : {i.isdigit()}")

# isalpah() - 알파벳으로만 이루어져 있는가, isdecimal() - 0~9사이의 숫자로만 이루어져 있는가