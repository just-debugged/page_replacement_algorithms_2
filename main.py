from tkinter import *
import subprocess
import os


def one():
    # tried doing it in their method but found os method more modular.
    # file1 = " C:\Users\Mihir Shah\PycharmProjects\pageReplacementOS\DiskScheduling.py"
    os.system('python DiskScheduling.py')
    # p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = p.communicate()


def two():
    # file2 = "python3 /Users/kevin/Desktop/OS/PageReplacement.py"
    os.system('python PageReplacement.py')
    # p = subprocess.Popen(file2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = p.communicate()


def three():
    # put your scheduling file in same folder and rename 'file3' below
    file3 = 'your scheduling file.py'
    os.system(file3)


def four():
    # put your concurrency file in same folder and rename 'file4' below
    file4 = 'your concurrency file.py'
    os.system(file4)


Menu = Tk()

Menu.title("Team No:21 OS PROJECT")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("800x700+0+0")
Menu.resizable(False, False)

L1 = Label(width="900", height="2", text="OS Lab Project", font=("Century Gothic", 30), bg="black", fg="white")
L1.pack()
f1 = Frame(bg="white").pack()
l1 = Label(text="Choose Algorithm: ", font=("Century Gothic", 15))
l1.pack(pady="40")
Button1 = Button(f1, text="Disk Scheduling Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=one).pack()
Button2 = Button(f1, text="Page Replacement Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=two)\
    .pack(pady="30")
Button3 = Button(f1, text="Scheduling Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca",
                 command=three).pack()
Button4 = Button(f1, text="Concurrency & Deadlock Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=four)\
    .pack(pady="30")

Menu.mainloop()
