from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
    )

@app.route("/proporcao")
def proporcao():
    #caminho até os arquivos dos gráficos
    grafico_proporcao_jovens_2010 = os.path.join("static", "assets", "plots", "grafico_proporcao_jovens_2010.json")
    grafico_proporcao_jovens_2022 = os.path.join("static", "assets", "plots", "grafico_proporcao_jovens_2022.json")
    
    #abre e carrega os arquivos dos gráficos
    with open(grafico_proporcao_jovens_2010, "r", encoding="utf-8") as a:
        grafico_proporcao_jovens_2010 = json.load(a)

    with open(grafico_proporcao_jovens_2022, "r", encoding="utf-8") as b:
        grafico_proporcao_jovens_2022 = json.load(b)

    return render_template(
        "./graficos/grafico_proporcao_jovens.html",
        grafico_proporcao_jovens_2010 = grafico_proporcao_jovens_2010,
        grafico_proporcao_jovens_2022 = grafico_proporcao_jovens_2022
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
