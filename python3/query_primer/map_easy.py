n, k = [int(x) for x in input().split()]
a = {}
for _ in range(n):
    key, name = input().split()
    a[int(key)] = name

for _ in range(k):
    student_id = int(input())
    print(a[student_id])

# 解答
# N, K = map(int, input().split())
# roster = {(x, y) for x, y in [input().split() for _ in range(N)]}

# for _ in range(K):
#     q = input()
#     for num, ID in roster:
#         if num == q:
#             print(ID)