N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    print(" ".join(map(str, A)))
    for i in range(1, N):
        target_num = A[i]
        j = i - 1
        while j >= 0 and A[j] > target_num:
            A[j+1] = A[j]
            j -= 1
            A[j+1] = target_num
        print(" ".join(map(str, A)))