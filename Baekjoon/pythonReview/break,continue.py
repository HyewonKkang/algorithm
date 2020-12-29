# 탈출문이라 제어문을 종료시키거나 건너뛰기 위해 사용하는 구문으로
# break, continue 문이 있습니다.
# break문
score = [92, 56, 33, 127, 99]

for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print("점수 처리 완료")

# 1 ~ 10 까지의 배열을 range()로 생성하고
# for in 문을 이용해 순차적으로 출력하되
# 6을 출력한 다음 반복문이 종료되도록 for문과 break문을 사용해주세요.
for a in range(1, 10):
    print(a, end = " ")
    if a == 6:
        break
print("\n반복문 종료!")

# continue 명령은 실행 시 돌고있던 바퀴를 강제로 종료시키고
# 바로 다음바퀴로 넘어가는 탈출구문입니다.
# 전체 반복문의 종료 여부에는 영향을 미치지 않으며 오로지
# 돌고 있던 바퀴만 스킵하는 기능을 가지고 있습니다.
score = [97, 46, 22, -1, 87]

for s in score:
    if (s == -1):
        continue
    print(s)
print("점수 처리 완료!")

# range()를 이용해 1 ~ 10 범위를 가지는 리스트를 생성하고
# for in 문을 이용해 리스트 내부 요소를 순차적으로 출력하되
# 홀수값만 콘솔창에 출력되고 짝수는 continue 구문으로 생략해보세요.
for a in range(1, 11):
    if a % 2 == 0:
        continue
    else:
        print(a, end = "")
print()