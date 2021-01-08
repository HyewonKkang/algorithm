def solution(people, limit):
    answer = 0
    people.sort()
    lightest = 0
    heaviest = len(people) - 1
    while lightest <= heaviest:
        if people[lightest] + people[heaviest] <= limit:
            lightest += 1
        heaviest -= 1
        answer += 1
    return answer

print(solution([70, 80, 50], 100))
print(solution([70, 50, 80, 50], 100))