# add = lambda a, b: a+b
# result = add(3,4)
# print(result)

# 5장 Class

class FourCal :
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
# a.setdata(4,2) # 이것과 FourCal.setdata(a,4,2)와 같다.
print(a.add())

class MoreFourCal(FourCal) : #상속
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(5,2)
print(b.pow())

class SafeFourCal(FourCal) :
    def div(self): # 메서드 오버라이딩 ( 똑같은 메서드 이름을 가져와 사용 )
        if self.second == 0 :
            return 0
        else:
            return self.first / self.second


