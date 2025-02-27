from fasthtml.common import *
from bancodedados import Obs, Itens

def mostrarItens(itens):
    return Div(H2("Itens"),Table(
        Thead(
            Tr(
                Th("Nome"),
                Th("Quantidade"),
                Th("Status"),
                Th("Motivo"),
                Th("Apagar")
            )
        ),
        Tbody(
            *[Tr(Td(item.nome), Td(item.quantidade), Td(item.status), Td(item.motivo) ,  Td(Form(method="post", action=f"/removerItem/{item.codigo}"), 
            Button('Apagar', type='submit'), hx_post=f"/removerItem/{item.codigo}", hx_target='#tabelaitens' )) for item in itens]
        ),
        cls="striped", id='tabelaitens'
    ))

def botaoGerenciarItens(codigoobs):

    return Div(Form(method="get", id='tela', hx_get=f'/gerenciaritens/{codigoobs}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Button('Gerenciar Itens',type='submit', style='width: 200px;' ), style="display: flex; flex-direction: column; align-items: center;")
        , style='margin: 0 auto; text-align: center;')


def formAdicionarItens(codigoobs):
    obs = Obs.get(Obs.codigo == codigoobs)
    codigocliente = obs.codigoCliente
    itens_lista= Itens.select().where(Itens.codigoObs == codigoobs)
    return Div(H3("Adicionar Item"),Form(method="post", hx_post=f"/adicionaritem", hx_target='#tabelaitens', hx_swap="InnerHtml")
    (Fieldset(Label("Código: ", Input(type="number", name="codigodoproduto", style="width: 10rem;"), style="grid-column: 1; grid-row: 1;place-self: center"),
     Label("Quantidade: ", Input(type="number", name="quantidade", style="width: 10rem;"), style="grid-column: 2; grid-row: 1 ;place-self: center"),
     Label("Motivo:", Select(Option("Vencido", value="Vencido"), Option("Falta", value="Falta"), name="motivo", style='width: 10rem;' ), style="grid-column: 1; grid-row: 2 ;place-self: center"),
     Label("Status: ", Select(Option("Entregar", value="Entregar"), Option("Recolher", value="Recolher"), name="status", style='width: 10rem;' ), style="grid-column: 2; grid-row: 2 ;place-self: center"),
    Input(name="codigoobs",value=f"{obs.codigo}", style="display:none"), Button("Adicionar", type="submit", style="grid-column: 1 / span 2; grid-row: 3 ;place-self: center"),
     style="border: white solid; display: grid; grid-template-columns: repeat(2fr, 2fr); gap: 5px; align-items: center;")
     ), mostrarItens(itens_lista), style="""
                display: flex-inline;
                justify-content: center;   /* 🎯 Centraliza horizontalmente */
                align-items: center;
                width: 30%;     /* 🏗️ Centraliza verticalmente */
                margin: 0 auto;
                text-align: center;            /* 📏 Ocupa altura total da tela */
            """)

