import os
import shutil

F1 = "F1.txt"
F2 = "F2.txt"
F1_ORIG = "F1_ORIG.txt"
F2_ORIG = "F2_ORIG.txt"

#Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).
def task1():
    with open(F2, 'r', encoding='utf-8') as f2_before:
        content = f2_before.read()
        print("Файл F2 после изменения:\n", content)
    with open (F1,'r', encoding='utf-8') as f1, open (F2,'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        for i in range(len(lines)):
            if (i+1) % 2 == 0:
                f2.write(lines[i])
    with open(F2, 'r', encoding='utf-8') as f2_after:
        content = f2_after.read()
        print("Файл F2 до изменения:\n", content)

    size_f1 = os.path.getsize(F1)
    size_f2 = os.path.getsize(F2)
    print(f'Размер файла F1: {size_f1} байт')
    print(f'Размер файла F2: {size_f2} байт\n')

    #restoring
    shutil.copy(F1_ORIG, F1)
    shutil.copy(F2_ORIG, F2)


#Скопировать в файл F2 только те строки из F1, которые начинаются с буквы «Я». Подсчитать количество слов в F2.
#В целях соответствия моим файлам в условии задачи букву "А" я заменил на букву "Я"
def task2():
    with open(F2, 'r', encoding='utf-8') as f2_before:
        content = f2_before.read()
        print("Файл F2 до изменения:\n", content)

    with open(F1, 'r', encoding='utf-8') as f1, open(F2, 'w', encoding='utf-8') as f2:
        for line in f1:
            if line.startswith('Я'):
                f2.write(line)
    with open (F2, 'r', encoding='utf-8') as f2_after:
        content = f2_after.read()
        print("Файл F2 после изменения:\n", content)

if __name__ == '__main__':
    task1()
    task2()