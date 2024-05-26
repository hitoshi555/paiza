class Miner:
    def __init__(self, old):
        self.old = old
        self.sum = 0

    def getAlcohol(self, price):
        return
    
    def getSoftdrink(self, price):
        self.sum += price
    
    def getFood(self, price):
        self.sum += price

class Adult(Miner):
    def __init__(self, old):
        super().__init__(old)
        self.alcohol = False
    
    def getAlcohol(self, price):
        self.sum += price
        self.alcohol = True
    
    def getFood(self, price):
        if self.alcohol:
            self.sum += (price - 200)
        else:
            self.sum += price



n , k = [int(item) for item in input().split()]
customer = []

for i in range(n):
    old = int(input())
    if old >= 20:
        customer.append(Adult(old))
    else:
        customer.append(Miner(old))

for i in range(k):
    data = input().split()
    num = int(data[0]) - 1
    price = int(data[2])
    if data[1] == 'food':
        customer[num].getFood(price)
    elif data[1] == 'alcohol':
        customer[num].getAlcohol(price)
    elif data[1] == 'softdrink':
        customer[num].getSoftdrink(price)

for c in customer:
    print(c.sum)
    

# 解答
# class Customer:
#     def __init__(self):
#         self.sum = 0

#     def take_food(self, price):
#         self.sum += price

#     def take_softdrink(self, price):
#         self.sum += price

#     def take_alcohol(self, price):
#         # 何もしない (却下)
#         pass

#     def get_sum(self):
#         return self.sum


# class Adult(Customer):
#     def __init__(self):
#         super().__init__()
#         self.alcohol = False

#     def take_food(self, price):
#         if self.alcohol:
#             self.sum += price - 200
#         else:
#             self.sum += price

#     def take_alcohol(self, price):
#         self.sum += price
#         self.alcohol = True


# n, k = [int(x) for x in input().split()]

# customers = [None] * n
# for i in range(n):
#     age = int(input())

#     if age >= 20:
#         customers[i] = Adult()
#     else:
#         customers[i] = Customer()

# for _ in range(k):
#     values = input().split()

#     index = int(values[0]) - 1
#     order = values[1]
#     price = int(values[2])

#     if order == "food":
#         customers[index].take_food(price)
#     elif order == "softdrink":
#         customers[index].take_softdrink(price)
#     else:
#         customers[index].take_alcohol(price)

# for customer in customers:
#     print(customer.get_sum())



    