def solution(nums):
    cnt = int(len(nums) / 2)
    units = []
    nums = list(set(nums))
    if len(nums) >= cnt:
        units.append(cnt)
    else:
        units.append(len(nums))
    return max(units)