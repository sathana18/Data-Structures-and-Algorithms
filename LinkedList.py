class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def _init_(self):
        self.head=None
        self.temp=None
    def create(self):
        data=int(input("Enter the data: "))
        newnode=Node(data)
        if self.head == None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
    def insert_at_front(self):
        data=int(input("Enter the data: "))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_at_middle(self):
        data=int(input("Enter the data: "))
        newnode=Node(data)
        pos=int(input("Enter the position: "))
        self.temp=self.head
        i=1
        while i<pos:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
    def insert_at_end(self):
        data=int(input("Enter the data: "))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
while True:
    print("""\nEnter 1.create
2.display
3.insert_at_front
4.insert_at_middle
5.insert_at_end\n""")
    choice=int(input("Enter the choice: "))
    if choice==1:
        obj=Linkedlist()
        obj.create()
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.insert_at_front()
    elif choice==4:
        obj.insert_at_middle()
    elif choice==5:
        obj.insert_at_end()
    elif choice==6:
        break
    else:
        print("Invalid choice")
