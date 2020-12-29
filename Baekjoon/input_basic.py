# 주석은 Ctrl + /
# 여러줄 주석은 삼중따옴표 '''

# 불필요한 공백은 에러를 유발함
#      print(1+2)

a = 1; b = 2; # 여러 명령을 한 줄에 작성 시 세미콜론으로 구분
Apple = "사과"
print(Apple)


# t is token
# d is document == tokens
def f(t, d):
    return d.count(t)


def tf(f, d):
    return 0.5 + 0.5 * f(t, d) / max([f(w, d) for w in d])


# input()으로 입력받은 값은 자동으로 문자로 인식!
# 따라서 연산 불가
a = input("첫 번째 수 : ")
b = input("두 번째 수 : ")
print("두 수의 합은 ", (int(a) + int(b)))

# 숫자로 변환할 때는 int("변환대상")을 이용 -> 정수로 변환
price = input("가격을 입력해주세요 : ")
num = input("개수를 입력해주세요 : ")
sum = int(price) * int(num)
print("총액은", sum, "원 입니다.")

# 입력할 값이 정수로 사용할 것이 한정적이라면
# 굳이 입력 후에 변환해주는 것이 아니라 입력단계에서
# 아예 정수로 입력을 받는 것도 가능합니다.
classroom = int(input("교실 개수를 입력해주세요."))
desk = int(input("책상 개수를 입력해주세요."))
sum = classroom * desk
print("수용인원은", sum, "명입니다.")