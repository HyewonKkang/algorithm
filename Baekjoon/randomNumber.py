# 난수 발생
# 난수란 무작위로 선택된 값을 난수라고 합니다.
# 파이썬에서는 import random 이라고 최 상단에 적으면 난수를
# 발생시킬 수 있습니다.
import random

# 정수 난수 : random.randint(시작값, 끝값)
print(random.randint(1, 100))

# 실수 난수 : random.random()
# ex) random.random() 입력시 0이상 1미만 실수 생성
print(random.random())

# 1~100 범위의 실수를 출력하는 코드를 아래에 작성해주세요.
print(random.random()*100)
print(random.random() + random.randint(1, 99))