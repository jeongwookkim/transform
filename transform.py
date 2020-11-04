import tkinter as tk

calc = tk.Tk ()
calc.title("이중전사 변환기")
calc.geometry("450x780")

def transform(event) :
    print(tk.Entry.get(display))

display = tk.Entry(calc, width=30) 
display.pack()

button_1 = tk.Button(calc, text='장', width=5)
button_1.bind('<Button-1>',transform)
button_1.pack()

button_2 = tk.Button(calc, text='페이지', width=5)
button_2.bind('<Button-1>',transform)
button_2.pack()

button_3 = tk.Button(calc, text='번', width=5)
button_3.bind('<Button-1>',transform)
button_3.pack()

button_4 = tk.Button(calc, text='시', width=5)
button_4.bind('<Button-1>',transform)
button_4.pack()

button_5 = tk.Button(calc, text='분', width=5)
button_5.bind('<Button-1>',transform)
button_5.pack()

button_6 = tk.Button(calc, text='개', width=5)
button_6.bind('<Button-1>',transform)
button_6.pack()

button_7 = tk.Button(calc, text='장', width=5)
button_7.bind('<Button-1>',transform)
button_7.pack()

button_8 = tk.Button(calc, text='쪽', width=5)
button_8.bind('<Button-1>',transform)
button_8.pack()

button_9 = tk.Button(calc, text='점', width=5)
button_9.bind('<Button-1>',transform)
button_9.pack()

calc.bind('<Return>', transform)

calc.mainloop ()