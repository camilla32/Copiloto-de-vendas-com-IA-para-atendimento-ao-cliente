def calcular_score(
    vende_refrigerante,
    vende_salgados,
    fluxo,
    espaco
):

    score = 0

    if vende_refrigerante:
        score += 30

    if vende_salgados:
        score += 20

    score += fluxo * 2

    score += espaco * 1.5

    return min(int(score), 100)