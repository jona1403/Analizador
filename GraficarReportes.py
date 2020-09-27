from tkinter import Scale, Tk, Frame, Label
from tkinter.ttk import Notebook, Entry
import tkinter as tk
def Graficar_Reporte_Tokens_Y_Reporte_Errores(ListaTokens, ListaErrores):
    window = tk.Tk()
    window.title("Scale,Tabs,Table Example")
    scrollbar = tk.Scrollbar(window)
    c = tk.Canvas(window, background="grey", yscrollcommand = scrollbar.set)
    scrollbar.config(command= c.yview)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    window.geometry("1150x400")

    frame2 = tk.Frame(c)
    c.pack(side="left", fill= "both", expand=True)
    c.create_window(0 ,0 , window = frame2, anchor= "nw")
    tablayout = Notebook(frame2)
    tab1 = Frame(tablayout)
    tab1.pack(fill="both")
    for row in range(len(ListaTokens)):
        for column in range(5):
            if row == 0:
                label = Entry(tab1, text=str(column))
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            else:
                label = Entry(tab1, text="Row : " + str(row) + " , Column : " + str(column))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
    tablayout.add(tab1, text="Tabla Errores")
    tab1 = Frame(tablayout)
    tab1.pack(fill="both")
    COntadorColumnas = 0
    ContadorFilas = 0
    for row in range(len(ListaTokens)):
        COntadorColumnas = 0
        for column in range(5):
            if row == 0:
                label = Label(tab1, text=str(ListaTokens[0][COntadorColumnas]), bg="blue", fg="black", padx=3,pady=3)
                label.config(font=('Times New Roman', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            else:
                label = Label(tab1, text=str(ListaTokens[ContadorFilas][COntadorColumnas]), bg="white", fg="black",padx=3, pady=3)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            COntadorColumnas+=1
        ContadorFilas+=1
    tablayout.add(tab1, text="Tabla Tokens")
    tablayout.pack(fill="both")
    window.update()
    c.config(scrollregion = c.bbox("all"))
    window.mainloop()
