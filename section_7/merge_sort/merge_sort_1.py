N = int(input())
A = list(map(int, input().split()))

INFTY = 1000000001
cnt = [0]

def merge(left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0 for _ in range(n1+1)]
    R = [0 for _ in range(n2+1)]
    for i in range(n1):
        L[i] = A[left+i]
    for i in range(n2):
        R[i] = A[mid+i]
    L[n1] = INFTY
    R[n2] = INFTY
    i = 0
    j = 0
    for k in range(left, right):
        cnt[0] += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(left, right):
    if left+1 < right:
        mid = int((left+right) / 2)
        merge_sort(left, mid)
        merge_sort(mid, right)
        merge(left, mid, right)

merge_sort(0, N)
print(" ".join(map(str, A)))
print(cnt[0])