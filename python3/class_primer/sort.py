class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)


sort_roster = sorted(roster, key=lambda u:u.old)

for student in sort_roster:
    print(student.name, student.old, student.birth, student.state)