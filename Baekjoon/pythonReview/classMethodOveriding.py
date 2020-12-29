# FourCal 클래스의 객체 a에 4와 0 값을 설정하고 div 메서드를
# 호출하면 4를 0으로 나누려고 하기 때문에 ZeroDivisionError 오류가 발생합니다.
# 하지만 0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면
# 메서드 오버라이딩을 이용합니다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# a = FourCal(4, 0)
# a.div()

# SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로
# 다시 작성하였습니다. 이렇게 부모 클래스에 있는 메서드를
# 동일한 이름으로 다시 만드는 것을 메서도 오버라이딩이라고 합니다.
# 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한
# 메서드가 호출됩니다.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())