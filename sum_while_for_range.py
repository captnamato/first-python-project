# Ініціалізуємо змінну sum для накопичення суми
sum = 0

# Перший цикл while для введення чисел
while True:
    num = int(input("Введіть ціле число (або 0, щоб завершити): "))
    
    # Вихід з першого циклу, якщо введено 0
    if num == 0:
        break
    
    # Другий цикл for для обчислення суми чисел від 0 до введеного числа включно
    for i in range(num + 1):
        sum += i

# Виводимо суму чисел, яка була накопичена
print("Сума введених чисел:", sum)
