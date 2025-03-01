from fasthtml.common import *
from bancodedados import Obs
from gerargrafico import grafico

def home():
    return Div(cardHome(), style=('display: flex; justify-content: space-around; text-align: center;'))

def obsResolvidas():
    obsresolvidas = Obs.select().where(Obs.status == True).count()
    return Span(obsresolvidas, Span("✅", style="font-size: 1rem; vertical-align: middle; "), style=('vertical-align: middle; font-size: 3rem;'))

def obsPendentes():
    obspendentes = Obs.select().where(Obs.status == False).count()
    return Span(obspendentes, Span("⚠️", style="font-size: 1rem; vertical-align: middle; "), style=('vertical-align: middle; font-size: 3rem;'))


def obsTotal(total):
    return Span(total, Span("⚠️✅", style="font-size: 1rem; vertical-align: middle; "), style=('vertical-align: middle; font-size: 3rem;'))



def cardHome():
    obspendentes = Obs.select().where(Obs.status == False).count()
    obsresolvidas = Obs.select().where(Obs.status == True).count()

    return Card(Div(cardObs('Pendentes', obsPendentes()),style="grid-column: 1"), Div(cardObs('Pendentes', obsResolvidas()), style="grid-column: 2"), 
                Div(cardObs("Total de OBS",obsTotal((obspendentes+obsresolvidas))), style="grid-column: 3"),
                Div(grafico(obspendentes, (obsresolvidas+obspendentes)),style="grid-column: 2; width: 300px;"), style="display: grid")

def cardObs(texto, quantity):
    return Card(H3(texto),Br(), quantity, style="width: 20rem; font-weight: 700; text-align: center; ")




