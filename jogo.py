
# ============================================================
# 🏝️ O SEGREDO NA ILHA
# RPG DE ESCOLHAS - 30 FASES
# ============================================================
from js import window
# ============================================================
# ESTADO DO JOGO
# ============================================================

state = {
    "personagem": "",

    "vida": 5,
    "sanidade": 5,

    "inv": [],

    "pistas": 0,

    "milo_vivo": True,
    "barbara_viva": True,
    "olivier_vivo": True,
    "amelie_viva": True,

    "confianca_milo": 0,
    "confianca_barbara": 0,

    "monstro_fraqueza": False,
    "monstro_derrotado": False,

    "batalha": 0
}


# ============================================================
# FUNÇÕES
# ============================================================

def escolher(msg, opcoes):
    resposta = window.prompt(msg + "\n\n" + " | ".join(opcoes))

    if resposta is None:
        return opcoes[0]

    return str(resposta).strip().lower()

def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)
        print(f"🎒 Você encontrou: {item}")


def perder_vida(qtd=1):
    state["vida"] -= qtd
    print(f"❤️ Vida: {state['vida']}")

    if state["vida"] <= 0:
        return True

    return False


def perder_sanidade(qtd=1):
    state["sanidade"] -= qtd
    print(f"🧠 Sanidade: {state['sanidade']}")

    if state["sanidade"] <= 0:
        return True

    return False


def personagem_secundario():

    if state["personagem"] == "Olivier":
        return "Amelie"
    else:
        return "Olivier"


def companheiros_vivos():

    vivos = []

    if state["milo_vivo"]:
        vivos.append("Milo")

    if state["barbara_viva"]:
        vivos.append("Barbara")

    if state["personagem"] == "Olivier":
        if state["amelie_viva"]:
            vivos.append("Amelie")

    else:
        if state["olivier_vivo"]:
            vivos.append("Olivier")

    return vivos


# ============================================================
# FASE 1 - ESCOLHA
# ============================================================

def fase1():

    print("""
============================================================
🏝️ O SEGREDO NA ILHA
============================================================

Há muitos anos, um membro da sua família desapareceu
misteriosamente em uma ilha distante.

O caso nunca foi solucionado.

Recentemente, sua família encontrou documentos antigos
que podem revelar o que aconteceu.

Por isso, vocês decidiram viajar até a ilha.

Antes de começar, escolha seu personagem:
""")

    op = escolher(
        "1) Olivier\n"
        "2) Amelie\n\n"
        "Escolha: ",
        ["1", "2"]
    )

    if op == "1":
        state["personagem"] = "Olivier"
    else:
        state["personagem"] = "Amelie"

    print(f"""
Você escolheu {state["personagem"]}.

A viagem para a ilha começa.
""")

    return "fase2"


# ============================================================
# FASE 2 - VIAGEM
# ============================================================

def fase2():

    print("""
============================================================
🚢 FASE 2 - A VIAGEM
============================================================

O barco atravessa o mar durante horas.

A ilha aparece no horizonte.

Durante a viagem, ninguém fala muito sobre o passado.
""")

    print(f"""
{state["personagem"]}:
— Por que todo mundo está evitando falar sobre essa ilha?

Um familiar responde:

— Porque o que aconteceu lá não foi algo normal.

{state["personagem"]}:
— E o que aconteceu?

Familiar:
— Quando chegarmos, você vai entender.
""")

    print("""
O barco chega ao porto.

A aventura começa.
""")

    return "fase3"


# ============================================================
# FASE 3 - CHEGADA
# ============================================================

def fase3():

    print("""
============================================================
🏝️ FASE 3 - CHEGADA
============================================================

A ilha parece pequena, mas existe uma grande floresta
ao redor da vila.

Alguns moradores observam vocês.
""")

    print("""
Milo:
— Vocês são os visitantes?

Barbara:
— Eu sabia que alguém viria.

Milo:
— Barbara...

Barbara:
— O quê? É verdade.
""")

    op = escolher(
        "\n1) Perguntar sobre a ilha\n"
        "2) Perguntar sobre sua família\n"
        "3) Perguntar sobre os desaparecimentos\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        print("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")
        state["confianca_milo"] += 1

    elif op == "2":
        print("""
Você:
— Vocês conhecem minha família?

Barbara:
— O sobrenome de vocês é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")
        state["pistas"] += 2

    else:
        print("""
Você:
— É verdade que pessoas desapareceram?

Milo:
— Sim.

Barbara:
— E algumas nunca foram encontradas.
""")
        state["pistas"] += 1

    return "fase4"


# ============================================================
# FASE 4 - CONHECENDO A VILA
# ============================================================

def fase4():

    print("""
============================================================
🏘️ FASE 4 - A VILA
============================================================

Milo mostra a vila.

Existem três lugares importantes:

Uma igreja antiga.

Uma casa abandonada.

Um farol.
""")

    print("""
Milo:
— Se querem descobrir alguma coisa, comecem por esses
lugares.

Barbara:
— Mas tomem cuidado.

Você:
— Por quê?

Barbara:
— Porque alguns lugares não gostam de visitantes.
""")

    op = escolher(
        "\n1) Igreja\n"
        "2) Casa abandonada\n"
        "3) Farol\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        return "fase5"

    if op == "2":
        return "fase6"

    return "fase7"


# ============================================================
# FASE 5 - IGREJA
# ============================================================

def fase5():

    print("""
============================================================
⛪ FASE 5 - A IGREJA
============================================================

A igreja está abandonada.

Nas paredes existem símbolos estranhos.
""")

    print("""
Barbara:
— Eu nunca vi esses símbolos.

Milo:
— Eu já.

Você:
— Onde?

Milo:
— Nos documentos antigos da ilha.
""")

    op = escolher(
        "\n1) Examinar os símbolos\n"
        "2) Procurar documentos\n"
        "3) Fotografar os símbolos\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        print("""
Você percebe que os símbolos formam um mapa.
""")
        state["pistas"] += 2

    elif op == "2":
        pegar("livro antigo")
        state["pistas"] += 3

    else:
        pegar("fotografia dos símbolos")
        state["pistas"] += 1

    return "fase8"


# ============================================================
# FASE 6 - CASA
# ============================================================

def fase6():

    print("""
============================================================
🏚️ FASE 6 - CASA ABANDONADA
============================================================

A casa está coberta de poeira.

Mesmo assim, alguns objetos parecem ter sido usados
recentemente.
""")

    print("""
Milo:
— Eu não gosto desse lugar.

Barbara:
— Você nunca gosta de lugar nenhum.

Milo:
— Porque normalmente eu estou certo.
""")

    op = escolher(
        "\n1) Procurar documentos\n"
        "2) Subir as escadas\n"
        "3) Ir ao porão\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        pegar("documentos da família")
        state["pistas"] += 3

    elif op == "2":
        pegar("chave enferrujada")
        state["pistas"] += 2
        perder_sanidade()

    else:
        pegar("fotografia antiga")
        state["pistas"] += 3

    return "fase8"


# ============================================================
# FASE 7 - FAROL
# ============================================================

def fase7():

    print("""
============================================================
🔦 FASE 7 - O FAROL
============================================================

No topo do farol existe uma caixa escondida.
""")

    print("""
Você encontra uma fotografia antiga.

Nela está parte da sua família.

Ao fundo aparece uma criatura que você não reconhece.
""")

    pegar("fotografia da criatura")
    state["pistas"] += 3

    print("""
Milo:
— Isso estava na fotografia?

Barbara:
— Não deveria existir.
""")

    return "fase8"


# ============================================================
# FASE 8 - PRIMEIRA NOITE
# ============================================================

def fase8():

    print("""
============================================================
🌙 FASE 8 - PRIMEIRA NOITE
============================================================

Durante a noite, vocês escutam três batidas.

TOC.

TOC.

TOC.
""")

    print("""
Milo:
— Não abre.

Você:
— Por quê?

Milo:
— Porque não tem ninguém lá fora.

Barbara:
— E é isso que me assusta.
""")

    op = escolher(
        "\n1) Abrir a janela\n"
        "2) Ignorar\n"
        "3) Sair pela porta\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        print("Não existe ninguém do lado de fora.")
        print("Mas há marcas enormes no chão.")
        state["pistas"] += 2
        perder_sanidade()

    elif op == "2":
        print("As batidas param depois de alguns minutos.")
        state["pistas"] += 1

    else:
        print("""
Vocês saem.

Barbara:
— Olhem para o chão.

Existem pegadas enormes.
""")
        state["pistas"] += 3

    return "fase9"


# ============================================================
# FASE 9 - O DESAPARECIMENTO
# ============================================================

def fase9():

    print("""
============================================================
🚨 FASE 9 - O DESAPARECIMENTO
============================================================

Na manhã seguinte, um morador desapareceu.

Os moradores estão assustados.
""")

    print("""
Milo:
— Ele estava aqui ontem.

Barbara:
— Então precisamos encontrá-lo.

Milo:
— Antes que seja tarde.
""")

    op = escolher(
        "\n1) Procurar na vila\n"
        "2) Procurar na floresta\n\n"
        "Escolha: ",
        ["1", "2"]
    )

    if op == "1":
        state["pistas"] += 1
        print("Você encontra marcas de sangue perto da floresta.")

    else:
        state["pistas"] += 2
        print("Vocês encontram pegadas enormes.")

    return "fase10"


# ============================================================
# FASE 10 - PROCURANDO O DESAPARECIDO
# ============================================================

def fase10():

    print("""
============================================================
🔎 FASE 10 - A INVESTIGAÇÃO
============================================================

Vocês seguem as pistas pela floresta.

Depois de algum tempo encontram um objeto pertencente
ao desaparecido.
""")

    pegar("objeto do desaparecido")

    print("""
Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    state["pistas"] += 2

    return "fase11"


# ============================================================
# FASE 11 - FLORESTA
# ============================================================

def fase11():

    print("""
============================================================
🌲 FASE 11 - A FLORESTA
============================================================

A floresta fica cada vez mais escura.

Vocês encontram uma trilha escondida.
""")

    op = escolher(
        "\n1) Seguir a trilha\n"
        "2) Marcar o caminho e voltar\n"
        "3) Separar o grupo\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        state["pistas"] += 2
        return "fase12"

    elif op == "2":
        state["pistas"] += 1
        return "fase12"

    else:
        print("""
Milo:
— Não acho uma boa ideia.

Barbara:
— Concordo.

Você decide seguir sozinho.
""")

        perder_sanidade()

        return "fase12"


# ============================================================
# FASE 12 - ACAMPAMENTO
# ============================================================

def fase12():

    print("""
============================================================
🔥 FASE 12 - ACAMPAMENTO
============================================================

Vocês montam um pequeno acampamento.

Durante a noite, conversam sobre a criatura.
""")

    print("""
Milo:
— Acho que aquilo não é um animal.

Barbara:
— Então o que é?

Milo:
— Não sei.

Você:
— Precisamos descobrir.
""")

    op = escolher(
        "\n1) Conversar com Milo\n"
        "2) Conversar com Barbara\n"
        "3) Dormir\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        state["confianca_milo"] += 2

    elif op == "2":
        state["confianca_barbara"] += 2

    else:
        print("Você descansa e recupera um pouco da sanidade.")
        state["sanidade"] += 1

    return "fase13"


# ============================================================
# FASE 13 - PEGADAS
# ============================================================

def fase13():

    print("""
============================================================
🐾 FASE 13 - PEGADAS
============================================================

Na manhã seguinte, vocês encontram pegadas gigantes.

Elas parecem ter sido feitas recentemente.
""")

    print("""
Barbara:
— Isso é grande demais.

Milo:
— E está indo naquela direção.

Você:
— Então vamos descobrir o que fez isso.
""")

    state["pistas"] += 3

    return "fase14"


# ============================================================
# FASE 14 - CABANA
# ============================================================

def fase14():

    print("""
============================================================
🏚️ FASE 14 - A CABANA
============================================================

Uma pequena cabana aparece no meio da floresta.

Dentro há um diário.
""")

    pegar("diário")

    print("""
No diário está escrito:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma forma de matar essa coisa.

Milo:
— Precisamos descobrir qual.
""")

    state["pistas"] += 3

    return "fase15"


# ============================================================
# FASE 15 - O DIÁRIO
# ============================================================

def fase15():

    print("""
============================================================
📖 FASE 15 - O DIÁRIO
============================================================

Vocês leem o diário inteiro.

Ele fala sobre uma criatura que vive escondida
nas profundezas da ilha.
""")

    print("""
O diário também menciona:

"Quando a criatura for ferida pelo símbolo original,
ela ficará vulnerável."
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    print("""
Milo:
— Então precisamos encontrar esse símbolo.

Barbara:
— E alguma coisa capaz de usá-lo.
""")

    return "fase16"


# ============================================================
# FASE 16 - EQUIPAMENTOS
# ============================================================

def fase16():

    print("""
============================================================
🎒 FASE 16 - PREPARAÇÃO
============================================================

Vocês precisam encontrar equipamentos antes de continuar.
""")

    op = escolher(
        "\n1) Procurar uma arma\n"
        "2) Procurar medicamentos\n"
        "3) Procurar o símbolo\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        pegar("arma")
        state["pistas"] += 1

    elif op == "2":
        pegar("medicamento")
        print("❤️ Vocês encontram medicamentos.")

    else:
        pegar("símbolo antigo")
        state["pistas"] += 3

    return "fase17"


# ============================================================
# FASE 17 - O LAGO
# ============================================================

def fase17():

    print("""
============================================================
🌊 FASE 17 - O LAGO
============================================================

O mapa indica que o próximo símbolo está perto de um lago.
""")

    print("""
Barbara:
— Eu não gosto desse lugar.

Milo:
— Então somos dois.

Você:
— Precisamos continuar.
""")

    op = escolher(
        "\n1) Procurar dentro da água\n"
        "2) Procurar ao redor do lago\n"
        "3) Ignorar o lago\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        perder_vida()
        pegar("cristal")
        state["pistas"] += 2

    elif op == "2":
        pegar("cristal")
        state["pistas"] += 2

    else:
        state["pistas"] += 1

    return "fase18"


# ============================================================
# FASE 18 - CAVERNA
# ============================================================

def fase18():

    print("""
============================================================
🕳️ FASE 18 - A CAVERNA
============================================================

O cristal aponta para uma caverna escondida.
""")

    print("""
Milo:
— Acho que estamos perto.

Barbara:
— Perto demais.
""")

    op = escolher(
        "\n1) Entrar\n"
        "2) Procurar outra entrada\n\n"
        "Escolha: ",
        ["1", "2"]
    )

    if op == "1":
        state["pistas"] += 3
    else:
        state["pistas"] += 1

    return "fase19"


# ============================================================
# FASE 19 - PRIMEIRO ENCONTRO
# ============================================================

def fase19():

    print("""
============================================================
👹 FASE 19 - O PRIMEIRO ENCONTRO
============================================================

Um rugido ecoa pela caverna.

A criatura aparece por alguns segundos.

Ela é enorme e desaparece rapidamente.
""")

    print("""
Milo:
— CORRE!

Barbara:
— AGORA!

Vocês fogem antes que ela alcance o grupo.
""")

    perder_sanidade()

    return "fase20"


# ============================================================
# FASE 20 - FUGA
# ============================================================

def fase20():

    print("""
============================================================
🏃 FASE 20 - FUGA DO MONSTRO
============================================================

A criatura começa a perseguir vocês.
""")

    op = escolher(
        "\n1) Correr para a esquerda\n"
        "2) Correr para a direita\n"
        "3) Se esconder\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":
        print("Vocês encontram uma saída.")
        state["pistas"] += 1

    elif op == "2":
        print("Vocês encontram uma sala escondida.")
        state["pistas"] += 2

    else:
        print("Vocês conseguem se esconder.")
        state["sanidade"] += 1

    return "fase21"


# ============================================================
# FASE 21 - DESCOBRINDO A FRAQUEZA
# ============================================================

def fase21():

    print("""
============================================================
🔎 FASE 21 - A FRAQUEZA
============================================================

Na sala escondida, vocês encontram uma inscrição.

Ela revela que o monstro pode ser ferido pelo símbolo
original da ilha.
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    print("""
Barbara:
— Então podemos derrotá-lo.

Milo:
— Sim.

Você:
— Mas precisamos chegar perto dele.
""")

    return "fase22"


# ============================================================
# FASE 22 - O ESCONDERIJO
# ============================================================

def fase22():

    print("""
============================================================
🏚️ FASE 22 - O ESCONDERIJO
============================================================

Vocês descobrem que a criatura possui um esconderijo
abaixo da ilha.
""")

    print("""
Milo:
— É lá que ela fica.

Barbara:
— Então é lá que vamos.

Você:
— Vamos acabar com isso.
""")

    return "fase23"


# ============================================================
# FASE 23 - RESGATE
# ============================================================

def fase23():

    print("""
============================================================
🆘 FASE 23 - O RESGATE
============================================================

Vocês encontram o morador desaparecido.

Ele está ferido, mas vivo.
""")

    print("""
Morador:
— Vocês precisam ir embora!

Você:
— O que aconteceu?

Morador:
— Ela está acordada.
""")

    op = escolher(
        "\n1) Levar o homem embora\n"
        "2) Deixá-lo escondido\n\n"
        "Escolha: ",
        ["1", "2"]
    )

    if op == "1":
        print("Vocês levam o homem para um local seguro.")

    else:
        print("Vocês o escondem em uma área protegida.")

    state["pistas"] += 1

    return "fase24"


# ============================================================
# FASE 24 - ENTRADA DO ESCONDERIJO
# ============================================================

def fase24():

    print("""
============================================================
🚪 FASE 24 - A ENTRADA
============================================================

Vocês encontram uma porta enorme no subterrâneo.

Ela possui o símbolo original.
""")

    if "símbolo antigo" in state["inv"]:
        print("""
O símbolo que vocês encontraram encaixa na porta.

Ela se abre.
""")
        state["pistas"] += 3

    else:
        print("""
Vocês precisam forçar a porta.

Isso faz um grande barulho.
""")
        perder_vida()

    return "fase25"


# ============================================================
# FASE 25 - O PASSADO
# ============================================================

def fase25():

    print("""
============================================================
📜 FASE 25 - O PASSADO DA FAMÍLIA
============================================================

Dentro do esconderijo existem documentos.

Eles revelam que sua família já encontrou a criatura
no passado.

Seu parente desaparecido tentou impedir que ela
fosse libertada.
""")

    print("""
Barbara:
— Então ele estava tentando proteger a ilha.

Milo:
— E ninguém contou isso para vocês.

Você:
— Agora eu sei por quê.
""")

    state["pistas"] += 4

    return "fase26"


# ============================================================
# FASE 26 - PREPARAÇÃO
# ============================================================

def fase26():

    print("""
============================================================
⚔️ FASE 26 - PREPARAÇÃO
============================================================

Antes da batalha, vocês precisam decidir como agir.
""")

    op = escolher(
        "\n1) Preparar a arma\n"
        "2) Preparar o símbolo\n"
        "3) Procurar mais informações\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":

        if "arma" in state["inv"]:
            print("A arma está pronta.")
            state["batalha"] += 1
        else:
            print("Vocês não possuem uma arma adequada.")

    elif op == "2":

        if "símbolo antigo" in state["inv"]:
            print("O símbolo está pronto.")
            state["batalha"] += 2
        else:
            print("Vocês não encontraram o símbolo.")

    else:

        print("""
Vocês descobrem uma informação importante:

A criatura fica mais fraca quando o símbolo é ativado.
""")

        state["monstro_fraqueza"] = True
        state["batalha"] += 2

    return "fase27"


# ============================================================
# FASE 27 - ENCONTRO FINAL
# ============================================================

def fase27():

    print("""
============================================================
👹 FASE 27 - O MONSTRO
============================================================

Vocês chegam à última sala.

A criatura está esperando.

Ela é muito maior do que parecia antes.
""")

    print("""
Milo:
— É agora.

Barbara:
— Não deixem ela chegar perto.

Você:
— Todo mundo pronto?

Milo:
— Não.

Barbara:
— Mas vamos mesmo assim.
""")

    return "fase28"


# ============================================================
# FASE 28 - BATALHA
# ============================================================

def fase28():

    print("""
============================================================
⚔️ FASE 28 - BATALHA CONTRA O MONSTRO
============================================================

A criatura ataca.

Vocês precisam agir rápido.
""")

    op = escolher(
        "\n1) Atacar o monstro\n"
        "2) Ativar o símbolo\n"
        "3) Ajudar Milo\n"
        "4) Ajudar Barbara\n\n"
        "Escolha: ",
        ["1", "2", "3", "4"]
    )

    # -------------------------
    # ATAQUE
    # -------------------------

    if op == "1":

        if "arma" in state["inv"] and state["monstro_fraqueza"]:

            print("""
Você ataca a criatura no ponto fraco.

Ela grita e recua.
""")

            state["batalha"] += 3

        else:

            print("""
Seu ataque não causa muito efeito.

A criatura contra-ataca.
""")

            perder_vida()

    # -------------------------
    # SÍMBOLO
    # -------------------------

    elif op == "2":

        if "símbolo antigo" in state["inv"]:

            print("""
Você ativa o símbolo.

A criatura começa a enfraquecer.
""")

            state["batalha"] += 4

        else:

            print("""
Você tenta ativar o símbolo.

Mas não possui o objeto necessário.
""")

            perder_sanidade()

    # -------------------------
    # AJUDAR MILO
    # -------------------------

    elif op == "3":

        if state["milo_vivo"]:

            print("""
Você salva Milo de um ataque.

Milo:
— Obrigado!

Ele consegue atacar a criatura.
""")

            state["confianca_milo"] += 2
            state["batalha"] += 2

        else:
            print("Milo não está mais aqui.")

    # -------------------------
    # AJUDAR BARBARA
    # -------------------------

    else:

        if state["barbara_viva"]:

            print("""
Você ajuda Barbara.

Barbara:
— Eu sabia que podia confiar em você!

Ela encontra uma abertura.
""")

            state["confianca_barbara"] += 2
            state["batalha"] += 2

        else:
            print("Barbara não está mais aqui.")

    return "fase29"


# ============================================================
# FASE 29 - ÚLTIMA ESCOLHA
# ============================================================

def fase29():

    print("""
============================================================
🔥 FASE 29 - ÚLTIMA ESCOLHA
============================================================

A criatura está ferida.

Mas ainda não foi derrotada.

Você tem uma última oportunidade.
""")

    print("""
Milo:
— Se atacarmos juntos, talvez consigamos.

Barbara:
— Ou podemos tentar selar a criatura novamente.
""")

    op = escolher(
        "\n1) Derrotar o monstro\n"
        "2) Selar o monstro\n"
        "3) Fugir\n\n"
        "Escolha: ",
        ["1", "2", "3"]
    )

    if op == "1":

        if state["batalha"] >= 5:

            state["monstro_derrotado"] = True
            return "fase30"

        else:

            print("""
Vocês atacam.

Mas não conseguiram enfraquecer a criatura o suficiente.
""")

            return "fase30"

    elif op == "2":

        print("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

        return "fase30"

    else:

        print("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

        return "fase30"


# ============================================================
# FASE 30 - FINAIS
# ============================================================

def fase30():

    print("""
============================================================
🏁 FASE 30 - O FINAL
============================================================
""")

    vivos = companheiros_vivos()

    # ========================================================
    # FINAL 1 - TODOS VIVOS + MONSTRO DERROTADO
    # ========================================================

    if state["monstro_derrotado"] and len(vivos) >= 3:

        print("""
🌟 FINAL PERFEITO

A criatura finalmente é derrotada.

Todos conseguem sair da câmara.

Milo:
— Nós realmente conseguimos.

Barbara:
— E ninguém morreu.

Você:
— Finalmente uma boa notícia.

A ilha fica em silêncio.

Todos sobrevivem.

O segredo da ilha foi descoberto.
""")

    # ========================================================
    # FINAL 2 - MONSTRO DERROTADO, MAS ALGUÉM MORREU
    # ========================================================

    elif state["monstro_derrotado"]:

        print("""
🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Mas nem todos conseguiram sobreviver.

Os sobreviventes deixam a ilha sabendo que nunca
esquecerão aqueles que ficaram para trás.
""")

        print("Sobreviventes:", vivos)

    # ========================================================
    # FINAL 3 - MONSTRO SELADO
    # ========================================================

    elif state["batalha"] >= 3:

        print("""
👁️ FINAL DO SELAMENTO

A criatura é selada novamente.

A ilha está segura...

Por enquanto.

Milo:
— E se ela escapar novamente?

Barbara:
— Então espero que não estejamos aqui.
""")

    # ========================================================
    # FINAL 4 - FUGA
    # ========================================================

    elif state["vida"] > 0:

        print("""
🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha fica para trás.

Mas, quando vocês olham para o mar...

A criatura aparece na costa.

Ela observa o barco partir.

Ela ainda está viva.
""")

    # ========================================================
    # FINAL 5 - TODOS MORREM
    # ========================================================

    else:

        print("""
💀 FINAL DA ILHA

A criatura vence.

Ninguém consegue escapar.

O segredo permanece enterrado na ilha.
""")

    # ========================================================
    # RESULTADO
    # ========================================================

    print("""
============================================================
                    🎮 FIM DO JOGO
============================================================
""")

    print("👤 Personagem:", state["personagem"])
    print("❤️ Vida:", state["vida"])
    print("🧠 Sanidade:", state["sanidade"])
    print("🔎 Pistas:", state["pistas"])
    print("🎒 Inventário:", state["inv"])

    print("\n👥 SITUAÇÃO DOS PERSONAGENS:")

    print("Milo:", "VIVO" if state["milo_vivo"] else "MORTO")
    print("Barbara:", "VIVA" if state["barbara_viva"] else "MORTA")
    print(
        "Olivier:",
        "VIVO" if state["olivier_vivo"] else "MORTO"
    )
    print(
        "Amelie:",
        "VIVA" if state["amelie_viva"] else "MORTA"
    )

    return "fim"


# ============================================================
# CENAS
# ============================================================

cenas = {

    "fase1": fase1,
    "fase2": fase2,
    "fase3": fase3,
    "fase4": fase4,
    "fase5": fase5,
    "fase6": fase6,
    "fase7": fase7,
    "fase8": fase8,
    "fase9": fase9,
    "fase10": fase10,
    "fase11": fase11,
    "fase12": fase12,
    "fase13": fase13,
    "fase14": fase14,
    "fase15": fase15,
    "fase16": fase16,
    "fase17": fase17,
    "fase18": fase18,
    "fase19": fase19,
    "fase20": fase20,
    "fase21": fase21,
    "fase22": fase22,
    "fase23": fase23,
    "fase24": fase24,
    "fase25": fase25,
    "fase26": fase26,
    "fase27": fase27,
    "fase28": fase28,
    "fase29": fase29,
    "fase30": fase30
}


# ============================================================
# COMEÇAR O JOGO
# ============================================================

cena = "fase1"

while cena != "fim":
    cena = cenas[cena]
    cena = cena()

print("TESTE DO JOGO FUNCIONOU!")

