class Deque:
    def init(self):
        self.items = []

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Deque is empty")
        return self.items.pop()

    def popleft(self):
        if len(self.items) == 0:
            raise IndexError("Deque is empty")
        return self.items.pop(0)
    
    def append(self, value):
        self.items.append(value)

    def appendleft(self, value):
        self.items.insert(0, value)

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("Deque is empty")
        return self.items[-1]
    
    def peekleft(self):
        if len(self.items) == 0:
            raise IndexError("Deque is empty")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
deque = Deque()
results = []
n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == "pop":
        results.append(deque.pop())
    elif query[0] == "popleft":
        results.append(deque.popleft())
    elif query[0] == "append":
        deque.append(int(query[1]))
    elif query[0] == "appendleft":
        deque.appendleft(int(query[1]))
    elif query[0] == "peek":
        results.append(deque.peek())
    elif query[0] == "peekleft":
        results.append(deque.peekleft())
    elif query[0] == "size":
        results.append(deque.size())
    elif query[0] == "is_empty":
        results.append(deque.is_empty())

for result in results:
    print(result)
