# while문
student = 1
while student <= 5:
    print(str(student) + "번 학생의 출석을 체크합니다.")
    student += 1

# 0 ~ 567 사이의 모든 n의 배수의 합계를 구할 수 있도록
# input()과 while문을 조합해보세요.
# if문을 사용하셔도 좋고 사용하지 않으셔도 좋습니다.
num = 0
sum = 0
add = int(input("몇의 배수 값의 총합을 구하시겠습니까?"))
while num <= 567:
    if num % add == 0:
        sum += num
    num += 1
print("0~567 사이의", add, "의 배수의 총합 : " + str(sum))