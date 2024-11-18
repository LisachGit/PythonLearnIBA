# def countAge(dogAge):
#     if dogAge == 1:
#         humanAge = 14
#     elif dogAge == 2:
#         humanAge = 22
#     elif dogAge > 2:
#         humanAge = 22 + (dogAge - 2) * 5
#     else:
#         humanAge = 0
#     return humanAge
#
#
# try:
#     age = int(input("Введите возраст пёсика\n"))
#     if age < 1:
#         print("Возраст не может быть меньше 1 года!")
#     else:
#         print("Возраст пёсика в человеческих годах:", countAge(age))
# except ValueError:
#     print("Вы ввели не возраст...")
from functools import reduce


# items = [1, 2, 3, 4, 5]
    # squared = []
    # for i in items:
    #     squared.append(i ** 2)
    # return squared
def task1():
    items = [1,2,3,4,5]
    squared = list(map(lambda x: x ** 2, items))
    return squared

print(task1())

# Используйте функцию reduce() и перепишите код
#
# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num

def task2():
    list = [1,2,3,4]
    product = reduce(lambda x, y: x * y, list)
    return product

print(task2())

# Используйте функцию map() и перепишите код
#
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)


def task3():
    numbers = [1,2,3,4,5]
    squared = list(map(lambda x: x ** 2, numbers))
    return squared

print(task3())

# Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()

def task4():
    x, y = [1,2,3] , [4,5,6]
    res = list(zip(x, y))
    return res

print(task4())

# Используйте функцию zip() чтобы преобразовать код:
#
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
# for i in range(len(name_hero)):numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#     print(name_hero[i], '-', name_real[i])


def task5():
    name_hero = [
        'Hulk',
        'Mr. Fantastic',
        'Invisible Woman',
        'Doctor Strange',
        'Doctor Octopus',
        'Spider-Man',
    ]

    name_real = [
        'Bruce Banner',
        'Reed Richards',
        'Sue Storm',
        'Stephen Strange',
        'Otto Octavius',
        'Peter Parker',
    ]
    namesList = list(zip(name_hero, name_real))
    return namesList

print(task5())

# С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.

def task6():
    numbers = [1, 2, 4, 5, 7, 8, 10, 11]
    oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))
    return oddNumbers

print(task6())