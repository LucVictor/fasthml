from fasthtml.common import *
from impressaoObs import botaoImpressaoObs

def formatarData(a):
    return a.strftime("%d/%m/%Y")

def emoji(a):
    if a == False:
        return 'Pendente ⚠️'
    else:
        return 'Concluído✅'

def listarObsProcurar(obs = []):
    if obs != []:
        return Div(Div(Table(
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
            cls="striped"), style="font-size: 14px; margin: 0 auto")
            , style="text-align: center", id='listarobs')
    else:
        Div()
def formprocurarObs():
    return Div(
        Div(Form(hx_swap="InnerHTML",  hx_post="/resultadoprocurarobs",  hx_taget="#listarobs")(Fieldset(
            H3("Procurar OBS"),
            Label("Código do Cliente:",Br(), Input(type="number", name="codigodocliente", style="width: 20rem")),
            Label("Status:",Br(), Select(Option("Pendente", value="False"), Option("Concluído", value="True"), name="status"), style="width: 20rem"),
            Label("Data:", Br(), Input(type="date", name="data"), style="width: 20rem"),
            Button("Procurar",Br(), type="Submit", style="width: 20rem")
        )),
        Div(listarObsProcurar(), id="listarobs")  )
    )