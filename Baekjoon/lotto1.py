# 로또복권 추첨기를 만들어보겠습니다.
# 로또복권은 1부터 45까지 숫자가 추첨될 수 있으며 숫자 6개를 추첨하면
# 당첨번호가 됩니다.
# 이 당첨번호는 중복된 값이 없어야 합니다.
# 로또복권을 추첨해서 작은 숫자부터 큰 숫자까지 정렬해 콘솔창에
# 출력하는 코드를 작성해주세요.
import random

get_number = list()
while(len(get_number) != 6):
    number = random.randint(1, 45)
    if number not in get_number:
        get_number.append(number)
get_number.sort()
print(get_number)