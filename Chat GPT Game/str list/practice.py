list_friends = []
list_friends.append("a")
list_friends.append("b")
list_friends.append("c")
list_friends.append("d")
print(list_friends)
print((list_friends[::3]))

print("оцінки учнів")
list_notes = [12,9,10,8,11]
print(list_notes)
bebe = {sum(list_notes)/5}
print(f"Сер бал:{bebe}")
print(f"Макс число: {max(list_notes)}")
print(f"Мін число: {min(list_notes)}\n")

# продукти

list_productes = ["хліб", "молоко", "сир"]
list_productes.append("кефір")
list_productes.append("картопля")
print(list_productes)
list_productes.pop(0)
print(list_productes)
print()
# улюблене чесло
list_future = []
a = int(input("Введи 1 улюблене число: "))
b = int(input("Введи 2 улюблене число: "))
c = int(input("Введи 3 улюблене число: "))
list_future.append(a)
list_future.append(b)
list_future.append(c)
print(f"Ваш список: {list_future}")
print(f"Макс число: {max(list_future)}")
print(f"Сума всіх чисел: {sum(list_future)}")








