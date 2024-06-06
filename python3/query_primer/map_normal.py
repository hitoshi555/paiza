n, k = [int(x) for x in input().split()]
roster = {}
for _ in range(n):
    key, name = input().split()
    roster[key] = name

for _ in range(k):
    datas = input().split()
    if datas[0] == "call":
        print(roster[datas[1]])
    elif datas[0] == "leave":
        del roster[datas[1]]
    elif datas[0] == "join":
        roster[datas[1]] = datas[2]

# 解答
# N, K = map(int, input().split())
# roster = {x: y for x, y in [input().split() for _ in range(N)]}

# for _ in range(K):
#     s = input().split()
#     if s[0] == "join":
#         num, ID = s[1:]
#         roster[num] = ID
#     elif s[0] == "leave":
#         num = s[1]
#         del roster[num]
#     else:
#         num = s[1]
#         print(roster[num])