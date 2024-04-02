import tkinter as tk
from tkinter import messagebox, filedialog

# GUI 창을 생성하고 초기 설정을 합니다.
window = tk.Tk()
window.title('Simple Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)

# 텍스트 영역을 생성합니다.
text_area = tk.Text(window)
text_area.grid(sticky='nsew', padx=2, pady=2)

# 창 크기가 변경될 때 텍스트 영역도 같이 변경되도록 합니다.
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 함수 정의 부분
def new_file():
    text_area.delete(1.0, tk.END)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, tk.END)
            file.write(text)
            messagebox.showinfo("저장", "파일이 저장되었습니다!")

def show_maker():
    messagebox.showinfo("만든 이", "손창우!")

def exit_program():
    window.destroy()

# 버튼 생성 및 배치
new_file_button = tk.Button(window, text='새 파일', command=new_file)
new_file_button.grid(row=1, column=0, sticky='ew', padx=2, pady=2)

save_file_button = tk.Button(window, text='저장', command=save_file)
save_file_button.grid(row=1, column=1, sticky='ew', padx=2, pady=2)

maker_button = tk.Button(window, text='만든 이', command=show_maker)
maker_button.grid(row=1, column=2, sticky='ew', padx=2, pady=2)

exit_button = tk.Button(window, text='종료', command=exit_program)
exit_button.grid(row=1, column=3, sticky='ew', padx=2, pady=2)

# 메인 루프를 시작합니다.
window.mainloop()




# # 숙제 : 새파일 누르면 싹다 지워지고. 저장 버튼누르면 윈도우에 저장할수 있게 하는 기능. 마지막으로 정보템에서 만등니 누르면.
# # 본인이름. 뜬느창 나오게 해주면된다.

# import tkinter as tkt
# from tkinter.filedialog import *
# from tkinter import filedialog
# from tkinter import messagebox


# window = tkt.Tk()
# window.title('Notepad')
# window.geometry('400x400+800+300')
# window.resizable(0,0)

# # window.iconbitmap(r"C:\Users\손창우\Documents\카카오톡 받은 파일\memo.ico")
# photo = tkt.PhotoImage(file=r"C:\Users\손창우\Documents\카카오톡 받은 파일\KakaoTalk_20240326_192953043.png")
# window.iconphoto(False, photo)

# #텍스트 창 만들기 
# text_area = tkt.Text(window)
# #공백 설정하기 
# window.grid_rowconfigure(0, weight =1)
# window.grid_columnconfigure(0, weight = 1)
# #텍스트 화면을 윈도우에 동서남북으로 붙인다
# text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)


# def new_file():
#     text_area.delete(1.0, tkt.END)

# def save_file():
#     # 저장 기능을 구현합니다. 사용자가 파일 이름을 입력하고 저장을 선택할 수 있습니다.
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt",
#                                              filetypes=[("Text documents", "*.txt"), ("All files", "*.*")])
#     if not file_path:  # 사용자가 취소를 누르면 아무 것도 하지 않습니다.
#         return
#     with open(file_path, 'w') as file:
#         text = text_area.get(1.0, tkt.END)
#         file.write(text)
#     messagebox.showinfo("저장 완료", "파일이 저장되었습니다!")

# def maker():
#     messagebox.showinfo("만든 이", "**손창우**")


# #메뉴 생성
# menuMaker = tkt.Menu(window)
# #첫번째 메뉴 만들기 
# first_menu = tkt.Menu(menuMaker, tearoff=0)
# #첫번째 메뉴의 세부메뉴 추가 및 함수 연결
# first_menu.add_command(label = '새 파일', command = new_file)
# first_menu.add_command(label = '저장', command = save_file)
# #메뉴 바 추가 
# menuMaker.add_cascade(label='파일', menu=first_menu)

# #메뉴 구성
# window.config(menu = menuMaker)

# first_menu.add_separator()
# #종료 옵션 추가하기
# first_menu.add_command(label='종료', command=window.destroy)

# #두번째 메뉴 추가 
# second_menu = tkt.Menu(menuMaker, tearoff=0)
# #세부 메뉴 추가, 함수 연결
# second_menu.add_command(label = '만든 이', command = maker)
# #메뉴 바 추가
# menuMaker.add_cascade(label='정보', menu = second_menu)


# window.mainloop() # 창 실행!









# import tkinter as tkt
# from tkinter.filedialog import *

# root = tkt.Tk()
# root.title("이름")

# lbl = tkt.Label(root, text = "이름")
# lbl.pack()

# txt = tkt.Entry(root)
# txt.pack()

# btn = tkt.Button(root,text="OK")
# btn.pack()

# root.mainloop()


