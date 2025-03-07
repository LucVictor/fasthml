from fasthtml.common import *

def loginPagina():
    return Div(Img(src='https://caicofrios.com.br/wp-content/uploads/2023/12/logo-caico.jpeg', style='height: 285px;'),Card(
        Form(method="post", action="/logar")(Fieldset(Label('Usuário:'), Input(type='text', name='usuario'), 
        Label('Senha:'), Input(type='password', name='senha'), Button('Logar', type='submit')))
        ,style='height: 285px;'), style='display:flex; margin:0 auto ;justify-content: center; transform: translateY(+50%); margin: 0 ; width: 100%, height: 100%')