# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close() # 원래 없던 것 추가했음
# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close() # 원래 없던 것 추가했음

# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

# with open("test.txt", "a", encoding='UTF=8') as f :
#     data = input("아무것이나 입력하시오. : ")
#     f.write(data)

# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# Life is too short
# you need java

# replace 함수를 사용해 보자.
# with open("test.txt", "w", encoding="UTF-8") as f :
#     f.write("Life is too short\nyou need java")

# with open("test.txt", "r+", encoding="UTF-8") as f :
#     data = f.read()
#     data2 = data.replace("java", "python")
#     f.write(data2) # 이 방법은 틀렸다.

with open("test.txt", "r", encoding="UTF-8") as f :
    data = f.read()
    data = data.replace("java", "python")
with open("test.txt", "w", encoding="UTF-8") as f :
    f.write(data)