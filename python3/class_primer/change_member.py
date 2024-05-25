class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    
    def getnum(self):
        print(self.number)

    def getname(self):
        print(self.name)

    def change_num(self, new_num):
        self.number = new_num
    
    def changeName(self, new_name ):
        self.name = new_name

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
    elif data[0] == 'change_num':
        roster_num = int(data[1]) - 1
        roster[roster_num].change_num(int(data[2]))
    elif data[0] == 'change_name':
        roster_num = int(data[1]) - 1
        roster[roster_num].changeName(data[2])

# class Employee:
#     def __init__(self, number, name):
#         self.number = number
#         self.name = name

#     def getnum(self):
#         return self.number

#     def getname(self):
#         return self.name

# 解答
# class Employee:
#     def __init__(self, number, name):
#         self.number = number
#         self.name = name

#     def getnum(self):
#         return self.number

#     def getname(self):
#         return self.name

#     def change_num(self, number):
#         self.number = number

#     def change_name(self, name):
#         self.name = name


# n = int(input())

# roster = []
# for _ in range(n):
#     values = input().split()

#     query = values[0]
#     if query == "make":
#         number = int(values[1])
#         name = values[2]
#         roster.append(Employee(number, name))
#     else:
#         index = int(values[1]) - 1
#         if query == "getnum":
#             number = roster[index].getnum()
#             print(number)
#         elif query == "getname":
#             name = roster[index].getname()
#             print(name)
#         elif query == "change_num":
#             new_num = int(values[2])
#             roster[index].change_num(new_num)
#         else:
#             new_name = values[2]
#             roster[index].change_name(new_name)


    