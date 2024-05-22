n = int(input())
users = [input().split(" ") for item in range(n)]

for i in range(len(users)):
    print('User{')
    print('nickname :', users[i][0])
    print('old :', users[i][1])
    print('birth :', users[i][2])
    print('state :', users[i][3])
    print('}')

# 解答
# N = int(input())

# for _ in range(N):
#     n, o, b, s = input().split()

#     print("User{")
#     print("nickname : " + n)
#     print("old : " + o)
#     print("birth : " + b)
#     print("state : " + s)
#     print("}")