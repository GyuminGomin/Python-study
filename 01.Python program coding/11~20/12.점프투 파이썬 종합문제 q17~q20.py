# Q.17 기초 메타 문자
"""
다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
1. acccb
2. a....b
3. aaab
4. a.cccb
답 2
"""


# Q.18 문자열 검색
"""
다음 코드의 결괏값은 무엇일까?
    >>> import re
    >>> p = re.compile("[a-z]+")
    >>> m = p.search("5 python")
    >>> m.start() + m.end()
답 10
"""


# Q.19 그루핑
"""
다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을
사용하여 작성하시오.

    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7768

"""
import re
def phone_num() :
    phone_num = """
    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7768
    """
    p = re.compile('(\w+\s\d+[-]\d+[-])\d+')
    m1 = p.sub('\g<1>####',phone_num)
    print(m1)

# phone_num()

# 정답
"""
import re

s = # 사이에 """ """ 존재
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768


pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)
"""

# Q.20 전방탐색
"""
다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net,
lee@myhome.co.kr 등과 매치된다. 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌
이메일 주소는 제외시키는 정규식을 작성하시오.
    .*[@].*[.].*$
"""
def extension() :
    while True :
        inp = input("이메일만 입력하시오.(***@***.***형식) 종료(q or Q) : ")
        if inp == 'q' or inp == 'Q' :
            break
        p = re.compile('.*[@].*[.](com|net)$')
        m = p.match(inp)
        if m == None :
            print("***@***.com, ***@***.net 만 입력해주세요.")
            print("--------------------------------------")
            continue
        else :
            print(m.group())
            break

# extension()

# 정답
"""
    import re
    
    pat = re.compile(".*[@].*[.](?=com$|net$).*$")
    
    print(pat.match("pahkey@gmail.com"))
    print(pat.match("kim@daum.net"))
    print(pat.match("lee@myhome.co.kr"))
    
    # 꼭 긍정형 전방탐색을 쓸 필요가 없음
    # pat = re.compile(".*[@].*[.](com$|net$).*$")
    # 이거로 해도 성립
"""
