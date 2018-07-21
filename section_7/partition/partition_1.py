def partition(p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i
        
N = int(input())
A = list(map(int, input().split()))
r = partition(0, N-1)

print(" ".join(map(str, A[:r]))+" ["+str(A[r])+"] "+" ".join(map(str, A[r+1:N])))