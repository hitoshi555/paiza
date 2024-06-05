# こっちタイムアウトした
# N, K = map(int, input().split())
# A = [int(input()) for _ in range(N)]
# K = [int(input()) for _ in range(K)]



# for k in K:
#     exist = k in A
#     print("YES" if exist else "NO")

# この問題の条件に注目すると 1 ≦ N , Q ≦ 100,000 とあるので、 Q × N は最大で 10,000,000,000 になり得ます。
# これでは実行時間内に答えを出すことはできません。

# 解答
N, Q = map(int, input().split())
A = {int(input()) for _ in range(N)}

for _ in range(Q):
    k = int(input())
    if k in A:
        print("YES")
    else:
        print("NO")