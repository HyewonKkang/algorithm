n = int(input())
tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))
d = int(input())
root = -1
answer = 0
for i, p in enumerate(parents):
    if p == -1:
        root = i
    else:
        tree[p].append(i)

def preorder(node):
    global answer
    if node == d:
        return
    if len(tree[node]) == 0:
        answer += 1
    if len(tree[node]) == 1 and tree[node][0] == d:
        answer += 1
    for child in tree[node]:
        preorder(child)

preorder(root)
print(answer)
