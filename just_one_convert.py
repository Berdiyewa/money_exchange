from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from time import strftime

win = Tk()
win.title(' Money exchange ')
win.geometry('700x700+400+50')
win.config(bg='darkslategrey')

# ============== frame ==============
main_frame = Frame(win, width=660, height=650)
main_frame.place(x=20, y=20)
logo_frame = LabelFrame(main_frame, width=160, height=60)
logo_frame.place(x=250, y=0)
pic_main_frame = LabelFrame(main_frame, width=90, height=90)
pic_main_frame.place(x=10, y=50)
pic_sec_frame = LabelFrame(main_frame, width=90, height=90)
pic_sec_frame.place(x=560, y=50)

check_frame = LabelFrame(main_frame, text='Check list',font=('Times', 14),
                                 fg='white', bg='darkred', bd=6, relief=GROOVE)
check_frame.place(x=0, y=250, width=660, height=400)

logo = ImageTk.PhotoImage(Image.open('image_flags/icbc.png').resize((150,50), Image.BILINEAR))
logo_lbl = Label(logo_frame, image=logo, bd=4, relief=RIDGE)
logo_lbl.place(x=0, y=0)


def time():
    string = strftime('%H:%M:%S %p')
    data_lbl.config(text=string)
    data_lbl.after(1000, time)

data = Label(main_frame, text='Data:', font=('Times', 18, 'bold'), fg='darkgreen')
data.place(x=180, y=155)

data_lbl = Label(main_frame, font=('Times', 16, 'bold'), fg='darkgreen', width=18)
data_lbl.place(x=250, y=155)
time()


IRR= 42032.50,   
TMT= 3.51,        
INR= 83.01, 
EGP= 30.90,       
JPY= 150.28,
AUD= 1.53, 
GBP= 0.79, 
ARS= 834.55,      
PKR= 278.59,      
BRL= 278.59, 
EUR= 0.93, 
EUR= 0.93, 
CAD= 1.35, 
EUR= 0.93, 
MYR= 4.78,
SGD= 1.35, 
CNH= 7.22,        
RUB= 92.28, 
TRY= 30.82, 
KZT= 447.64,       
SAR= 3.75,        
AED= 3.67,        
UZS= 12311.42,    
KGS= 89.43




def clear():
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    data_entry.delete(0, END)

def convertation():
    second_entry.delete(0, END)
    if first_combo.selection_get() == 'Iran IRR':
        ex1 = f'{int(first_entry.get()) * 42032.50}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Turkmenistan TMT':
        ex1 = f'{int(first_entry.get()) * 3.51}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'India INR':
        ex1 = f'{int(first_entry.get()) * 83.01}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Egipt EGP':
        ex1 = f'{int(first_entry.get()) * 30.90}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Japan JPY':
        ex1 = f'{int(first_entry.get()) * 150.28}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Australia AUD':
        ex1 = f'{int(first_entry.get()) * 1.53}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'England GBP':
        ex1 = f'{int(first_entry.get()) * 0.79}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Argentina ARS':
        ex1 = f'{int(first_entry.get()) * 834.55}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Pakistan PKR':
        ex1 = f'{int(first_entry.get()) * 278.59}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Brazil BRL':
        ex1 = f'{int(first_entry.get()) * 278.59}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'France EUR':
        ex1 = f'{int(first_entry.get()) * 0.93}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Italy EUR':
        ex1 = f'{int(first_entry.get()) * 0.93}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Canada CAD':
        ex1 = f'{int(first_entry.get()) * 1.35}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Spain EUR':
        ex1 = f'{int(first_entry.get()) * 0.93}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Malazia MYR':
        ex1 = f'{int(first_entry.get()) * 4.78}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Singapur SGD':
        ex1 = f'{int(first_entry.get()) * 1.35}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'China CNH':
        ex1 = f'{int(first_entry.get()) * 7.22}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Russia RUB':
        ex1 = f'{int(first_entry.get()) * 92.28}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Turkey TRY':
        ex1 = f'{int(first_entry.get()) * 30.82}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Kazagistan KZT':
        ex1 = f'{int(first_entry.get()) * 447.64}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Saud Arabystan SAR':
        ex1 = f'{int(first_entry.get()) * 3.75}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'UEA - AED':
        ex1 = f'{int(first_entry.get()) * 3.67}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Uzbekistan UZS':
        ex1 = f'{int(first_entry.get()) * 12311.42}'
        second_entry.insert(END, ex1)
    if first_combo.selection_get() == 'Gyrgyzystan KGS':
        ex1 = f'{int(first_entry.get()) * 89.43}'
        second_entry.insert(END, ex1)

def add_bill():
    inf_text.insert(END, f'\t\t\t Your information here:\n')
    inf_text.insert(END, f' Country: \t {first_combo.get()}\t{first_entry.get()}\n')
    inf_text.insert(END, f' Convertation country: \t USD \t{second_entry.get()}\n')
    inf_text.insert(END, f'====================================================\n')



country_name = ('Iran IRR', 'Turkmenistan TMT', 'India INR', 'Egipt EGP', 'Japan JPY',
                'Australia AUD', 'England GBP', 'Argentina ARS', 'Pakistan PKR',
                'Brazil BRL', 'France EUR', 'Italy EUR', 'Canada CAD', 'Spain EUR', 'Malazia MYR',
                'Singapur SGD', 'China CNH', 'Russia RUB', 'Turkey TRY', 'Kazagistan KZT', 
                'Saud Arabystan SAR', 'UEA - AED', 'Uzbekistan UZS', 'Gyrgyzystan KGS')

country_pic = ('iran.webp', 'turkmenistan.png', 'india.png', 'egipt.png', 'japan.png',
                'australia.jpeg', 'eng.png', 'argentina.jpeg', 'pakistan.webp',
                'brazil.webp', 'france.png', 'italy.png', 'kanada.jpeg', 'spain.png', 'malazia.webp',
                'singapur.png', 'china.jpg', 'russia.png', 'turkey.png', 'kazak.jpeg', 
                'saudi_arabia.webp', 'uea.png', 'uzbekistan.jpeg', 'kirgizistan.png')


# ==============   FIRST   ==============

def sel_first_country(e):
    global img_country
    country_index = first_combo.current()

    if os.path.exists(f'image_flags/{country_pic[country_index]}'):
        img_country = ImageTk.PhotoImage(Image.open(f'image_flags/{country_pic[country_index]}').resize((80,80), Image.BILINEAR))
    else:
        img_country = ImageTk.PhotoImage(Image.open(f'image_flags/logo.jpeg').resize((80,80), Image.BILINEAR))

    main.config(image = img_country)


phot_main = ImageTk.PhotoImage(Image.open('image_flags/logo.jpeg').resize((80,80), Image.BILINEAR))
main = Label(pic_main_frame, image=phot_main, bd=4, relief=RIDGE)
main.place(x=0, y=0)


first_combo = ttk.Combobox(main_frame, values=country_name, font=('Times', 16, 'bold'), foreground='saddlebrown',
                           background='white', width=16)
first_combo.current(0)
first_combo.bind('<<ComboboxSelected>>', sel_first_country)
first_combo.place(x=120, y=65)

first_entry = Entry(main_frame, font=('Times', 16, 'bold'), width=18)
first_entry.place(x=120, y=100)

# ==============   SECOND   ==============

photo_main = ImageTk.PhotoImage(Image.open('image_flags/usd.png').resize((80,80), Image.BILINEAR))
main_two = Label(pic_sec_frame, image=photo_main, bd=4, relief=RIDGE)
main_two.place(x=0, y=0)

second_lbl = Label(main_frame, text='USD', font=('Times', 18, 'bold'), fg='saddlebrown', bg='white', width=15)
second_lbl.place(x=340, y=65)

second_entry = Entry(main_frame, font=('Times', 16, 'bold'), width=19)
second_entry.place(x=340, y=100)

# ============== data + button ==============



btn_clear = Button(main_frame, text='CLEAR', font=('Times', 18, 'bold'), fg='darkgreen', command=clear, width=12)
btn_clear.place(x=50, y=200)

btn_Bill = Button(main_frame, text='BILL', command=add_bill, font=('Times', 18, 'bold'), fg='darkgreen', width=12)
btn_Bill.place(x=250, y=200)

btn_convert = Button(main_frame, text='CONVERT', font=('Times', 18, 'bold'), fg='darkgreen', command=convertation, width=12)
btn_convert.place(x=450, y=200)

# ============== information save ==============


y_scroll = Scrollbar(check_frame, orient=VERTICAL)
inf_text = Text(check_frame, font=('Times', 16, 'bold'), bg='white', 
                             fg='green', yscrollcommand=y_scroll.set)
y_scroll.config(command=inf_text.yview)
y_scroll.pack(side=RIGHT, fill=Y)
inf_text.pack(fill=BOTH, expand= TRUE)


win.mainloop()