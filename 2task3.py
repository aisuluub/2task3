number = float(input("Введите число: "))
number = round(number)
if number % 1 == 0:
    print((number - 1), number, (number + 1))
else:
    print("Введите целое число!")

