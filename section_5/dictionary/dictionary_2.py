N = int(input())
A = [input() for i in range(N)]

D = {}
for row in A:
    order, key = row.split()
    if order[0] == "i":
        D[key] = 1
    else:
        if key in D.keys():
            print("yes")
        else:
            print("no")