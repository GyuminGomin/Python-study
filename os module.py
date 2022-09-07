import os

# os.getcwd()
"""
현재 파일의 경로를 찾을 수 있는 함수
"""
cwd = os.getcwd()
print(cwd)
print()

# os.listdir()
"""
지정된 경로에 존재하는 파일과 디렉터리 목록을 구하는 함수
경로 지정을 안해주면 현재 파일이 존재하는 디렉터리의 목록
"""
list = os.listdir()
print(list)
print()
path = r'C:' # r''가 경로지정할 수 있다는 것...

# os.chdir(path)
"""
작업하고 있는 디렉토리를 변경합니다.
"""
### os.chdir("C:\\Users\\a6351\\PycharmProjects\\pythonProject\\파이썬 공부 2022-08-14 이후") # 디렉터리로 이동

# os.mkdir(디렉토리를 만들 경로)
"""
디렉토리(폴더)를 만드는 방법
"""

# os.rmdir(삭제할 디렉토리 경로)
"""
디렉토리(폴더)를 삭제하는 방법 -> 디렉토리 안에 파일이 하나라도 있으면 실행되지 않는다.
"""

# os.removedirs(삭제할 디렉토리 경로)
"""
가장 안에 있는 디렉토리 폴더부터 한개씩 차례대로 삭제를 한다.
실행을 해봤을 때, 빈폴더만 삭제가 가능했다. os.rmdir()과 차이점을 느끼지 못했다.
"""

# os.remove(삭제할 파일의 경로)
"""
파일을 삭제
"""

# os.rmtree(path)
"""
파일을 포함한 디렉토리 삭제
"""

# os.path.isdir(path)
"""
폴더가 존재할 때 True 아닐때 False를 반환
"""

# os.path.isfile(path)
"""
파일이 존재할 때 True 아닐때 False를 반환
"""

# os.path.exists(path)
"""
폴더나 파일이 존재할 때 True 반환
"""

# os.path.getsize(path)
"""
파일의 크기를 조회 단위는 kB
"""

# os.path.split(path)
"""
튜플 형태로 폴더 제일 끝과 그 나머지 부분을 분리
ex. C:/파이썬/python.py 를 경로로 지정 -> ('C:/파이썬', 'python.py')
"""

# os.path.splitext(path)
"""
경로와 파일의 확장자명을 분리
"""

# os.path.join()
"""
폴더 이름과 파일 이름을 합쳐주는 함수
"""

# os.path.dirname(path)
"""
경로만 꺼내주는 함수
"""

# os.path.basename(path)
"""
파일 이름만 꺼내주는 함수
"""