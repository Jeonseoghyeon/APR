class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n
        
class LinkedList:
    def __init__(self):
        Head = Node('Head')
        self.head = Head
        self.size = 0
    
    def insert(self, idx, data):
        new = Node(data)
        cur = self.head
        for i in range(idx):
            cur = cur.next
        new.next = cur.next
        cur.next = new
        self.size += 1
        
    def delete(self, idx):
        cur = self.head
        for i in range(idx):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        return
    
    def change(self, idx, data):
        cur = self.head
        for i in range(idx+1):
            cur = cur.next
        cur.data = data
        return
        
    def search(self, idx):
        if idx >= self.size:
            return -1
        cur = self.head
        for i in range(idx):
            cur = cur.next
        return cur.next.data
        
for _ in range(int(input())):
    N,M,L = map(int,input().split())
    arr = list(input().split())
    mylist = LinkedList()
    for i in range(N):
        mylist.insert(i,arr[i])
    for j in range(M):
        cmd = list(input().split())
        if cmd[0]=='I':
            mylist.insert(int(cmd[1]), cmd[2])
        elif cmd[0]=='D':
            mylist.delete(int(cmd[1]))
        else:
            mylist.change(int(cmd[1]), cmd[2])
    print(f'#{_+1} {mylist.search(L)}')