# TODO: 테케 3~6, 9, 12 실패하는 이유 고민
# def solution(ingredient):
#     answer = 0
#     ingredient = ''.join(str(i) for i in ingredient)
#     while '1231' in ingredient:
#         answer += ingredient.count('1231')
#         ingredient = ingredient.replace('1231', '')
#     return answer


def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1
    return answer
