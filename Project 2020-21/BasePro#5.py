''' after edit profile button'''

from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

# users - ID, user_name, password

def Editname():
    Manage2 = Tk()
    Manage2.title('Change username')
    Manage2['background'] = 'plum'
    
    name = Label(Manage2, text = 'New User Name', fg = 'white', background = 'black', font = ('Candara', 15))
    name.place(x = 10, y = 50)

    name_en = Entry(Manage2)
    name_en.place(x = 200, y = 50)

    password = Label(Manage2, text = 'Password', fg = 'white', background = 'black', font = ('Candara', 15))
    password.place(x = 10, y = 100)

    pass_en = Entry(Manage2, show = '*')
    pass_en.place(x = 200, y = 100)

    BId = Label(Manage2, text = 'User ID', fg = 'white', background = 'black', font = ('Candara', 15))
    BId.place(x = 10, y = 150)

    bid_en = Entry(Manage2)
    bid_en.place(x = 200, y = 150)

    def update():
        update1 = 'Update users_details set user_name = %s where password = %s and User_ID = %s'
        val = []
        val.append(name_en.get())
        val.append(pass_en.get())
        val.append(bid_en.get())

        tup = tuple(val)
        mycursor.execute(update1,tup)
        mydb.commit()
        print(mycursor.rowcount,"record(s) updated")

    submit = Button(Manage2, text = 'Change', command = update, fg = 'white', background = 'black', font = ('Candara', 15))
    submit.place(x = 120, y = 200)

    Manage2.geometry('370x300')
    Manage2.resizable(False,False)
    Manage2.mainloop()

def EditPassword():
    Manage2 = Tk()
    Manage2.title('Change password')
    Manage2['background'] = 'plum'
    
    bid = Label(Manage2, text = 'User ID', fg = 'white', background = 'black', font = ('Candara', 15))
    bid.place(x = 10, y = 50)

    bid_en = Entry(Manage2)
    bid_en.place(x = 250, y = 50)

    password = Label(Manage2, text = 'New Password', fg = 'white', background = 'black', font = ('Candara', 15))
    password.place(x = 10, y = 100)

    pass_en = Entry(Manage2, show = '*')
    pass_en.place(x = 250, y = 100)

    confirm = Label(Manage2, text = 'Please make sure that your password contains atleast 8 characters \n and atleast 3 special symbols', fg = 'black', background = 'cyan', font = ('Candara', 11))
    confirm.place(x = 10, y = 150)

    def update():
        update = 'Update users_details set password = %s where User_ID = %s'
        val = []
        val.append(pass_en.get())
        val.append(bid_en.get())

        tup = tuple(val)
        mycursor.execute(update,tup)
        mydb.commit()
        print(mycursor.rowcount,"record(s) updated")

    submit = Button(Manage2, text = 'Change', command = update, fg = 'white', background = 'black', font = ('Candara', 15))
    submit.place(x = 10, y = 200)

    Manage2.geometry('480x300')
    Manage2.resizable(False,False)
    Manage2.mainloop()

def EditPhone():
    Manage2 = Tk()
    Manage2.title('Change Phone number')
    Manage2['background'] = 'plum'
    
    bid = Label(Manage2, text = 'User ID', fg = 'white', background = 'black', font = ('Candara', 15))
    bid.place(x = 10, y = 50)

    bid_en = Entry(Manage2)
    bid_en.place(x = 250, y = 50)

    phone = Label(Manage2, text = 'New Phone Number', fg = 'white', background = 'black', font = ('Candara', 15))
    phone.place(x = 10, y = 100)

    phone_en = Entry(Manage2)
    phone_en.place(x = 250, y = 100)

    def update():
        # users_personal - ID, first_name, last_name, gmail, user_post, phone_no
        update = 'Update users_details set Phone_No = %s where user_ID = %s'
        val = []
        val.append(phone_en.get())
        val.append(bid_en.get())

        tup = tuple(val)
        mycursor.execute(update,tup)
        mydb.commit()
        print(mycursor.rowcount,"record(s) updated")

    submit = Button(Manage2, text = 'Change', command = update, fg = 'white', background = 'black', font = ('Candara', 15))
    submit.place(x = 10, y = 200)

    Manage2.geometry('420x300')
    Manage2.resizable(False,False)
    Manage2.mainloop()

def Editmail():
    Manage2 = Tk()
    Manage2.title('Change Mail Address')
    Manage2['background'] = 'plum'
    
    bid = Label(Manage2, text = 'User ID', fg = 'white', background = 'black', font = ('Candara', 15))
    bid.place(x = 10, y = 50)

    bid_en = Entry(Manage2)
    bid_en.place(x = 200, y = 50)

    mail = Label(Manage2, text = 'New Gmail', fg = 'white', background = 'black', font = ('Candara', 15))
    mail.place(x = 10, y = 100)

    mail_en = Entry(Manage2)
    mail_en.place(x = 200, y = 100)

    def update():
        # users_personal - ID, first_name, last_name, gmail, user_post, phone_no
        update = 'Update users_details set gmail = %s where user_ID = %s'
        val = []
        val.append(mail_en.get())
        val.append(bid_en.get())

        tup = tuple(val)
        mycursor.execute(update,tup)
        mydb.commit()
        print(mycursor.rowcount,"record(s) updated")

    submit = Button(Manage2, text = 'Change', command = update, fg = 'white', background = 'black', font = ('Candara', 15))
    submit.place(x = 10, y = 200)

    Manage2.geometry('370x300')
    Manage2.resizable(False,False)
    Manage2.mainloop()


Manage = Tk()
Manage.title('Manage your bookings')

Manage['background'] = 'Gold'

message = 'Options available for editing your profile'
label = Label(Manage, text = message, fg = 'black',background = 'sky blue', font = ('Candara', 18))#
label.place(x = 50, y = 10)

''' Buttons '''
Edit_name = Button(Manage, text = '1. Edit your username', command = Editname, fg = 'white', background = 'black', font = ('Candara', 15))
Edit_name.place(x = 50, y = 80)

Edit_password = Button(Manage, text = '2. Edit your password', command = EditPassword, fg = 'white', background = 'black', font = ('Candara', 15))
Edit_password.place(x = 50, y = 160)

Edit_phone = Button(Manage, text = '3. Edit your phone number', command = EditPhone, fg = 'white', background = 'black', font = ('Candara', 15))
Edit_phone.place(x = 50, y = 240)

Edit_gmail = Button(Manage, text = '4. Edit your email', command = Editmail, fg = 'white', background = 'black', font = ('Candara', 15))
Edit_gmail.place(x = 50, y = 320)


#Manage.resizable(False,False)
Manage.geometry('550x550')
Manage.mainloop()
