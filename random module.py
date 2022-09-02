import random as r
""""""
r.randrange(1, 7) # 1에서 6까지의 정수 증 하나를 무작위로 추출
r.randrange(1,7,2) # 1에서 6까지 2스텝씩
r.randrange(7) # 0에서 6까지의 정수
""""""
r.randint(1,3) # 1이상 3 이하 정수
""""""
r.random() # 0이상 1미만 수중 무작위로 추출
""""""
abc=['a','b','c','d']
r.shuffle(abc) # abc 리스트의 순서를 무작위로 바꿈
r.choice(abc) # abc 리스트중 아무 하나의 원소를 추출
print(r.choices(abc, weights=[2,1,1,1], k=5)) # 가중치를 두어 원하는 갯수 추출
""""""
