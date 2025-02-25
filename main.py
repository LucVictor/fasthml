from fasthtml.common import *
from itens import mostrarItens, controleItensObs
from formulario import formularioObs
from procurarCliente import procurarCliente
from listarObs import listarObs
from verObs import visualizarObs
from topbar import topbar
from layout import layout
from bancodedados import *
from cadastrarPessoas import formularioCadastrarPessoa
from listarPessoas import listarPessoas

app,rt = fast_app()




@rt('/')
def get(): return layout()


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
    cliente = Clientes.get(Clientes.codigo == codigoCliente)
    pessoas = Pessoas.select()
    if cliente:
        return formularioObs(cliente, pessoas)
    return procurarCliente()

@rt('/cadastrarobs')
def cadastrarobs(codigoCliente: int, cliente: str, motorista: str, solicitante: str, picote: str, data: str):
    print(codigoCliente)
    return '1'


@rt('/pessoas')
def pessoas():
    listagem = Pessoas.select()
    return layout(listarPessoas(listagem))

@rt('/cadastrarpessoas')
def cadastrarPessoas():
    return layout(formularioCadastrarPessoa())

@rt('/cadastrarpessoa')
def cadastrarPessoa(nomePessoa: str, cargoPessoa: str):
    nova_pessoa = Pessoas(nome=nomePessoa, cargo=cargoPessoa)
    nova_pessoa.save()
    return formularioCadastrarPessoa()

@rt('/deletarpessoa/{pessoaID}')
def deletarpessoa(pessoaID: int):
    pessoa = Pessoas.get(Pessoas.id==pessoaID)
    if pessoa:
        pessoa.delete_instance()
        listagem = Pessoas.select()
        return listarPessoas(listagem)
    return 'error'

@rt('/procurarcliente')
def procurarcliente():
    return layout(procurarCliente())

@rt('/verobs/{codigoobs}')
def verobs(codigoobs: int):
    obs = Obs.get(Obs.codigo == codigoobs)
    if obs:
        return visualizarObs(obs)
    return listarObs()

@rt('/listaobs')
def listaObs():
    listagem = Obs.select()
    return layout(listarObs(listagem))

serve()