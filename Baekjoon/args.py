# 함수를 호출할 때는 함수 정의시에 지정한 인수(파라미터, 매개변수,
# 입력값)의 개수만큼 값을 전달해야 합니다.
# 인수 개수가 달라지면 에러가 납니다.
def add(n1, n2):
    return n1 + n2
def add_three(n1, n2, n3):
    return n1 + n2 + n3
result1 = add(3, 6)
print(result1)

result2 = add_three(3, 6, 9)
print(result2)

# 가변인자 리스트는 파라미터(인수, 매개변수, 입력값) 왼쪽에 *을
# 붙여서 선언하며 이 경우 들어오는 자료를 모두 튜플로 묶어서
# *인수명 에 전달합니다.
def add_num(*nums):
    sum = 0
    print(type(nums))
    for num in nums:
        sum += num
    return sum
result1 = add_num(3, 5, 7, 9)
result2 = add_num()
result3 = add_num(100, 200, 300, 400, 500, 600, 700, 800)
print(result1, result2, result3)

# 가변인자는 콤마 이후의 인수를 전부 튜플로 묶어서 가져옵니다.
# 따라서 집어넣을때는 가장 우측에 가변인자를 배치해야합니다.
# 가변인자의 우측에 일반인수가 있으면 왼쪽에 있는 가변인자가 모든
# 요소를 가져가버려 값을 전달받지 못하는 인자가 발생합니다.
# 따라서 여러 인자를 설정 시 가변인자를 가장 오른쪽에 배치해야 합니다.
def add_num2(s, *nums):
    print(s)
    sum = 0
    for num in nums:
        sum += num
    return sum
print(add_num2(3, 6, 9, 12))

# 인수의 기본값.
# 아래의 코드는 간격이 1인 경우도 간격을 입력해야해서 불편합니다.
def calc_stepsum(start, end, step):
    sum = 0
    for num in range(start, end + 1, step):
        sum += num
    return sum
print(calc_stepsum(1, 10, 1))

# 만약 일반적인 상황에 넣어주는 인수값이 정해져있다면 디폴트값 선언을
# 통해 특수한 경우에만 인수를 입력하게 만들어줄 수도 있습니다.
def calc_stepsum2(start, end, step=1):
    sum = 0
    for num in range(start, end+1, step):
        sum += num
    return sum
print(calc_stepsum2(1, 10, 2))
print(calc_stepsum2(1, 10))

# 연습 - n개의 정수를 전달받아 가장 큰 숫자를 찾아 리턴하는 함수를
# 작성하세요. (get_max)
def get_max(*nums):
    max = nums[0]
    for num in nums:
        if(max < num):
            max = num
    return max
print(get_max(-14, 95, -78, 33, 92, 262, 87, 55))

# 연습2
# n개의 정수를 입력받아 그 정수들의 평균을 리턴하는 코드를 작성해보세요.
# 단, 0개를 입력받는 경우는 "입력받은 요소가 없습니다"라고 출력하면 됩니다.
def get_avg(*nums):
    sum = 0
    if(len(nums) == 0):
        print("입력받은 요소가 없습니다.")
        return
    else:
        for num in nums:
            sum += num
        avg = sum / len(nums)
        return avg

print(get_avg(1, 2, 3, 4, 5))