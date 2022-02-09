from itertools import product
def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for new in list(product(vowels, repeat=i)):
            dictionary.append(''.join(new))
    dictionary.sort()

    for idx, w in enumerate(dictionary):
        if w == word:
            return idx + 1