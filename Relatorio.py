#video referecia:https://www.youtube.com/watch?v=TXlkiMIBlTM
#youtube.com/watch?v=Av1fItUacgQ
#Tentando fazer um programa para o salão de um amigo
import tkinter as tk
import datetime as dt
from tkinter import ttk
import pandas as pd
import win32com.client as win32

clientes_excel = pd.read_excel('Salao.xlsx', engine='openpyxl')

#Lista para o combobox (Testando sem banco de dados)
lista_tipos=["Corte","Unha","Mechas"]
lista_tipo_pagamento=["Dinheio","Pix","Credito","Debito"]
lista_dados=[]

janela = tk.Tk()
def center(win):
    win.update_idletasks()
    # Definir a dimensão da janela usando largura (width) e altura (height)
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width


    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2


    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    win.deiconify()

def inserindo_dados():
    cliente = entry_cliente.get() #Pegando informação na entrada cliente
    servicos = entry_servicos.get() #Pegando informação na combobox servicos
    pagamento = entry_tipo_pagamento.get() #Pegando informação na combobox tipo de pagamento

    data_servico = dt.datetime.now()  #Chamando o metodo do dia atual
    data_servico = data_servico.strftime("%d/%m/%Y %H:%M") #Metodo para editar o dia da maneira correta ex: dia/mes/ano hora:minuto

    dados = clientes_excel.shape[0] + len(lista_dados)+1
    dados_str = "DAD-{}".format(dados)
    lista_dados.append((dados_str, cliente, servicos, pagamento, data_servico))







#Tamaho tela (Depende do que você está fazendo recomendo ir testando
janela.minsize(300,210)
#Função para abrir no meio da janela
center(janela)
#Titulo
janela.title('Serviços salão')


#================================== Conteúdo programa ===================================
#Titulo
label_descricao = tk.Label(text="Salão William")
label_descricao.grid(row=1, column=0,padx=10,pady=10, stick='nswe',columnspan=4)

#Titulo cliente
label_cliente = tk.Label(text="Cliente")
label_cliente.grid(row=2, column=0,padx=10,pady=10, stick='nswe',columnspan=2)

#Entrada cliente
entry_cliente = tk.Entry()
entry_cliente.grid(row=2, column=2,padx=10,pady=10, stick='nswe',columnspan=2)

#Titulos Serviços
label_tipdo_servico = tk.Label(text="Tipo do serviço")
label_tipdo_servico.grid(row=3, column=0,padx=10,pady=10, stick='nswe',columnspan=2)

#Combobox serviços
entry_servicos = ttk.Combobox(values=lista_tipos) #Lista criada no início
entry_servicos.grid(row=3, column=2,padx=10,pady=10, stick='nswe',columnspan=2)

#Titulo Pagamento
label_tipo_pagamento = tk.Label(text="Tipo de pagamento")
label_tipo_pagamento.grid(row=4, column=0,padx=10,pady=10, stick='nswe',columnspan=2)

#Combobox tipo de pagamento
entry_tipo_pagamento = ttk.Combobox(values=lista_tipo_pagamento) #Lista criada no início
entry_tipo_pagamento.grid(row=4, column=2,padx=10,pady=10, stick='nswe',columnspan=2)


botao_confirmar = tk.Button(text="Confirmar", command=inserindo_dados)
botao_confirmar.grid(row=5, column=0,padx=10,pady=10, stick='nswe',columnspan=4)




janela.mainloop()

novo_clientes_excel = pd.DataFrame(lista_dados, columns=['Codigo','Data','Cliente','Serviços','Tipo de pagamento'])
clientes_excel = clientes_excel.append(novo_clientes_excel, ignore_index=True)
clientes_excel.to_excel('Salao.xlsx', index=False)
print(lista_dados)
