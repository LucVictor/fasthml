from fasthtml.common import *



def mostrarItens_obs(itens):
    return Div(H3("Itens:"), Table(
        Thead(
            Tr(
                Th("Nome"),
                Th("Quantidade"),
                Th("Status"),
                Th("Quantidade")
            )
        ),
        Tbody(
            *[Tr(Td(item.nome), Td(item.quantidade), Td(item.status), Td(item.motivo)) for item in itens]
        ),
        cls="striped", id='tabelaitens'
    ), style="text-align: center;")

def mostrarItens(itens):
    return Table(
        Thead(
            Tr(
                Th("Nome"),
                Th("Quantidade"),
                Th("Status"),
                Th("Quantidade"),
                Th("Apagar")
            )
        ),
        Tbody(
            *[Tr(Td(item.nome), Td(item.quantidade), Td(item.status), Td(item.motivo) ,  Td(Form(method="post", action=f"/removerItem/{item.codigo}"), 
            Button('Apagar', type='submit'), hx_post=f"/removerItem/{item.codigo}", hx_target='#tabelaitens' )) for item in itens]
        ),
        cls="striped", id='tabelaitens'
    )



def controleItensObs(obs):
    return Div(H3("Adicionar Item"),Form(method="post", hx_post=f"/adicionaritem", hx_target='#tabelaitens', hx_swap="InnerHtml")
    (Fieldset(Label("Código:", Input(type="number", name="codigodoproduto")),
     Label("Quantidade:", Input(type="number", name="quantidade"), style="grid-column: 2;"),
     Label("Motivo:", Select(Option("Vencido", value="Vencido"), Option("Falta", value="Falta"), name="motivo", style='width: 10rem;' ), style="grid-column: 1 ;place-self: center"),
     Label("Status:", Select(Option("Entregar", value="Entregar"), Option("Recolher", value="Recolher"), name="status", style='width: 10rem;' ), style="grid-column: 2 ;place-self: center"),
    Input(name="codigoobs",value=f"{obs.codigo}", style="display:none"), Button("Adicionar", type="submit", style="grid-column: 1 / span 2;")
    ,style="grid-template-columns: repeat(2, 3fr); gap: 20px; align-items: center;") ), style="text-align: center; border: white solid; display: grid;")


