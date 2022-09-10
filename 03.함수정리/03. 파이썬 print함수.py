# print 함수
"""
에디터 실행화면에 결과물 출력하는 함수
파이썬 GUI 그래픽 프로그래밍이 아닌 경우 print()출력은 기본이며 디버깅을 위한 오류 출력에도 자주 사용
- ,와 +의 구분 (,는 스페이스 +는 공백없이)
- print("*3 문자 "*3) 는 엔터키가 그대로 적용됨 '*3도 같음
- print('문자열', end = '원하는 기호') 는 print다음에 오는 엔터를 원하는 기호로 바꿈
- print('문자열','문자열' sep = '원하는 기호') 문자열 사이에 원하는 기호를 넣음
    - f = open('dump.txt', 'w')
    - print('Hello Python', file = f) 파일 형식을 지정한대로 파일생성 또는 읽기 가능
파일인자는 출력결과를 파일, 표준에러처리?로 보낼 수 있음
- print('%d,%f,%s'%(123,1.23,'str')
- print( '%9d'%(123) )  >      123
- print( '%09d'%(123) )  >000000123

- print('Hello Python'.center(20))
- print('Hello Python!'.rjust(20))
- print('Hello Python!'.ljust(20))
- print('Hello Python!'.zfill(20))
- print('hello python!'.capitalize())
- print('hello python!'.upper())

"""

# print의 format함수 : 엄청 많음
"""
- print( '{}, {}, {}'.format(1,2,3)  >1, 2, 3
- print( '{0}, {1}, {2}'.format(1,2,3) >1, 2, 3
- print( '{abc}, {def}, {ghi}'.format(abc = 1, def = 2, ghi = 3) )  >1, 2, 3
    - a = 'apple'
    - b = 'banana'
    - print( 'a is {0[a]}, b is {0[b]}'.format(locals()) )  >a is apple, b is banana
    - print( 'a is {a}, b is {b}'.format(**locals()) )  >a is apple, b is banana
"""

