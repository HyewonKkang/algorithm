def solution(s):
    answer = 10000
    stack = []
    s_ = s
    for i in range(1, len(s)+1):
        s = s_
        cnt = 1
        new_str = ''
        while len(s) != 0:
            if not stack:
                stack.append(s[:i])
                s = s[i:]
                continue
            if stack[-1] != s[:i]:
                if cnt != 1:
                    new_str += str(cnt)
                new_str += stack[-1]
                stack.clear()
                stack.append(s[:i])
                cnt = 1
            else:
                cnt += 1
            s = s[i:]
        if cnt != 1:
            new_str += str(cnt)
        new_str += stack[-1]
        stack.clear()
        if len(new_str) < answer:
            answer = len(new_str)
    return answer