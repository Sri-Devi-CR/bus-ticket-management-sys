'''from tkinter import *
from PIL import ImageTk,Image

LogIn_window = Tk()
LogIn_window.title("Login Page")

path = "C:\\Users\\Jeyakumar\\Desktop\\My File!!\\@Class 12\\Online Class\\Comp Class\\Project 2020-21\\Images_Pro\\3.JPG"
photo = Image.open(path)
Tk_image = ImageTk.PhotoImage(photo)

message = 'Log In to access your account!'
sentence = Label(LogIn_window, text = message, fg = 'white', image = Tk_image, font = ('Candara',15,'italic'), compound = 'center')
#sentence.config(bg = 'plum')
sentence.grid(column = 1, row = 5, sticky = N)

LogIn_window.mainloop()
'''
'''
from tkinter import *
     
canvas = Canvas(width=300, height=300, bg='white')   
canvas.pack(expand=YES, fill=BOTH)                   
     
widget = Label(canvas, text='Spam', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)       
mainloop()
'''
'''
#Enabling and disabling of a button
try:
    import Tkinter as tk
except:
    import tkinter as tk
    
def switchButtonState():
    if (button1['state'] == tk.NORMAL):
        button1['state'] = tk.DISABLED
    else:
        button1['state'] = tk.NORMAL
        
app = tk.Tk()
app.geometry("300x100")
button1 = tk.Button(app, text="Python Button 1",
                    state=tk.DISABLED)
button2 = tk.Button(app, text="EN/DISABLE Button 1",
                    command = switchButtonState)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)
app.mainloop()
'''
'''
from tkinter import *
from PIL import ImageTk,Image 
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)


def s():
    val = []
    val.append(Username.get())
    val.append(Password.get())
    
    print((val[0],))

    print(mycursor.execute(select,(val[0],)))
    mycursor.fetchall()
    
    if(mycursor.execute(select,(val[0],)) != None) and (mycursor.execute(select2,(val[1],)) != None):
        #move into new window
        move = Label(LogIn_window, text = 'Moving to your account')
        LogIn_window_canvas.create_window(350,400, window = move)

    else:
        error = Label(LogIn_window, text = 'Sorry, your acc does not exist, create one')
        LogIn_window_canvas.create_window(350,400, window = error)

select = 'Select ID from users where User_Name = %s'
select2 = 'Select ID from users where Password = %s'

LogIn_window = Tk()
LogIn_window_canvas = Canvas(LogIn_window, width=600, height=600)
LogIn_window_canvas.grid(column=0,row=0)


Username = Entry(LogIn_window)
LogIn_window_canvas.create_window(350, 200, window = Username)

Password = Entry(LogIn_window)
LogIn_window_canvas.create_window(350, 300, window = Password)

sub = Button(LogIn_window,text = 'Submit', command = s)
LogIn_window_canvas.create_window(350,500, window = sub)
'''
'''
from tkinter import *

class Table:
    def __init__(self,root): 
        for i in range(total_columns): 
            for j in range(total_rows):
                self.e = Entry(Booking_canvas, width=20, fg='blue', font=('Arial',16,'bold'))
                self.e.place(x=i*100, y=j*50)
                self.e.insert(END, lst[j][i]) 


lst = [('Adults:','Male:','' ,'Female:',''), 
       ('Child(ren):','Boy:','','Girl:','')]

# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0])



Booking_canvas = Tk()

v = StringVar(Booking_canvas, '1')
Rbs = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10'}
for (key, value) in Rbs.items():
    Radiobutton(Booking_canvas, text = key, variable = v,
                value = value, indicator = 0,
                background = 'light blue').place(x = int(key)*30, y = 200)
t = Table(Booking_canvas)
Booking_canvas.mainloop()
'''
'''
# Insert for displaying a table wasn't working
from tkinter import *

def onclick():
   pass

li = [1]
root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, li[0])
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()
'''
'''
#Select where query to display table of available buses
from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

def Find_Bus(): #with where conditions
    val = []
    val.append(From_En.get())
    val.append(To_En.get())
    tup = tuple(val)
    mycursor.execute('Select * from Bus_Stand where From_dest = %s and To_dest = %s limit 0,10',tup) # where conditions
    mycursor.fetchall()
    i = 0
    Booking2 = Tk()
    Booking2.title('Available  Buses')
    Booking2['background'] = 'Cyan'

##    scrollbar = Scrollbar(Booking2)
##    scrollbar.pack(side = BOTTOM, fill = Y)
    
    for bus in mycursor:
        print(type(bus))
        for j in range(len(bus)):
            e = Entry(Booking2)
            e.grid(row = i+1, column = j+1)
            e.insert(END, str(bus[j]))
        i += 1

    Back = Button(Booking2, text = '<<<<< Back >>>>>', command = Booking2.destroy,background = 'Plum')
    Back.place(x = i, y = j*50)
    Booking2.geometry('1150x400')
    Booking2.mainloop()

def Find_Bus2(): #without where conditions
    mycursor.execute('Select * from Bus_Stand limit 0,10') # where conditions
    i = 0
    Booking2 = Tk()
    Booking2.title('Available  Buses')
    Booking2['background'] = 'Cyan'

##    scrollbar = Scrollbar(Booking2)
##    scrollbar.pack(side = BOTTOM, fill = Y)
    
    for bus in mycursor:
        print(type(bus))
        for j in range(len(bus)):
            e = Entry(Booking2)
            e.grid(row = i+1, column = j+1)
            e.insert(END, str(bus[j]))
        i += 1

    Back = Button(Booking2, text = '<<<<< Back >>>>>', command = Booking2.destroy,background = 'Plum')
    Back.place(x = i, y = j*50)
    Booking2.geometry('1150x400')
    Booking2.mainloop()

Booking = Tk()

From = Label(Booking, text = 'From:', fg = 'black', font = ('Candara', 15), background = 'light blue')
From.place(x = 100, y = 80)

To = Label(Booking, text = 'To : ', fg = 'black', font = ('Candara', 15), background = 'light blue')
To.place(x = 100, y = 140)

From_En = Entry(Booking)
From_En.place(x = 200, y = 80)#, ipady = 3)

To_En = Entry(Booking)
To_En.place(x = 200, y = 140)


Find = Button(Booking, text = '    Find Buses    ', command = Find_Bus2, font=('Candara',18))
Find.place(x = 300, y = 630)
Booking.mainloop()
'''
'''
from tkinter import * 
from tkinter import messagebox 
  
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  
messagebox.showinfo("showinfo", "Information") 
  
messagebox.showwarning("showwarning", "Warning") 
  
messagebox.showerror("showerror", "Error") 
  
messagebox.askquestion("askquestion", "Are you sure?") 
  
messagebox.askokcancel("askokcancel", "Want to continue?") 
  
messagebox.askyesno("askyesno", "Find the value?") 
  
  
messagebox.askretrycancel("askretrycancel", "Try again?")   
  
root.mainloop()  

'''

''' write the ticket details in a file '''
''' Create a table for ticket savings, and while connecting (all files to one) display
their name, ticket no, etc and also manage them using sql queries
Else - link users and bus_stand'''

'''
from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

with open('Booking_details.csv', 'a+') as f:
    val = []
    select = 'Select first_name, last_name, phone_no from users_personal where user_id = %s'
    ID = int(input('ID : '))
    mycursor.execute(select, (ID,))
    fetch_val = mycursor.fetchone()
    print(fetch_val)
    f.write(fetch_val)
'''
'''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import mysql.connector as sql
##
book = Tk()
book.title('Your ticket')
book['background'] = 'Black'

label1 = Label(book, text = '                Ticket Details                ', font = ('Canadara', 18), fg = 'gold', background = 'black', relief = RAISED)
label1.place(x = 70, y = 10)

frm = Label(book, text = 'From destination (stand + city)   -', font = ('Canadara', 14), fg = 'white', background = 'black')
frm.place(x = 20, y = 70)

to = Label(book, text = 'To destination    -', font = ('Canadara', 14), fg = 'white', background = 'black')
to.place(x = 20, y = 100)

timed = Label(book, text = 'Timing of departure    -', font = ('Canadara', 14), fg = 'white', background = 'black')
timed.place(x = 20, y = 130)

timea = Label(book, text = 'Timing of arrival    -', font = ('Canadara', 14), fg = 'white', background = 'black')
timea.place(x = 20, y = 160)

fm = Label(book, text = 'No. of female(s)    -', font = ('Canadara', 14), fg = 'white', background = 'black')
fm.place(x = 20, y = 190)

m = Label(book, text = 'No. of male(s) (if conditions)    -', font = ('Canadara', 14), fg = 'white', background = 'black')
m.place(x = 20, y = 220)

b = Label(book, text = 'No. of boy(s)    -', font = ('Canadara', 14), fg = 'white', background = 'black')
b.place(x = 20, y = 250)

g = Label(book, text = 'No. of girl(s)    -', font = ('Canadara', 14), fg = 'white', background = 'black')
g.place(x = 20, y = 280)


##var1 = StringVar()
##var2 = StringVar()
##var3 = StringVar()
##
##Radiobutton(book, text = "group1", variable = var1, value = 0).pack()
##Radiobutton(book, text = "group2", variable = var2, value = 0).pack()
##Radiobutton(book, text = "group3", variable = var3, value = 0).pack()
##
##
##book.geometry('550x550')
##
'''

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import mysql.connector as sql
'''
mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

root = Tk()


select = 'Select * from bus_stand'
mycursor.execute(select)
rows = mycursor.fetchall()
print(rows)
for i in range(len(rows)):
    print(rows[i],type(rows[i]),'\n')
'''

''' select only one out of the radiobutton '''
'''
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 

def my_upd():
    r2_v.set(r1_v.get())  # read from first group and set the second group
    print('Radiobutton  value :',r1_v.get())

r1_v = tk.StringVar()
r1_v.set('Passed') # (default value ) Can assign value Appear or Failed

r1 = tk.Radiobutton(my_w, text='Passed', variable=r1_v, value='Passed',command=my_upd)
r1.grid(row=1,column=1) 

r2 = tk.Radiobutton(my_w, text='Failed', variable=r1_v, value='Failed',command=my_upd)
r2.grid(row=1,column=2) 

r3 = tk.Radiobutton(my_w, text='Appearing', variable=r1_v, value='Appear',command=my_upd )
r3.grid(row=1,column=3) 


##r2_v = tk.StringVar()
##r2_v.set('Passed') # default value
##
##r4 = tk.Radiobutton(my_w, text='Passed', variable=r2_v, value='Passed',command=my_upd)
##r4.grid(row=2,column=1) 
##
##r5 = tk.Radiobutton(my_w, text='Failed', variable=r2_v, value='Failed',command=my_upd)
##r5.grid(row=2,column=2) 
##
##r6 = tk.Radiobutton(my_w, text='Appearing', variable=r2_v, value='Appear',command=my_upd )
##r6.grid(row=2,column=3) 
##
my_w.mainloop()
'''
root = Tk()

r = IntVar()
##r.get()
##row = [(1,'annyeong'),(2, 'Hola'),(3,'namaste')]
row = [(2, 'KA-513-1727', 'Bangalore', 'Shanthi Nagar', 'Chennai', 'Koyambedu Bus Stand', '9PM', '6AM', 'Non-AC Semi-Sleeper', 'Anirudh Rao'), (3, 'KA-560-1237', 'Bangalore', 'Shanthi Nagar', 'Chennai', 'Koyambedu Bus Stand', '10:30PM', '7AM', 'Non-AC Sleeper', 'Viraj')]
for i in range(len(row)):
    rb1 = Radiobutton(root, text = str(row[i][0]), variable = r, value = i)
    rb1.pack()

##rb2 = Radiobutton(root, text = 'Option 2', variable = r, value = 2)
##rb2.pack()
##
##rb3 = Radiobutton(root, text = 'Option 3', variable = r, value = 3)
##rb3.pack()
##
##rb4 = Radiobutton(root, text = 'Option 4', variable = r, value = 4)
##rb4.pack()

root.mainloop()





































