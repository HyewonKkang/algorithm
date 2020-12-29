# 클래스의 상속
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것입니다.
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나
# 기존 기능을 변경하려고 할 때 사용합니다.
# 상속의 개념을 사용하여 FourCal() 클래스에 a의 b제곱을 구하는 기능을 추가합니다.
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

# class 클래스이름(상속할클래스이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의
# 모든 기능을 사용할 수 있어야 합니다.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())