class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def _init_(self):
        self.root=None
        self.temp=None
        self.temp1=None
    def creation(self,data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
        else:
            self.temp=self.root
            self.temp1=self.root
            flag=0
            while True:
                if self.temp.left is None:
                   self.temp.left=newnode
                   break
                elif self.temp.right is None:
                    self.temp.right=newnode
                    break
                elif flag==0:
                    self.temp=self.temp1.left
                    flag=1
                else:
                    self.temp=self.temp1.right
                    flag=0
                    self.temp1=self.temp1.left
    def PrintInorder(self,node):
        if node is None:
            return
        else: 
            self.PrintInorder(node.left)
            print(node.data,end=" ")
            self.PrintInorder(node.right)
    def PrintPreorder(self,node):
        if node is None:
            return
        else:
            print(node.data,end=" ")
            self.PrintPreorder(node.left)
            self.PrintPreorder(node.right)
    def PrintPostorder(self,node):
        if node is None:
            return
        else:
            self.PrintPostorder(node.left)
            self.PrintPostorder(node.right)
            print(node.data,end=" ")
        

n=int(input("Enter the number of node size:"))
a=BinaryTree()
for i in range (1,n+1):
    data=int(input(f"Enter the data for node {i}: "))
    a.creation(data)
print("In-order traversal of the binary tree:")
a.PrintInorder(a.root)
print("\nPre-order traversal of the binary tree:")
a.PrintPreorder(a.root)
print("\nPost-order traversal of the binary tree:")
a.PrintPostorder(a.root)
