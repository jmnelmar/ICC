'''
Considerations:
Node: i
left child: 2i + 1
right child: 2i + 2
parent: (i - 1)/2
'''
class BinaryMinHeap:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.heap = []

    def insert(self,element):
        self.heap.append(element)
        self._siftup(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def get_max(self):
        pass

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval
        

    def extract_max(self):
        pass

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)
    
    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old),new)

    def build(self):
        #self.heap = arr.copy()
        for i in range(len(self.heap))[::-1]:
            self._siftdown

    def _siftup(self, i):
        parent = (i - 1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2

        while (
            (left < len(self.heap) and self.heap[i] > self.heap[left]) or
            (right < len(self.heap) and self.heap[i] > self.heap[right])
               ):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

