N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

combinations = {}

def create_combinations(idx, sum):
    combinations[sum] = 1
    if idx >= N:
        return
    create_combinations(idx+1, sum)
    create_combinations(idx+1, sum+A[idx])
    return

create_combinations(0, 0)

for target in M:
    if target in combinations.keys():
        print("yes")
    else:
        print("no")