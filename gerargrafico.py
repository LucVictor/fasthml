from fasthtml.common import *

def grafico(x, y):
    return Div(
        Canvas(id="speedometer", style="margin: 0 auto; width: 300px; height: 100px;"),
        Script(f"""
            var ctx = document.getElementById('speedometer').getContext('2d');
            var speedometerChart = new Chart(ctx, {{
                type: 'doughnut',
                data: {{
                    labels: ['Pendentes', 'Resolvidas'],
                    datasets: [{{
                        data: [{x}, {y} - {x}],  // 📊 Usa a variável do Python
                        backgroundColor: ['red', 'green'],
                        borderWidth: 0
                    }}]
                }},
                options: {{
                    rotation: 270, // Começa no topo (270°)
                    circumference: 180, // Apenas metade do círculo (180°)
                    cutout: '80%', // Faz parecer um velocímetro
                    plugins: {{
                        legend: {{
                            display: true,
                            position: 'bottom',  // 📌 Legenda abaixo do gráfico
                            labels: {{
                                boxWidth: 20,
                                padding: 10
                            }}
                        }},
                        title: {{
                            display: true,
                            text: "Gráfico de resoluções",  // 🏆 Título atualizado
                            color: "#D4D4D4",
                            font: {{
                                size: 18
                            }}
                        }}
                    }}
                }}
            }});
        """)
    )






