from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from services.score_service import calcular_score
from services.recommendation_service import recomendar_produto
from services.objection_service import responder_objecao

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")


@app.route("/simulacao")
def simulacao():
    return render_template("simulacao.html")


@app.route("/calcular", methods=["POST"])
def calcular():

    dados = request.json

    score = calcular_score(
        dados["vende_refrigerante"],
        dados["vende_salgados"],
        dados["fluxo"],
        dados["espaco"]
    )

    recomendacao = recomendar_produto(score)

    return jsonify({
        "score": score,
        "recomendacao": recomendacao
    })


@app.route("/objecao", methods=["POST"])
def objecao():

    dados = request.json

    resposta = responder_objecao(
        dados["objecao"]
    )

    return jsonify({
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run(debug=True)