import tkinter as t

window = t.Tk()

label1 = t.Label(window, text="Label 1")
label2 = t.Label(window, text="Label 2")

tombol1 = t.Button(window, text="Tombol 1")
tombol2 = t.Button(window, text="Tombol 2")

# Method Potitioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
window.mainloop()
