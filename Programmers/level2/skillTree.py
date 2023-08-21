from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for leaf in skill_trees:
        skills = deque(skill)
        for l in leaf:
            if l not in skills: continue
            if l != skills[0]:
                break
            else:
                skills.popleft()
        else:
            answer += 1
    return answer
