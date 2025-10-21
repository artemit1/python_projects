# Завдання 1
print("Завдання 1")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

choice1 = input("Введіть 'суму' для обчислення суми або 'добуток' для обчислення добутку: ").strip().lower()

if choice1 == "суму":
    result = a + b + c
    print("Сума трьох чисел:", result)
elif choice1 == "добуток":
    result = a * b * c
    print("Добуток трьох чисел:", result)
else:
    print("Некоректний вибір!")

# Завдання 2
print("\nЗавдання 2")
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
z = float(input("Введіть третє число: "))

choice2 = input("Введіть 'максимум', 'мінімум' або 'середнє': ").strip().lower()

if choice2 == "максимум":
    result = max(x, y, z)
    print("Максимум трьох чисел:", result)
elif choice2 == "мінімум":
    result = min(x, y, z)
    print("Мінімум трьох чисел:", result)
elif choice2 == "середнє":
    result = (x + y + z) / 3
    print("Середнє арифметичне трьох чисел:", result)
else:
    print("Некоректний вибір!")
