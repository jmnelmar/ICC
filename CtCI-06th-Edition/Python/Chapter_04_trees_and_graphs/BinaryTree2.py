class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right = None

    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if self.data > data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)

    def inorder(self):
        if self.left: self.left.inorder()
        print(self.data, end=',')
        if self.right: self.right.inorder()

    
    def preorder(self):
        print(self.data, end=',')
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

    def postorder(self):
        if self.left: self.left.postorder()
        if self.right: self.right.postorder()
        print(self.data, end=',')
    
    def find(self, value) -> bool:
        if value == self.data:
            return True
        else:
            if value < self.data:
                return self.left.find(value)
            else:
                return self.right.find(value)
        
        return False
        

bt = TreeNode(5)
bt.insert(3)
bt.insert(6)
bt.insert(1)
bt.insert(7)
print('inorder')
bt.inorder()
print('\npreorder')
bt.preorder()
print('\npostorder')
bt.postorder()
print('\nsearching 7',end=', ')
if bt.find(7) : print("Found") 
else: print("Not Found")
