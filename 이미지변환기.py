import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import *
import  os
from os import rename, listdir
import ctypes
import win32api
from tkinter import messagebox
root=tk.Tk()    

file_list_py = list() #파일이 담겨있는 리스트
path1="" #파일경로 선언
def path(): #경로 입력 받는 함수
    global path1
    path1 = filedialog.askdirectory()
    text_widget.insert(tk.END,  path1)
def chage():#변경버튼
    global file_list_py
    if len(path1) ==0 or    selected_item[0].get()=="변경할 타입" or  selected_item[1].get()=="변경될 타입":
       win32api.MessageBox(0, "경로와 파일 형식을 완성하세요.", "오류", 16)        
    elif len(file_list_py) >0: 
        for name in file_list_py:
           replaced = name.replace(selected_item[0].get(),selected_item[1].get())
           rename(path1+'\\'+name, path1+'\\'+replaced)
        messagebox.showinfo("성공","변환 성공" )

        text_widget1.delete(1.0, tk.END)
        file_list = os.listdir(path1)
        file_list_py = [file for file in file_list if file.endswith(selected_item[1].get())] ## 
        for file in file_list_py:
            text_widget1.insert(tk.END,  file+ '\n')
             
    #진행과정을 출력합니다.
    
def on_select(*args):
    global file_list_py
    text_widget1.delete(1.0, tk.END)
    file_list = os.listdir(path1)
    file_list_py = [file for file in file_list if file.endswith(selected_item[0].get())] ## 
    for file in file_list_py:
        text_widget1.insert(tk.END,  file+ '\n')
        
def on_select2(*args):
    text_widget1.insert(tk.END,  selected_item[1].get()+ '\n')

root.title('이미지 형식 변환 프로그램')


#창 크기 +붙은 부분은 좌상단 떨어진 위치
root.geometry("400x300")
button = tk.Button(root, text='경로', command=path)
button.place(x=0, y=30)

button = tk.Button(root, text='변경하기', command=chage)
button.place(x=0, y=80)


text_widget = tk.Text(root, width=30, height=1)
text_widget.pack()


global selected_items 
selected_item = [tk.StringVar() for _ in range(2)]
values = ["jpg","png","webp"] # 1 ~ 31 까지의 
combobox = ttk.Combobox(root, height=0,width=10, values=values,textvariable=selected_item[0])
combobox.pack()
combobox.set("변경할 타입") 
combobox.place(x=0, y=240)
combobox.bind("<<ComboboxSelected>>", on_select)


combobox2 = ttk.Combobox(root, height=0,width=10, values=values,textvariable=selected_item[1])
combobox2.pack()
combobox2.set("변경될 타입") 
combobox2.place(x=300, y=240)
combobox2.bind("<<ComboboxSelected>>", on_select2)

text_widget1 = tk.Text(root, width=30, height=10)
text_widget1.pack()
root.mainloop()
