n = int(input())
# これリスト型、辞書型じゃない
s = [None] * n

for i in range(n):
    a,b = input().split(" ")
    s[i] = [a, b]

S = input()

for i in s:
    if i[0] == S:
        print(i[1])
        break

# 解答
# n = int(input())
# zaisan = {}

# for i in range(n):
#     [s, a] = input().split()
#     zaisan[s] = a

# S = input()

# print(zaisan[S])