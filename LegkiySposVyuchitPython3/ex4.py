cars = 100
space_in_cars = 4.0
drivers = 30
passenqers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_passenqers_per_car = passenqers / cars_driven

print('В наличаи, cars, "автомобилей." ')
print('И только', drivers, "Водителей вышло на работу.")
print('Получается, что', cars_not_driven, "машин пустуют.")
print('Мы можем перевести сегодня', carpool_capacity, "человек.")
print("Сегодня нужно отвезти", passenqers, "человек.")
print("В каждой машине будет примерно", average_passenqers_per_car, "человека.")
