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

@app.route("/empregados")
def empregados():
    #caminho até os arquivos dos gráficos
    grafico_jovens_empregados_2010 = os.path.join("static", "assets", "plots", "grafico_jovens_empregados_2010.json")
    grafico_jovens_empregados_2022 = os.path.join("static", "assets", "plots", "grafico_jovens_empregados_2022.json")

     #abre e carrega os arquivos dos gráficos
    with open(grafico_jovens_empregados_2010, "r", encoding="utf-8") as c:
        grafico_jovens_empregados_2010 = json.load(c)

    with open(grafico_jovens_empregados_2022, "r", encoding="utf-8") as d:
        grafico_jovens_empregados_2022 = json.load(d)

    return render_template(
        "./graficos/grafico_jovens_empregados.html",
        grafico_jovens_empregados_2010 = grafico_jovens_empregados_2010,
        grafico_jovens_empregados_2022 = grafico_jovens_empregados_2022
    )

@app.route("/etaria")
def etaria():
    #caminho até os arquivos dos gráficos
    grafico_distribuicao_etaria_2010 = os.path.join("static", "assets", "plots", "grafico_distribuicao_etaria_2010.json")
    grafico_distribuicao_etaria_2022 = os.path.join("static", "assets", "plots", "grafico_distribuicao_etaria_2022.json")

     #abre e carrega os arquivos dos gráficos
    with open(grafico_distribuicao_etaria_2010, "r", encoding="utf-8") as e:
        grafico_distribuicao_etaria_2010 = json.load(e)

    with open(grafico_distribuicao_etaria_2022, "r", encoding="utf-8") as f:
        grafico_distribuicao_etaria_2022 = json.load(f)

    return render_template(
        "./graficos/grafico_distribuicao_etaria.html",
        grafico_distribuicao_etaria_2010 = grafico_distribuicao_etaria_2010,
        grafico_distribuicao_etaria_2022 = grafico_distribuicao_etaria_2022
    )

@app.route("/instrucao")
def instrucao():
    #caminho até os arquivos dos gráficos
    grafico_nivel_instrucao_2010 = os.path.join("static", "assets", "plots", "grafico_nivel_instrucao_2010.json")
    grafico_nivel_instrucao_2022 = os.path.join("static", "assets", "plots", "grafico_nivel_instrucao_2022.json")

     #abre e carrega os arquivos dos gráficos
    with open(grafico_nivel_instrucao_2010, "r", encoding="utf-8") as g:
        grafico_nivel_instrucao_2010 = json.load(g)

    with open(grafico_nivel_instrucao_2022, "r", encoding="utf-8") as h:
        grafico_nivel_instrucao_2022 = json.load(h)

    return render_template(
        "./graficos/grafico_nivel_instrucao.html",
        grafico_nivel_instrucao_2010 = grafico_nivel_instrucao_2010,
        grafico_nivel_instrucao_2022 = grafico_nivel_instrucao_2022
    )

@app.route("/superior")
def superior():
    #caminho até os arquivos dos gráficos
    grafico_superior_ciencia_computacao_2010 = os.path.join("static", "assets", "plots", "grafico_superior_ciencia_computacao_2010.json")
    grafico_superior_ciencia_computacao_2022 = os.path.join("static", "assets", "plots", "grafico_superior_ciencia_computacao_2022.json")

     #abre e carrega os arquivos dos gráficos
    with open(grafico_superior_ciencia_computacao_2010, "r", encoding="utf-8") as g:
        grafico_superior_ciencia_computacao_2010 = json.load(g)

    with open(grafico_superior_ciencia_computacao_2022, "r", encoding="utf-8") as h:
        grafico_superior_ciencia_computacao_2022 = json.load(h)

    return render_template(
        "./graficos/grafico_superior_ciencia_computacao.html",
        grafico_superior_ciencia_computacao_2010 = grafico_superior_ciencia_computacao_2010,
        grafico_superior_ciencia_computacao_2022 = grafico_superior_ciencia_computacao_2022
    )

@app.route("/salarial")
def salarial():
    #caminho até os arquivos dos gráficos
    grafico_distribuicao_salarial_2010 = os.path.join("static", "assets", "plots", "grafico_distribuicao_salarial_2010.json")
    grafico_distribuicao_salarial_2022 = os.path.join("static", "assets", "plots", "grafico_distribuicao_salarial_2022.json")

     #abre e carrega os arquivos dos gráficos
    with open(grafico_distribuicao_salarial_2010, "r", encoding="utf-8") as g:
        grafico_distribuicao_salarial_2010 = json.load(g)

    with open(grafico_distribuicao_salarial_2022, "r", encoding="utf-8") as h:
        grafico_distribuicao_salarial_2022 = json.load(h)

    return render_template(
        "./graficos/grafico_distribuicao_salarial.html",
        grafico_distribuicao_salarial_2010 = grafico_distribuicao_salarial_2010,
        grafico_distribuicao_salarial_2022 = grafico_distribuicao_salarial_2022
    )



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
