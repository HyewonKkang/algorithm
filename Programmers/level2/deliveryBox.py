from collections import deque

def solution(order):
    main, sub = [], []
    order = deque(order)
    for i in range(1, len(order) + 1):
        if i == order[0]:
            main.append(order.popleft())
            while True:
                if sub and order[0] == sub[-1]:
                    main.append(order.popleft())
                    sub.pop()
                else: break
        else:
            sub.append(i)
    return len(main)
