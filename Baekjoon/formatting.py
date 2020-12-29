# 문자열 포매팅은 가변 출력 자료와 고정 출력 자료를 구분해서
# 출력 양식을 지정해두고 가변 출력 자료만 교체하는 출력 방식입니다.
# 문자열 내부에 포매팅 문자를 이용해서 가변 출력 자료 위치를 지정하며
# %d는 정수, %f는 실수, %s는 문자열 %h는 16진수, %o는 8진수 등
# 여러가지 포매팅 문자를 활용할 수 있습니다.
# 만약 %를 문자로서 사용하고 싶다면 %%와 같이 두 번 연달아 씁니다.
tvxq = 5
print("동방신기는 " + str(tvxq) + "명!")
print("동방신기는", tvxq, "명!")
print("동방신기는 %d명!" % tvxq)

# %를 문자열로 쓰고 싶다면 %s를 사용합니다.
percent = 97
print("오늘 학습 진도율은 %d%%" %percent)

# 만약 포매팅이 여럿인 경우는 % 뒤에 나열된 자료를 ()로 감싸줍니다.
month = 6
day = 6
anni = "현충일"
print("%d월 %d일은 %s" %(month, day, anni))

print("%10s %20s %5s" % ("name", "major", "age"))
print("%10s %20s %5s" % ("Albert", "computer scient", "21"))
print("%10s %20s %5s" % ("Jenny", "mathmatics", "20"))
print("%10s %20s %5s" % ("Tom", "economics", "22"))

#  ssn변수에 주민번호를 문자열로 입력받아 ex)"971216-1209321"
#  여기서 성별과 출생년도를 추출한 후 포맷팅을 사용하여
#  "xx년생 남자or여자"라는 결과를 출력하세요.
ssn = input("주민번호를 입력하세요: ")
birth = ssn[0:2]
if (int(ssn[7]) % 2 == 1):
    gender = "남자"
else:
    gender = "여자"
print("%s년생 %s" %(birth, gender))