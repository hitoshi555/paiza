n = int(input())
input_line = [input() for i in range(n)]
flag = False
for item in input_line:
    a = int(item)
    if a == 7:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")