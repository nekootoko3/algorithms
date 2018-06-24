A = list(input().split())


if __name__ == '__main__':
    stack = []
    for item in A:
        if str.isdecimal(item):
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()
            if item == "+":
                stack.append(a+b)
            elif item == "-":
                stack.append(a-b)
            elif item == "*":
                stack.append(a*b)
            else:
                print("invalid item")
    print(stack.pop())