from fasthtml.common import *

def botaoMenu(nome, link):
    return Button(A(nome, style='text-decoration: none; color: white;', href=f'/{link}'), style='margin-right: 5px;')

def listarPessoas(pessoas):
    return  Div(botaoMenu('Cadastrar Pessoa', 'cadastrarpessoas'), Table(
        Thead(
            Tr( Th("Nome"),
                Th("Cargo")
            )
        ),
        Tbody(
            *[Tr(Td(pessoa.nome), Td(pessoa.cargo),
            Td(Div(Form(method="get", action=f"/deletarpessoa/{pessoa.id}", id='tela', hx_get=f'/deletarpessoa/{pessoa.id}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Fieldset(
            Label(Button('Excluir',type='submit')),
        ))))) for pessoa in pessoas]
        ),
        cls="striped"
    ), id='listarobs',  style='text-align: center;')