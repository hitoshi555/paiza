n = int(input())
users = {}

for i in range(n):
    s = input()
    users[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split(" ")
    users[p] = users[p] + int(a)

S = input()
print(users[S])