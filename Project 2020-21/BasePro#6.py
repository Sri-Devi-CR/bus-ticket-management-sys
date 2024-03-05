''' Booking a ticket '''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import mysql.connector as sql
import random

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)
##create = 'Create table Bus_Stand(ID int Auto_Increment Primary Key, Bus_No varchar(15), From_dest varchar(50),\
##            From_Stand varchar(50),To_dest varchar(50),To_Stand varchar(50), Departure_Timings varchar(20), Arrival_Timings varchar(20),Type varchar(50), Driver varchar(50))'
##mycursor.execute(create)

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
            messagebox.askquestion("Confirmation", "Confirm your booking?")
            messagebox.askquestion("2nd confirmation", "Are you sure?")
            messagebox.showinfo("Thank you", "Thank You! Please screenshot your ticket displayed. \n\
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
