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
def adicionarItem(codigodoproduto: int, codigoobs: int, quantidade: int, status: str, motivo: str):
    produto = Produto.get(Produto.codigo == codigodoproduto)
    novo_item = Itens(nome = produto.nome, codigoObs= codigoobs, quantidade=quantidade, status=status, motivo=motivo )
    novo_item.save()
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    return mostrarItens(itens_lista)

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

@rt('/cadastrarobs/')
def cadastrarobs(motorista:str, codigoCliente:int, picote:str, data:str, solicitante:str, numeroPedido:int ):
    procurar_cliente = Clientes.get(Clientes.codigo == codigoCliente)
    nova_obs = Obs(data = data, cliente=procurar_cliente.nome, codigoCliente=codigoCliente, picote=picote, status=False, 
    solicitante=solicitante, motorista=motorista, numeroPedido=numeroPedido, usuario='teste', ultimaAtualizacao=data)
    nova_obs.save()
    return Redirect("/listaobs")


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
    codigocliente = obs.codigoCliente
    cliente = Clientes.get(Clientes.codigo == codigocliente)
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    if obs:
        return visualizarObs(obs, cliente, itens_lista)
    return listarObs()

@rt('/listaobs')
def listaObs():
    listagem = Obs.select()
    return layout(listarObs(listagem))

serve(port=5000)