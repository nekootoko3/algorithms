N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    print(" ".join(map(str, A)))
    for i in range(1, N):
        target_num = A[i]
        for j in range(i):
            if A[j] > target_num:
                tmp_idx = i
                while j < tmp_idx:
                    A[tmp_idx] = A[tmp_idx-1]
                    tmp_idx -= 1
                A[j] = target_num
                break
        print(" ".join(map(str, A)))