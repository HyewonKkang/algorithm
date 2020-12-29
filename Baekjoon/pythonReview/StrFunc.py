# 문자열은 숫자 자료에 비해 복잡하므로 보다 다양한 함수, 메서드를
# 사용해 편집하거나 조작할 수 있도록 지원합니다.
# 함수 : 공용적으로 내장된 기능(. 없이 실행)
# 메서드 : 클래스에 속한 함수 (.가 왼쪽에 붙음)
s = "python programming class"

print(len(s))

# find는 왼쪽에서부터, rfind는 오른쪽에서부터 찾는다.
print(s.find("o"), s.rfind("o"))

s1 = "C programming"
if s1.find("gram") == -1:
    print("C와 관련없는 단어입니다.")
else:
    print("C와 관련있는 단어입니다.")

# print(s1.index("x")) # 에러 발생

print(s.count("python"))

s2 = """생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은
생각하지 않으려고 하는 생각이 옳은 생각이라고 생각합니다."""
print("'생각'의 등장 횟수 : ", s2.count("생각"))

# 특정 문자가 특정 문자열 내부에 포함되어있는지 여부는
# in, not in 키워드로 조회할 수 있습니다.
# in 키워드는 "있는지" 여부를 질문하는 것이며 있으면 True 없으면
# False 입니다. 반면 not in 키워드는 "없는지" 여부를 질문하며
# 있으면 False, 없으면 True 입니다.
s = "python programming"
print("a" in s, "z" in s)
print("pro" in s, "x" not in s)

# startswith() 는 시작 문자열을 검사하고
# endswith()는 끝나는 문자열을 검사해
# 내가 제시한 문자열과 일치하면 True 일치하지 않으면 False입니다.
name = "홍길동"
if name.startswith("홍"):
    print("홍씨입니다.")
if name.startswith("박"):
    print("박씨입니다.")

file = "cat.jpg"
if file.endswith(".jpg"):
    print("그림파일입니다.")
    
# 문자 요소 확인
# .isalpha() - 알파벳으로만 구성된 문자열인지 검사
# .islower(), .isupper() - 소문자, 대문자로 구성되었는지 검사
# .isdecimal() - 숫자로만 이루어졌는지 검사

height = input("당신의 키를 입력해주세요.")
if height.isdecimal():
    print("키 : " + height + "cm")
else:
    print("숫자만 입력해주세요.")

# 문자열 변경
# .lower(), .upper() - 대문자를 소문자로, 소문자를 대문자로 변경
# .swapcase() - 대소문자를 서로 변경
# capitalize() - 문자열의 첫 글자만 대문자로 변경
# title() - 문자열 내부의 모든 단어의 첫 글자를 대문자로 변경
s = "Good afternoon! my name is CHAE"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())
s = s.upper()
print(s)

# 파이썬에서는 문자열의 왼쪽과 오른쪽의 공백을 제거할 수 있는 명령어
# .strip(), .lstrip(), .rstrip()을 제공합니다.
# .strip()은 양쪽 공백 제거, .lstrip()은 왼쪽 공백 제거,
# 그리고 .rstrip()은 오른쪽 공백을 제거합니다.
s = "    abc1234    "
print(s + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")
print(s.strip() + "님")

# .split("쪼갤지점")을 이용하면 쪼갤지점을 지정해서
# 하나의 문자열을 여러개로 쪼갤 수 있습니다.
# 만약 .split()과 같이 쪼갤지점을 입력하지 않는다면
# 그 때는 그냥 띄어쓰기, 탭, 엔터키 등을 기준으로 쪼개줍니다.
s1 = "떡볶이 김말이 닭강정"
print(s1.split(" "))
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)

for c in city:
    print(c, "찍고", end = " ")
print()

# join()은 "문자열".join(입력받을자료) 문법을 사용하며
# 입력받을자료 에 해당하는 자료의 인덱스번호 사이사이마다
# "문자열"에 해당하는 자료를 집어넣어줍니다.
s= " ^~^"
print(s.join("안알려줌"))

# split과 함께 사용하여 구분자를 교체하는 것도 가능합니다.
s3 = "배?고?프?다"
s4 = s3.split("?")
print("!".join(s4))

print(",".join("abcdefg"))

# .replace(찾을문자, 바꿀문자)는 찾아 바꾸기입니다.
# 특정 문자열 내부에서 내가 찾는 문자를 지정한 문자로 교체해줍니다.
s = "파이썬 프로그래밍! 파이썬은 문자열을 관리할 수 있는 많은 \
메서드들이 있어요!"
print(s.replace("파이썬", "python"))