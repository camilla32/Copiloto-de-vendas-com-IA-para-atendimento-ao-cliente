def responder_objecao(objecao):

    respostas = {

        "coca":
        """
        A proposta da FYS não é substituir marcas líderes,
        mas ampliar as opções disponíveis para o consumidor.
        """,

        "espaco":
        """
        Recomendamos iniciar apenas com o Guaraná da Amazônia FYS,
        reduzindo a necessidade de espaço inicial.
        """,

        "marca":
        """
        A FYS é a marca de refrigerantes do Grupo Heineken,
        com sabores diferenciados e menos açúcar.
        """
    }

    return respostas.get(
        objecao.lower(),
        "Posso ajudar com mais informações sobre a FYS."
    )