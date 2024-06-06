n, x, p = [int(x) for x in input().split()]
roster = []

for i in range(n):
    s = int(input())
    roster.append(s)

roster.append(x)
roster.append(p)

newlist = sorted(roster)

print(newlist.index(p) + 1)

# 解答
# N, X, P = map(int, input().split())
# A = [int(input()) for _ in range(N)]

# A.append(X)
# A.append(P)
# print(sorted(A).index(P) + 1)