# a.setdata(m, n) 메서드를 수행하지 않고 add를 수행하면 오류가 발생합니다.
# 이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는
# setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는
# 생성자를 구현하는 것이 안전한 방법입니다.
# 생성자(Constructure)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미합니다.
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 됩니다.

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
        result = self.fisrt - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일합니다.
# 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어
# 객체가 생성되는 시점에 자동으로 호출되는 차이가 있습니다.
# 따라서 __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와
# 마찬가지로 first와 second라는 객체변수가 생성될 것입니다.
a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.div())
print(a.mul())