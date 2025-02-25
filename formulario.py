from fasthtml.common import *

def formularioObs(cliente, pessoas):
    return Div(Form(method="post", action=f"/cadastrarobs/", hx_post='/cadastrarobs/')(
        Fieldset(
            Label('Cod. Cliente', Input(type="text", value=f'{cliente.codigo}', name='codigoCliente')),
            Label('Cliente', Input(type="text", value=f'{cliente.nome}'), name='cliente'),
            Label("Motorista", *[Select(Option(pessoa.nome), value=f'{pessoa.nome}', name='motorista' ) for pessoa in pessoas]),
            Label("Solicitante", *[Select(Option(pessoa.nome), value=f'{pessoa.nome}', name='solicitante') for pessoa in pessoas]),
            Label("Picotes preso?", Select(Option('Sim'), Option('Não'), name='picote')),
            Label('Data da ocorrência', Input(type='date', name='data'))

        ),
        Button("Criar", type="submit"), style='margin: 0 auto; text-align: center;'
), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;')