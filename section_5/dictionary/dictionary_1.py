N = int(input())
A = [input() for i in range(N)]
M = 1046527
T = [0 for i in range(M)]

# 各文字をバイト列にした後、それらを10進数にして、文字列として結合する
def get_key(value: str) -> int:
    converted_value = ""
    for s in value:
        b = s.encode()
        converted_value += str(b[0])
    return int(converted_value)

def h1(key: int) -> int:
    return key % M

def h2(key: int) -> int:
    move_value = 1 + (key % (M-1))
    return move_value

def h(key:int, i:int) -> int:
    hash_value = (h1(key) + i+h2(key)) % M
    return hash_value

def find(key: int) -> bool:
    i = 0
    while True:
        j = h(key, i)
        if T[j] == key:
            return True
        elif T[j] == 0 or i >= M:
            return False
        else:
            i += 1


def insert(key: int) -> None:
    i = 0
    while True:
        j = h(key, i)
        if T[j] == 0:
            T[j] = key
            return
        else:
            i += 1


for row in A:
    order, value = row.split()
    key = get_key(value)
    if order[0] == "i":
        insert(key)
    else:
        if find(key):
            print("yes")
        else:
            print("no")