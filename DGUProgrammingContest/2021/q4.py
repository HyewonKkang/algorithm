inputs = input().split(';')
nums = list(map(int, inputs[0:3]))
strings = inputs[3:]
if '0' in nums:
    print("No possible sentence.;")
else:
    s = strings[0:nums[0]]
    p = strings[nums[0]:nums[0] + nums[1]]
    o = strings[nums[0] + nums[1]:]
    for s_ in s:
        for p_ in p:
            for o_ in o:
                print(s_ + ' ' + p_ + ' '+ o_ + ';', end = '')