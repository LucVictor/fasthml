from fasthtml.common import *

def botaoMenu(nome, link):
    return Button(A(nome, style='text-decoration: none; color: white;', href=f'/{link}'), style='margin-right: 5px;')

def formularioCadastrarUsuario():
        return Div(H3('Gerenciar Usuários'), Form(method="post", action="/cadastrarusuario", id='tela', hx_post='/cadastrarusuario', hx_target='#listausuario', hx_swap='InnerHTML')(
        Fieldset(Label('Usuario:', style='font-size'), 
        Input(name='usuario', type="text", required=True, style='text-align: center; width: 200px;'), 
        Fieldset(Label('Senha:', style='font-size'), 
        Input(name='senha', type="password", required=True, style='text-align: center; width: 200px;'),
        Br(),
        Button('Cadastrar', type='submit',  style="width: 200px;"),
        ), style='margin: 0 auto; text-align: center;')), style="width: 500px;")

def listarUsuarios(usuarios):
    return  Card(formularioCadastrarUsuario(), Table(
        Thead(
            Tr( Th("Usuario", style='width: 100px; text-align: center;'),
               Th("Ações", style='width: 100px; text-align: center;')
            )
        ),
        Tbody(
            *[Tr(Td(usuario.usuario, style='text-align: center;'),
            Td(Div(Form(method="get", action=f"/deletarusuario/{usuario.id}", id='tela', hx_get=f'/deletarusuario/{usuario.id}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Fieldset(
            Label(Button('Excluir',type='submit', style='width: 100px;; margin-top: 1rem')), style='text-align: center; align-items: center'
        ))))) for usuario in usuarios]
        ),
        cls="striped"
    ), id='listausuario',  style='text-align: center; width: 500px; margin: 0 auto;')