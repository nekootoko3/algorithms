import sys

class Priority_queue:
    def __init__(self):
        self.queue = [None for _ in range(2000000)]
        self.size = 0

    def max_heapify(self, idx):
        l = idx*2
        r = idx*2 + 1
        largest = idx
        if l <= self.size and self.queue[l] > self.queue[largest]:
            largest = l
        if r <= self.size and self.queue[r] > self.queue[largest]:
            largest = r

        if idx != largest:
            self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
            self.max_heapify(largest)

    def insert(self, n):
        self.size += 1
        self.queue[self.size] = n
        idx = self.size
        while idx > 1 and self.queue[idx//2] < self.queue[idx]:
            self.queue[idx//2], self.queue[idx] = self.queue[idx], self.queue[idx//2]
            idx = idx//2

    def extract_max(self):
        m = self.queue[1]
        # priority_queue の末尾を取り出してキューの先頭に代入し、heapサイズを一つ小さくする
        self.queue[1] = self.queue[self.size]
        self.queue[self.size] = None
        self.size -= 1
        # 最大ヒープを再度構成する
        self.max_heapify(1)
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