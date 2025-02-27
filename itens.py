from fasthtml.common import *



def mostrarItens_obs(itens):
    return Div(H3("Itens:"), Table(
        Thead(
            Tr(
                Th("Nome"),
                Th("Quantidade"),
                Th("Status"),
                Th("Motivo")
            )
        ),
        Tbody(
            *[Tr(Td(item.nome, style="text-align: center;"), Td(item.quantidade, style="text-align: center;"), Td(item.status, style="text-align: center;"), Td(item.motivo, style="text-align: center;")) for item in itens]
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
                Th("Motivo"),
                Th("Apagar")
            )
        ),
        Tbody(
            *[Tr(Td(item.nome), Td(item.quantidade), Td(item.status), Td(item.motivo) ,  Td(Form(method="post", action=f"/removerItem/{item.codigo}"), 
            Button('Apagar', type='submit'), hx_post=f"/removerItem/{item.codigo}", hx_target='#tabelaitens' )) for item in itens]
        ),
        cls="striped", id='tabelaitens'
    )



