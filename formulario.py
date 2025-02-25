from fasthtml.common import *

def formularioObs(cliente, pessoas):
    return Div(Form(method="post", action=f"/cadastrarobs", id='tela', hx_post=f'/cadastrarobs')(
        Fieldset(
            Label('Cod. Cliente', Input(type="text", value=f'{cliente.codigo}'), id='codigoCliente'),
            Label('Cliente', Input(type="text", value=f'{cliente.nome}'), id='cliente'),
            Label("Motorista", *[Select(Option(pessoa.nome), value=f'{pessoa.nome}') for pessoa in pessoas],id='motorista'),
            Label("Solicitante", *[Select(Option(pessoa.nome), value=f'{pessoa.nome}') for pessoa in pessoas], id='solicitante'),
            Label("Picotes preso?", Select(Option('Sim'), Option('Não'), id='picote')),
            Label('Data da ocorrência', Input(type='date'), id='data')

        ),
        Button("Criar", type="submit"), style='margin: 0 auto; text-align: center;'
), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;')