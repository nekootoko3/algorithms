import sys

class Priority_queue:
    def __init__(self):
        self.queue = [None for _ in range(2000000)]
        self.tail = 0

    def max_heapify(self, idx):
        l = idx*2
        r = idx*2 + 1
        largest = idx
        if l <= self.tail and self.queue[l] > self.queue[largest]:
            largest = l
        if r <= self.tail and self.queue[r] > self.queue[largest]:
            largest = r

        if idx != largest:
            self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
            self.max_heapify(largest)

    def insert(self, n):
        self.tail += 1
        self.queue[self.tail] = n
        parent = self.tail // 2
        while parent != 0:
            self.max_heapify(parent)
            parent = parent // 2

    def extract_max(self):
        m = self.queue[1]
        # priority_queue の末尾を取り出し、キューの先頭に代入する
        self.queue[1] = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail -= 1
        # 最大ヒープを再度構成する
        for i in range(self.tail//2, 0, -1):
            self.max_heapify(i)
        return m

pq = Priority_queue()
while True:
    order, *key = sys.stdin.readline().split()
    if order == "insert":
        pq.insert(int(key[0]))
    elif order == "extract":
        m = pq.extract_max()
        print(m)
    else:
        break