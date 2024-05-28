class Customer:
    in_store = True
    def __init__(self):
        self.sum = 0

    def take_food(self, price):
        self.sum += price

    def take_softdrink(self, price):
        self.sum += price

    def take_alcohol(self, price=500):
        # 何もしない (却下)
        pass

    def get_sum(self):
        return self.sum

    def out_store(self):
        self.in_store = False


class Adult(Customer):
    def __init__(self):
        super().__init__()
        self.alcohol = False

    def take_food(self, price):
        if self.alcohol:
            self.sum += price - 200
        else:
            self.sum += price

    def take_alcohol(self, price=500):
        self.sum += price
        self.alcohol = True


n, k = [int(x) for x in input().split()]
cunt = 0

customers = [None] * n
for i in range(n):
    age = int(input())

    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Customer()

for _ in range(k):
    values = input().split()

    index = int(values[0]) - 1
    order = values[1]

    if order == "0":
        customers[index].take_alcohol()
    elif order == "A":
        customers[index].out_store()
        print(customers[index].get_sum())
        cunt += 1
    else:
        price = int(values[2])

        if order == "food":
            customers[index].take_food(price)
        elif order == "softdrink":
            customers[index].take_softdrink(price)
        else:
            customers[index].take_alcohol(price)

print(cunt)

# 解答
#   解説
#       未成年のお客さんのクラス・成年済のお客さんのクラスに会計をする関数を追加し、会計ごとに金額を出力し、退店者数を +1 する必要があります。
#       退店者数はグローバル変数で管理することもできますが、お客さんに関する情報なので、クラスの中で管理するのが望ましいです。そこでクラスの静的メンバを用いることができます。
#       静的メンバとは、オブジェクト間を超えて共有される変数や関数のことです。これを用いることで、お客さん一人一人が退店した人数を覚えておくよりも、効率的に退店した人数を記憶しておくことができます。
# class Customer:
#     n = 0

#     def __init__(self):
#         self.sum = 0

#     def take_food(self, price):
#         self.sum += price

#     def take_softdrink(self, price):
#         self.sum += price

#     def take_alcohol(self, price=500):
#         # 何もしない (却下)
#         pass

#     def accounting(self):
#         Customer.n += 1
#         print(self.sum)


# class Adult(Customer):
#     def __init__(self):
#         super().__init__()
#         self.alcohol = False

#     def take_food(self, price):
#         if self.alcohol:
#             self.sum += price - 200
#         else:
#             self.sum += price

#     def take_alcohol(self, price=500):
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

#     if order == "0":
#         customers[index].take_alcohol()
#     elif order == "A":
#         customers[index].accounting()
#     else:
#         price = int(values[2])

#         if order == "food":
#             customers[index].take_food(price)
#         elif order == "softdrink":
#             customers[index].take_softdrink(price)
#         else:
#             customers[index].take_alcohol(price)

# print(Customer.n)