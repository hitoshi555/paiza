class Hero:
    def __init__(self, level, hp, Opower, Dpower, agility, wisdom, luck):
        self.level = level
        self.hp = hp
        self.Opower = Opower
        self.Dpower = Dpower
        self.agility = agility
        self.wisdom = wisdom
        self.luck = luck

    def levelup(self, h, a, d, s, c, f):
        self.level += 1
        self.hp += h
        self.Opower += a
        self.Dpower += d
        self.agility += s
        self.wisdom += c
        self.luck += f
    
    def muscle_training(self, h, a):
        self.hp += h
        self.Opower += a
    
    def running(self, d, s):
        self.Dpower += d
        self.agility += s
    
    def study(self, c):
        self.wisdom += c
    
    def pray(self, f):
        self.luck += f
    
    def profile(self):
        print(self.level, self.hp, self.Opower, self.Dpower, self.agility, self.wisdom, self.luck)

n, k = [int(item) for item in input().split()]

heros = [None] * n
for i in range(n):
    [level, hp, Opower, Dpower, agility, wisdom, luck] = [int(item) for item in input().split()]
    heros[i] = Hero(level, hp, Opower, Dpower, agility, wisdom, luck)

for i in range(k):
    values = input().split()
    index = int(values[0]) - 1
    if values[1] == "levelup":
        h = int(values[2])
        a = int(values[3])
        d = int(values[4])
        s = int(values[5])
        c = int(values[6])
        f = int(values[7])
        heros[index].levelup(h, a, d, s, c, f)
    elif values[1] == "muscle_training":
        h = int(values[2])
        a = int(values[3])
        heros[index].muscle_training(h, a)
    elif values[1] == "running":
        d = int(values[2])
        s = int(values[3])
        heros[index].running(d, s)
    elif values[1] == "study":
        c = int(values[2])
        heros[index].study(c)
    elif values[1] == "pray":
        f = int(values[2])
        heros[index].pray(f)

for i in range(len(heros)):
    print(heros[i].level, heros[i].hp, heros[i].Opower, heros[i].Dpower, heros[i].agility, heros[i].wisdom, heros[i].luck)



#解答
# class Hero:
#     def __init__(self, lv, hp, at, df, sp, cl, ft):
#         self.lv = lv
#         self.hp = hp
#         self.at = at
#         self.df = df
#         self.sp = sp
#         self.cl = cl
#         self.ft = ft

#     def levelup(self, hp, at, df, sp, cl, ft):
#         self.lv += 1
#         self.hp += hp
#         self.at += at
#         self.df += df
#         self.sp += sp
#         self.cl += cl
#         self.ft += ft

#     def muscle_training(self, hp, at):
#         self.hp += hp
#         self.at += at

#     def running(self, df, sp):
#         self.df += df
#         self.sp += sp

#     def study(self, cl):
#         self.cl += cl

#     def pray(self, ft):
#         self.ft += ft

#     def print(self):
#         print(self.lv, self.hp, self.at, self.df, self.sp, self.cl, self.ft)


# n, k = [int(x) for x in input().split()]

# heroes = [None] * n
# for i in range(n):
#     lv, hp, at, df, sp, cl, ft = [int(x) for x in input().split()]
#     heroes[i] = Hero(lv, hp, at, df, sp, cl, ft)

# for _ in range(k):
#     values = input().split()

#     index = int(values.pop(0)) - 1
#     event = values.pop(0)

#     if event == "levelup":
#         hp, at, df, sp, cl, ft = [int(x) for x in values]
#         heroes[index].levelup(hp, at, df, sp, cl, ft)
#     elif event == "muscle_training":
#         hp, at = [int(x) for x in values]
#         heroes[index].muscle_training(hp, at)
#     elif event == "running":
#         df, sp = [int(x) for x in values]
#         heroes[index].running(df, sp)
#     elif event == "study":
#         cl = int(values[0])
#         heroes[index].study(cl)
#     else:
#         ft = int(values[0])
#         heroes[index].pray(ft)

# for hero in heroes:
#     hero.print()