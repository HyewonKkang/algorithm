# 집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형입니다.
# 집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있습니다.
s1 = set([1, 2, 3])
print(s1) # {1, 2, 3}

# 혹은 다음과 같이 문자열을 입력하여 만들 수도 있습니다.
# 비어 있는 집합 자료형은 s = set()으로 만들 수 있습니다.
s2 = set("Hello")
print(s2) # {'o', 'e', 'H', 'l'}

# set이 가지는 특징
# 1. 중복을 허용하지 않습니다.
# 2. 순서가 없습니다(unordered).
# list, tuple은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수
# 있지만 set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
# (딕셔너리 역시 순서가 없는 자료형이라 인덱싱을 지원하지 않습니다.)
# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이
# 리스트나 튜플로 변환한 후 해야 합니다.
# 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한
# 필터 역할로 종종 사용하기도 합니다.
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합
# 1. &     2. intersection
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
# 1. |     2. union
print(s1 | s2)
print(s1.union(s2))

# 차집합
# 1. -     2. difference
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))

# 집합 관료형 관련 함수들
# 값 1개 추가하기 (add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 (update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 특정 값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
