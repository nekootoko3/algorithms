import sys

def max_heapify( idx):
    l = idx*2
    r = idx*2 + 1
    largest = idx
    if l <= size[0] and queue[l] > queue[largest]:
        largest = l
    if r <= size[0] and queue[r] > queue[largest]:
        largest = r

    if idx != largest:
        queue[idx], queue[largest] = queue[largest], queue[idx]
        max_heapify(largest)

def insert(n):
    size[0] += 1
    queue[size[0]] = n
    idx = size[0]
    while idx > 1 and queue[idx//2] < queue[idx]:
        queue[idx//2], queue[idx] = queue[idx], queue[idx//2]
        idx = idx//2

def extract_max():
    m = queue[1]
    # priority_queue の末尾を取り出してキューの先頭に代入し、heapサイズを一つ小さくする
    queue[1] = queue[size[0]]
    queue[size[0]] = None
    size[0] -= 1
    # 最大ヒープを再度構成する
    max_heapify(1)
    return m

size = [0]
queue = [None for _ in range(2000000)]
while True:
    order, *key = sys.stdin.readline().split()
    if order[0] == "i":
        insert(int(key[0]))
    elif order == "extract":
        m = extract_max()
        print(m)
    else:
        break