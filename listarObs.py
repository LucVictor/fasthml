from fasthtml.common import *

def formatarData(a):
    return a.strftime("%d/%m/%Y")

def emoji(a):
    if a == False:
        return '⚠️'
    else:
        return '✅'

def listarObs(obs):
    return Div(Table(
        Thead(
            Tr( Th("Data"),
                Th("Cliente"),
                Th("Picote"),
                Th("Status"),
                Th("U. Atu."),
                Th("Ação"), 
            )
        ),
        Tbody(
            *[Tr(Td(formatarData(obs.data)), Td(obs.cliente), Td(obs.picote),  
            Td((emoji(obs.status))
            ), Td(formatarData(obs.ultimaAtualizacao)),
            Td(Div(Form(method="get", action=f"/verobs/{obs.codigo}", id='tela', hx_get=f'/verobs/{obs.codigo}', hx_target='#conteudo', hx_swap='InnerHTML')(
        Fieldset(
            Label(Button('Abrir',type='submit')),
        ))))) for obs in obs]
        ),
        cls="striped"
    ), id='listarobs',  style='text-align: center;')
