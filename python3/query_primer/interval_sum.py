N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = [0] + A[:]
for i in range(1, N + 1):
    ans[i] += ans[i - 1]


for _ in range(K):
    i1, i2 = [int(x) for x in input().split()]
    print(ans[i2] - ans[i1 - 1])

# 解答
# N, K = map(int, input().split())
# A = [int(input()) for _ in range(N)]

# ans = [0] + A[:]
# for i in range(1, N + 1):
#     ans[i] += ans[i - 1]

# for _ in range(K):
#     left, right = map(int, input().split())

#     print(ans[right] - ans[left - 1])