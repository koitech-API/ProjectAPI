from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    #caminho até os arquivos dos gráficos
    razao_jovens_ocupacao_2010 = os.path.join("static", "assets", "plots", "razao_jovens_ocupacao_2010.json")
    distribuicao_renda_2010 = os.path.join("static", "assets", "plots", "distribuicao_renda_2010.json")

    #abre e carrega os arquivos dos gráficos
    with open(razao_jovens_ocupacao_2010, "r", encoding="utf-8") as f:
        razao_jovens_ocupacao_2010_json = json.load(f)
    with open(distribuicao_renda_2010, "r", encoding="utf-8") as o:
        distribuicao_renda_2010_json = json.load(o)

    return render_template(
        "index.html",
        razao_jovens_ocupacao_2010_json=razao_jovens_ocupacao_2010_json,
        distribuicao_renda_2010_json=distribuicao_renda_2010_json
    )

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
