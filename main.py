from fasthtml.common import *
from itens import mostrarItens, controleItensObs
from formulario import formularioObs
from procurarCliente import procurarCliente

app,rt = fast_app()

class Cliente:
    def __init__(self, nome: str, codigo: int):
        self.nome = nome
        self.codigo = codigo

cliente1 = Cliente(codigo=1, nome='cliente teste')

clientes = [cliente1]

@rt('/')
def get(): return procurarCliente()


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


serve()