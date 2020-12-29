# 계산기는 이전에 계산한 결괏값을 기억하고 있어야 하므로
# 이를 유지하기 위해서 result 전역 변수(global)을 사용합니다.
# add 함수는 매개변수 num에 받은 값을 이전에 계산한 결괏값에 더한 후
# 돌려주는 함수입니다.
# 이때 한 프로그램에서 2대의 계산기가 필요한 상황이 발생했을 때
# 다음과 같이 함수를 각각 따로 만들어야 합니다.
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 계산기 1의 결괏값이 계산기 2에 아무 영향을 끼치지 않음을 알 수 있습니다.
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요할 때는
# 클래스를 사용하면 간단하게 해결할 수 있습니다.
print("=" * 40)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num): # 빼기 기능을 더하려면 다음과 같은 뺴기 함수 추가
        self.result -= num
        return self.result

cal1 = Calculator() # Calculator 클래스로 만든 객체 cal1
cal2 = Calculator() # Calculator 클래스로 만든 객체 cal2

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 클래스 구조 만들기
class newClass:
    pass

a = newClass() # 객체 생성
print(type(a)) # <class '__main__.newClass'>

# 객체에 숫자 지정할 수 있게 만들기
class FourCal1:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# setdata 메서드에는 self, first, second 총 3개의 매개변수가 필요한데
# 실제로는 a.setdata(4, 2)처럼 2개 값만 전달합니다.
# 그 이유는 a.setdata(4, 2)처럼 호출하면 setdata 메서드의 첫 번째
# 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기
# 때문입니다. (self ---> 객체 a)

a = FourCal1()
a.setdata(4, 2)
print(a.first)
print(a.second)

# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이
# 독립적인 값을 유지한다.
b = FourCal1()
b.setdata(3, 7)
print(b.first)

print(id(a.first))
print(id(b.first))

class FourCal2:
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
        result = self.fist / self.second
        return result

a = FourCal2()
a.setdata(4,2)
print(a.add()) # result = a.first + a.second
