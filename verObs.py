from fasthtml.common import *
from bancodedados import Obs, Itens, Pessoas, Clientes
from itens import mostrarItens_obs
from gerenciaritens import botaoGerenciarItens


def emoji(a):
    if a == False:
        return Option('Pendente ⚠️', value='False'), Option('Concluído ✅', value='True')
    else:
        return Option('Concluído ✅', value='True'), Option('Pendente ⚠️', value='False')

def formatarData(a):
    return a.strftime("%d/%m/%Y")



def visualizarObs(codigoobs):
    obs = Obs.get(Obs.codigo == codigoobs)
    codigocliente = obs.codigoCliente
    cliente = Clientes.get(Clientes.codigo == codigocliente)
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    return Div(H2("Visualizar OBS"), Form(method="post", action="/editarobs/")(
        Fieldset(
            Label('Razão:',  Br(), Input(type="text", value=f'{cliente.nome}', disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("Fantasia: ", Br(), Input(type="text", value=f'{cliente.fantasia}',disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("CNPJ: ",  Br(), Input(type="text", value=f'{cliente.cnpj}',disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("Endereço: ",  Br(), Input(type="text", value=f'{cliente.rua} - {cliente.numero} {cliente.bairro}/{cliente.cidade}',disabled=True, style='width: 20rem;'), style="place-self: center"),
            Label("Pedido: ", Br(), Input(type="text", value=f'{obs.numeroPedido}', style='width: 20rem;', disabled=True), style="place-self: center"),
            Label('Data: ',  Br(), Input(type='date', value=f'{obs.data}', style='width: 20rem;', disabled=True), style="place-self: center"),
            Label("Motorista: ",  Br(), Input(type="text", value=f'{obs.motorista}', style='width: 20rem;', disabled=True), style="place-self: center"),
            Label("Solicitante: ",  Br(), Input(type="text", value=f'{obs.solicitante}', style='width: 20rem; ', disabled=True), style="place-self: center"),
            Label("Status: ",  Br(), Select(emoji(obs.status), name="status",id="status", style='width: 10rem;' ), style="grid-column: 1 ; grid-row: 4 ;place-self: center"),
            Label('Usuário:', Br(), Input(type='text', value=f"{obs.usuario}", disabled=True), style="grid-column: 3 ; grid-row: 3;place-self: center"),
            Div(mostrarItens_obs(itens_lista), botaoGerenciarItens(codigoobs), style="display: inline; grid-column: 2; grid-row: 4; place-self: center"),
            Button("Salvar", type="submit", style='place-self: center; grid-column: 2; grid-row: 6; width: 160px;'),
            Input(value=f'{obs.codigo}', name="codigoobs", style='display: none;'),

              style="border: white solid; display: grid; grid-template-columns: repeat(3, 2fr); gap: 20px; align-items: center;")
            ), style="""
                display: flex-inline;
                justify-content: center;
                align-items: center;
                width: 100%;
                margin: 0 auto;
                text-align: center;
            """)

def obsImpressao(codigoobs):
    obs = Obs.get(Obs.codigo == codigoobs)
    codigocliente = obs.codigoCliente
    cliente = Clientes.get(Clientes.codigo == codigocliente)
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    return Div(H2("OBS"),Img(src="https://caicomatriz.lucascoding.com.br/static/imagens/logo.png", width="120px", style="padding-bottom: 10px"), Form(method="post", action="/profile")(
        Fieldset(
            Label('Razão:',  Br(), f'{cliente.nome}', style="padding: 5px;  place-self: center"),
            Label("Fantasia: ", Br(), f'{cliente.fantasia}', style="padding: 5px;  place-self: center"),
            Label("CNPJ: ",  Br(), f'{cliente.cnpj}', style="padding: 5px;  place-self: center"),
            Label("Endereço: ",  Br(), f'{cliente.rua} - {cliente.numero} {cliente.bairro}/{cliente.cidade}', style="padding: 5px;  place-self: center"),
            Label("Pedido: ", Br(), f'{obs.numeroPedido}', style="padding: 5px;  place-self: center"),
            Label('Data: ',  Br(), f'{formatarData(obs.data)}', style="padding-top: 20px ;padding: 5px;  place-self: center"),
            Label("Recolher Picote? ", Div(f"{obs.picote}", style="font-weight: bold"), style="  grid-column: 1/ span 2 ;place-self: center", name='solicitante'), 
            Br(),
            Div(mostrarItens_obs(itens_lista), style="display: inline; grid-column: 1 / span 2; grid-row: 5 ; place-self: center"),
            Br(),
            Div(H4("Entregue em: _____/_____/_____"), style="padding-top: 20px ; grid-column: 1 / span 2; grid-row: 6 ; place-self: center"),
              style="text-size: 12px; display: grid; grid-template-columns: repeat(30px, 30px); align-items: center;")
            ), style="""
                display: flex-inline;
                justify-content: center;
                align-items: center;
                width: 100%;
                margin: 0 auto;
                text-align: center;
                
            """)