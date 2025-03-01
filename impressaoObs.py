from fasthtml.common import *
from verObs import obsImpressao

def impressaoObs(id):
    return Div(Div(
        obsImpressao(id)
    ), style="""
    size: 21cm 29.7cm;
    margin: 3mm 4mm 3mm 4mm;""")



def botaoImpressaoObs(i):
    return Div(Form(method="get", id='tela', hx_get=f'/impressaoobs/{i}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Button('Imprimir',type='submit', style='width: 100px;' ), style="display: flex; flex-direction: column; align-items: center;")
        , style='margin: 0 auto; text-align: center;')