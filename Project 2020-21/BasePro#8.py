''' After logging in '''

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

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
    pass
    ''' move to window where hire/bus'''

def cancel():
    '''delete booking - algorithm?'''

def show():
    '''show current bookings - algorithm?'''

def logout():
    messagebox.askyesno("askyesno", "Log out?")
    Home.destroy()
    ''' later go to home page (#1) '''

def edit():
    ''' base pro #5 '''

Book = Button(Home, text = 'Book a Bus', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
Book.place(x = 30, y = 100)

Cancel = Button(Home, text = 'Cancel bookings', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
Cancel.place(x = 30, y = 200)

Show = Button(Home, text = 'Show bookings', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
Show.place(x = 900, y = 100)

Log_out = Button(Home, text = 'Log out', command = logout, fg = 'light green', background = 'black', font = ('Candara', 20))
Log_out.place(x = 900, y = 200)

Edit = Button(Home, text = 'Edit Profile', command = book, fg = 'light green', background = 'black', font = ('Candara', 20))
Edit.place(x = 500, y = 500)

Home.geometry('1165x600')
Home.resizable(False,False)
Home.mainloop()
