from fasthtml.common import *


class Produto:
    def __init__(self, nome: str, codigo: int, status: str, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.status = status
        self.quantidade = quantidade
produto1 = Produto(nome='teste', codigo=1, status='Recolher', quantidade=1)
produto2 =  Produto(nome='teste', codigo=2, status='Entregar', quantidade=2)
itens = [produto1, produto2]

def mostrarItens():
    return Table(
        Thead(
            Tr(
                Th("Código"),
                Th("Nome"),
                Th("Ação"),
                Th("Quantidade"),
                Th("Apagar")
            )
        ),
        Tbody(
            *[Tr(Td(item.codigo), Td(item.nome), Td(item.status), Td(item.quantidade), Td(Form(method="post", action=f"/removerItem/{item.codigo}"), 
            Button('Apagar', type='submit'), hx_post=f"/removerItem/{item.codigo}", hx_target='#tabelaitens' )) for item in itens]
        ),
        cls="striped"
    )


def controleItensObs():
    return Div(Form(method="post", hx_post="/adicionaritem", hx_target='#itens')
    (Fieldset(Label("Código:", Input(type="number")), Label("Quantidade:", Input(type="number"), Label("Recolher ou Entregar:"), 
    Select(Option("📄 Papel", value="papel"), Option("🧴 Plástico", value="plastico"), Option("🍾 Vidro", value="vidro"), Option("🥫 Metal", value="metal")) ), 
    Div(mostrarItens(), id='tabelaitens'))))


