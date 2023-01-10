import tkinter as tk
import datetime as dt
from tkinter import ttk

#https://www.youtube.com/watch?v=TXlkiMIBlTM
janela = tk.Tk()
#Titulo
janela.title('Serviços salão')
#==========================================
label_descricao = tk.Label(text="Entre com os dados:")
label_descricao.grid(row=1, column=0,padx=10,pady=10, stick='nswe',columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0,padx=10,pady=10, stick='nswe',columnspan=4)

janela.mainloop()

