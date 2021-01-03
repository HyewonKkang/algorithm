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
        if(self.size == 1):
            self.last = None
        else:
            p.next = del_node.next
        self.size -= 1
        return del_node.data


    def print_list(self, N, K):
        s = ''
        p = self.last
        for _ in range(N):
            for j in range(K-1):
                p = p.next
            s += str(self.delete(p))
            if self.isEmpty():
                pass
            else:
                s += ', '
        return s

N, K = map(int, input().split())
c = CircularLinkedList()
for i in range(N, 0, -1):
    c.insert(i)
print("<", end = '')
print(c.print_list(N, K), end = '')
print(">", end = '')