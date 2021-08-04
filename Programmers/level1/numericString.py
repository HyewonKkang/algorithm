def solution(s):
    answer = ''
    word = ''
    nums = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(s)):
        if s[i].isdigit():
            if word != '':
                answer += str(nums.index(word))
            answer += s[i]
            word = ''
        else:
            if word in nums:
                answer += str(nums.index(word))
                word = s[i]
            else:
                word += s[i]
    if word != '':
        answer += str(nums.index(word))
    return int(answer)