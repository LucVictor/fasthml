from fasthtml.common import *

def topbar():
    return Div(Img(src='https://caicofrios.com.br/wp-content/uploads/2023/12/logo-caico.jpeg', width='60px', style='  background-image: none;'), 
    Div(botaoMenu('Ver OBS','listaobs'), botaoMenu('Criar OBS','procurarcliente'), botaoMenu('Procurar OBS','procurarobs'), style='display: flex; align-items: center;'), style="display: flex; justify-content: space-between")

def botaoMenu(nome, link):
    return Button(A(nome, style='text-decoration: none; color: white;', href=f'/{link}'), style='margin-right: 5px;')
