# 정규 표현식(Regular Expressions)
"""
복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는
모든 곳에서 사용한다.
- 정규 표현식을 줄여서 "정규식"이라고도 말한다.
"""

# 문제
"""
다음과 같은 문제가 주어졌다고 가정해 보자.
    주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의
    뒷자리를 * 문자로 변경해 보자.
"""

    # 정규식 안사용한 것

# data = """
# park 800905-1049118
# kim  700905-1059119
# """
#
# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))


    # 정규식 사용

# import re
#
# data = """
# park 800905-1049118
# kim  700905-1059119
# """
#
# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))


# 1. 정규 표현식의 기초, 메타 문자
"""
정규표현식에서 사용하는 메타 문자(meta characters)에는 다음과 같은 것이 있다.
    . ^ $ * + ? { } [ ] \ | ( )
정규 표현식에 위 메타 문자를 사용하면 특별한 의미를 갖게 된다.
"""

    # 문자 클래스 []
"""
"[ ] 사이의 문자들과 매치"라는 의미를 가짐
- [] 안엔 어떤 문자도 들어갈 수 있다.
    [abc] -> "a,b,c중 한 개의 문자와 매치"
- [] 안의 두 문자 사이에 하이폰(-)을 사용하면 두 문자 사이의 범위(From-To)를 의미
    [a-c] -> [abc]와 동일, [0-5] -> [012345]와 동일
- [^0-9] -> 0~9의 수를 빼고 전부 (not의 의미가 있다.)

    cf) 별도의 표기법
    \d  ==  [0-9]
    \D  ==  [^0-9]
    \s  ==  [ \t\n\r\f\v]
    \S  ==  [^ \t\n\r\f\v]
    \w  ==  [a-zA-Z0-9_] 문자,숫자와 매치
    \W  ==  [^a-zA-Z0-9] 문자,숫자 아닌 문자와 매치
"""

    # Dot(.)
"""
정규식 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨
- 참고로 정규식 작성할 때 re.DOTALL 옵션을 주면 \n 문자와도 매치됨
    a.b == aab == a0b -> "a + 모든문자 + b" 
    a[.]b != aab != a0b -> "a + Dot(.)문자 + b"
    - cf) 문자 클래스 [] 내에 .은 모든 문자가 아니라 .문자 한개를 의미
"""

    # 반복(*)
"""
ca*t
* 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미 -> 메모리 제한으로 2억 개정도만 가능

정규식 ca*t
문자열 ct, cat, caaat 모두 Match
"""

    # 반복(+)
"""
ca+t
+ 앞에 있는 문자 a가 최소 한번 이상 반복될 때 사용
"""

    # 반복({m,n}, ?)
"""
{}메타 문자를 사용하면 반복 횟수를 고정할 수 있다.
{1,}는 +와 동일, {0,}는 *와 동일
    ca{2}t -> 반드시 a 2번 반복
    ca{2,5}t -> 반드시 a 2번이상 5번이하 반복
?메타 문자가 의미하는 것은 {0,1}
    ab?c -> b가 있어도 되고 없어도 된다.
"""


# 2. 파이썬에서 정규 표현식을 지원하는 re모듈
"""
파이썬은 정규 표현식을 지원하기 위해 re(regular expression) 모듈을 제공한다.
re 모듈은 파이썬을 설치할 때 자동으로 설치되는 기본 라이브러리이다.
    >>> import re
    >>> p = re.compile('ab*')
    위는 사용방법
"""


# 3. 정규식을 이용한 문자열 검색
"""
컴파일된 패턴 객체를 사용하여 문자열 검색을 수행. 컴파일 된 패턴 객체는 다음과 같은 4가지
메서드를 제공한다.
    match() -> 문자열의 처음부터 정규식과 매치되는지 조사한다.
    search() -> 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
    findall() -> 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
    finditer() -> 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
match, search 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려줌
"""

    # match
"""
    >>> import re
    >>> p = re.compile('[a-z]+')
match 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다. 위 패턴에 match 메서드 수행
>>> m = p.match("python")
>>> print(m)
"""
# import re
# p = re.compile('[a-z]+')
#
# m = p.match("python")
# print(m) # <re.Match object; span=(0, 6), match='python'>
#
# m = p.match("3 python")
# print(m) # None (처음부터 조사하기 때문에 3이 뒤에 붙어 있으면 python이 그대로 출력)

# 아래의 방식으로 사용함 match함수안에 group함수 존재
# m = p.match( 'string goes here' )
# if m:
#     print('Match found: ', m.group())
# else:
#     print('No match')

    # search
"""
    >>> import re
    >>> p = re.compile('[a-z]+')
match는 첫 문자부터 순서대로 살펴보지만, search는 모든 문자를 살펴보고 제거할건 제거함
>>> m = p.search("python")
>>> print(m)
<re.Match object; span=(0, 6), match='python'>

>>> m = p.search("3 python")
>>> print(m)
<re.Match object; span=(2, 8), match='python'>
"""

    # findall
"""
    >>> import re
    >>> p = re.compile('[a-z]+')
정규식과 매칭되는 모든 문자열을 리스트로 돌려줌
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']
"""

    # finditer
"""
    >>> import re
    >>> p = re.compile('[a-z]+')
정규식과 매칭되는 모든 문자열을 반복 가능하 객체로 돌려줌
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x01F5E390>
>>> for r in result: print(r)
...
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
"""


# 4. match 객체의 메서드
"""
match 메서드와 search 메서드를 통해 돌려준 match 객체에 대해 알아봄
    group() -> 매치된 문자열을 돌려준다.
    start() -> 매치된 문자열의 시작 위치를 돌려준다.
    end() -> 매치된 문자열의 끝 위치를 돌려준다.
    span() -> 매치된 문자열의 (시작,끝)에 해당하는 튜플을 돌려준다.
"""
# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(m.group()) # python
# print(m.start()) # 0
# print(m.end()) # 6 (위치라 5일줄 알았는데, +1이 되네)
# print(m.span()) # (0,6)

# import re
# p = re.compile('[a-z]+')
# m = p.search("3 python")
# print(m.group()) # python
# print(m.start()) # 2
# print(m.end()) # 8
# print(m.span()) # (2,8)
"""
import re
p = re.compile('[a-z]+')
m = p.search("3 python")
위 코드를 축약할 수 있음
import re
m = re.search('[a-z]+','3 python')
"""


# 5. 컴파일 옵션
"""
정규식을 컴파일 할 때 다음 옵션을 사용할 수 있다.
    DOTALL(S) -> .이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
    IGNORECASE(I) -> 대소문자에 관계없이 매치할 수 있도록 한다.
    MULTILINE(M) -> 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관련)
    VERBOSE(X) -> verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들 수
    있고 주석등을 사용할 수 있게된다.)
    - cf) 옵션을 사용할 때, re.DOTALL 처럼 전체 옵션 이름을 써도 되고, re.S처럼 약어도 가능
"""

    # DOTALL, S
"""
. 메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 있다. 만약 \n 문자도
포함하여 매치하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 됨

    >>> import re
    >>> p = re.compile('a.b')
    >>> m = p.match('a\nb')
    >>> print(m)
    None
정규식이 a.b인 경우 문자열 a\nb는 매치되지 않는다.
    
    >>> import re
    >>> p = re.compile('a.b', re.DOTALL)
    >>> m = p.match('a\nb')
    >>> print(m)
    <re.Match object; span=(0, 3), match='a\nb'>
보통 re.DOTALL 옵션은 여러 줄로 이루어진 문자열에서 \n에 상관없이 검색할 때 많이 사용됨
"""

    # IGNORECASE, I
"""
대 소문자 구별 없이 매치를 수행할 때 사용하는 옵션
    
    >>> import re
    >>> p = re.compile('[a-z]+', re.I)
    >>> p.match('python')
    <re.Match object; span=(0, 6), match='python'>
    >>> p.match('Python')
    <re.Match object; span=(0, 6), match='Python'>
    >>> p.match('PYTHON')
    <re.Match object; span=(0, 6), match='PYTHON'>
"""

    # MULTILINE, M
"""
여러 줄과 매치될 수 있도록 수행할 때 사용하는 옵션
^메타 문자는 문자열의 처음을 의미
$메타 문자는 문자열의 마지막을 의미
예를 들어 정규식이 ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고,
만약 정규식이 python$ 이라면 문자열의 마지막은 항상 python으로 끝나야 한다.

"""

# import re
#
# p = re.compile("^python\s\w+")
#
# data = """python one
# life is too short
# python two
# you need python
# python three"""
#
# print(p.findall(data))

# "^python\s\w+" 정규식은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에
# 단어가 와야 한다는 의미이다.

"""
^ 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우
이럴 때 사용하는 옵션이 바로 re.MULTILINE 또는 re.M이다.
"""

# import re
# p = re.compile("^python\s\w+", re.MULTILINE)
#
# data = """python one
# life is too short
# python two
# you need python
# python three"""
#
# print(p.findall(data))

    # VERBOSE, X
"""
보기 어렵고 이해하기 힘든 정규식을 주석 또는 줄 단위로 구분할 수 있게 해주는 옵션
re.VERBOSE, re.X

re.VERBOSE 옵션을 사용하면, 문자열에 사용된 whitespace는 컴파일할 때 제거된다.
(단 []안에 사용한 whitespace는 제외). 그리고 줄 단위로 #기호를 사용해 주석 작성가능
"""

# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# # 위 정규식을 바꿔주면

# charref = re.compile(r"""
# &[#]                # Start of a numeric entity reference
#  (
#      0[0-7]+         # Octal form
#    | [0-9]+          # Decimal form
#    | x[0-9a-fA-F]+   # Hexadecimal form
#  )
#  ;                   # Trailing semicolon
# """, re.VERBOSE)


# 5. 백슬래시 문제
"""
정규 표현식을 파이썬에서 사용할 때 혼란을 주는 요소가 한 가지 있는데, 바로 백슬래시(\)이다.

ex. 어떤 파일 안에 있는 "\section" 문자열을 찾기 위한 정규식을 만든다고 가정해 보자.
    \section == [ \t\n\r\f\v]ection -> 이 정규식은 \s 문자가 whitespace로 해석되어 의도한 대로 매치가 이루어지지 않는다.
    의도한 대로 매치하고 싶다면, \\section처럼 변경해야 한다.
        >>> p = re.compile('\\section')
    정규식 엔진에 \\문자를 전달하려면 파이썬은 \\\\처럼 4개나 사용해야 한다.
        >>> p = re.compile('\\\\section')
    이러한 문제로 인해 파이썬 정규식에는 Raw String 규칙이 생겨나게 되었다.
    컴파일해야 하는 정규식이 Raw String임을 알려 줄 수 있도록 파이썬 문법을 만든 것
        >>> p = re.compile(r'\\section')       
"""

# 6. 메타 문자
"""
+,*,[],{}등의 메타 문자는 매치가 진행될 때 현재 맻되고 있는 문자열의 위치가 변경된다.(보통 소비된다고 표현)
이와 달리 문자열을 소비시키지 않는 메타 문자도 있다. 이것을 문자열 소비가 없는(zerowidth assertions) 메타문자
"""

    # |
"""
| 메타 문자는 or과 동일한 의미로 사용된다. A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.
    >>> p = re.compile('Crow|Servo')
    >>> m = p.match('CrowHello')
    >>> print(m)
    <re.Match object; span=(0, 4), match='Crow'>
"""

    # ^
"""
^ 메타 문자는 맨 처음과 일치함을 의미한다. re.MULTILINE을 사용할 경우엔 여러 줄의 문자열
일 때 각 줄의 처음과 일치 하게 된다.
    >>> print(re.search('^Life', 'Life is too short'))
    <re.Match object; span=(0, 4), match='Life'>
    >>> print(re.search('^Life', 'My Life'))
    None
"""

    # $
"""
$ 메타 문자는 맨 마지막과 일치함을 의미
    >>> print(re.search('short$', 'Life is too short'))
    <re.Match object; span=(12, 17), match='short'>
    >>> print(re.search('short$', 'Life is too short, you need python'))
    None
"""

    # \A
"""
\A는 문자열의 처음과 매치됨을 의미한다. ^ 메타 문자와 동일한 의미이지만 re.MULTILINE
옵션을 사용할 경우 ^은 각 줄의 문자열의 처음과 매치되지만 \A는 줄과 상관없이 전체
문자열의 처음하고만 매치된다.
"""

    # \Z
"""
\Z는 문자열의 끝과 매치됨을 의미한다. 이것 역시 $ 메타 문자와 다르게 전체 문자열의 끝과 매치
"""

    # \b
"""
\b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.
    >>> p = re.compile(r'\bclass\b')
    >>> print(p.search('no class at all'))  
    <re.Match object; span=(3, 8), match='class'>
    >>> print(p.search('the declassified algorithm'))
    None
    >>> print(p.search('one subclass is'))
    None
\bclass\b 정규식은 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨을 의미한다.
- cf) \b 메타 문자를 사용할 때 유의할점
    \b는 파이썬 리터럴 규칙에 의하면 백스페이스(BackSpace)를 의미하므로 백스페이스가
    아닌 단어 구분자임을 알려 주기 위해 r'\bclass\b'처럼 Raw String임을 알려주는 기호
    r을 반드시 붙여줘야 한다.
"""

    # \B
"""
\B 메타 문자는 \b 메타 문자와 반대의 경우이다. whitespace로 구분된 단어가 아닌 경우만 매치
    >>> p = re.compile(r'\Bclass\B')
    >>> print(p.search('no class at all'))  
    None
    >>> print(p.search('the declassified algorithm'))
    <re.Match object; span=(6, 11), match='class'>
    >>> print(p.search('one subclass is'))
    None
class 단어의 앞뒤에 whitespace하나라도 존재하면 매치가 안된다.
"""


# 07. 그루핑
"""
ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다고 하자.
이럴때 필요한 것이 그루핑(Grouping)이다.
    (ABC)+
그룹을 만들어 주는 메타 문자는 바로 ()이다.
    >>> p = re.compile('(ABC)+')
    >>> m = p.search('ABCABCABC OK?')
    >>> print(m)
    <re.Match object; span=(0, 9), match='ABCABCABC'>
    >>> print(m.group())
    ABCABCABC
ex.
    >>> p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
    >>> m = p.search("park 010-1234-1234")
위에서 이름만 뽑아내고 싶다면,
    >>> p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group(1))
    park
group(인덱스)
    group(0) -> 매치된 전체 문자열
    group(1) -> 첫 번째 그룹에 해당되는 문자열
    group(2) -> 두 번째 그룹에 해당되는 문자열
    group(n) -> n 번째 그룹에 해당되는 문자열
위 예시에서 전화번호만 뽑아내고 싶다면
    >>> p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group(2))
    010-1234-1234
위 예시에서 국번만 뽑아내고 싶다면
    >>> p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group(3))
    010
그룹을 중첩되게 사용하는 것도 가능하다. 그룹이 중첩되어 있는 경우 바깥쪽부터 시작하여
안쪽으로 들어갈수록 인덱스가 증가한다.
"""

    # 그루핑된 문자열 재참조하기
"""
그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조(Backreferences)할 수 있는점이다.
    >>> p = re.compile(r'(\b\w+)\s+\1')
    >>> p.search('Paris in the the spring').group()
    'the the'
정규식 (\b\w+)\s+\1은 그룹 +" "+ 그룹과 동일한 단어와 매치됨을 의미함
이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.
이것을 가능하게 해주는 것은 \1 메타 문자이다. \1은 정규식의 그룹 중 첫 번째 그룹을 가리킴
"""

    # 그루핑된 문자열에 이름 붙이기
"""
정규식 안에 그룹이 무척 많다고 가정하면, 엄청 혼란스러울 것이다.
그래서 그룹을 인덱스가 아닌 이름으로 참조할 수 있도록 하는 것
    (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
ex.
    >>> p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
    >>> m = p.search("park 010-1234-1234")
    >>> print(m.group("name"))
    park
ex2.
    >>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
    >>> p.search('Paris in the the spring').group()
    'the the'
그룹 이름을 사용하면 \1 대신에 (?P=그룹이름) 이라는 확장 구문을 사용 할 수 있다.
"""


# 08. 전방 탐색
"""

"""