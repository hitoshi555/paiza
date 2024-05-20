n = int(input())
input_line = input().split(" ")
cut = 0
for item in input_line:
    a = int(item)
    if a % 3 == 0:
        cut += 1

print(cut)