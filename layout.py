from fasthtml.common import *
from topbar import topbar

def layout(conteudo=''):
    if conteudo:
        return Div(Div(topbar(), style='width: 95%; margin: 0 auto;'), Div(conteudo, id='conteudo', style='width: 90%; margin: 0 auto;'), style='width: 100%;', id='layout')
    return Div(Div(topbar()), Div(id='conteudo'))