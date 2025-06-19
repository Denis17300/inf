# Завдання 1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, linestyle="-", color="green")
plt.plot(x, y, marker='o', linestyle='', color='red')

plt.title("Лінійний графік")
plt.xlabel("Вісь X")
plt.ylabel("Вісь Y")
plt.grid(True)
plt.show()



# Завдання 2
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [15, 25, 10, 30]

plt.bar(categories, values, color=['red', 'green', 'blue', 'yellow'])
plt.title("Стовпчикова діаграма")
plt.xlabel("Категорії")
plt.ylabel("Значення")
plt.show()


# Завдання 3
import matplotlib.pyplot as plt

labels = ['Кава', 'Чай', 'Сік', 'Вода', 'Лимонад']
sizes = [25, 15, 15, 35, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Кругова діаграма")
plt.axis('equal')
plt.show()


# Завдання 4
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, color='red', marker='o', s=100)
plt.title("Діаграма розсіювання")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


# Завдання 5
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000) * 100  # випадкові дані

plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("Гістограма")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.show()


# Індивідуальне завдання
import matplotlib.pyplot as plt

months = ['Січ', 'Лют', 'Бер', 'Квіт', 'Трав']
users = [100, 150, 200, 300, 500]

plt.plot(months, users, color='blue', marker='o', linestyle='-')
plt.title("Зростання кількості користувачів за місяцями")
plt.xlabel("Місяць")
plt.ylabel("Кількість користувачів")
plt.grid(True)
plt.show()
