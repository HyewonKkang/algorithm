# 함수는 반복적으로 사용되는 코드다발을 함수이름에 저장한 것입니다.
# 변수에는 자료를 저장할 수 있다면 함수에는 실행문을 저장합니다.
# 이 실행문은 불완전한 실행문일 수 있으며, 불완전한 실행문인경우
# 실행 가능한 상태로 만들기 위해 자료를 요청할 수 있습니다.
# 함수 문법은 def 함수이름(입력값):
# 아래에 실행문을 들여쓰기로 작성 입니다.
def add(a, b):
    print(a + b)
add(10, 5)

def calcsum(x):
    y = 0
    for num in range(x+1):
        y += num
    return y
result1 = calcsum(4)
result2 = calcsum(10)
print(result1)
print(result2)

# 인수
# 인수는 함수를 실행하는데 있어서 불완전한 부분을 보충하기 위해
# 받는 자료를 지칭하는 단어이다.
# 인수 말고도 파라미터, 매개변수, 입력값 등으로도 부르며
# 이 4가지 용어가 비슷한 빈도로 사용되기 때문에 모두 알아야 한다.
# 인수는 갯수제한이 없으며 인수가 없는 함수도 존재한다.
# 인수가 없는 함수는 일반적으로 완성된 실행문을 가진다.
def calcsum10():
    sum = 0
    for num in range(11):
        sum += num
    return sum
result = calcsum10()
print(result)

# 모든 함수에 리턴값을 다 작성할 필요는 없습니다.
# 함수 실행 후 내부 로직만 실행하고 끝낼 의도라면 굳이
# 리턴을 적지 않고 실행할 실행문만 작성합니다.
def multi(n1, n2):
    result = n1 * n2
    print("%d x %d = %d" % (n1, n2, result))
multi(3, 6)

# 함수의 리턴값은 오로지 하나로 리턴됩니다.
# 하나의 변수에 담을 수 있게 리턴되며, 단 여러개를 나열한 경우는
# ','로 나열해 리턴구문을 사용하게 되며 이 때는 튜플로 묶어서
# 하나의 변수로 받을 수 있게 처리됩니다.
def sum_and_mul(n1, n2):
    return n1 + n2, n1 * n2
result = sum_and_mul(3, 7)
print(result)

sum, mul = sum_and_mul(3, 7)
print(sum)
print(mul)

# return구문의 용도는 사실 두 가지입니다.
# 1. return 값을 호출한 위치에 가져다 둔다.
# 2. return문 실행 시 즉시 함수를 종료한다.
# 이 두 가지는 동시에 진행되는 로직입니다.
# 따라서 문장에 2개 이상의 return문을 작성하면 첫 번째 리턴문까지만
# 함수가 실행되고 바로 종료됩니다.
def sum_and_sub(n1, n2):
    return n1 + n2
    return n1 - n2
result = sum_and_sub(7, 2)
print(result)

# return문은 단독으로도 사용할 수 있습니다.
# return문 뒤에 아무것도 작성하지 않은 경우는 값을 전달하는 기능은
# 없이 그냥 함수를 강제 중료시키는 기능만 수행합니다.
# 즉, 함수 내부에서 break문과 같은 용도로 사용할 수 있습니다.
def say_nickname(nick):
    if nick == "바보":
        print("별명을 다시 입력하세요.")
        return
    print("나의 별명은 %s입니다." % nick)
nickname = input("별명 : ")
say_nickname(nickname)