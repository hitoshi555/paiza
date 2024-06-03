class Robot:
    def __init__(self, level, x, y):
        self.level = level
        self.x = x
        self.y = y

h, w, n, k = [int(x) for x in input().split()]

maps = [[0]*w]*h