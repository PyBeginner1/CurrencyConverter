from tkinter import *
#kinter calls tabs notebooks
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Currency Converter")
root.geometry("500x500")


#create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady =10)

#create frame
currency_frame = Frame(my_notebook, width =480, height =480)
currency_frame.pack(fill ='both', expand = 1)

convert_frame = Frame(my_notebook)
convert_frame.pack(fill ='both', expand = 1)

#add tabs
my_notebook.add(currency_frame, text = 'Currencies')
my_notebook.add(convert_frame, text = 'Convert')

#disable the 2nd tab until the input in the 1st is entered
my_notebook.tab(1, state='disabled')



def lock():
    #missing entry fields
    if not  home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        #open message error box
        messagebox.showwarning("Warning", 'You didnt fill out all the entries')
    else:
        #disable entry fields after hitting lock
        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        #enable 2nd tab after hitting lock buuton
        my_notebook.tab(1, state='normal')
        amount_label.config(text=f'Amount of {home_entry.get()} to {conversion_entry.get()} ')
        converted_label.config(text=f'Equals this many {conversion_entry.get()} ')
        convert_button.config(text=f'Convert from {home_entry.get()} ')


#to unlock entry fields after being disabled(state='disable')
def unlock():
    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    rate_entry.config(state='normal')
    #disable 2nd tab
    my_notebook.tab(1, state='disabled')


#creating labelframe
#your currency frame
home = LabelFrame(currency_frame, text = "Your Home Currency")
home.pack(pady=20)
#entry box
home_entry = Entry(home, font =('Shanti', 24))
home_entry.pack(pady=10, padx = 10)



#convert currency frame
conversion = LabelFrame(currency_frame, text = "Conversion Currency")
conversion.pack(pady=20)

conversion_label = Label(conversion, text = 'Currency to convert to:')
conversion_label.pack(pady= 10)
conversion_entry = Entry(conversion, font=('Shanti', 24))
conversion_entry.pack(pady=10, padx = 10)
rate_label = Label(conversion, text ='Current Conversion Rate:')
rate_label.pack(pady =20)
rate_entry = Entry(conversion, font=('Shanti', 24))
rate_entry.pack(pady=10, padx = 10)



#button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady = 10)

#create buttons
lock_button = Button(button_frame, text='Lock', command =lock)
lock_button.grid(row = 0, column = 0)
unlock_button = Button(button_frame, text ="Unlock", command = unlock)
unlock_button.grid(row = 0, column = 2, padx = 20)

def convert():
    #clear converrted_entry field if there is any value
    converted_entry.delete(0, END)

    #converting
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    #convert to 2 decimals
    conversion = round(conversion, 2)
    #add commas
    conversion = '{:,}'.format(conversion)

    #update converted_entry
    converted_entry.insert(0, conversion)



def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


#creating label frame in convert tab
amount_label = LabelFrame(convert_frame, text = 'Amount to ')
amount_label.pack(pady=10)

#create enrty field
amount_entry =Entry(amount_label, font =('Shanti', 24))
amount_entry.pack(pady = 10, padx = 10)
#button
convert_button = Button(amount_label, text = 'Convert', command = convert)
convert_button.pack(pady =20)


#equals frame
converted_label = LabelFrame(convert_frame, text = 'Equals this many ')
converted_label.pack(pady = 20)
#entry
converted_entry =Entry(converted_label, font=('Shanti, 24'), bd = 0, bg= 'systembuttonface')    #bd & bg for invisible entry box
converted_entry.pack(padx= 10, pady=10)

#clear button
clear_button = Button(convert_frame, text = 'Clear', command = clear)
clear_button.pack(pady = 20)


#fake label for spacing
spacer = Label(convert_frame, text ="", width = 68)
spacer.pack()
spacer1 = Label(convert_frame, text ="", width = 60)
spacer1.pack()





root.mainloop()
