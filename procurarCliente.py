from fasthtml.common import *

def procurarCliente():
    return Div(Form(method="post", action="/criarobs", id='tela', hx_post='/criarobs', hx_target='#tela', hx_swap='InnerHTML')(
        Fieldset(Label('Código do Cliente:', style='font-size'), Input(name='codigoCliente', type="numeric", inputmode="numeric", pattern="[0-9]*", size="5", style='text-align: center; width: 150px;'), 
        Button('Procurar',type='submit', style='width: 120px;' ), style="display: flex; flex-direction: column; align-items: center;"),
        ), style='margin: 0 auto; text-align: center;')




