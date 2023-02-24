# A/B калькулятор

import tkinter as tk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm

# Функция закрытия программы
def do_close():
    root.destroy()

# Функция форматирование процентов
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'
    
def do_processing():
    # Считование данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get()) 
    
    # Проверка данных из полей ввода
    if n1<=0 or n2<=0:
        mb.showerror(title="Ошибка", message="Неверное количество посетителей")
        return
    
    # Открытие окна результата
    popup_window(n1, c1, n2, c2)  

# Функция вызова окна результата
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B результат")
    
    # Добавления окна вывода текста
    txtOutput = tk.Text(window, font = ('Courir New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300) 
    
    # Добавление заголовка 
    txtOutput.insert(tk.END, '                                                    Контрольная     Тестовая' + os.linesep)
    txtOutput.insert(tk.END, '                                                    группа                группа' + os.linesep)
    txtOutput.insert(tk.END, '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _' + os.linesep)
    
    # Добавление вывода конверсии и стандартного отклонения
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Конверсия                            ' + num_percent(p1)
        + '            ' + num_percent(p2) + os.linesep)
         
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение    ' + num_percent(sigma1)
        + '             ' + num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END, '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _' + os.linesep)    
    
    # Добавление вывода возможных разбросов
    z1 = 1.96
    lower1_95 = p1-z1*sigma1
    if lower1_95 < 0:
        lower1_95 = 0
    upper1_95 = p1+z1*sigma1
    if upper1_95 > 1:
        upper1_95 = 0
        
    lower2_95 = p2-z1*sigma2
    if lower2_95 < 0:
        lower2_95 = 0
    upper2_95 = p2+z1*sigma2
    if upper2_95 > 1:
        upper2_95 = 1
    
    txtOutput.insert(tk.END, '95% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                   От                       ' + num_percent(lower1_95)
        + '            ' + num_percent(lower2_95) + os.linesep)
    txtOutput.insert(tk.END, '                   До                       ' + num_percent(upper1_95)
        + '            ' + num_percent(upper2_95) + os.linesep)
    txtOutput.insert(tk.END, '                                  ' + os.linesep)      
    
    z2 = 2.575
    lower1_99 = p1-z2*sigma1
    if lower1_99 < 0:
        lower1_99 = 0
    upper1_99 = p1+z2*sigma1
    if upper1_99 > 1:
        upper1_99 = 0
        
    lower2_99 = p2-z2*sigma2
    if lower2_99 < 0:
        lower2_99 = 0
    upper2_99 = p2+z2*sigma2
    if upper2_99 > 1:
        upper2_99 = 1
    
    txtOutput.insert(tk.END, '99% Возможный разброс  ' + os.linesep)
    txtOutput.insert(tk.END, '                   От                       ' + num_percent(lower1_99)
        + '            ' + num_percent(lower2_99) + os.linesep)
    txtOutput.insert(tk.END, '                   До                       ' + num_percent(upper1_99)
        + '            ' + num_percent(upper2_99) + os.linesep)
    txtOutput.insert(tk.END, '                                  ' + os.linesep)                    
    
    # Вычисление Z и P
    z_score = (p2-p1)/math.sqrt(sigma1*sigma1+sigma2*sigma2)
    txtOutput.insert(tk.END, 'Z = ' + "{:.7f}".format(z_score) + os.linesep)
    
    p_value = norm.sf(x=z_score, loc=0, scale=1)
    txtOutput.insert(tk.END, 'P = ' + "{:.7f}".format(p_value) + os.linesep)
     
    # Добавление оценки результатов 
    confidence_95 = False
    if p_value < 0.025 or p_value > 0.975:
        confidence_95 = True
        
    confidence_99 = False
    if p_value < 0.005 or p_value > 0.995:
        confidence_99 = True     
            
    lblComment95 = tk.Label(window, text = "95% уверенность:", font = ('Helvetica', 10, 'bold'))
    lblComment95.place(x=25, y=25)
    
    if confidence_95:
        lblResult95 = tk.Label(window, text = "ДА", font = ('Helvetica', 12, 'bold'), fg = '#008800')
        lblResult95.place(x=160, y=25)
    else:
        lblResult95 = tk.Label(window, text = "НЕТ", font = ('Helvetica', 12, 'bold'), fg = '#ff0000')
        lblResult95.place(x=160, y=25)      
    
    lblComment99 = tk.Label(window, text = "99% уверенность:", font = ('Helvetica', 10, 'bold'))
    lblComment99.place(x=25, y=65)
    
    if confidence_99:
        lblResult99 = tk.Label(window, text = "ДА", font = ('Helvetica', 12, 'bold'), fg = '#008800')
        lblResult99.place(x=160, y=65)
    else:
        lblResult99 = tk.Label(window, text = "НЕТ", font = ('Helvetica', 12, 'bold'), fg = '#ff0000')
        lblResult99.place(x=160, y=65) 
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", bg='#990000', fg='white', font = ('Helvetica', 10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    # Перевод фокуса на созданное окно
    window.focus_force()
    
# Создание шлавного окна
root = tk.Tk()
root.geometry("400x400")
root.title("A/B калькулятор")

# Добавление метки заголовка 
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление метки заголовка контрольной группы
lblTitle = tk.Label(text = "Контрольная группа", font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle.place(x=40, y=81)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetica', 10, 'bold'))
lblVisitors1.place(x=40, y=120)

entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entVisitors1.place(x=125, y=120, width=90, height=20)
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversions1.place(x=40, y=147)

entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConversions1.place(x=125, y=147, width=90, height=20)
entConversions1.insert(tk.END, '0')

# Добавление метки заголовка тестовой группы
lblTitle = tk.Label(text = "Тестовая группа", font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle.place(x=40, y=186)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text = "Посетители:", font = ('Helvetica', 10, 'bold'))
lblVisitors2.place(x=40, y=225)

entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entVisitors2.place(x=125, y=225, width=90, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversions2.place(x=40, y=252)

entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')
entConversions2.place(x=125, y=252, width=90, height=20)
entConversions2.insert(tk.END, '0')

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text="Расчитать", bg='#003300', fg='white', font = ('Helvetica', 10, 'bold'), command=do_processing)
btnProcess.place_configure(x=50, y=320, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", bg='#990000', fg='white', font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=260, y=320, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()


