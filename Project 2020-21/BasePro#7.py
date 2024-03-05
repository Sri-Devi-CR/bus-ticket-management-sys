''' Checking for hiring/booking(local)/booking(city to city) '''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import mysql.connector as sql
import csv

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'P@ssword1',
    charset = 'utf8',
    database = 'mydatabase')

mycursor = mydb.cursor(buffered = True)

##create1 = 'Create table Local(ID int AUTO_INCREMENT PRIMARY KEY, Bus_No varchar(20),Timings time, From_dest varchar(50), To_dest varchar(50))'
##mycursor.execute(create1)

##create2 = 'Create table Hire(ID int AUTO_INCREMENT PRIMARY KEY, Bus_Plate_No varchar(20), From_dest varchar(50), To_dest varchar(50), Phone_No int)'
##mycursor.execute(create2)
def Validate2():
    print(r.get()+1)
    print(rows[r.get()])
    if r.get()+1:
        Book['state'] = NORMAL
    else:
        messagebox.showerror("Error", "Please select the ID to book your ticket!")


def HireBus():   
    
    def ConfirmBooking():
        messagebox.askquestion("askquestion", "Confirm your booking?")
        messagebox.askquestion("askquestion", "Are you sure?")
        messagebox.showinfo("showinfo", "Thank You! Please screenshot your ticket displayed. \n\
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
    ''' move to base pro #6i'''
        
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
