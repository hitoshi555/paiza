n = int(input())
[a, b] = [int(item) for item in input().split(" ")]

users = {
    "paiza":1,
    "kyouko":1,
}

cut = 0
while True:
    cut +=1
    users["kyouko"] = users["kyouko"] + (users["paiza"] * a)
    users["paiza"] = users["paiza"] + (users["kyouko"] % b)
    
    if users["kyouko"] > n:
        print(cut)
        break