n, k, q = [int(x) for x in input().split()]

num_array = [None] * n
for i in range(n):
    value = int(input())
    num_array[i] = value

num_array.insert(k, q)

for num in num_array:
    print(num)

# 解答
# N, K, Q = map(int, input().split())
# A = [int(input()) for _ in range(N)]

# A.insert(K, Q)

# for a in A:
#     print(a)
