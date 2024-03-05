''' Sign Up 1 and 2 '''
from tkinter import *
import random
from PIL import ImageTk,Image 
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor()

ID = random.randint(0,9999999)
print('Your user ID is : ', ID)
#Users_details - User_ID, First_name, Last_name, Gmail, Phone_no, User_name, Password
insert = 'Insert into users_details(User_ID, First_name, Last_name, Gmail, Phone_no, User_name, Password) values (%s,%s,%s,%s,%s,%s,%s)'
def Input_data():
    val1 = []
    val1.extend(val)
    val1.append(Username_en.get())
    val1.append(Password_en.get())
    print(val1)
    tup = tuple(val1)
    mycursor.execute(insert, tup)
    mydb.commit()
    print(mycursor.rowcount,"record(s) inserted")
    

def Next():
    global val
    val = []
    val.append(ID)
    val.append(F_Name_en.get())
    val.append(L_Name_en.get())
    val.append(Gmail_en.get())
    val.append(doj_en.get())
    print(val)

    SignUp_window1.destroy()
    
    SignUp_window2 = Tk()
    SignUp_window2.title("Signing You Up! <Page 2>")

    SignUp_window2_canvas = Canvas(SignUp_window2, width=600, height=600)
    SignUp_window2_canvas.grid(column=0,row=0)

    SignUp_window2_image = ImageTk.PhotoImage(Image.open("Bus4.png"))
    SignUp_window2_canvas.create_image(350,300, image = SignUp_window2_image)#25,125

    '''Labels, Entries, Button'''
    Username = Label(SignUp_window2, text = 'User Name', font = ('Candara',12), background = 'plum', justify = LEFT)
    Username.grid(column = 0, row = 1)
    SignUp_window2_canvas.create_window(200,150, window = Username)

    Password = Label(SignUp_window2, text = 'New Password',font = ("Candara",12), background = 'plum', justify = LEFT)
    Password.grid(column = 0, row = 2)
    SignUp_window2_canvas.create_window(200,190, window = Password)

    ID_dis = Label(SignUp_window2, text = '          '+str(ID)+' : is your User ID,\n THIS IS A MUST DURING BOOKINGS',font = ("Candara",12), background = 'plum', justify = LEFT)
    ID_dis.grid(column = 0, row = 3)
    SignUp_window2_canvas.create_window(200,270, window = ID_dis)

    global Username_en, Password_en
    Username_en = Entry(SignUp_window2)
    Username_en.grid(column = 1, row = 1)
    SignUp_window2_canvas.create_window(400,150, window = Username_en)

    Password_en = Entry(SignUp_window2, show='*')
    Password_en.grid(column = 1, row = 2)
    SignUp_window2_canvas.create_window(400,190, window = Password_en)

    password = Label(SignUp_window2, text = 'Password should atleast contain 8 characters & symbols',fg = 'White', font = ("Candara",10), background = 'black')
    SignUp_window2_canvas.create_window(300,230, window = password)

    submit = Button(SignUp_window2, text = 'Submit',command = Input_data, font =("Candara",10), background = 'Sky blue')
    submit.grid(column = 0, row = 3)
    SignUp_window2_canvas.create_window(200,320, window = submit)

    SignUp_window2.geometry('550x380')
    SignUp_window2.resizable(False,False)

    SignUp_window2.mainloop()


SignUp_window1 = Tk()
SignUp_window1.title('Signing you up - 1')

SignUp_window1_canvas = Canvas(SignUp_window1, width=600, height=600)#620,413
SignUp_window1_canvas.grid(column=0,row=0)

SignUp_window1_image = ImageTk.PhotoImage(Image.open("Bus4.png"))
SignUp_window1_canvas.create_image(350,300, image = SignUp_window1_image)#25,125

F_Name = Label(SignUp_window1, text = 'First Name', font = ("Candara",12), background = 'plum', justify = LEFT)
F_Name.grid(column = 0,row = 1)
SignUp_window1_canvas.create_window(200,150, window = F_Name)

L_Name = Label(SignUp_window1, text = 'Last Name', font = ("Candara",12), background = 'plum', justify = LEFT)
L_Name.grid(column = 0,row =2)
SignUp_window1_canvas.create_window(200,190, window = L_Name)

Gmail = Label(SignUp_window1, text = 'Email',font = ("Candara",12), background = 'plum', justify = LEFT)
Gmail.grid(column = 0,row =3)
SignUp_window1_canvas.create_window(200,230, window = Gmail)

doj = Label(SignUp_window1, text = 'Phone number', font=("Candara",12), background = 'plum', justify = LEFT)
doj.grid(column = 0, row = 5)
SignUp_window1_canvas.create_window(200,270, window = doj)

F_Name_en = Entry(SignUp_window1)
F_Name_en.grid(column = 1,row=1)
SignUp_window1_canvas.create_window(350,150, window = F_Name_en)

L_Name_en = Entry(SignUp_window1)
L_Name_en.grid(column = 1,row=2)
SignUp_window1_canvas.create_window(350,190, window = L_Name_en)

Gmail_en = Entry(SignUp_window1)
Gmail_en.grid(column = 1,row=3)
SignUp_window1_canvas.create_window(350,230, window = Gmail_en)

doj_en = Entry(SignUp_window1)
doj_en.grid(column = 1, row = 4)
SignUp_window1_canvas.create_window(350,270, window = doj_en)

Next = Button(SignUp_window1, text = '<<<<< Next >>>>>', command = Next, font=("Candara",10), background = 'sky blue')
SignUp_window1_canvas.create_window(200, 310, window = Next)

SignUp_window1.geometry('600x450')
SignUp_window1.resizable(False,False)

SignUp_window1.mainloop()
