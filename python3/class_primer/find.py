N = int(input())
users = []

for _ in range(N):
    n, o, b, s = input().split(" ")
    users.append([n, o, b, s])

O = int(input())
for i in range(len(users)):
    if O == int(users[i][1]):
        print(users[i][0])
        break

# 解答
# class Student:
#     def __init__(self, name, old, birth, state):
#         self.name = name
#         self.old = old
#         self.birth = birth
#         self.state = state


# n = int(input())

# roster = [None] * n
# for i in range(n):
#     name, old, birth, state = input().split()
#     roster[i] = Student(name, old, birth, state)

# k = input()
# for student in roster:
#     if student.old == k:
#         print(student.name)
#         break