# 2개의 변수 : 저장되는 실제 값(DATA FIELD)/ 다음 노드가 무엇인지 저장된 곳(LINK FIELD)
# 첫번째 노드가 무엇인지 말해주는 놈이 HEAD

class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def search(self, idx):
        current = self.head
        for i in range(idx):
            current = current.next
        return current.data

    def insert(self, idx, data):
        new = Node(data)
        current = self.head
        for i in range(idx):
            current = current.next     
        new.next = current.next
        current.next = new
        self.size += 1
        
        
for _ in range(int(input())):
    N,M,L = map(int,input().split())
    arr = list(input().split())
    mylist = LinkedList()
    mylist.head = Node(arr[0])
    mylist.size += 1
    
    for i in range(N-1):
        mylist.insert(i,arr[i+1])
    
    for j in range(M):
        idx,data = map(int,input().split())
        mylist.insert(idx-1, data)
        
    print(f'#{_+1} {mylist.search(L)}')


