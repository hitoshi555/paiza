N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

for _ in range(K):
    k = input()
    if k == "pop":
        del A[0]
    else:
        for a in A:
            print(a)


# 両端キューは collections モジュールの deque クラスとして用意されています。
# この deque オブジェクトの popleft メソッドの計算量は O(1) です。
# from collections import deque

# N, K = map(int, input().split())
# A = deque([int(input()) for _ in range(N)])

# f = 0
# for _ in range(K):
#     s = input()
#     if s == "pop":
#         A.popleft()
#         continue
#     for a in A:
#         print(a)