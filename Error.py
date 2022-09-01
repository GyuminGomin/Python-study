class Bird :
    def fly(self):
        raise NotImplementedError # 파이썬 내장 오류 -> 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부로 오류 발생

class Eagle(Bird) :
    pass

eagle = Eagle()
eagle.fly()

