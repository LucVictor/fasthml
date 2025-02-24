from fasthtml.common import *

def formularioObs(cliente):
    return Div(Form(method="post", action="/profile")(
        Fieldset(
            Label('Cliente', Input(type="text", value=f'{cliente.nome}')),
            Label("Motorista", Input(type="text")),
            Label("Solicitante", Input(type="text")),
            Label("Picotes preso?", Select(Option('Sim'), Option('Não') )),
            Label('Data da ocorrência', Input(type='date'))

        ),
        Button("Criar", type="submit"), style='margin: 0 auto; text-align: center;'
), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;')