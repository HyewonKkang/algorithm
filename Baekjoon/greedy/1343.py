polyomino = input()

polyomino = polyomino.replace('XXXX', 'AAAA')
polyomino = polyomino.replace('XX', 'BB')

if 'X' in polyomino:
    print(-1)
else:
    print(polyomino)