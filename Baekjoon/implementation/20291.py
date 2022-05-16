n = int(input())
files = [input() for _ in range(n)]
dict = {}

for file in files:
    extension = file[file.rfind('.')+1:]
    if extension in dict:
        dict[extension] += 1
    else:
        dict[extension] = 1
total = list(zip(dict.keys(),dict.values()))
total.sort()
for i in range(len(total)):
    print(total[i][0], total[i][1])