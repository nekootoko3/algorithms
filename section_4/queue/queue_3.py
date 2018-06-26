N, qms = map(int, input().split())

raw_proc = [input() for i in range(N)]
queue = [{} for i in range(N+1)]
limit = N+1
for i in range(N):
    name, time = raw_proc[i].split()
    time = int(time)
    queue[i] = {"name": name, "time": time}


def enque(tail, p):
    queue[tail] = p
    tail = (tail+1) % limit
    return tail


def deque(head):
    proc = queue[head]
    head = (head+1) % limit
    return proc, head


if __name__ == '__main__':
    head = 0
    tail = N
    total_time = 0
    while head != tail:
        p, head = deque(head)
        t = min(qms, p["time"])
        p["time"] = p["time"] - t
        total_time += t
        if p["time"] > 0:
            tail = enque(tail, p)
        else:
            print("{} {}".format(p["name"], total_time))
