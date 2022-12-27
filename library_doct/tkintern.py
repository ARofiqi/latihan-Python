import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(background="white")
window.geometry("500x200")
window.resizable(False,False)
window.title("My App")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    print(NAMA_DEPAN.get(),NAMA_BELAKANG.get())
    pesan = "Hallo,",NAMA_DEPAN.get(),NAMA_BELAKANG.get()
    showinfo(title="Hallo",message=pesan)

# frame input
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=20,pady=10,fill="x",expand=True)

# komponen komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. nama depan entry
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama Belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. nama belakang entry
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()