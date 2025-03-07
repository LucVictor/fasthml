from fasthtml.common import *

def formularioObs(cliente, pessoas):
    return Div(H3('Formulário de OBS'),Form(method="post", hx_post=f"/cadastrarobs")(
        Fieldset(
            Label('Cod. Cliente', Br(), Input(name='Codigo_Cliente', type="number", value=f'{cliente.codigo}', readonly=True, style='width: 20rem;text-align: center')),
            Label('Razão:',  Br(), Input(type="text", value=f'{cliente.nome}', readonly=True, style='width: 20rem;'), style="place-self: center"),
            Label("Fantasia: ", Br(), Input(type="text", value=f'{cliente.fantasia}',readonly=True, style='width: 20rem;'), style="place-self: center;text-align: center"),
            Label('Data: ',  Br(), Input(type='date', name="data", style='width: 20rem; ; text-align: center'), style="place-self: center"),
            Label("Motorista", Br(), Select(*[Option(pessoa.nome) for pessoa in pessoas if pessoa.cargo == "Motorista"], name='motorista', style='width: 20rem;text-align: center')),
            Label("Solicitante", Br(), Select(*[Option(pessoa.nome)  for pessoa in pessoas] , name='solicitante', style='width: 20rem;text-align: center')),
            Label("Número do Pedido: ", Br(), Input(type="number", name="numeroPedido", style='width: 20rem;'), style="place-self: center;text-align: center"),
            Label("Endereço: ",  Br(), Input(type="text", value=f'{cliente.rua} - {cliente.numero} {cliente.bairro}/{cliente.cidade}',readonly=True, style='width: 20rem;'), style="place-self: center"),
            Label("Recolher Picote?: ",  Br(), Select(Option('Sim'),Option('Não'), name='picote'), style="grid-column: 3 ;place-self: center"), 
            Button("Cadastrar OBS", type="submit", style="grid-column: 2 ;place-self: center"),
            style="text-align: center;border: white solid; display: grid; grid-template-columns: repeat(3, 2fr); gap: 20px; align-items: center;")))