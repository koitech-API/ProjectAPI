from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    #caminho até os arquivos dos gráficos
    grafico_razao_jovens_ocupados_sjc_sp_2010_2022 = os.path.join("static", "assets", "plots", "grafico_razao_jovens_ocupados_sjc_sp_2010_2022.json")
    grafico_distribuicao_salarial_sjc_sp_2010_2022 = os.path.join("static", "assets", "plots", "grafico_distribuicao_salarial_sjc_sp_2010_2022.json")
    grafico_populacao_jovem_residente_sjc_sp_2010_2022 = os.path.join("static", "assets", "plots", "grafico_populacao_jovem_residente_sjc_sp_2010_2022.json")
    grafico_razao_jovens_residentes_sjc_sp_2010_2022 = os.path.join("static", "assets", "plots", "grafico_razao_jovens_residentes_sjc_sp_2010_2022.json")
    grafico_escolaridade_sjc_sp_2010 = os.path.join("static", "assets", "plots", "grafico_escolaridade_sjc_sp_2010.json")
    grafico_escolaridade_sjc_sp_2022 = os.path.join("static", "assets", "plots", "grafico_escolaridade_sjc_sp_2022.json")
    grafico_superior_ti_2010_2022 = os.path.join("static", "assets", "plots", "grafico_superior_ti_2010_2022.json")
    grafico_proporcao_formacao_ti_2010_2022 = os.path.join("static", "assets", "plots", "grafico_proporcao_formacao_ti_2010_2022.json")
    
    
    #abre e carrega os arquivos dos gráficos
    with open(grafico_razao_jovens_ocupados_sjc_sp_2010_2022, "r", encoding="utf-8") as a:
        grafico_razao_jovens_ocupados_sjc_sp_2010_2022 = json.load(a)
    with open(grafico_distribuicao_salarial_sjc_sp_2010_2022, "r", encoding="utf-8") as b:
        grafico_distribuicao_salarial_sjc_sp_2010_2022 = json.load(b)
    with open(grafico_populacao_jovem_residente_sjc_sp_2010_2022, "r", encoding="utf-8") as c:
        grafico_populacao_jovem_residente_sjc_sp_2010_2022 = json.load(c)
    with open(grafico_razao_jovens_residentes_sjc_sp_2010_2022, "r", encoding="utf-8") as d:
        grafico_razao_jovens_residentes_sjc_sp_2010_2022 = json.load(d)
    with open(grafico_escolaridade_sjc_sp_2010, "r", encoding="utf-8") as e:
        grafico_escolaridade_sjc_sp_2010 = json.load(e)
    with open(grafico_escolaridade_sjc_sp_2022, "r", encoding="utf-8") as f:
        grafico_escolaridade_sjc_sp_2022 = json.load(f)
    with open(grafico_superior_ti_2010_2022, "r", encoding="utf-8") as g:
        grafico_superior_ti_2010_2022 = json.load(g)
    with open(grafico_proporcao_formacao_ti_2010_2022, "r", encoding="utf-8") as h:
        grafico_proporcao_formacao_ti_2010_2022 = json.load(h)
    

    return render_template(
        "index.html",
        grafico_razao_jovens_ocupados_sjc_sp_2010_2022 = grafico_razao_jovens_ocupados_sjc_sp_2010_2022,
        grafico_distribuicao_salarial_sjc_sp_2010_2022 = grafico_distribuicao_salarial_sjc_sp_2010_2022,
        grafico_populacao_jovem_residente_sjc_sp_2010_2022 = grafico_populacao_jovem_residente_sjc_sp_2010_2022,
        grafico_razao_jovens_residentes_sjc_sp_2010_2022 = grafico_razao_jovens_residentes_sjc_sp_2010_2022,
        grafico_escolaridade_sjc_sp_2010 = grafico_escolaridade_sjc_sp_2010,
        grafico_escolaridade_sjc_sp_2022 = grafico_escolaridade_sjc_sp_2022,
        grafico_superior_ti_2010_2022 = grafico_superior_ti_2010_2022,
        grafico_proporcao_formacao_ti_2010_2022 = grafico_proporcao_formacao_ti_2010_2022
    )

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
