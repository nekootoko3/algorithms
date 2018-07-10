N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

def exhastive_search(target, head, sum):
    for i in range(head, N):
        sum += A[i]
        if target == sum:
            return True
        elif target > sum:
            if exhastive_search(target, i+1, sum):
                return True
            sum -= A[i]
        else:
            sum -= A[i]
    return False


for target in M:
    sum = 0
    result = "no"
    for i in range(N):
        if exhastive_search(target, i, sum):
            result = "yes"
            break
    print(result)