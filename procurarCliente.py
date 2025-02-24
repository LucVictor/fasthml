from fasthtml.common import *



def procurarCliente():
    return Div(Form(method="post", action="/criarobs", id='tela', hx_post='/criarobs', hx_target='#tela', hx_swap='InnerHTML')(
        Fieldset(
            Label('Cliente', Input(name='codigoCliente',type="number"), Button('Procurar',type='submit')),
        ), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;'))