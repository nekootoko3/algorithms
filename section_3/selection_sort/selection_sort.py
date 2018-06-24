N = int(input())
A = list(map(int, input().split()))

if __name__ == "__main__":
    cnt = 0
    for i in range(N):
        tmp_idx = i
        for j in range(i+1, N):
            if A[tmp_idx] > A[j]:
                tmp_idx = j
        if tmp_idx != i:
            A[i], A[tmp_idx] = A[tmp_idx], A[i]
            cnt += 1

    print(" ".join(map(str, A)))
    print(cnt)