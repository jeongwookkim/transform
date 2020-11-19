import tkinter

from tkinter import *
from functools import partial


# def show_result(lb, result) :
#     output = result.get()
#     print(result.get())
#     lb.config(text="%s" % output)
#     return


def output_result(textArea, result):
    output = result.get()
    print(result.get())
    textArea.insert(1.0, result.get() + '\n')
    textField.delete(0, 'end')

    return


# 화면 그리기
root = Tk()
root.title("이중전사 변환기")
root.geometry("390x780+100+100")

# lb = Label(root)
# lb.grid(row=1, column=0)

# 결과값 변수 선언
result = StringVar()

# 텍스트 필드 그리기 및 변수 선언
textField = Entry(root, textvariable=result, width=30) # Entry는 자신이 만든 객체를 리턴함
textField.grid(row=2, column=1, columnspan=3, padx=25, pady=10) # grid는 상태 변화 함수임 쉽게 말해 return Type void와 같음

# show_result = partial(show_result, lb, result)

btn = Button(root, text="Enter(변환)", width=10, command=lambda: output_result()) # 위와 동일
btn.grid(row=2, column=4, pady=10);

# 엔터 눌렀을 때 이벤트 거는 것
# root.bind('<Return>', lambda event: show_result())
root.bind('<Return>', lambda event: output_result())

textArea = Text(root, width=49, height=55)
textArea.grid(row=3, column=1, columnspan=4, padx=15) 

output_result = partial(output_result, textArea, result)

#스크롤바 그리기 및 변수 선언
# S = Scrollbar(root)
# T = Text(root)
# S.config(command=T.yview)
# T.config(yscrollcommand=S.set)


# T.insert(END, quote)


# button_1 = tkinter.Button(root, text='장', width=5)
# quote = button_1.bind('<Button-2>',transform)
# button_1.pack()

# button_2 = tkinter.Button(root, text='페이지', width=5)
# quote = button_2.bind('<Button-1>',transform)
# button_2.pack()

# button_3 = tkinter.Button(root, text='번', width=5)
# quote = button_3.bind('<Button-1>',transform)
# button_3.pack()

# button_4 = tkinter.Button(root, text='시', width=5)
# quote = button_4.bind('<Button-1>',transform)
# button_4.pack()

# button_5 = tkinter.Button(root, text='분', width=5)
# quote = button_5.bind('<Button-1>',transform)
# button_5.pack()

# button_6 = tkinter.Button(root, text='개', width=5)
# quote = button_6.bind('<Button-1>',transform)
# button_6.pack()

# button_7 = tkinter.Button(root, text='장', width=5)
# quote = button_7.bind('<Button-1>',transform)
# button_7.pack()

# button_8 = tkinter.Button(root, text='쪽', width=5)
# quote = button_8.bind('<Button-1>',transform)
# button_8.pack()

# button_9 = tkinter.Button(root, text='점', width=5)
# quote = button_9.bind('<Button-1>',transform)
# button_9.pack()


root.mainloop()