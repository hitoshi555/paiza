import math

N, L = input().split(" ")
# digs = [int(tok) for tok in input().split()]  
input_line = [input() for i in range(int(N))]
ans = int(L)
for item in input_line:
    eL = int(item)
    if ans > eL:
        p = math.floor(eL / 2)
        ans += p
    if ans < eL:
        p = math.floor(ans / 2)
        ans = p
print(ans)