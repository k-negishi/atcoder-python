n = int(input())
p = list(map(int, input().split()))

p1 = p[0]
others = p[1:]
if not others:
    print(0)
else:
    p_max = max(others)
    if p1 > p_max:
        print(0)
    else:
        print(p_max - p1 + 1)
