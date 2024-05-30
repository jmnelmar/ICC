import BinaryTree
import Node

class BinaryMinHeap(BinaryTree):
    def __init__(self, data):
        super().__init__(data)

    def insert(self, data, parent):
        super().insert(data, parent)
        self.fix(parent)

    