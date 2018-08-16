N = int(input())

A = [None for _ in range(N+1)]
node = 1
for key in input().split():
    A[node] = key
    node += 1

for i in range(1, N+1):
    key = str(A[i])
    parent_id = i//2
    left_id = 2*i
    right_id = 2*i+1
    out = "node {}: key = {}, ".format(str(i), key)
    if parent_id != 0:
        out += "parent key = {}, ".format(str(A[parent_id]))
    if left_id < N+1:
        out += "left key = {}, ".format(str(A[left_id]))
        if right_id < N+1:
            out += "right key = {}, ".format(str(A[right_id]))
    print(out)
