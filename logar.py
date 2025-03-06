from fasthtml.common import *

def loginPagina():
    return Div(Card(
        Form(method="post", action="/logar")(Fieldset(Label('Usuário'), Input(type='text', name='usuario'), 
        Label('Senha'), Input(type='password', name='senha'), Button('Logar', type='submit')))
        ), style='display:flex; margin:0 auto ;justify-content: center; transform: translateY(+50%); margin: 0 ; width: 100%, height: 100%')