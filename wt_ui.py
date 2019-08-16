# window title Daily hours
# start button
# click start button -> print datetime.datetime.now and save to variable
# stop button
# click stop button -> print datetime.datetime.now and save to variable
# print timedate.timedelta(difference start stop)  round to quarter of an hour
#  ? rounding: if minutes < 7.5 -> 0 minutes, elif minutes >= 7.5 -> 0.5 hours ?
import tkinter
# from tkinter import *
from tkinter import ttk

startBtn = False

def start_time():
    global startBtn
    startBtn = True


root = tkinter.Tk()
root.title("Arbeitszeiten")

mainframe = ttk.Frame(root, padding="5 5 10 10")
mainframe.grid(column=0, row = 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight = 1)
tkinter.Button(mainframe, text="Start")
mainframe.mainloop()