N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

exhaustive_dict = {}

def create_exhastive_list(head, sum):
    for i in range(head, N):
        sum += A[i]
        exhaustive_dict[sum] = 1
        create_exhastive_list(i+1, sum)
        sum -= A[i]

head = 0
sum = 0
create_exhastive_list(head, sum)

for target in M:
    if target in exhaustive_dict.keys():
        print("yes")
    else:
        print("no")