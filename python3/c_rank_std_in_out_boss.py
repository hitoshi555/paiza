N = int(input())
input_line = [input() for i in range(N)]
for item in input_line:
    a, b = item.split(" ")
    print(a, int(b)+1)