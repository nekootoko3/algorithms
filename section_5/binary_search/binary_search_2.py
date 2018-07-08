N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

def binary_search(target_num, head, tail):
    while head <= tail:
        idx = int((head+tail)/2)
        if target_num == S[idx]:
            return True
        elif target_num < S[idx]:
            tail = idx - 1
        else:
            head = idx + 1
    return False


match_count = 0
for target_num in T:
    if binary_search(target_num, 0, len(S)-1):
        match_count += 1

print(str(match_count))