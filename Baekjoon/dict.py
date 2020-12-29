# 딕셔너리는 사전이라고도 하며 key, value 쌍으로 자료를 저장합니다.
# {}를 이용해 저장하며 key:value, key2:value2 ...와 같이
# 콜론을 이용해 key와 value를 매칭시켜 저장합니다.
# 딕셔너리는 인덱스번호로 내부 자료 조회가 불가능합니다.
dic = {"멍멍이":"홍길동", "야옹이":"강감찬", "메뚜기":"장보고"}
print(type(dic))
print(dic)

# 사전에서 사용하는 key값은 중복값을 가질 수 없고
# 변경이 가능한 요소(리스트, 일반 변수 등...)은 올 수 없습니다.
# 반면에 value 값은 중복된 요소가 들어와도 상관이 없으며
# 변경 가능한 요소 및 불가능한 요소가 모두 올 수 있습니다.
# 사전에서 자료를 조회할 때는 index값 대신 key값을 사용합니다.
# key값으로 value를 얻을 수는 있지만 반대로는 불가능합니다.
print(dic["야옹이"])
print(dic["멍멍이"])

# 검색하는 키가 사전 내부에 존재하지 않으면 에러를 발생시킵니다.
# print(dic["귀뚜라미"])

# .get()을 사용하면 없다고 안내만 하고 에러는 발생하지 않습니다.
print(dic.get("귀뚜라미"))

# None 대신 없을때 출력할 멘트를 지정할 수도 있습니다.
print(dic.get("귀뚜라미", "없는 자료입니다"))
print(dic.get("메뚜기"))

# 딕셔너리 자료형은 무조건 key값 기반으로 움직이기 때문에
# in, not in 키워드 조회시 key값을 기준으로 결과가 출력됩니다.
if "강감찬" in dic:
    print("사전에 있는 단어입니다.")
else:
    print("사전에 없는 단어입니다.")

# 사전 데이터 관리
# 사전 자료형은 변경 가능한 자료형입니다. 따라서 실행중에 삽입, 삭제,
# 수정 등의 편집을 자유롭게 할 수 있습니다.
# 사전[key] = value 문법을 사용합니다.
# 추가한 key가 기존에 존재하는 key라면 value값을 교체해주고
# 그렇지 않다면 key:value 쌍이 사전에 추가됩니다.
dic = {"boy":"소년", "student":"학생", "book":"책"}
dic["book"] = "서적"
print(dic)

dic["girl"] = "소녀"
print(dic)

# 삭제는 del 명령어를 이용해 할 수 있습니다.
# del 명령어를 사용하는 경우는 key값을 이용해 key:value를 삭제합니다.
del dic["boy"]
print(dic)

# 딕셔너리 자료형도 두 개 이상을 합쳐줄 수 있습니다.
# 이 경우 기존딕셔너리.update(병합딕셔너리) 를 사용하며
# 만약 key 값이 겹치는 경우는 병합딕셔너리의 key값이 최종 반영됩니다.
dic1 = {"boy":"소년", "school":"학교", "book":"서적"}
dic2 = {"student":"학생", "teacher":"선생님", "book":"책"}
dic1.update(dic2)
print(dic1)

# dict()를 이용해 비어있는 딕셔너리를 만들 수도 있고, 다른 자료형을
# 딕셔너리 자료형으로 변경할 수도 있습니다.
# 2차원 리스트를 딕셔너리로 변경 가능합니다.
li = [
        ["이순신", 95],
        ["김유신", 84],
        ["강감찬", 35]
    ]
dic = dict(li)
print(dic)

# 딕셔너리를 비우고 싶다면 빈 딕셔너리를 대입
# 혹은 .clear()를 이용해도 딕셔너리를 비울 수 있다.
dic.clear()
print(dic)

# 문제
user = {"kim1234":"kkk1234",
        "lee4567":"lll4567",
        "park9876":"ppp9876"}
# user에 내장된 key:value는 아이디:비밀번호 입니다.
# input()을 이용해 id변수에는 id를, pw변수에는 비밀번호를 입력받아
# id와 pw가 모두 user 내부에 입력된 쌍과 일치할때만
# id님 로그인을 환영합니다, 그렇지 않은 경우
# 없는 아이디 입력시 "아이디가 없습니다", 아이디는 있는데
# 비밀번호가 틀렸을 경우는 "비밀번호가 다릅니다" 라고 출력해주세요.
print("\n아이디와 비밀번호를 입력하세요.")
id = input("아이디: ")
pw = input("비밀번호: ")
if id in user:
    if pw == user[id]:
        print(id + "님 로그인을 환영합니다.")
    else:
        print("비밀번호가 다릅니다.")
else:
    print("아이디가 없습니다.")