# 1 завдання
monday = ["Nazar", "Vlad", "Sasha"]
tuesday = ["Sasha", "Pasha", "Nazar"]

print(set(monday) ^ set(tuesday))
print(set(monday) & set(tuesday))
print(set(monday) - set(tuesday))

# 2 завдання
team_a = {"Nazar", "Sasha", "Vlad"}
team_b = {"Sasha", "Pasha", "Vlad"}
print(team_a | team_b)
print(team_a ^ team_b)
print(team_a & team_b)

# 3 завдання
numbers = [5, 2, 3, 2, 1, 5, 4]
a = set(numbers)
b = sorted(a)
print(b)

# 4 завдання
sentence = input("Введіть речення: ")
words = sentence.split()
unique_words = set(words)
print("Кількість унікальних слів:", len(unique_words))

