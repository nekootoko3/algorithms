N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
M = list(map(int, input().split()))

def solve(idx, target):
    if target == 0:
        return True
    elif target < 0:
        return False
    if idx >= N:
        return False
    if solve(idx+1, target) or solve(idx+1, target-A[idx]):
        return True
    return False


for target in M:
    if solve(0, target):
        print("yes")
    else:
        print("no")