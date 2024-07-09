first = int(input('Введите число: '))
second = int(input('Введите число 2: '))
third = int(input('Введите число 3: '))
if first != third and third != second and second != first:
    print(0)
elif first!= second or first == third:
    print(2)
elif first == second and second == third:
    print(3)