n = int(input())
a = list(map(int, input().split()))

for i in range(0, len(a)-3):
    if a[i] == a[i+1] and a[i+1] == a[i+2]:
        print("Yes")
        exit()

print("No")