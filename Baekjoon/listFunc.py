# 리스트에서 사용하는 메서드들
# append(자료) : 배열의 마지막 인덱스+1 위치에 입력된 자료 전부 추가
# insert(위치, 자료) : 지정한 위치 뒤로 기존 자료 밀어내고 새 자료 추가
# extend(리스트) : 리스트 + 리스트 처리(단 기존 리스트에 바로 적용)
nums = [1, 2, 3, 4]
nums.append(5)
print(nums)

nums.insert(2, 99)
print(nums)

print("-" * 40)
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
print(list1 + list2)
print(list1, list2)

list1.extend(list2)
print(list1)

# 리스트 삭제
# 리스트 내부 요소를 삭제하는데는 인덱스 번호를 이용하거나 혹은
# 자료 그 자체를 지목해서 삭제할 수 있습니다.
# .remove(자료) : 삭제할 자료를 직접 지목
# del(리스트[인덱스번호]) : 해당 리스트의 해당 인덱스번호 삭제
# 리스트[:] = [] 해당 범위 자료 삭제, 슬라이싱 지정 가능
score = [88, 95, 70, 100, 99, 80, 78, 50]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)

# 리스트 내부 전체 요소 삭제하기
list1 = [1, 3, 5, 7, 9]
list1.clear()
print(list1)

# .pop() 연산은 가장 마지막 인덱스에 있는 자료를 삭제해줍니다.
# 여타 명령어와는 달리 자료나 위치에 대한 입력을 하지 않아도 되기
# 때문에 자신이 무슨 자료를 삭제하는지 모를 수도 있습니다..
# 따라서 이를 보완하기 위해 .pop() 연산은 print()구문으로
# 삭제하는 자료가 뭔지 확인할 수 있습니다.
# 또한 .pop(인덱스번호) 입력시 마지막 자료가 아닌 입력번호 자료를
# 삭제해주는 기능도 있습니다.
score = [88, 52, 89, 96, 100]
score.pop()
print(score.pop())
print(score)
print(score.pop(1))
print(score)

# 리스트 검색은 문자와 큰 차이가 없습니다.
# .index(자료) : 조회자료가 몇 번 인덱스인지 출력. 없을 시 에러 발생
# .count(자료) : 리스트 내에 찾는 자료가 몇 개인지 정수로 출력
score = [88, 92, 100, 78, 95, 66, 32, 74]
perfect = score.index(100)
print("만점받은 학생의 번호는 %d번 학생입니다." % (perfect+1))

perfectNum = score.count(100)
print("만점자의 수는 %d명입니다." % perfectNum)

# 리스트 길이 조회시 len()을 사용하며, 최대값은 max(),
# 최소값은 min()을 사용해서 구할 수 있습니다.
print("학생 수는 %d명입니다." % len(score))
print("최고점수는 %d점입니다." % max(score))
print("최저점수는 %d점입니다." % min(score))

# 리스트 내부의 요소 유무 조회시 in, not in을 사용합니다.
# 요소 in 리스트 -> 요소가 리스트 내에 내장된 경우 True 아니면 False
# 요소 not in 리스트 -> 위와 반대로 True, False 출력
answer = input("결제를 진행하시겠습니까?")
if answer in ["ok", "yes", "응", "ㅇㅋ", "ㄱㄱ", "네", "예"]:
    print("결제가 완료되었습니다.")
else:
    print("안녕히 가세요.")

# .sort()는 내부 요소를 크기가 작을수록 0번에 가깝게 재배치해줍니다.
# .reverse()는 내부 요소를 인덱스번호 역순으로 재배치해줍니다.
score = [88, 95, 70, 100, 99]
score.sort() # 오름차순 정렬
print(score)
score.reverse() # 내림차순 정렬
print(score)

# .sort(reverse=True)로 정렬시 오름차순이 아닌 내림차순으로 정렬
score.sort(reverse=True)
print(score)