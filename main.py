from fasthtml.common import *
from itens import mostrarItens, controleItensObs
from formulario import formularioObs
from procurarCliente import procurarCliente
from listarObs import listarObs
from verObs import visualizarObs

app,rt = fast_app()

class Cliente:
    def __init__(self, nome: str, codigo: int):
        self.nome = nome
        self.codigo = codigo

cliente1 = Cliente(codigo=1, nome='cliente teste')

clientes = [cliente1]

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


@rt('/')
def get(): return listarObs()


@rt('/adicionaritem')
def adicionarItem(number: int):
    for i in itens:
        if i.codigo == number:
            itens.append(i)
            return mostrarItens()
    return mostrarItens()

@rt('/removerItem/{number}')
def removerItem(number: int):
    for i in itens:
        if i.codigo == number:
            itens.remove(i)
            return mostrarItens()
    return mostrarItens()

@rt('/criarobs')
def criarObs(codigoCliente: int):
    for i in clientes:
        if i.codigo == codigoCliente:
            return formularioObs(i)
    return procurarCliente()

@rt('/visualizarObs/{obsCodigo}')
def visualizarObs(obsCodigo: int):
    for i in obs:
        if i.codigo == obsCodigo:
            return visualizarObs(i)
    return listarObs()

serve()