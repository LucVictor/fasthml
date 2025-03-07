from fasthtml.common import *
from itens import mostrarItens
from formulario import formularioObs
from procurarCliente import procurarCliente
from listarObs import listarObs, filtrarObsStatus
from verObs import visualizarObs
from topbar import topbar
from layout import layout
from bancodedados import Usuarios, Produto, Pessoas, Obs, Itens, Clientes
from cadastrarPessoas import formularioCadastrarPessoa
from listarPessoas import listarPessoas
from gerenciaritens import formAdicionarItens
from impressaoObs import impressaoObs
from procurarobs import formprocurarObs, listarObsFiltro
from index import home
from logar import loginPagina
from verificarUsuario import login_requerido
from listarUsuarios import listarUsuarios
import os



app,rt = fast_app(live=True, session=True,  hdrs=(Script(src="https://cdn.jsdelivr.net/npm/chart.js"),Style("""
        @media print {
            .no-print {
                display: none !important;
            }
        }
    """),))


@rt('/')
@login_requerido
def get(req: Request):
    return layout(home())

@rt('/editarobs')
def editarObs(codigoobs: int):
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
    solicitante=solicitante, motorista=motorista, numeroPedido=numeroPedido, usuario=req.session.get('usuario'), ultimaAtualizacao=data)
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

@rt('/usuarios')
def listarUsuario():
    usuarios = Usuarios.select()
    return layout(listarUsuarios(usuarios))


@rt('/cadastrarusuario')
def listarUsuario(usuario: str, senha: str):
    usuario = Usuarios(usuario = usuario, senha=senha)
    usuario.save()
    listagemusuarios = Usuarios.select()
    return listarUsuarios(listagemusuarios)


@rt('/deletarusuario/{id}')
def deletarusuario(id: int):
    print(id)
    usuario = Usuarios.get(Usuarios.id== id)
    usuario.delete_instance()
    listagemusuarios = Usuarios.select()
    return listarUsuarios(listagemusuarios)


@rt('/procurarcliente')
@login_requerido
def procurarcliente(req: Request):
    return layout(procurarCliente())

@rt('/verobs/{codigoobs}')
def verobs(codigoobs: int):
    return visualizarObs(codigoobs)

@rt('/listaobs')
@login_requerido
def listaObs(req: Request):
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
@login_requerido
def procurarobs(req: Request):
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


@rt('/login')
def login():
    return loginPagina()

@rt('/logar')
def logar(req: Request, usuario: str, senha: str):
    try:
        usuario = Usuarios.get(Usuarios.usuario == usuario, Usuarios.senha == senha)
        if usuario:
            req.session["usuario"] = usuario.usuario
            return Redirect("/")
    except:
        return Redirect("/login")
    


@rt("/logout")
def logout(req: Request):
    req.session.pop("usuario", None)  # 🔓 Remove o usuário da sessão
    return Redirect("/")

serve(port=3000)
