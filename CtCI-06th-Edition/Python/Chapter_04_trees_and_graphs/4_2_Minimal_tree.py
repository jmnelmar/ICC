'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo­
rithm to create a binary search tree with minimal height.
'''
import pytest

class TreeNode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.data}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()


class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        
        if data < self.data:
            if self.left is None:
                self.left.data = data
            else:
                self.insert(self.left)
        elif data > self.data:
            if self.right is None:
                self.right.data = data
            else:
                self.insert(self.right)

def CreateMiminalBST(arr):
    return CreateMBST(arr, 0, len(arr) - 1)
    
def CreateMBST(arr, start, end):
    if end < start:
        return
        
    mid = (start + end) // 2
    n = TreeNode(arr[mid])
    n.left = CreateMBST(arr, start, mid - 1)
    n.right = CreateMBST(arr, mid + 1, end)
    return n

def MinimalTree(arr, start, end):
    if start > end:
        return 
    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    node.left = MinimalTree(arr, start, mid - 1)
    node.right = MinimalTree(arr, mid + 1, end)
    return node

if __name__ == "__main__":
    #test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    test_array = [1,2,3,4,5,6,7]
    #print(CreateMiminalBST(test_array))
    print(MinimalTree(test_array, 0, len(test_array) - 1))

def createMinimalBST(arr, start, end):
    if start > end:
        return
    
    mid = (start + end) // 2

    n = TreeNode(arr[mid])
    n.left = createMinimalBST(arr, start, mid + 1)
    n.right = createMinimalBST(arr, mid - 1, end)
    return n
