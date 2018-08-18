from heapq import heappop, heappush
import sys

queue = []
while True:
    order, *key = sys.stdin.readline().split()
    if order == "insert":
        heappush(queue, -int(key[0]))
    elif order == "extract":
        print(-heappop(queue))
    else:
        break