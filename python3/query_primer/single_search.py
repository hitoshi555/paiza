N, K = [int(x) for x in input().split()]

datas = []

for _ in range(N):
    data = int(input())
    datas.append(data)

flag = K in datas
if flag:
    print("YES")
else:
    print("NO")

# 解答 map 使っている
# N, K = map(int, input().split())
# A = [int(input()) for _ in range(N)]

# exist = False
# for a in A:
#     if a == K:
#         exist = True
#         break

# print("YES" if exist else "NO")