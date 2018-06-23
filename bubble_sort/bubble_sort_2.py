N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    flg = True
    cnt = 0
    while flg:
        for i in range(N):
            flg = False
            for j in range(N-1, i, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
                    cnt += 1
                    flg = True
    print(" ".join(map(str, A)))
    print(cnt)