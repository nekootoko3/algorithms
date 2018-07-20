N = int(input())
A = list(map(int, input().split()))

INFTY = 1000000001
cnt = [0]

def merge(left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = A[left:left+n1]
    R = A[mid:mid+n2]
    L.append(INFTY)
    R.append(INFTY)
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