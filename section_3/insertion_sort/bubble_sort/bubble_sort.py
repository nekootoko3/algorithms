N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    cnt = 0
    for i in range(N):
        for j in range(N-1, i, -1):
            if j > 0 and A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                cnt += 1
    print(" ".join(map(str, A)))
    print(cnt)