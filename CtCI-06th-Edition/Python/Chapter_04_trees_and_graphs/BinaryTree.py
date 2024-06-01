from Node import Node
def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:
    def __init__(self,data=None):
        self.root = Node(data)

    def insert(self, data, parent):
        if self.root is None:
            self.root.data = data
        else:
            if data < parent.data:
                if parent.left is None:
                    parent.left = Node(data)
                else:
                    self.insert(data, parent.left)
            elif data > parent.data:
                if parent.right is None:
                    parent.right = Node(data)
                else:
                    self.insert(data, parent.right)
    
    def inorder(self,node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data,end=",")
            self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data,end=',')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=',')
        
if __name__ == '__main__':
    bt = BinaryTree('g')
    bt.insert('c',bt.root)
    bt.insert('b',bt.root)
    bt.insert('a',bt.root)
    bt.insert('e',bt.root)
    bt.insert('d',bt.root)
    bt.insert('f',bt.root)
    bt.insert('i',bt.root)
    bt.insert('h',bt.root)
    bt.insert('j',bt.root)
    bt.insert('k',bt.root)
    print('\nin order traverse left-current-right')
    bt.inorder(bt.root)
    print('\n\npre order traverse current-left-right')
    bt.preorder(bt.root)
    print('\n\npost order traverse root-right-left')
    bt.postorder(bt.root)
    print('')
   
     