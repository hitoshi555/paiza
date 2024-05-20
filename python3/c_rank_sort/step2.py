n = int(input())
a = [int(input()) for i in range(n)]
a.sort(reverse=True)

for i in a:
    print(i)