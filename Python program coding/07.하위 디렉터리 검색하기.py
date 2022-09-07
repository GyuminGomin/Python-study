# 조건
"""
1. 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일(*.py)만 출력해주는 프로그램
2. os.path.join(), os.listdir(), os.path.splitext(), os.path.isdir() 사용
3. 이 파일이 존재하는 디렉토리부터 시작해서 찾아보기
"""

import os

def search(dir) :
    filenames = os.listdir(dir)
    for filename in filenames :
        full_filename = os.path.join(dir,filename)
        # isdir_path = os.path.isdir(full_filename)
        if os.path.isdir(full_filename) == True: # 여기서 긴 함수는 변수로 선언해주면 이해하기 쉽다.
            search(full_filename)
        # ext = os.path.splitext(full_filename)[-1]
        elif os.path.splitext(full_filename)[-1] == '.py' :
            full_filename_list = full_filename.split('\\')
            print("\t-",full_filename_list[-2])
            print(full_filename) # 내부에 있는 py파일만 뽑아 가져오는 거기 때문에, 완벽하게 분리시키긴 어렵다.


dirname = r'C:\Users\a6351\PycharmProjects\pythonProject\파이썬 공부 2022-08-14 이후'
search(dirname)

# 이 문제를 풀어보면서, 궁금점이 하나 생겼다.
#   - 디렉토리 : ()
#       - 불라불라.py
#       - 불라불라.py
#       - 불라불라.py
#       - 하위 디렉토리 : ()
#           - 불라불라.py
#           - 불라불라.py
# 위 형태로 만들고 싶은데 위 방식처럼 해결은 불가능 하다.