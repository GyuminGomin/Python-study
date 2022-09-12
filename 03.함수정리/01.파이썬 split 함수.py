# split 함수
"""
문자열.split()
문자열.split('구분자')
문자열.split('구분자',분할횟수)
문자열.split(sep='구분자',maxsplit=분할횟수)
"""

import re

p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))