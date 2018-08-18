def max_heapify(idx):
    l = idx*2
    r = idx*2 + 1
    largest = idx
    if l < len(pq) and pq[l] > pq[largest]:
        largest = l
    if r < len(pq) and pq[r] > pq[largest]:
        largest = r

    if idx != largest:
        pq[idx], pq[largest] = pq[largest], pq[idx]
        max_heapify(largest)


def insert(n):
    pq.append(n)
    inserted = len(pq)-1
    parent = inserted // 2
    while parent != 0:
        max_heapify(parent)
        parent = parent // 2

def extract_max():
    m = pq[1]
    # priority_queue の末尾を取り出し、キューの先頭に代入する
    tail = pq.pop()
    if len(pq) > 1:
        pq[1] = tail
    # 最大ヒープを再度構成する
    for i in range((len(pq)-1)//2, 0, -1):
        max_heapify(i)
    return m

pq = [None]
while True:
    order, *key = input().split()
    if order == "insert":
        insert(int(key[0]))
    elif order == "extract":
        m = extract_max()
        print(m)
    else:
        break