# 지역 변수
# 지역변수는 함수 내부에 선언된 변수입니다.
# 지역변수는 함수가 호출되면 스택영역에 같이 할당되며
# 함수 실행문을 모두 실행하면 지역과 함께 같이 소멸되어 재호출이 불가능합니다.
def introduce():
    word = "하이!" # 지역변수 word
    print(word)
introduce()

# 다른 지역간에는 같은 이름의 변수를 서로 보유할 수 있습니다.
# 이 경우 각각의 변수는 서로 다른 변수로 간주됩니다.
def kim():
    temp = "김철수"
    print(temp)
def lee():
    temp = 2 ** 10
    return temp
def park(a):
    temp = a * 2
    print(temp)
kim()
print(lee())
park(6)

# 지역변수가 지역 내부에서만 호출 가능하며 지역이 소멸되면
# 같이 소멸되는 유형의 함수였다면 전역변수는 프로그램 내부 어디서도
# 호출이 가능하며 프로그램 종료 전까지 유지되는 변수입니다.
sale_rate = 0.9 # 전역변수

def calc_price(price):
    print("오늘의 할인율 : ", sale_rate)
    today_price = price * sale_rate # 지역변수
    print("오늘의 가격 : ", today_price)

calc_price(10000)
sale_rate = 0.7
calc_price(10000)
print(sale_rate)
#print(today_price) # 에러발생

# 파이썬은 전역 영역도 하나의 지역으로 간주하며 따라서 다른 지역간에는
# 같은 이름의 변수를 여럿 만들 수 있다는 규칙에 따라 전역변수와
# 지역변수를 동시에 같은 이름으로 생성할 수 있습니다.
# 이 경우 호출하는 위치에서 가장 가까운 변수가 우선적으로 호출됩니다.
price = 1000

def sale():
    price = 500
    print("local:", id(price))
sale()
print("global:", id(price))
print(price)

# 만약 지역 내부에서 전역변수의 값을 고치고 싶은 경우는
# 지역 내부의 변수가 전역변수와 같은 변수가 되도록 동기화해야 합니다.
# 이떄 사용하는 키워드가 바로 global입니다.
# global 키워드를 받은 변수는 전역변수와 동기화됩니다.
# 따라서 global 키워드는 전역변수가 미리 선언되어야만 쓸 수 있습니다.
print("=" * 40)
price = 1000
def sales():
    global price # 지역변수 price를 새로 만들지 말고 동기화
    price = 500
sales()
print(price)