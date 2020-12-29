apple = "사과"
print(apple)

# 파이썬 메모리공간에는 주소가 부여되어 있습니다.
# 저장주소를 확인하기 위해 id()를 사용합니다.
# 주소값은 랜덤하게 배정됩니다.
print(id(apple))

# 이미 저장된 apple 변수에 새롭게 "애플" 문자열을 저장
apple = "애플"
print(apple)
print(id(apple))

