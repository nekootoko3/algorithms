process_num, qms = map(int, input().split())
raw_procs = [input() for i in range(process_num)]


if __name__ == '__main__':
    procs = []
    for row in raw_procs:
        name, time = row.split()
        procs.append({
            "name": name,
            "time": int(time),
        })

    total_time = 0
    current_proc = 0
    while len(procs) > 0:
        if procs[current_proc]["time"] > qms:
            procs[current_proc]["time"] = procs[current_proc]["time"] - qms
            total_time += qms
            if current_proc == len(procs)-1:
                current_proc = 0
            else:
                current_proc += 1
        else:
            total_time += procs[current_proc]["time"]
            print("{} {}".format(procs[current_proc]["name"], total_time))
            del procs[current_proc]
            if current_proc == len(procs):
                current_proc = 0