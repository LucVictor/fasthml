from fasthtml.common import *


def formularioObs():
    return Div(Div(Form(method="post", action="/criarObs")(
        Fieldset(
            Label('Código do Cliente', Input(name="number")),
        ),
        Button("Criar", type="submit"), style='width: 50%; margin: 0 auto; text-align: center;'
)), style='display: flex; justify-content: space-between; margin: 0 auto; text-align: center;')



