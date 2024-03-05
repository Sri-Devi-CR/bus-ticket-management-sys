from tkinter import *
from PIL import ImageTk,Image 
import mysql.connector as sql
from tkinter import messagebox
import random, time

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

def Home_win():
    def SignUpWindow():
        home_window.destroy()
        SignUp_wins()
        
    def SignInWindow():
        home_window.destroy()
        LogIn_win()

    '''Windows along with canvas'''
    # Home Window
    home_window = Tk()
    home_window.title('Home Page')

    home_window_canvas = Canvas(home_window, width=620, height=413)
    home_window_canvas.grid(column=0,row=0)

    home_window_image = ImageTk.PhotoImage(Image.open("Bus3.jpg"))
    home_window_canvas.create_image(25,125, image = home_window_image)

    home_window_text = 'Welcome to Sify Bus Travel Agency! \n Pleased to have you here!'
    home_window_message = Label(home_window_canvas, text = home_window_text, image = home_window_image, fg = 'black', font = ("Candara", 18, 'italic'), compound = 'bottom')#, justify = CENTER)
    home_window_message.config(bg = 'light green')
    home_window_message.grid(column = 1, row = 5, sticky = N)

    '''Labels, Buttons and Entries'''
    # home_window:
    Label1 = Label(home_window, text = 'First time travelling in our agency?', font = ("Candara",15, 'italic'),background = 'orange', justify = LEFT)
    Label1.grid(column = 30,row = 1)
    home_window_canvas.create_window(200,150, window = Label1)

    Label2 = Label(home_window, text = 'Travelled more than once?', font = ("Candara",15, 'italic'),background = 'orange', justify = LEFT)
    Label2.grid(column = 30,row = 2)
    home_window_canvas.create_window(165,250, window = Label2)

    Label3 = Label(home_window, text = 'Remember: Social Distancing, Mask all the time, Sanitize!! :)', font = ("Candara",15, 'italic'),background = 'Plum', justify = LEFT)
    Label3.grid(column = 500,row = 200)
    home_window_canvas.create_window(300,600, window = Label3)

    SignUp = Button(home_window, text = 'Sign Me Up!' , command = SignUpWindow, font = ("Candara",13, 'italic'), background = 'coral', fg = 'Black',anchor='w')
    home_window_canvas.create_window(450, 150, window=SignUp)

    SignIn = Button(home_window, text = 'Sign In' , command = SignInWindow, font = ("Candara",13, 'italic'), background = 'coral', fg = 'Black',anchor='w')
    home_window_canvas.create_window(430, 250, window=SignIn)

    home_window.geometry('764x641')#Right X Bottom
    home_window.resizable(False,False)#True,True)#

    home_window.mainloop()

def SignUp_wins():
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
        SignUp_window2.destroy()
        LogIn_win()        

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

        global SignUp_window2
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
        SignUp_window2.destroy()


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
    SignUp_window1.destroy()

def LogIn_win():
##    SignUp_window2.destroy()
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
                
                LogIn_window.destroy()
                After_LogIn_win()
                

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

def After_LogIn_win():
    Home = Tk()
    Home.title('Home page')
    Home['background'] = 'Cyan'

    Home_canvas = Canvas(Home, width=620, height=413)
    Home_canvas.grid(column=0,row=0)

    img = Image.open("1.png")
    Home_image = ImageTk.PhotoImage(img)
    Home_canvas.create_image(25,125, image = Home_image)
    Home_canvas.image = Home_image

    Home_text = 'Welcome to your home page!                              '
    Home_message = Label(Home_canvas, text = Home_text, image = Home_image, fg = 'black', font = ("Candara", 18, 'italic'), compound = 'bottom')#, justify = CENTER)
    Home_message.image = Home_image
    Home_message.config(bg = 'sky blue')
    Home_message.grid(column = 1, row = 5, sticky = N)

    def book():
        Hire_Book_OP_win()

    def logout():
        mess = messagebox.askyesno("Log out?", "Are you sure you want to log out?")
        if mess:
            Home.destroy()
            Home_win()
            

    def edit():
        Edit_Pro_win()

    Book = Button(Home, text = 'Book a Ticket', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
    Book.place(x = 30, y = 100)

    hii = Button(Home, text = 'Hire a Bus', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
    hii.place(x = 30, y = 200)
##
##    Show = Button(Home, text = 'Show bookings', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
##    Show.place(x = 900, y = 100)

    Log_out = Button(Home, text = 'Log out', command = logout, fg = 'light green', background = 'black', font = ('Candara', 20))
    Log_out.place(x = 900, y = 200)

    Edit = Button(Home, text = 'Edit Profile', command = edit, fg = 'light green', background = 'black', font = ('Candara', 20))
    Edit.place(x = 900, y = 100)

    Home.geometry('1165x600')
    Home.resizable(False,False)
    Home.mainloop()


def Hire_Book_OP_win():#hire/book options window
    def Validate2():
        print(r.get()+1)
        print(rows[r.get()])
        if r.get()+1:
            Book['state'] = NORMAL
        else:
            messagebox.showerror("Error", "Please select the ID to book your ticket!")


    def HireBus():   
        
        def ConfirmBooking():
            fir = messagebox.askyesno("1st Conformation", "Confirm your booking?")
            if fir:
                sec = messagebox.askyesno("2nd Conformation", "Are you sure?")
                if sec:
                    third = messagebox.showinfo("Thank you", "Thank You! Please screenshot your ticket displayed. \n\
                                            Check Booked_ticket.csv for your ticket details which would be saved TEMPORARILY")

                    book = Tk()
                    book.title('Hired Bus')
                    book['background'] = 'black'

                    # ID, Bus_plate_no, From_dest, To_dest, Phone_no

                    index = r.get() # Booked row (bus)
                    di_in = rows[index]

                    label1 = Label(book, text = '                Ticket Details                ', font = ('Canadara', 18), fg = 'gold', background = 'black', relief = RAISED)
                    label1.place(x = 70, y = 10)

                    bus_no = Label(book, text = 'Bus Number   -   ' + str(di_in[1]),font = ('Canadara', 14), fg = 'white', background = 'black')
                    bus_no.place(x = 20, y = 70)

                    bus_type = Label(book, text = 'From destination   -   '+ str(di_in[2]), font = ('Canadara', 14), fg = 'white', background = 'black')
                    bus_type.place(x = 20, y = 100)

                    bus_driver = Label(book, text = 'To destination   -   '+ str(di_in[3]), font = ('Canadara', 14), fg = 'white', background = 'black')
                    bus_driver.place(x = 20, y = 130)

                    frm = Label(book, text = 'Number of seats available    -   ' + str(45), font = ('Canadara', 14), fg = 'white', background = 'black')
                    frm.place(x = 20, y = 160)

                    to = Label(book, text = 'Phone no    -   '+ str(di_in[4]), font = ('Canadara', 14), fg = 'white', background = 'black')
                    to.place(x = 20, y = 190)

                    book.geometry('550x350')
                    book.mainloop()

                    with open('Booked_ticket.csv','w+') as f: ### NOT COMPLETED
                        f.truncate(0)
                        f.write('Bus Number   -   ' + str(di_in[1]) + '\n')
                        f.write('From destination   -   '+ str(di_in[2]) + '\n')
                        f.write('To destination   -   '+ str(di_in[3]) + '\n')
                        f.write('Number of seats available    -   ' + str(45) + '\n')
                        f.write('Phone no    -   '+ str(di_in[4]) + '\n')


        Hire = Tk()
        Hire.title('Buses available')
        
        column_names = ['ID', 'Bus Number', 'From Destination', 'To Destination', 'Phone number']
        mycursor.execute('Select * from Hire limit 0,10')
        i = 0
        flag = 0
        
        
        global rows
        rows = mycursor.fetchall()
        
            
        for hire_bus in rows:
            for j in range(len(hire_bus)):
                e = Label(Hire, borderwidth = 1, relief = 'ridge', bg = 'cyan')
                if flag == 0:
                    e.config(text = column_names[j]+'\n'+str(hire_bus[j]))
                else:
                    e.config(text = str(hire_bus[j]))

                e.grid(row = i+1, column = j+1)
            i += 1
            flag = 1

        global r, Book
        pos_y = 250
        r = IntVar(Hire)

        for k in range(len(rows)):
            RB_k = Radiobutton(Hire, text = str(rows[k][0]), variable = r, value = k)
            RB_k.place(x = 150, y = pos_y)
            pos_y += 30

        Back = Button(Hire, text = '<<<<< Back >>>>>', command = Hire.destroy,font = ("Candara", 10, 'italic'),background = 'Plum')
        Back.place(x = i, y = 250)
                
        Book = Button(Hire, text = 'Book',command = ConfirmBooking, fg = 'black', background = 'plum', font = ('Candara', 10))
        Book.place(x = 200, y = 300)
        Book['state'] = DISABLED

        validate2 = Button(Hire, text = 'Validate <and click on book>',command = Validate2, fg = 'black', background = 'plum', font = ('Candara', 10))
        validate2.place(x = 200, y = 250)

        Hire.geometry('400x500')
        Hire.mainloop()

        
    def BookTicket():
        Book_Tic_win()
            
    def main():
        global All_Options
        All_Options = Tk()
        All_Options.title('Choice Options')

        All_Options['background'] = 'black'

        message = Label(All_Options, text = 'Here you can choose hire buses or \n book your ticket to travel between states.', fg = 'black', background = 'plum', font = ('candara', 18, 'italic'), compound = 'center')
        message.place(x = 10, y = 20)

        Hire = Button(All_Options, text = 'To Hire bus(es)', command = HireBus, fg = 'black', background = 'cyan', font = ('Candara', 15))
        Hire.place(x=20,y=120)

        Book =  Button(All_Options, text = 'To Book your ticket', command = BookTicket, fg = 'black', background = 'cyan', font = ('Candara', 15))
        Book.place(x=250,y=120)


        All_Options.geometry('500x320')
        All_Options.mainloop()

    main()

def Book_Tic_win():
    def Validate():
        if From_En.get() and To_En.get() and Journ_Date.get() and Journ_Time.get():
            Find['state'] = NORMAL
        else:
            messagebox.showerror("Error", "Please enter all the fields required!")

    def Validate2():
        print(r.get()+1)
        print(rows[r.get()])
        if r.get()+1:
            Book['state'] = NORMAL
        else:
            messagebox.showerror("Error", "Please select the ID to book your ticket!")
        
    def Find_Bus():
        print('Entered fields',From_En.get(),To_En.get(),Journ_Date.get(),Journ_Time.get())
        if (From_En.get() != None) and (To_En.get() != None) and (Journ_Date.get() != None) and (Journ_Time.get() != None):
            def ConfirmBooking():
                fi = messagebox.askyesno("Confirmation", "Confirm your booking?")
                if fi:
                    se = messagebox.askyesno("2nd confirmation", "Are you sure?")
                    if se:
                        th = messagebox.showinfo("Thank you", "Thank You! Please screenshot your ticket displayed. \n\
                                            Check Booked_ticket.csv for your ticket details which would be saved TEMPORARILY")

                        ''' IMPORTANT '''
                        ''' write the ticket details in a file '''
                        ''' Create a table for ticket savings, and while connecting (all files to one) display
                        their name, ticket no, etc and also manage them using sql queries
                        Else - link users and bus_stand'''
                        
                            

                        book = Tk()
                        book.title('Your ticket')
                        book['background'] = 'Black'

                        # ID 0, Bus_No 1, From_dest 2, From_stand 3, To_dest 4, To_stand 5, departure_timings 6
                        # Arrival_timings 7 , Type 8, driver 9

                        index = r.get() # Booked row (bus)
                        di_in = rows[index]
                        
                        label1 = Label(book, text = '                Ticket Details                ', font = ('Canadara', 18), fg = 'gold', background = 'black', relief = RAISED)
                        label1.place(x = 70, y = 10)

                        bus_no = Label(book, text = 'Bus Number   -   ' + str(di_in[1]),font = ('Canadara', 14), fg = 'white', background = 'black')
                        bus_no.place(x = 20, y = 70)

                        bus_type = Label(book, text = 'Bus type   -   '+ str(di_in[8]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        bus_type.place(x = 20, y = 100)

                        bus_driver = Label(book, text = 'Bus driver   -   '+ str(di_in[9]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        bus_driver.place(x = 20, y = 130)

                        frm = Label(book, text = 'From destination    -   ' + str(di_in[2]) + ' , ' + str(di_in[3]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        frm.place(x = 20, y = 160)

                        to = Label(book, text = 'To destination    -   '+ str(di_in[4])+ ' , ' + str(di_in[5]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        to.place(x = 20, y = 190)

                        timed = Label(book, text = 'Timing of departure    -   '+ str(di_in[6]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        timed.place(x = 20, y = 220)

                        timea = Label(book, text = 'Timing of arrival    -   '+ str(di_in[7]), font = ('Canadara', 14), fg = 'white', background = 'black')
                        timea.place(x = 20, y = 250)

                        fm = Label(book, text = 'No. of female(s)    -   '+ str(v.get()), font = ('Canadara', 14), fg = 'white', background = 'black')
                        fm.place(x = 20, y = 280)

                        m = Label(book, text = 'No. of male(s)    -   '+ str(v2.get()), font = ('Canadara', 14), fg = 'white', background = 'black')
                        m.place(x = 20, y = 310)

                        b = Label(book, text = 'No. of boy(s)    -   '+ str(v3.get()), font = ('Canadara', 14), fg = 'white', background = 'black')
                        b.place(x = 20, y = 340)

                        g = Label(book, text = 'No. of girl(s)    -   '+ str(v4.get()), font = ('Canadara', 14), fg = 'white', background = 'black')
                        g.place(x = 20, y = 370)

                        j = 0
                        seat = random.randint(1,45)
                        for i in range(v.get()+v2.get()+v3.get()+v3.get()):
                            sea = Label(book, text = 'Seat number    -   '+ str(seat+j), font = ('Canadara', 14), fg = 'white', background = 'black')
                            sea.place(x = 20, y = 430+j*30)
                            j += 1

                        book.geometry('600x550')

                        with open('Booked_ticket.csv','w+') as f: ### NOT COMPLETED
                            f.write('Bus Number   -   ' + str(di_in[1]) + '\n')
                            f.write('Bus type   -   '+ str(di_in[8]) + '\n')
                            f.write('Bus driver   -   '+ str(di_in[9]) + '\n')
                            f.write('From destination    -   ' + str(di_in[2]) + ' , ' + str(di_in[3]) + '\n')
                            f.write('To destination    -   '+ str(di_in[4])+ ' , ' + str(di_in[5]) + '\n')
                            f.write('Timing of departure    -   '+ str(di_in[6]) + '\n')
                            f.write('Timing of arrival    -   '+ str(di_in[7]) + '\n')
                            
                            f.write('No. of female(s)    -   '+ str(v.get()) + '\n')
                            f.write('No. of male(s)    -   '+ str(v2.get()) + '\n')
                            f.write('No. of boy(s)    -   '+ str(v3.get()) + '\n')
                            f.write('No. of girl(s)    -   '+ str(v4.get()) + '\n')
                            
                            f.write('Journey Date    -   '+ str(Journ_Date.get()) + '\n')

            Booking2 = Tk()
            Booking2.title('Available Buses')
            Booking2['background'] = 'Cyan'

            column_names = ['ID', 'Bus Number', 'From Destination', 'Starting Point', 'To Destination', 'Ending Point',
                            'Departure Timings', 'Arrival Timings', 'Type', 'Driver']
            mycursor.execute('Select * from Bus_Stand where From_Dest = %s and To_Dest = %s limit 0,10',\
                             (From_En.get(), To_En.get()))
                    
            flag = 0
            pos_y = 310
            i = 0
            
            global rows
            rows = mycursor.fetchall()

            for bus in rows:
                for j in range(len(bus)):
                    e = Label(Booking2,borderwidth = 1,relief="ridge", bg = 'cyan')
                    
                    if flag == 0:
                        e.config(text = column_names[j]+'\n'+str(bus[j]))
                    else:
                        e.config(text = str(bus[j]))
                        
                    e.grid(row = i+1, column = j+1)
                    
                    # value -	The value of each radiobutton is assigned to the control variable when it is turned on by the user.
                    # variable -	It is the control variable which is used to keep track of the user's choices. It is shared among all the radiobuttons.  
                    mess = Label(Booking2, text = 'Choose the corresponding ID of the row for which you want to book your bus ticket',fg = 'black', font = ('Candara', 15), background = 'sky blue')
                    mess.place(x = 250, y = 250)            
    ##                var = IntVar()
    ##                Radio_Buttoni = Radiobutton(Booking2, text = str(rows[i][0]), variable = var, value = 1, bg = 'light green')
    ##                Radio_Buttoni.place(x = 250, y = pos_y)
                
                
                flag = 1
                i += 1

            ''' Radio Button '''
            global r, Book
            r = IntVar(Booking2)
            
            for k in range(len(rows)):
                RB_k = Radiobutton(Booking2, text = str(rows[k][0]), variable = r, value = k)#rows[k][0])
                RB_k.place(x = 250, y = pos_y)
                pos_y += 30

            Back = Button(Booking2, text = '<<<<< Back >>>>>', command = Booking2.destroy,font = ("Candara", 10, 'italic'),background = 'Plum')
            Back.place(x = i, y = 5*50)
                
            Book = Button(Booking2, text = 'Book',command = ConfirmBooking, fg = 'black', background = 'plum', font = ('Candara', 10))
            Book.place(x = 500, y = 310)
            Book['state'] = DISABLED

            validate2 = Button(Booking2, text = 'Validate <and click on book>',command = Validate2, fg = 'black', background = 'plum', font = ('Candara', 10))
            validate2.place(x = 300, y = 310)

            Booking2.geometry('950x400')
            Booking2.mainloop()

    Booking = Tk()
    Booking.title('Booking your ticket')

    Booking['background'] = 'magenta'

    Booking_window_text = '<<<<<<<<  Book Your Ticket  >>>>>>>>'
    Booking_window_message = Label(Booking, text = Booking_window_text, fg = 'black', font = ("Candara", 18, 'italic'), compound = 'bottom')
    Booking_window_message.config(bg = 'gold')
    Booking_window_message.place(x = 200, y = 20)

    '''Labels, Buttons'''
    From = Label(Booking, text = 'From:', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    From.place(x = 100, y = 80)

    clicked = StringVar()
    clicked.set('Non-AC Semi-Sleeper')
    Type = Label(Booking, text = 'Type:', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    Type.place(x = 540, y = 80)

    Type_Drop = OptionMenu(Booking, clicked, 'AC Sleeper','AC Semi-sleeper', 'Non-AC Sleeper', 'Non-AC Semi-Sleeper')
    Type_Drop.place(x = 600, y = 80)

    To = Label(Booking, text = 'To : ', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    To.place(x = 100, y = 140)

    Jour_Date = Label(Booking, text = 'Journey Date: ', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    Jour_Date.place(x = 100, y = 200)

    Jour_Time = Label(Booking, text = 'Journey Time : ', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    Jour_Time.place(x = 100, y = 260)

    Adult = Label(Booking, text = 'Adults: ', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    Adult.place(x = 100, y = 320)

    Male = Label(Booking, text = 'Male: ', fg = 'black', font = ('Candara', 14), background = 'sky blue')
    Male.place(x = 120, y = 380)

    place_x = 90#143
    v = IntVar(Booking, '1')
    Rbs = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10'}
    for (key, value) in Rbs.items():
        RB1 = Radiobutton(Booking, text = key, variable = v,
                    value = value, indicator = 0,
                    background = 'sky blue').place(x = place_x+50, y = 420)#380
        place_x += 20

    Female = Label(Booking, text = 'Female: ', fg = 'black', font = ('Candara', 14), background = 'sky blue')
    Female.place(x = 380, y = 380)#120,445

    v2 = IntVar(Booking, '1')
    place_x2 = 380#170
    for (key, value) in Rbs.items():
        RB2 = Radiobutton(Booking, text = key, variable = v2,
                    value = value, indicator = 0,
                    background = 'sky blue').place(x = place_x2+50, y = 420)#450
        place_x2 += 20

    Child = Label(Booking, text = 'Child(ren): ', fg = 'black', font = ('Candara', 15), background = 'sky blue')
    Child.place(x = 100, y = 480)

    Boy = Label(Booking, text = 'Boy: ', fg = 'black', font = ('Candara', 14), background = 'sky blue')
    Boy.place(x = 120, y = 540)

    v3 = IntVar(Booking, '1')
    place_x3 = 90
    for (key, value) in Rbs.items():
        RB3 = Radiobutton(Booking, text = key, variable = v3,
                    value = value, indicator = 0,
                    background = 'sky blue').place(x = place_x3+50, y = 580)
        place_x3 += 20

    Girl = Label(Booking, text = 'Girl: ', fg = 'black', font = ('Candara', 14), background = 'sky blue')
    Girl.place(x = 380, y = 540)

    v4 = IntVar(Booking, '1')
    place_x4 = 380
    for (key, value) in Rbs.items():
        RB4 = Radiobutton(Booking, text = key, variable = v4,
                    value = value, indicator = 0,
                    background = 'sky blue').place(x = place_x4+50, y = 580)
        place_x4 += 20

    '''Entries'''
    From_En = Entry(Booking)
    From_En.place(x = 200, y = 80)#, ipady = 3)

    To_En = Entry(Booking)
    To_En.place(x = 200, y = 140)

    Journ_Date = Entry(Booking)
    Journ_Date.place(x = 260, y = 200)

    Journ_Time = Entry(Booking)
    Journ_Time.place(x = 260, y = 260)

    Find = Button(Booking, text = '    Find Buses    ', command = Find_Bus, font=('Candara',18))
    Find['state'] = DISABLED
    Find.place(x = 100, y = 630)

    Validate = Button(Booking, text = 'Validate',command=Validate, font=('Candara',18))
    Validate.place(x = 400, y = 630)

    Booking.geometry('850x850')
    Booking.mainloop()

def Edit_Pro_win():
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

        mail = Label(Manage2, text = 'New Email', fg = 'white', background = 'black', font = ('Candara', 15))
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

Home_win()

