from fasthtml.common import *
from itens import mostrarItens_obs
def emoji(a):
    if a == False:
        return Option('Pendente ⚠️', value='False'), Option('Concluído ✅', value='True')
    else:
        return Option('Concluído ✅', value='True'), Option('Pendente ⚠️', value='False')



def visualizarObs(obs, cliente, itensObs):
    return Div(H2("Visualizar OBS"), Form(method="post", action="/profile")(
        Fieldset(
            Label('Razão:', Input(type="text", value=f'{cliente.nome}', disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("Fantasia:", Input(type="text", value=f'{cliente.fantasia}',disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("Pedido:", Input(type="text", value=f'{obs.numeroPedido}', style='width: 20rem;' ,disabled=True), style="place-self: center"),
            Label('Data:', Input(type='date', value=f'{obs.data}', style='width: 20rem;'), style="place-self: center"),
            Label("Motorista:", Input(type="text", value=f'{obs.motorista}', style='width: 20rem;'), style="place-self: center"),
            Label("Solicitante:", Input(type="text", value=f'{obs.solicitante}', style='width: 20rem; '), style="place-self: center"),
            Label("Status:", Select(emoji(obs.status), id="status", style='width: 10rem;' ), style="grid-column: 2 ;place-self: center"), Div(mostrarItens_obs(itensObs), style="grid-column: 2; grid-row: 4; place-self: center"),
            Button("Salvar", type="submit", style='place-self: center; grid-column: 2; grid-row: 6; width: 160px;'), style="border: white solid; display: grid; grid-template-columns: repeat(3, 2fr); gap: 20px; align-items: center;")
            ), style="""
                display: flex-inline;
                justify-content: center;   /* 🎯 Centraliza horizontalmente */
                align-items: center;
                width: 100%;     /* 🏗️ Centraliza verticalmente */
                margin: 0 auto;
                text-align: center;            /* 📏 Ocupa altura total da tela */
            """)
          