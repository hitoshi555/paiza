n,m,k = input().split(" ")
a = [input() for i in range(int(n))]
for item in a:
    score = 0
    nums = item.split(" ")
    for p in nums:
        if int(p) == int(k):
            score +=1
    print(score)

        