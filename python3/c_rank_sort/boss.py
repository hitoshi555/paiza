n = int(input())
a = [input().split(" ") for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])

b = sorted(a, reverse=True, key=lambda x: (x[1], x[0])) 

for i in range(len(b)):
    print(str(b[i][0])+" "+str(b[i][1]))

# 解答
# N = int(input())
# kingin = [0] * N

# for i in range(N):
#     [a, b] = [int(j) for j in input().split()]
#     kingin[i] = [b, a]

# kingin.sort(reverse=True)

# for i in range(N):
#     [a, b] = kingin[i]
#     print(b, a)