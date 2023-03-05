import tkinter as tk 

window = tk.Tk()

window.geometry('1100x400')
window.title('Mi fisrt python windows')

label = tk.Label(window, text='Hello World', font=('Arial', 18))
label.pack(padx=20 , pady=20)

textbox = tk.Text(window, height=3 ,font=('Arial', 14))
textbox.pack(padx=10)

button = tk.Button(window, text='Click', font=('Arial', 10))
button.pack(padx=10, pady=10)


buttonframa = tk.Frame(window)
buttonframa.columnconfigure(0, weight=1)
buttonframa.columnconfigure(1, weight=1)
buttonframa.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframa, text='1', font=('Arial',18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
btn2 = tk.Button(buttonframa, text='2', font=('Arial',18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)
btn3 = tk.Button(buttonframa, text='3', font=('Arial',18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)
btn4 = tk.Button(buttonframa, text='4', font=('Arial',18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)
btn5 = tk.Button(buttonframa, text='5', font=('Arial',18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
btn6 = tk.Button(buttonframa, text='6', font=('Arial',18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
btn7 = tk.Button(buttonframa, text='7', font=('Arial',18))
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)
btn8 = tk.Button(buttonframa, text='8', font=('Arial',18))
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)
btn9 = tk.Button(buttonframa, text='9', font=('Arial',18))
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)
btn0 = tk.Button(buttonframa, text='0', font=('Arial',18))
btn0.grid(row=3, column=1, sticky=tk.W +tk.E)

buttonframa.pack(fill='x')
window.mainloop()