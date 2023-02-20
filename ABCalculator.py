# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()
    
def do_processing():
    # Считование данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get()) 
    
    popup_window(n1, c1, n2, c2)  

# Функция вызова окна результата
def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B результат")
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", bg='#990000', fg='white', font = ('Helvetica', 10, 'bold'), command=window.destroy)
    btnClosePopup.place(x=160, y=250, width=90, height=30)
    
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


