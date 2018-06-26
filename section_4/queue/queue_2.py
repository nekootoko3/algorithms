from collections import deque
 
process_num, qms = map(int ,input().split())
que = deque({})
 
for i in range(process_num):
    name, time = input().split()
    time = int(time)
    que.append({"name":name, "time":time})
 
if __name__ == '__main__':
    total_time = 0
    while len(que)>0:
        atop = que.popleft()
        spend = min(atop["time"], qms)
        atop["time"] -= spend
        total_time += spend
        if(atop["time"] == 0):
            print("{} {}".format(atop["name"], total_time))
        else:
            que.append(atop)

