def ввод():
    кнопка_начать.pack_forget()
    группа_ввода.pack()
    кнопка_готово.pack()

def проверка():
    try:
        float(ввод_литров.get())
        float(ввод_жирности.get())
        вывод()
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Число?')
        return False

def вывод():
    кг = float(ввод_литров.get())*float(ввод_жирности.get())
    вывод = str(кг) + " кг."
    вывод_кг = Label(окно, bg="black", fg="white", text=вывод)
    вывод_кг.pack()
    fail = open('История конвертера литров в килограммы.txt', 'a')
    fail.write("\n" + now.strftime("%d-%m-%Y %H:%M") + " : " + вывод)
    fail.close()

from tkinter import *
from tkinter import messagebox
from datetime import *
now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M")

окно = Tk()
окно["bg"] = "black"
окно.title("Конвертер литров в килограммы.")
тд = Label(окно, bg="black", fg="white", text="Текущая дата и время:")
тд.pack()
дмгчм = Label(окно, bg="black", fg="white", text=now.strftime("%d-%m-%Y %H:%M"))
дмгчм.pack()
кнопка_начать = Button(окно, text="Начать", bg="black", fg="white", command=ввод)
кнопка_начать.pack(expand=True, fill=BOTH)

группа_ввода = Frame(relief=SUNKEN, bg="black")
группа_ввода.pack_forget()

требование_ввода_литров = Label(master=группа_ввода, bg="black", fg="white", text="Литры:")
требование_ввода_литров.grid(row=0, column=0, sticky="e")
ввод_литров = Entry(master=группа_ввода)
ввод_литров.grid(row=0, column=1, columnspan=3)
требование_ввода_жирности = Label(master=группа_ввода, bg="black", fg="white", text="Жирность (%):")
требование_ввода_жирности.grid(row=1, column=0, sticky="e")
ввод_жирности = Entry(master=группа_ввода)
ввод_жирности.grid(row=1, column=1, columnspan=3)



кнопка_готово = Button(окно, text="Готово", bg="black", fg="white", command=проверка)
кнопка_готово.pack_forget()

окно.mainloop()