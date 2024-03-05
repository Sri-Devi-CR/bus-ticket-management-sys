'''Project - Interactive Page (Tumblr + Planner)'''
'''import mysql.connector as sql
import csv, tkinter

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor()
mycursor.execute('Create table Users(id int AUTO_INCREMENT PRIMARY KEY, First_Name varchar(30), Last_Name varchar(30), \
              Gmail varchar(30), New_Password varchar(40), DOB date NULL, Gender varchar(7))')

user_list = []
Header = ['First_Name', 'Last_Name', 'Gmail', 'New Password', 'DOB', 'Gender']

#Function 1 for user account intialization
def Users():
    insert = 'Insert into Users(First_Name, Last_Name, Gmail,New_Password, DOB, Gender) values(%s,%s,%s,%s,%s,%s)'
    
    """Loop to number of accounts for a user"""
    n = int(input("How many accounts do you wanna create?"))
    for i in range(n):
        print("First_Name , Last_Name , Gmail Address , New Password , Date Of Birth , Gender")
        record_list = eval(input("Enter your records correspondingly in []:"))
        tup = tuple(record_list)
        user_list.append(tup)
    mycursor.executemany(insert, user_list)#Insert the account details into the table
    """Extra copy of accounts in a csv file"""
    with open('Users.csv','a+') as users:
        csvwriter = csv.writer(users)
        #csvwriter.writerow(Header)
        csvwriter.writerows(user_list)

Users()#Function Call
mydb.commit()
print(mycursor.rowcount,"record(s) inserted")
'''

## Button on Image ##
## Can be used as Like button ##
## Complex AF ##
'''
import tkinter as tk
from PIL import ImageTk, Image

class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        self.number = tk.IntVar()
        self.button = tk.Button(canvas, textvariable=self.number, command=self.buttonclicked)
        self.id = canvas.create_window(50, 100, width=25, height=25, window=self.button)

    def buttonclicked(self):
        self.number.set(self.number.get()+1)  # auto updates Button

root = tk.Tk()
#root.resizable(width=True, height=True)
#root.wm_attributes("-topmost", 1)

imgpath = "C:\\Users\\Jeyakumar\\Desktop\\My File!!\\@Class 12\\Online Class\\Comp Class\\Project 2020-21\\Images_Pro\\3.JPG"
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root)#, bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=photo)

CanvasButton(canvas)  # create a clickable button on the canvas

root.geometry('626x419')
root.mainloop()
'''
'''
## Button under the image ##
import tkinter
from PIL import Image
from PIL import ImageTk

window = tkinter.Tk()
file = Image.open('C:\\Users\\Jeyakumar\\Desktop\\My File!!\\@Class 12\\Online Class\\Comp Class\\Project 2020-21\\Images_Pro\\3.JPG')
img = ImageTk.PhotoImage(file)
background = tkinter.Label(window, image=img)
background.image = img
background.pack()
window.minsize(height=window.winfo_height(), width=window.winfo_width())
number = 0

def buttonclicked():
    global number
    number = number+1
    button.configure(text=number)

button = tkinter.Button(window, text=0, command=buttonclicked)
button.pack()
window.mainloop()
'''

## Widget - Canvas ##
'''
from tkinter import *
master = Tk()

canvas_width = 80
canvas_height = 40
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


mainloop()
'''
'''
from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)

mainloop()
'''
from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title("Painting")
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>", paint)

message = Label(master, text = "Signature \n < No editing option is made accessible >")
message.pack( side = BOTTOM )
    
mainloop()




















