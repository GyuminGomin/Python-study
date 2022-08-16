# f = open("새파일.txt", 'w', encoding= 'UTF-8')
# for i in range(1,11) :
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close() # 파이썬 내장함수 open을 사용
with open("foo.txt", "w") as f : # with문을 사용하면 f.close()가 자동으로 실행 with문을 빠져나갈때
    f.write("Life is too short, you need python")


# readline_test.py
## f = open("C:\\Users\\a6351\\PycharmProjects\\pythonProject\\파이썬 공부 2022-08-14 이후\\새파일.txt", 'r', encoding='UTF-8')
# while True :
#     line = f.readline() # 위 파일을 읽어 첫번째 라인을 출력시켜주는 것
#     if not line : break
#     print(line)

# lines = f.readlines() # readlines...
# for line in lines :
#     line = line.strip() # 줄바꿈 \n을 제거해주는 것 지웠다 썼다 실행해보면 구별 가능
#     print(line)

# data = f.read()
# print(data)
## f.close()


