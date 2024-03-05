''' Home window'''

from tkinter import *
from PIL import ImageTk,Image


def SignUpWindow():
    pass
'''Change to their resp windows'''
def SignInWindow():
    pass

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
