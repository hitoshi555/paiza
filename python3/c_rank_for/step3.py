n = int(input())
input_line = [input() for i in range(n)]
check_num = int(input())

for i in range(len(input_line)):
    sample = int(input_line[i])
    if sample == check_num:
        print(i + 1)
        break