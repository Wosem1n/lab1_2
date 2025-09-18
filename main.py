n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
    num = int(input(f"Введите {i+1} число: "))
    numbers.append(num)

print("Изначальный массив: ", numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Отсортированный массив: ", numbers)

