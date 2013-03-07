class Heap(list):

    _length = None

    def __init__(self, *args):
        super(Heap, self).__init__(*args)
        self.build()
        self._length = len(self)

    def root(self):
        return self.valid_index(0)

    def parent(self, i):
        return self.valid_index((i - 1) / 2)

    def left_child(self, i):
        return self.valid_index(2 * i + 1)

    def right_child(self, i):
        return self.valid_index(2 * i + 2)

    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        maxi = i
        if left != None and not self.valid_cond(i, left):
            maxi = left
        if right != None and not self.valid_cond(maxi, right):
            maxi = right
        if maxi != i:
            self.swap(i, maxi)
            self.heapify(maxi)
        return self

    def build(self):
        for i in xrange(len(self)/2 - 1, -1, -1):
            self.heapify(i)
        return self

    def sort(self):
        self.build()
        self._length = len(self)
        for i in xrange(len(self) - 1, 0, -1):
            self.swap(self.root(), i)
            self._length -= 1;
            self.heapify(self.root())
        return self

    def swap(self, i, j):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp

    def __add__(self, rhs):
        # TODO
        return Heap(list.__add__(self, rhs))

    def valid_index(self, i):
        return i if 0 <= i < len(self) else None

    def valid_cond(self, parent, child):
        return self[parent] >= self[child]

    def __get_or_none(self, i):
        try:
            return self.__getitem__(i)
        except:
            return None

    # def __str__(self):
    #     return '[' + ', '.join([str(x) for x in self[:len(self)]]) + ']'

    def append(self, *args):
        super(Heap, self).append(*args)
        self._updateToRealLength();

    def __len__(self):
        return self._length if self._length != None else self.realLength()

    def realLength(self):
        return super(Heap, self).__len__()

    def _updateToRealLength(self):
        # TODO inelegant
        self._length = super(Heap, self).__len__()

    def _updateLength(self):
        # TODO inelegant
        diff = self._length - self.realLength()
        if diff > 0:
            self.extend([-float('inf')] * diff)

    def __getitem__(self, item):
        result = list.__getitem__(self, item)
        try:
            return Heap(result)
        except TypeError:
            return result
