# 이중 루프문이란 반복문 내부의 실행문으로 다시 반복문을 집어넣은
# 구문을 의미합니다. 이 경우 안쪽의 실행문이 모두 끝나야 한 바퀴
# 돈 것으로 간주하는 반복문의 특성상 안쪽의 반복문이 모두 돌아야
# 바깥쪽이 비로소 한 바퀴 돈 것으로 간주하기 때문에
# 최종적으로는 바깥쪽 반복문 실행횟수 * 안쪽 반복문 실행횟수만큼 실행합니다.
for dan in range(2, 10):
    print(dan, "단")
    for hang in range(1, 10):
        print(dan, "*", hang, "=", dan*hang)

# 아래 구문은 *을 다섯 번 연달아 찍는 구문입니다.
for j in range(5):
    for i in range(5):
        print("*", end = "")
    print()

# 아래 보이는 변수 dan에 숫자를 입력하면
# 1 ~ 9 까지 곱해 결과를 얻어내는 구구단 로직을 작성해주세요.

dan = int(input("구구단 단수를 입력해주세요."))

for hang in range(1, 10):
    print(str(dan) + "*" + str(hang) + "=" + str(dan*hang))