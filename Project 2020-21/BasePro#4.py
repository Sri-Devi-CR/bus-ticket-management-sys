''' Log In window '''
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

select = 'Select * from users_details where User_Name = %s' #unique - primary key
select2 = 'Select * from users_details where Password = %s'
select2 = 'Select * from users_details where User_ID = %d'

def LogIn():
    try:
        val = []
        val.append(Username_en.get())
        val.append(Password_en.get())
        val.append(str(User_ID_en.get()))
        
        tup = tuple(val)
        print('Tuple',tup)
        
        mycursor.execute(select, (tup[0],))
        row = mycursor.fetchone()
        print('Fetched row',row)

        if (row[5] == Username_en.get()) and (row[6] == Password_en.get()) and (row[0] == int(User_ID_en.get())):
            move = Label(LogIn_window, text = ':) Moving to your account...')
            LogIn_window_canvas.create_window(400,350, window = move)

    ####    elif ((row[0] != Username_en.get()) and (row[1] == Password_en.get())) or ((row[0] == Username_en.get()) and (row[1] != Password_en.get())):
        elif (row[5] != Username_en.get()) or (row[6] != Password_en.get()) or (row[0] != int(User_ID_en.get())):
            error = Label(LogIn_window, text = '(^^)\' Sorry, either of the records are wrong.\n Please consider rechecking your inputs! ')
            LogIn_window_canvas.create_window(400,380, window = error)

        elif (row[5] != Username_en.get()) and (row[6] != Password_en.get()) and (row[0] != int(User_ID_en.get())):
            error = Label(LogIn_window, text = ' :] Sorry, your acc does not exist, create one!')
            LogIn_window_canvas.create_window(400,380, window = error)

    except TypeError:
        error = Label(LogIn_window, text = ' (^~^)\' Sorry, your acc does not exist, create one! ')
        LogIn_window_canvas.create_window(400,380, window = error)

LogIn_window = Tk()
LogIn_window.title('Log In')

LogIn_window_canvas = Canvas(LogIn_window, width=600, height=600)
LogIn_window_canvas.grid(column=0,row=0)

LogIn_window_image = ImageTk.PhotoImage(Image.open("Bus5.png"))
LogIn_window_canvas.create_image(350,300, image = LogIn_window_image)#25,125

'''Labels,Entries and Buttons'''
Username = Label(LogIn_window, text = 'User Name',fg = 'White' , font = ('Candara',12), background = 'black', justify = LEFT)
LogIn_window_canvas.create_window(200, 200, window = Username)

Password = Label(LogIn_window, text = 'Password',fg = 'White' ,font = ("Candara",12), background = 'black', justify = LEFT)
LogIn_window_canvas.create_window(200, 250, window = Password)

User_ID = Label(LogIn_window, text = 'User ID',fg = 'White' ,font = ("Candara",12), background = 'black', justify = LEFT)
LogIn_window_canvas.create_window(200, 300, window = User_ID)


Username_en = Entry(LogIn_window)
LogIn_window_canvas.create_window(350, 200, window = Username_en)

Password_en = Entry(LogIn_window, show = '*')
LogIn_window_canvas.create_window(350, 250, window = Password_en)

User_ID_en = Entry(LogIn_window)
LogIn_window_canvas.create_window(350, 300, window = User_ID_en)

Log = Button(LogIn_window, text = '    Log In    ', command = LogIn, fg = 'black' , font = ('Candara',12), background = 'plum', justify = LEFT)
LogIn_window_canvas.create_window(200, 350, window = Log)

LogIn_window.geometry('600x450')
LogIn_window.resizable(False,False)

LogIn_window.mainloop()
