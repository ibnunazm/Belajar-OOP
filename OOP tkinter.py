import tkinter
main_window = tkinter.Tk()
label1 = tkinter.Label(main_window, text="Label1")
label2 = tkinter.Label(main_window, text="Label2")

tombol1 = tkinter.Button(main_window, text="Tombol1")
tombol2 = tkinter.Button(main_window, text="Tombol2")

#method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method menampilkan GUI
main_window.mainloop()