class Heap(list):

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
        if right != None and not self.valid_cond(i, maxi):
            maxi = right
        if maxi != i:
            self.swap(i, maxi)
            self.heapify(maxi)

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

    def __getitem__(self, item):
        result = list.__getitem__(self, item)
        try:
            return Heap(result)
        except TypeError:
            return result

h = Heap([1, 2, 3])
h.heapify(0)
print h
