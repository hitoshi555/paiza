n = int(input())
input_line = [input() for i in range(n)]
for item in input_line:
    info = item.split(" ")
    
    hhmm = info[0].split(":")
    hh =int(hhmm[0])
    mm =int(hhmm[1])

    mm += int(info[2])
    hh += int(info[1])

    if mm >= 60:
        mm -= 60
        hh += 1

    if hh >= 24:
        hh -= 24
        
    print(str(hh).zfill(2)+":"+str(mm).zfill(2))