# 클래스 변수
# 클래스 변수는 ㅋ클래스 안에 함수를 선언하는 것과 마찬가지로
# 클래스 안에 변수를 선언하여 생성합니다.
# 클래스 변수는 클래스이름.클래스변수 로 사용할 수 있습니다.
class Family:
    lastname = "김" # 클래스 변수
a = Family()
b = Family()
c = Family()
print(a.lastname)
print(b.lastname)
print(c.lastname)

# 클래스 변수는 클래스로 만든 모든 객체에 공유됩니다.
# 이는 id 함수를 사용하면 알 수 있는데, 아래와 같이 id 값이 모두 같으므로
# a.lastname, b.lastname, c.lastname은 모두 같은 메모리를
# 가리키고 있습니다.
print(id(a.lastname)) #2591221197200
print(id(b.lastname)) #2591221197200
print(id(c.lastname)) #2591221197200