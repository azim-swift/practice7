# Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
# Допускается использовать любую графическую библиотеку питона.Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import itertools as it
import copy as c

def delete_clean(): # Функция для очистки текста
    vivod.delete('1.0','end')
def combi():
    n = int(vvod.get()) # Размер квадратной матрицы
    matrix_ORIGINAL = [[(j + 1) * (i + 1) for j in range(0, n)] for i in range(n)]  # СОЗДАЕМ МАТРИЦУ
    matrix = c.deepcopy(matrix_ORIGINAL)  # КОПИРУЕМ МАТРИЦУ ДЛЯ РАБОТЫ С НЕЙ
    minus = n - 1  # определяет индекс для элемента побочной диагонали
    main_line = [matrix_ORIGINAL[i][i] for i in range(n)]  # СОЗДАЕМ СПИСОК ИЗ ГЛАВНОЙ ДИАГОНАЛИ
    second_line = []
    for i in range(0, n):
        second_line.append(matrix_ORIGINAL[i][minus])
        minus -= 1

    minus = n - 1  # снова присваиваем значение
    flag = 0  # отвечает за ведущую строку в комбинации
    save = 0  # спомогательная переменная
    vivod.insert(END,"исходная матрица \n\n\n")
    vivod.insert(END,'\n'.join('\t'.join(map(str, row)) for row in matrix))
    n_on_n = n * n
    while flag < n:  # ИДЕМ ДО ТЕХ ПОР ПОКА НЕ ПРОЙДЕМ ПО ВСЕМ ПАРАМ
        vivod.insert(END,f'\n\nвведущая пара  {matrix[flag][flag]}, {matrix[flag][minus - flag]}\n\n')
        if matrix[flag][flag] + matrix[flag][minus - flag] < n_on_n:

            for i in range(0, n):

                if i == flag:  # ЕСЛИ ПАРА ВЕДУЩАЯ НЕ ТРОГАЕМ ЕЕ

                    minus -= 1

                    vivod.insert(END,'\n'.join('\t'.join(map(str, row)) for row in matrix))
                    vivod.insert(END,'\n\n')
                    continue

                else:

                    save = matrix[i][i]

                    matrix[i][i] = matrix[i][minus]

                    matrix[i][minus] = save

                    minus -= 1  # ИНДЕКС ДЛЯ ПОБОЧНОЙ ДИАГОНАЛИ
                    vivod.insert(END,'\n'.join('\t'.join(map(str, row)) for row in matrix))
                    vivod.insert(END ,'\n\n')

            else:

                None

        matrix = c.deepcopy(matrix_ORIGINAL)  # КОГДА ЗАКОНЧИМ С ПАРОЙ ПРИВОДИМ К ИСХОДНОЙ РАБОЧУЮ МАТРИЦУ
        minus = n - 1  # ПРИВОДИМ К ИСХОДНОМУ ЗНАЧЕНИЕЮ ИНДЕКС ПОБОЧНОЙ ДИАГОНЛИ
        flag += 1  # ПЕРЕМЕННАЯ ДЛЯ УКАЗАНИЯ ВЕДУЩЕЙ ПАРЫ

    """-------------------------------------"""
    """    С ПОМОЩЬЮ БИБЛИОТЕКИ ITERTOOLS   """
    """-------------------------------------"""

    flag = 0
    res = 0
    vivod.insert(END,"работа через itertools")

    while flag <= n:
        for i in range(0, n):
            if i == flag:
                vivod.insert(END, f'\n{main_line[i]},{second_line[i]}\n ведущая пара')

                res = main_line[i]
                sec = second_line[i]
                continue
            else:
                if res + sec >= n_on_n:
                    continue
                result = list(it.permutations((main_line[i], second_line[i]), 2))
                if result[0][0] != res:
                    vivod.insert(END, f'пара в исходной матрице до  {result[0]} пара после {result[1]}\n')

        flag += 1


root = tk.Tk() # Cоздание окна
root.title("Бригады") # Название программы
root.geometry('720x480+100+200') # Разрешение
root.resizable(False, False) #  Константы для изменения разрешения окна

label_1 = tk.Label(root, text='Введите число для квадратной матрицы',font=('Times New Roman',15,'bold')).grid(row=0,column=0,pady = 5, padx = 10) # Текст

label_1 = tk.Label(root, text='МЫ ОТБРАСЫВАЕМ КОМБИНАЦИЮ  У КОТОРОЙ ВЕДУЩАЯ ПАРА В СУММЕ БОЛЬШЕ n^2',font=('Times New Roman',10,'bold')).place(x=10,y=70) # Текст

vvod = (tk.Entry(root)) # Поле ввода
vvod.grid(row=0,column= 1)

btn1 = tk.Button(root,text='Вычислить',command= combi).grid(row=1,column= 1,pady = 5) # Кнопка вычисления

vivod = tk.Text(root,width=68,height=23) # Окно вывода
vivod.place(x=150, y=100)

scroll = Scrollbar(root,orient=VERTICAL) # Скроллбар
scroll.place(x=685,y=100,height=370)
vivod.config(yscrollcommand=scroll.set)
scroll.config(command=vivod.yview)

clean = tk.Button(root,text = "Очистить",command=delete_clean,pady = 5) # Кнопка очистки
clean.place(x=70,y=100)

root.mainloop() # Запуск цикла
