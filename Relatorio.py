#video referecia:https://www.youtube.com/watch?v=TXlkiMIBlTM
import tkinter as tk
import datetime as dt
from tkinter import ttk


lista_tipos=["Corte","Unha","Mechas"]

janela = tk.Tk()
def center(win):
    # Parametro para deixar a janela no centro da tela

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # Definir a dimensão da janela usando largura (width) e altura (height)
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()

janela.minsize(280,200)

#Função para abrir no meio da janela
center(janela)
#Titulo
janela.title('Serviços salão')
#================================== Conteúdo programa ===================================
label_descricao = tk.Label(text="Entre com os dados:")
label_descricao.grid(row=1, column=0,padx=10,pady=10, stick='nswe',columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0,padx=10,pady=10, stick='nswe',columnspan=4)

label_tipdo_servico = tk.Label(text="Tipo do serviço")
label_tipdo_servico.grid(row=3, column=0,padx=10,pady=10, stick='nswe',columnspan=2)

entry_servicos = ttk.Combobox(values=lista_tipos)
entry_servicos.grid(row=3, column=2,padx=10,pady=10, stick='nswe',columnspan=2)

label_vezes=tk.Label(text="Servicos feitos")
label_vezes.grid(row=4, column=0,padx=10,pady=10, stick='nswe',columnspan=2)

entry_vezes = tk.Entry()
entry_vezes.grid(row=4, column=2,padx=10,pady=10, stick='nswe',columnspan=2)

botao_confirmar = tk.Button(text="Confirmar")
botao_confirmar.grid(row=5, column=0,padx=10,pady=10, stick='nswe',columnspan=4)




janela.mainloop()


