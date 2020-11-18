from tkinter import *
from functools import partial

# def show_result(lb, result) :
#     output = result.get()
#     print(result.get())
#     lb.config(text="%s" % output)
#     return

def output_result(textArea, result) :
    output = result.get()
    print(result.get())
    textArea.insert(END,result.get() + '\n')
    return
    
# 화면 그리기
root = Tk()
root.title("이중전사 변환기")
root.geometry("450x200+100+200")

# lb = Label(root)
# lb.grid(row=1, column=0)

# 결과값 변수 선언
result = StringVar()

# 텍스트 필드 그리기 및 변수 선언
textField = Entry(root, textvariable=result).grid(row=2,column=0) 

# show_result = partial(show_result, lb, result)

btn = Button(root, text="글자입력", command=output_result).grid(row=3, column=0)

# 엔터 눌렀을 때 이벤트 거는 것
# root.bind('<Return>', lambda event: show_result())
root.bind('<Return>', lambda event: output_result())

textArea = Text(root)
textArea.grid(row=4, column=0)

output_result = partial(output_result, textArea, result)

# 스크롤바 그리기 및 변수 선언
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





root.mainloop ()