n = int(input())
a = [int(input()) for _ in range(n)]

poped = a.pop(0)

for i in a:
    print(i)