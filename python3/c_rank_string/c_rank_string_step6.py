s = input().split(":")

hh =int(s[0])
mm =int(s[1])

mm += 30

if mm >= 60:
    mm -= 60
    hh += 1

if hh >= 24:
    hh -= 24

print(str(hh).zfill(2)+":"+str(mm).zfill(2))