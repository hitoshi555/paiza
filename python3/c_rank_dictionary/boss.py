p, q, r = input().split(" ")
ab = {}
bc = {}
ac = {}

for i in range(int(p)):
    a, b = input().split(" ")
    ab[int(a)] = int(b)

for i in range(int(q)):
    b, c = input().split(" ")
    bc[int(b)] = int(c)

for key,value in ab.items():
    if value in bc:
        c = bc[value]
        ac[key] = c

ans = sorted(ac.items())

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])

# 解答
# [p, q, r] = [int(i) for i in input().split()]
# AB = {}
# BC = {}

# for _ in range(p):
#     [i, j] = [int(n) for n in input().split()]
#     AB[i] = j

# for _ in range(q):
#     [j, k] = [int(n) for n in input().split()]
#     BC[j] = k

# AC = {}

# for i in range(1, p + 1):
#     AC[i] = BC[AB[i]]

# for i, k in AC.items():
#     print(i, k)