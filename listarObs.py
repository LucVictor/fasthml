from fasthtml.common import *
from impressaoObs import botaoImpressaoObs

def formatarData(a):
    return a.strftime("%d/%m/%Y")

def emoji(a):
    if a == False:
        return 'Pendente ⚠️'
    else:
        return 'Concluído✅'


def filtroObsConcluida():
    return Div(Form(method="get", action="/filtrarobs/True", hx_get="/filtrarobs/True", hx_swap="InnerHTML", hx_target="#listarobs")(Fieldset(
        Button("Concluidas ✅", type="submit", style="background-color: green;  border: none"))), style="margin:0 auto; grid-column: 2; grid-row: 1; width: 150px")


def filtroObsPedente():
    return Div(Form(method="get", action="/filtrarobs/False ", hx_get="/filtrarobs/False", hx_swap="InnerHTML", hx_target="#listarobs")(Fieldset(
        Button("Pendentes ⚠️",  type="submit", style="background-color: #FFCC00; border: none")
    )),  style="margin:0 auto; grid-column: 1; grid-row: 1; width: 150px")

def filtroObsTodos():
    return Div(Form(method="get", action="/filtrarobs/Todos ", hx_get="/filtrarobs/Todos", hx_swap="InnerHTML", hx_target="#listarobs")(Fieldset(
        Button("Todos ✅⚠️",  type="submit", style="")
    )),  style="margin:0 auto; grid-column: 3; grid-row: 1; width: 150px")


def filtrarObsStatus():
    return Div(H3("Filtro Rápido"), Div(filtroObsTodos(), filtroObsPedente(), filtroObsConcluida(), style="display: grid; gap: 1rem"),
     style="width: 100%; text-align: center; border: grey solid 1px;")

def listarObs(obs, pagina):
    return Div(H3("OBS pendentes:"), Div(Table(
        Thead(
            Tr( Th("Data", style="width: 100px; text-align: center;"),
                Th("Razão", style="text-align: center;"),
                Th("Picote Preso?", style="text-align: center;"),
                Th("Status", style="text-align: center;"),
                Th("Ação", style="width: 200px; text-align: center;")
            )
        ),
        Tbody(
            *[Tr(Td(formatarData(obs.data), style="text-align: center;"), Td(obs.cliente, style="text-align: center;"), Td(obs.picote, style="text-align: center;"),  
            Td((emoji(obs.status)), style="text-align: center;"
            ),
            Td(Div(Form(method="get", action=f"/verobs/{obs.codigo}", id='tela', hx_get=f'/verobs/{obs.codigo}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Fieldset(
            Label(Button('Abrir',type='submit', style="width: 80px; margin-right: 3px;")),
        ))), botaoImpressaoObs(obs.codigo), style="display: flex;align-content:center, align-self: center, justify-content: center"), ) for obs in obs]
        ),
        cls="striped"), style="font-size: 14px; margin: 0 auto"),
        Div(
            Button("⬅️ Anterior", hx_target="#listarobs", hx_get=f"/obs/{pagina - 1}", href=f"/obs/{pagina - 1}", cls="btn") if pagina > 1 else "",
            Button("➡️ Próximo", hx_target="#listarobs", hx_get=f"/obs/{pagina + 1}", cls="btn") if len(obs) > 1 else "",
            style="margin-top: 20px; display: flex; gap: 10px;"
        )
        , style="text-align: center", id='listarobs')


