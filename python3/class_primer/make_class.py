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
roster = [None] * n
num = 0
for i in range(n):
    data = input().split()
    if data[0] == 'make':
        number = data[1]
        name = data[2]
        roster[num] = Employee(number, name)
        num += 1
    elif data[0] == 'getnum':
        roster_num = int(data[1]) - 1
        roster[roster_num].getnum()
    elif data[0] == 'getname':
        roster_num = int(data[1]) - 1
        roster[roster_num].getname()


    