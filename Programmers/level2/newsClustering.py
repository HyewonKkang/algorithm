def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    string1 = []
    string2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            string1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            string2.append(str2[i:i+2])

    # intersection
    if len(string1) > len(string2):
        r1 = [string1.remove(x) for x in string2 if x in string1]
    else:
        r1 = [string2.remove(x) for x in string1 if x in string2]

    # union
    r2 = string1 + string2
    if len(r2) == 0:
        answer = int(65536)
    else:
        answer = int(len(r1) / len(r2) * 65536)

    return answer



# import copy
# def getIntersection(li1, li2):
#     result = []
#     for w1 in li1:
#         for w2 in li2:
#             if w1 == w2:
#                 result.append(w1)
#                 li2.remove(w2)
#                 break
#     return result
#
# def getIntersectionAndUnion(li1, li2):
#     result = []
#     total = li1 + li2
#     result1 = getIntersection(li1, li2)
#     result1_ = copy.deepcopy(result1)
#     result2 = []
#
#     for i in range(len(total)):
#         if total[i] in result1_:
#             result1_.remove(total[i])
#         else:
#             result2.append(total[i])
#
#     result.append(result1)
#     result.append(result2)
#
#     return result