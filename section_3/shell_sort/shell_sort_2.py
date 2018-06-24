N = int(input())
A = [int(input()) for i in range(N)]

def insertion_sort(A, N, diff, cnt):
    for i in range(diff, N):
        tmp_num = A[i]
        j = i - diff
        while j >= 0 and A[j] > tmp_num:
            A[j+diff] = A[j]
            j = j - diff
            cnt += 1
        A[j+diff] = tmp_num
    return cnt

if __name__ == "__main__":
    cnt = 0
    diffs = []
    h = 1
    while h <= N:
        diffs.append(h)
        h = h*3 + 1
    diffs.reverse()
    diffs_cnt = len(diffs)
    for diff in diffs:
        cnt = insertion_sort(A, N, diff, cnt)
    print(diffs_cnt)
    print(" ".join(map(str, diffs)))
    print(cnt)
    for num in A:
        print(num)
