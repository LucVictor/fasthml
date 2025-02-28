from fasthtml.common import *
from itens import mostrarItens
from formulario import formularioObs
from procurarCliente import procurarCliente
from listarObs import listarObs, filtrarObsStatus
from verObs import visualizarObs
from topbar import topbar
from layout import layout
from bancodedados import *
from cadastrarPessoas import formularioCadastrarPessoa
from listarPessoas import listarPessoas
from gerenciaritens import formAdicionarItens
from impressaoObs import impressaoObs
from procurarobs import formprocurarObs, listarObsFiltro
from index import home



app,rt = fast_app(live=True, hdrs=(Script(src="https://cdn.jsdelivr.net/npm/chart.js"),Style("""
        @media print {
            .no-print {
                display: none !important;
            }
        }
    """),))




@rt('/')
def get(): return layout(home())

@rt('/editarobs')
def editarObs(codigoobs: int, status: str):
    obs = Obs.get_by_id(codigoobs)
    obs.status = bool(status)
    obs.save()
    return Redirect("/listaobs")


@rt('/adicionaritem')
def adicionarItem(codigodoproduto: int, codigoobs: int, quantidade: int, status: str, motivo: str):
    produto = Produto.get(Produto.codigo == codigodoproduto)
    novo_item = Itens(nome = produto.nome, codigoObs= codigoobs, quantidade=quantidade, status=status, motivo=motivo )
    novo_item.save()
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    return mostrarItens(itens_lista)

@rt('/gerenciaritens/{codigoobs}')
def gerenciaritens(codigoobs: int):
    return formAdicionarItens(codigoobs)


@rt('/removerItem/{id}')
def removerItem(id: int):
    item = Itens.get(Itens.codigo == id)
    item.delete_instance()
    itens_lista= Itens.select().where(Itens.codigoObs == item.codigoObs)
    return mostrarItens(itens_lista)

@rt('/criarobs')
def criarObs(codigoCliente: int):
    cliente = Clientes.get(Clientes.codigo == codigoCliente)
    pessoas = Pessoas.select()
    if cliente:
        return formularioObs(cliente, pessoas)
    return procurarCliente()

@rt('/cadastrarobs/')
def cadastrarobs(motorista:str, Codigo_Cliente:int, picote:str, data:str, solicitante:str, numeroPedido:int ):
    print(motorista, Codigo_Cliente, picote, data, solicitante, numeroPedido)
    procurar_cliente = Clientes.get(Clientes.codigo == Codigo_Cliente)
    nova_obs = Obs(data = data, cliente=procurar_cliente.nome, codigoCliente=Codigo_Cliente, picote=picote, status=False, 
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
    return visualizarObs(codigoobs)

@rt('/listaobs')
def listaObs():
    pagina = 1
    por_pagina = 5
    offset = (pagina - 1) * por_pagina
    listagem = Obs.select().where(Obs.status==False).limit(por_pagina).offset(offset)
    return layout(Div( listarObs(listagem, pagina)))

@rt("/obs/{pagina}")
def listar_Clientes(pagina: int):
    por_pagina = 5
    offset = (pagina - 1) * por_pagina
    listagem = Obs.select().where(Obs.status==False).limit(por_pagina).offset(offset)
    return listarObs(listagem, pagina)


@rt('/filtrarobs/{opcao}')
def filtrarobs(opcao: str):
    match opcao:
        case 'Todos':
            filtro = Obs.select()
            return listarObs(filtro)
        case 'False':
            filtro = Obs.select().where(Obs.status==bool(False))
            return listarObs(filtro)
    filtro = Obs.select().where(Obs.status==bool(True))
    return listarObs(filtro)

@rt('/impressaoobs/{id}')
def imprimirobs(id: int): 
    return impressaoObs(id)

@rt('/procurarobs')
def procurarobs():
    return layout(formprocurarObs())

@rt('/resultadoprocurarobs')
def resultadoprocurarobs(codigodocliente: str, data: str, status: str):
    obs = Obs.select()
    if codigodocliente:
        obs = obs.select().where(Obs.codigoCliente==codigodocliente)
    if data:
        obs = obs.select().where(Obs.data==data)
    if status:
        match status:
            case 'False':
                obs = obs.select().where(Obs.status == False)
            case 'True':
                obs = obs.select().where(Obs.status == True)
    return listarObsFiltro(obs)




serve(port=5000)