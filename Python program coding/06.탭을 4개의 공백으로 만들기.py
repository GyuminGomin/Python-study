# 조건
"""
1. python tabto4.py src dst
- src는 탭을 포함하고 있는 원본 파일
- dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일
- 위 명령어를 커맨드창에서 실행시키면
- src에선 탭이 있는 파일인데, dst에선 공백 4개로 변환되어 있을 것
cf. 명령어를 이해하고 있으면, 위 명령어를 그대로 실행하면 안된다는 것을 알고 있을 것 이다.
--- 따라서 나는 python "06.탭을 4개의 공백으로 만들기.py" 06.src 06.dst 를 실행할 것
"""

# import sys
#
# for i in sys.argv :
#     if i == sys.argv[0] :
#         continue
#     elif i == sys.argv[1] :
#         with open(sys.argv[1], "r", encoding="cp949") as f :
#             data = f.read()
#             data = data.replace("\t"," "*4)
#     elif i == sys.argv[2] :
#         with open(sys.argv[2], "w", encoding="cp949") as f :
#             f.write(data)
#             print(data)
#             print("실행이 완료되었습니다.")

import sys

src = sys.argv[1]
dst = sys.argv[2]

with open(src,"r",encoding="cp949") as f :
    data = f.read()
    data2 = data.replace("\t"," "*4)
with open(dst,"w",encoding="cp949") as f :
    f.write(data2)
    print(data2)
    print("실행이 완료되었습니다.")

# 06.src로 그냥 만들어서 실행하니 tab이랑 space*4가 구별이 안가서 txt파일로 만듬