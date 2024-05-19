n = int(input())
input_line = [input() for i in range(n)]
ans = int(input_line[0])
for item in input_line:
    if ans < int(item):
        ans = int(item)
print(ans)