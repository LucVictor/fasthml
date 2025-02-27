from fasthtml.common import *
from topbar import topbar

def layout(conteudo=''):
    if conteudo:
        return Div(Div(topbar(), cls="no-print"), Div(conteudo, id='conteudo', style='width: 90%; margin: 0 auto;'), style='', id='layout')
    return Div(Div(topbar()), Div(id='conteudo'))