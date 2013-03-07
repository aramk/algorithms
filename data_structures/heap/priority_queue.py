from heap import *

class PriorityQueue(Heap):
    def max(self):
        return self[0]

    def extractMax(self):
        if len(self) == 0:
            raise Exception('Heap is empty')
        maxi = self.max()
        self[0] = self[self._length - 1]
        self._length -= 1
        self.heapify(0)
        return maxi

    def increase(self, i, key):
        if key < self[i]:
            raise Exception('Key cannot be decreased')
        self[i] = key
        while i > 0 and not self.valid_cond(self.parent(i), i):
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def insert(self, key):
        self._length += 1
        self._updateLength()
        self.increase(self._length - 1, key)

