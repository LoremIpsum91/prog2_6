import gspread
from tkinter import *
from datetime import datetime
from fpdf import FPDF

# подключаем таблицу
sa = gspread.service_account(filename='nth-suprstate-273909-a8b636151c70.json')
sh = sa.open('prog2_6_2')
wks = sh.worksheet('Sheet1')


def create_pdf(text, filename):
    font_size_mm = 14 * 0.5

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.add_page()

    for line in text:
        if len(line) == 0:
            pdf.ln()
        else:
            pdf.cell(0, font_size_mm, '   '.join(line), ln=1)

    pdf.output('pdfs/' + filename + '.pdf', 'F')


def final():
    wks.update_cell(1, 1, str(name.get()) + '    ' + str(datetime.now().date()))
    wks.update_cell(3, 2, int(mas.get())*int(speed.get())**2/2)
    wks.update_cell(4, 2, int(mas.get()))
    wks.update_cell(5, 2, int(speed.get()))
    create_pdf(wks.get_all_values(), str(datetime.now().date()) + '-' + str(name.get()))


# создаем графический интрефейс
root = Tk()
root['bg'] = '#2F4F4F'
root.geometry('1500x1500')

frame = Frame(root, bg='#293133', bd=5)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

label = Label(frame, text='Введите название файла:',
              bg='#293133',
              fg='white')
label.config(font=("Courier", 20))
label.pack()

name = Entry(frame, bg='white')
name.pack()

space = Frame(frame, bg='#293133', bd=5, width=10, height=50)
space.pack()

label = Label(frame, text='Введите значение %s:' % wks.cell(4, 3).value,
              bg='#293133',
              fg='white')
label.config(font=("Courier", 20))
label.pack()

mas = Entry(frame, bg='white')
mas.pack()

space = Frame(frame, bg='#293133', bd=5, width=10, height=50)
space.pack()

label = Label(frame, text='Введите значение %s:' % wks.cell(5, 3).value,
              bg='#293133',
              fg='white')
label.config(font=("Courier", 20))
label.pack()

speed = Entry(frame, bg='white')
speed.pack()

space = Frame(frame, bg='#293133', bd=5, width=10, height=50)
space.pack()

btn_result = Button(frame, text='Build', bg='yellow', command=final)
btn_result.pack()

root.mainloop()