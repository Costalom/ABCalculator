# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

# Создание шлавного окна
root = tk.Tk()
root.geometry("400x400")
root.title("A/B калькулятор")

# Добавление метки заголовка 
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root, text="Расчитать", bg='#003300', fg='white', font = ('Helvetica', 10, 'bold'))
btnProcess.place_configure(x=50, y=320, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", bg='#990000', fg='white', font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=260, y=320, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()


