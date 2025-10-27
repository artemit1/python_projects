list_1 = [1, 1, 3]
print(list_1)

# перетворення зі списку в множину
set_list = set(list_1)
print(set_list)


# спосіб створення
letters = set(["1", "2", "3", "4"])

# gecnf vyj;byf
empty_set = set()


fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)
# добавити елемент
fruits.add("orange")
print(fruits)

# добавити декілька елементів
fruits.update({"mango", "grape", "qiwi"})
print(fruits)

# видалити елемент
# remove - якщо немає елементу буде помилка
fruits.remove("orange")
print(fruits)

# discard - якщо немає елементу не буде помилки, буде также
fruits.discard("grape")
print(fruits)

# pop - видаляє рандомний момент АЛЕ в множині, а так останній
fruits.pop()
print(fruits)

# clear - повністю очищує
fruits.clear()
print(fruits)


# перевірити наявність елементу
print("apple" in fruits)
print("apple" not in fruits)

a = {1, 2, 3}
b = {4, 5, 6}


# обєднання множин
c = a | b
print(c)

# перетин
print(a & b)

# різниця(Що є в a(на 1 місці) але немає в b(на 2 місці))
print(a - b)

# симетрична різниця
print(a ^ b)

# len - кількість елементів
# max(), min(), sum()
