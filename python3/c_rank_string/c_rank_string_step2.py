n = input()
S = list(input())
ans = "NO"
for item in S:
    if item == n:
        ans = "YES"
        break
print(ans)