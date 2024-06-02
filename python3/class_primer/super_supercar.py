class SuperCar:
    def __init__(self, amount_of_fuel, fuel_efficiency):
        self.amount_of_fuel = amount_of_fuel
        self.fuel_efficiency = fuel_efficiency
        self.driving_distance = 0

    def run(self):
        if self.amount_of_fuel <= 0:
            return
        else:
            self.amount_of_fuel -= 1
            self.driving_distance += self.fuel_efficiency

class SuperSuperCar(SuperCar):
    def __init__(self, amount_of_fuel, fuel_efficiency):
        super().__init__(amount_of_fuel, fuel_efficiency)
    
    def fly(self):
        if self.amount_of_fuel >= 5:
            self.amount_of_fuel -= 5
            distance = self.fuel_efficiency ** 2
            self.driving_distance += distance
        else:
            self.run()

class SuperSuperSuperCar(SuperSuperCar):
    def __init__(self, amount_of_fuel, fuel_efficiency):
        super().__init__(amount_of_fuel, fuel_efficiency)
    
    def fly(self):
        if self.amount_of_fuel >= 5:
            self.amount_of_fuel -= 5
            distance = self.fuel_efficiency ** 2
            self.driving_distance += 2 * distance
        else:
            self.run()
    
    def teleport(self):
        fuel = self.fuel_efficiency ** 2
        if self.amount_of_fuel >= fuel:
            self.amount_of_fuel -= fuel
            distance = self.fuel_efficiency ** 4
            self.driving_distance += distance
        else:
            self.fly()

n, k = [int(x) for x in input().split()]
cars = [None]* n

for i in range(n):
    values = input().split()
    if values[0] == "supersupersupercar":
        amount_of_fuel = int(values[1])
        fuel_efficiency = int(values[2])
        cars[i] = SuperSuperSuperCar(amount_of_fuel, fuel_efficiency)
    elif values[0] == "supersupercar":
        amount_of_fuel = int(values[1])
        fuel_efficiency = int(values[2])
        cars[i] = SuperSuperCar(amount_of_fuel, fuel_efficiency)
    else:
        amount_of_fuel = int(values[1])
        fuel_efficiency = int(values[2])
        cars[i] = SuperCar(amount_of_fuel, fuel_efficiency)

for i in range(k):
    values = input().split()
    index = int(values[0]) - 1
    if values[1] == "fly":
        cars[index].fly()
    elif values[1] == "teleport":
        cars[index].teleport()
    else:
        cars[index].run()

for car in cars:
    print(car.driving_distance)

# 解答
# class superCar:
#     def __init__(self, f, f_c):
#         self.fuel = f
#         self.fuel_consumption = f_c
#         self.mileage = 0

#     def run(self):
#         if self.fuel <= 0:
#             return

#         self.fuel -= 1
#         self.mileage += self.fuel_consumption

#     def get_mileage(self):
#         return self.mileage


# class superSuperCar(superCar):
#     def fly(self):
#         if self.fuel < 5:
#             super().run()
#         else:
#             self.fuel -= 5
#             self.mileage += self.fuel_consumption ** 2


# class superSuperSuperCar(superCar):
#     def fly(self):
#         if self.fuel < 5:
#             super().run()
#         else:
#             self.fuel -= 5
#             self.mileage += 2 * self.fuel_consumption ** 2

#     def teleport(self):
#         if self.fuel < self.fuel_consumption ** 2:
#             self.fly()
#         else:
#             self.fuel -= self.fuel_consumption ** 2
#             self.mileage += self.fuel_consumption ** 4


# n, k = [int(x) for x in input().split()]

# cars = [None] * n
# for i in range(n):
#     values = input().split()

#     car_type = values[0]
#     fuel = int(values[1])
#     fuel_consumption = int(values[2])

#     if car_type == "supercar":
#         cars[i] = superCar(fuel, fuel_consumption)
#     elif car_type == "supersupercar":
#         cars[i] = superSuperCar(fuel, fuel_consumption)
#     else:
#         cars[i] = superSuperSuperCar(fuel, fuel_consumption)

# for _ in range(k):
#     values = input().split()

#     index = int(values[0]) - 1
#     func = values[1]

#     if func == "run":
#         cars[index].run()
#     elif func == "fly":
#         cars[index].fly()
#     else:
#         cars[index].teleport()

# for car in cars:
#     print(car.get_mileage())