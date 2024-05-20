m = int(input())
c = [input() for i in range(m)]
n = int(input())
s = [input() for i in range(n)]

for i in range(len(c)):
    for j in range(len(s)):
        flag = False

        if s[j].find(c[i]) >= 0:
            flag = True

        if flag:
            print("YES")
        else:
            print("NO")
        