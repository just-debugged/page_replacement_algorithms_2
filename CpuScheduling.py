from tkinter import *

# Menu = Tk()
# Menu.title("Team No:21 OS PROJECT")
# Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
# Menu.geometry("800x700+0+0")
# Menu.resizable(False, False)
# Menu.mainloop()

# all list of same size where same index represents qualities of one process
AT = [3, 3, 3]  # arrival time list
BT = [4, 3, 2]  # Burst time or the time required for cpu execution
CT = []  # Completion time or the time at which process is finished execution
TAT = []  # CT - AT
WT = []  # TAT - BT

timeCpu = 0

for i in range(0, len(AT)):
    print(timeCpu)
    # to make up for idle CPU time
    while AT[i] > timeCpu:
        print("timeCpu:", timeCpu)
        print("AT", AT[i])
        timeCpu += 1
    # Calculating CT by adding Current CPU time and BT
    timeCpu += BT[i]
    CT.append(timeCpu)

    TAT.append(CT[i] - AT[i])
    WT.append(TAT[i] - BT[i])

print(CT, TAT, WT)
