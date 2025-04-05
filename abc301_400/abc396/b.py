q = int(input())
stack = []

for _ in range(100):
    stack.append(0)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        stack.append(x)
    else:
        print(stack.pop())
