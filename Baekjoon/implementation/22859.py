import sys
from collections import deque

html = sys.stdin.readline().rstrip()[6:-7]
html = html.replace('<p>', '#')
html = html.replace('<div title="', '@title : ')
html = html.replace('">', '')
html = html.replace('</p>', '')

docs = []
q = deque(html[1:])
while q:
    open = q.popleft()
    if open == '<':
        close = q.popleft()
        while close != '>':
            close = q.popleft()
    else:
        docs.append(open)


html = ''.join(docs)
html = ' '.join(html.split())

html = html.replace('#', '\n')
html = html.replace('@', '\n')

answer = list(html.split('\n'))
for ans in answer:
    print(ans.strip())