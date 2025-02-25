from fasthtml.common import *

def formularioCadastrarPessoa():
        return Div(Form(method="post", action="/cadastrarpessoa", id='tela', hx_post='/cadastrarpessoa', hx_target='#conteudo', hx_swap='InnerHTML')(
        Fieldset(Label('Nome da Pessoa:', style='font-size'), 
        Input(name='nomePessoa', type="text", style='text-align: center; width: 200px;'), 
        Label('Cargo:', style='font-size'), 
        Select(Option('Motorista', value='Motorista'), Option('Vendedor', value='Motorista'), Option('Encarregado', value='Encarregado'),  Option('Conferente', value='Conferente'), id="cargoPessoa", style='width: 140px; align-text: center;'  ),
        Button('Cadastrar',type='submit', style='width: 120px;' ), style="display: flex; flex-direction: column; align-items: center;"),
        ), style='margin: 0 auto; text-align: center;')