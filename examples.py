# Линейный алгоритм
name = int(input('Введите ваше имя: '))
print("Здраствуйте," + name)

# Разветленный полный агоритм
number = int(input())
if number < 0:
    print('Число отрицательное')
else:
    print('Число положительное или равно 0')

# Развлетленный неполный алгоритм
age = int(input())
if age == 23:
    print('Мы ровесники!')

# Разветленный множественный алгоритм
age = int(input())
if age == 23:
    print('Мы ровесники!')
elif age > 23:
    print('Ты меня старше')
else:
    print('Ты младше меня')

# Преобразование в bool
coins = 5
if coins:
    print('У вас' + coins + 'монет')
    