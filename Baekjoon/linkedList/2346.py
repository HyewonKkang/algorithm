class CircularLinkedList:
    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, data):
        new_node = self.Node(data, None)
        if self.isEmpty():
            new_node.next = new_node # 새 노드는 자신을 참조
            self.last = new_node # last는 새 노드 참조
        else:
            new_node.next = self.last.next # 새 노드는 첫 노드를 참조
            self.last.next = new_node # last가 참조하는 노드와 새 노드 연결
        self.size += 1

    def delete(self, p): # 연결 리스트의 첫 노드 삭제
        del_node = p.next
        if self.size == 1:
            self.last = None
        else:
            p.next = del_node.next
        self.size -= 1
        return del_node.data

    def print_list(self, idx):
        s = ''
        p = self.last
        for i in range(idx):
            p = p.next
        s += str(self.delete(p)) + ' '

        return s

if __name__ == '__main__':
    N = int(input())
    c = CircularLinkedList()
    L = list(map(int, input().split()))
    ballon = {}
    for i in range(1, N+1):
        c.insert(i)
        ballon[i] = L[i - 1]
    print(ballon)
    idx = 1
    isFirst = 0
    while(c.isEmpty() != 1):
        if(isFirst == 0):
            print(c.print_list(0), end = '')
            isFirst += 1
            continue
        idx = idx + ballon[idx]
        print(c.print_list(idx), end='')
        # c.delete(idx)

