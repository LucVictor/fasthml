from fasthtml.common import *

def mostrarObs():
    return Table(
        Thead(
            Tr(
                Th("Data"),
                Th("Cliente"),
                Th("Status"),
                Th("Ação")
            )
        ),
        Tbody(
            *[Tr(Td(item.codigo), Td(item.nome), Td(item.status), Td(item.quantidade), Td(Form(method="post", action=f"/removerItem/{item.codigo}"), 
            Button('Abrir', type='submit'), hx_post=f"/removerItem/{item.codigo}", hx_target='#tabelaitens' )) for item in itens]
        ),
        cls="striped"
    )

def listarObs():
    return Div()