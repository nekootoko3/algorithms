def max_heapify(idx):
    left = idx*2
    right = idx*2+1
    largest = idx
    if left <= N and A[left] > A[idx]:
        largest = left
    if right <= N and A[right] > A[largest]:
        largest = right

    if largest != idx:
        A[idx], A[largest] = A[largest], A[idx]
        max_heapify(largest)


def build_max_heap():
    for idx in range((N+1)//2, 0, -1):
        max_heapify(idx)

N = int(input())
A = [None]
A.extend(list(map(int, input().split())))

build_max_heap()
print(" " + " ".join(map(str, A[1:])))