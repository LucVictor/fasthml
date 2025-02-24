from fasthtml.common import *

class Obs:
    def __init__(self, data, cliente: str, codigo: int, status: str, itens: str, solicitante: str, motorista: str):
        self.data = data
        self.codigo = codigo
        self.status = status
        self.cliente = cliente
        self.itens = itens
        self.solicitante = solicitante
        self.motorista = motorista

obs1 = Obs(data='24/02/2025', status='Pedente', cliente='Cliente teste', codigo= 1, itens='Item de teste', solicitante='soliciante teste', motorista='teste')

obs=[obs1]

def listarObs():
    return Div(Table(
        Thead(
            Tr( Th("Data"),
                Th("Data"),
                Th("Cliente"),
                Th("Status"),
                Th("Ação")
            )
        ),
        Tbody(
            *[Tr(Td(obs.data), Td(obs.cliente), Td(obs.status), Td(Form(method="get", hx_get=f"/visualizarObs/{obs.codigo}", hx_target='#listarobss', hx_swap='innerHTML'), 
            Button('Abrir', type='submit'))) for obs in obs]
        ),
        cls="striped"
    ), id='listarobss')
