class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    
    def getnum(self):
        print(self.number)

    def getname(self):
        print(self.name)

n = int(input())

# roster = []
# roster.append()で追加すると16行目いらなくなる
roster = []
for i in range(n):
    data = input().split()
    if data[0] == 'make':
        number = data[1]
        name = data[2]
        roster.append(Employee(number, name))
    elif data[0] == 'getnum':
        roster_num = int(data[1]) - 1
        roster[roster_num].getnum()
    elif data[0] == 'getname':
        roster_num = int(data[1]) - 1
        roster[roster_num].getname()

class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name

# 解答
# n = int(input())

# roster = []
# for _ in range(n):
#     values = input().split()

#     query = values[0]
#     if query == "make":
#         number = int(values[1])
#         name = values[2]
#         roster.append(Employee(number, name))
#     elif query == "getnum":
#         index = int(values[1]) - 1
#         number = roster[index].getnum()
#         print(number)
#     else:
#         index = int(values[1]) - 1
#         name = roster[index].getname()
#         print(name)


    