N, K = map(int, input().split())

data = {}
for _ in range(N):
    s = input()
    data[s] = []

for _ in range(K):
    a, p, m = input().split()

    data[a].append((p,m))

for key, value in data.items():
    print(key)
    for item in value:
        print(item[0], item[1])
    print("-----")

# 解答
# N, K = map(int, input().split())
# departments = {input(): [] for _ in range(N)}

# for _ in range(K):
#     a, p, m = input().split()

#     departments[a].append((p, m))

# for key, val in departments.items():
#     print(key)
#     for p, m in val:
#         print(p, m)

#     print("-----")