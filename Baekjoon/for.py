# 반복문 for
# for문은 in 오른쪽 컬렉션 내부의 요소들을 왼쪽부터
# 하나씩 꺼내서 in 왼쪽 변수에 대입해 실행문을 실행합니다.
# 실행 횟수는 처음부터 컬렉션 갯수 바퀴수로 정해져 있습니다.
# 컬렉션이란 여러 값을 모아놓은 집합이며 리스트, 문자열이
# 가장 대표적인 예시입니다.
# 리스트는 [] 사이에 있는 자료이며, 문자열도 "문자 배열"
# 이기 때문에 컬렉션으로 취급됩니다.
for student in [1, 2, 3, 4, 5]:
    print(student, "번 학생의 출석을 체크합니다.")

for alphabet in "abcdefghijklmnop":
    print(alphabet, end="")

# for문을 사용할 때 목표 반복횟수가 늘어나면 일일이 손으로
# 리스트를 만들기가 어렵습니다. 따라서 range()를 이용해
# 범위를 지정해 리스트를 구성하는 방식을 주로 사용합니다.
# range(시작값, 끝값+1, 증가값) 문법을 사용하며
# 시작값은 적은대로, 끝값은 1을 빼줘야 적용범위가 잡힙니다.
# range(끝값+1)이며 숫자를 하나만 넣었을때 시작값은 0, 증가값은
# 1로 자동으로 삽입됩니다.
# range(시작값, 끝값+1)이며 숫자를 두 개 넣었을 때 증가값도 1이며
# range(시작값, 끝값+1, 증가값)을 넣으면 간격이 증가값을 따릅니다.
for student in range(5): # 1~4 출력
    print(student, "번 학생의 성적을 등록합니다.")

for number in range(10,0, -5):
    print(number)

# in 왼쪽에 변수를 사용하면 그 변수는 in 오른쪽 요소를 순서대로
# 받아서 저장할 수 있습니다.
# 그러나 그것이 반드시 실행문에서 in 왼쪽 변수를 사용해야 한다는
# 의미는 아닙니다.
for a in range(5):
    print("Hello Python!")

for x in range(1, 51):
    if x % 10 == 0:
        print("+", end="")
    else:
        print("-", end="")
print()

for x in range(1, 51):
    if x % 10: # 0
        print("-", end="")
    else:
        print("+", end="")
print()
for x in range(5):
    print("-"*9, end="")
    print("+", end="")
print()

# for in 문을 이용해서 10번 반복하는 반복문을 만들어주세요
# 만든 반복문의 실행문은 num이라는 변수에 정수 숫자를 입력받으며
# num 변수에 홀수가 들어오면 건너뛰고 짝수가 들어오는 경우만
# sum 변수에 num에 있는 값의 합계를 누적시킵니다.
# 10번 입력되고 난 다음 총 합이 몇인지 출력하는 코드를 작성해주세요.
sum = 0
for x in range(1, 11):
    print(x, "번째 입력을 받습니다.")
    num = int(input("짝수를 입력해주시면 총합에 반영됩니다."))
    if num % 2 == 0:
        sum += num
print("총합 : ", sum)