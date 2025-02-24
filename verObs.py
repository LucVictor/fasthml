from fasthtml.common import *



def visualizarObs(i):
    return Div(Form(method="post", action="/profile")(
        Fieldset(
            Label('Cliente', Input(type="text", value=f'{i.cliente}')),
            Label("Motorista", Input(type="text", value=f'{i.motorista}')),
            Label("Solicitante", Input(type="text", value=f'{i.soliciante}')),
            Label('Data da ocorrência', Input(type='date', value=f'{i.data}'))

        ),
        Button("Criar", type="submit"), style='margin: 0 auto; text-align: center;'
), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;')