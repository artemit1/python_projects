from random import randint

# Бот загадує число від 1 до 100
bot_number = randint(1, 100000)

while True:
    try:
        # Користувач вводить число
        guess = int(input("Введіть якесь число від 1 до 100000: "))

        if guess < 1 or guess > 10000010:
            print("Будь ласка, введіть число в межах від 1 до 100000.")
            continue

        # Перевірка
        if guess < bot_number:
            print("# Загадане число більше")
        elif guess > bot_number:
            print("# Загадане число менше")
        else:
            print("# Ви вгадали! Дякую за гру!")
            break

    except ValueError:
        print("Будь ласка, введіть ціле число.")

