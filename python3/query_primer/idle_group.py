n, k = [int(x) for x in input().split()]
members = [input() for _ in range(n)]

for i in range(k):
    datas = input().split()
    if datas[0] == "handshake":
        sorted_members = sorted(members)
        for name in sorted_members:
            print(name)
    elif datas[0] == "leave":
        members.remove(datas[1])
    elif datas[0] == "join":
        members.append(datas[1])

# 解答
# N, K = map(int, input().split())
# names = {input() for _ in range(N)}

# for _ in range(K):
#     event = input()

#     if event == "handshake":
#         for name in sorted(names):
#             print(name)
#     else:
#         event, name = event.split()
#         if event == "join":
#             names.add(name)
#         else:
#             names.remove(name)