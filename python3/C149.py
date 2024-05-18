S = list(input())
T = list(input())

for i in T:
    for j in S:
        if i.lower() == j or i.upper() == j:
            print(j , end="")
