n = int(input())
a = [input().split(" ") for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])

b = sorted(a, reverse=True, key=lambda x: (x[0], x[1])) 

for i in range(len(b)):
    print(str(b[i][0])+" "+str(b[i][1]))

# 解答
# n = int(input())
# ab = [None] * n

# for i in range(n):
#     [a, b] = input().split()
#     a = int(a)
#     b = int(b)
#     ab[i] = [a, b]

# ab.sort(reverse=True)

# for i in range(n):
#     [a, b] = ab[i]
#     print(a, b)