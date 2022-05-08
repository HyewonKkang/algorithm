def solution(rooms, target):
    exception = {}
    priorities = {}
    room = {}
    people = {}
    for info in rooms:
        tmp = info.replace('[',' ').replace(']',' ').split()
        room[int(tmp[0])] = tmp[1].split(',')

    for ex in room[target]:
        exception[ex] = -1
    for key, value in room.items():
        for name in value:
            if name not in exception:
                if name in people:
                    people[name].append(key)
                else:
                    people[name] = [key]
                    priorities[name] = []

    for key, val in people.items():
        priorities[key].append(len(val))

    for key, val in people.items():
        nearest = abs(val[0] - target)
        for v in val:
            nearest = min(abs(v - target), nearest)
        priorities[key].append(nearest)

    for key in people:
        priorities[key].append(key)

    values = [val for val in priorities.values()]

    values.sort(key=lambda x:(x[0], x[1], x[2]))
    answer = [val[2] for val in values]

    return answer


print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))
print(solution(["[1234]None,Of,People,Here","[5678]Wow"], 1234))
