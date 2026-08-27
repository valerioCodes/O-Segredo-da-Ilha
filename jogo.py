from js import document, window

# ============================================================
# 🏝️ O SEGREDO NA ILHA
# ============================================================

# ------------------------------------------------------------
# ELEMENTOS DA TELA
# ------------------------------------------------------------

tela = document.getElementById("jogo")
imagem = document.getElementById("imagem-fase")
botoes = document.getElementById("botoes")
status = document.getElementById("status")


# ============================================================
# FUNÇÕES DA TELA
# ============================================================

def limpar_tela():
    tela.innerHTML = ""


def limpar_botoes():
    botoes.innerHTML = ""


def mostrar(texto):
    bloco = document.createElement("div")
    bloco.className = "texto-jogo"
    bloco.innerHTML = str(texto).replace("\n", "<br>")
    tela.appendChild(bloco)


def mudar_imagem(nome):
    imagem.src = nome
    imagem.style.display = "block"


def imagem_fase(numero):
    mudar_imagem(f"fase_{numero:02d}.png")


def atualizar_status():
    status.innerHTML = (
        f"❤️ Vida: {state['vida']} &nbsp;&nbsp; "
        f"🧠 Sanidade: {state['sanidade']} &nbsp;&nbsp; "
        f"🔎 Pistas: {state['pistas']} &nbsp;&nbsp; "
        f"🎒 Itens: {len(state['inv'])}"
    )


def preparar_fase(numero):
    limpar_tela()
    limpar_botoes()

    # Só existem imagens até a fase 20
    if numero <= 20:
        imagem_fase(numero)
    else:
        imagem.style.display = "none"

    atualizar_status()


def escolher(msg, opcoes):

    limpar_botoes()

    mostrar(msg)

    resposta = window.prompt(
        msg + "\n\n" + " | ".join(opcoes)
    )

    if resposta is None:
        resposta = opcoes[0]

    resposta = str(resposta).strip().lower()

    limpar_botoes()

    return resposta


# ============================================================
# ESTADO
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
# FUNÇÕES DO JOGO
# ============================================================

def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)
        mostrar("🎒 Você encontrou: " + item)


def perder_vida(qtd=1):
    state["vida"] -= qtd
    atualizar_status()
    mostrar("❤️ Vida: " + str(state["vida"]))

    return state["vida"] <= 0


def perder_sanidade(qtd=1):
    state["sanidade"] -= qtd
    atualizar_status()
    mostrar("🧠 Sanidade: " + str(state["sanidade"]))

    return state["sanidade"] <= 0


def personagem_secundario():
    if state["personagem"] == "Olivier":
        return "Amelie"
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
# FASE 1
# ============================================================

def fase1():

    preparar_fase(1)

    mostrar("""
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
        "Escolha seu personagem:",
        ["1) Olivier", "2) Amelie"]
    )

    if op.startswith("1"):
        state["personagem"] = "Olivier"
    else:
        state["personagem"] = "Amelie"

    mostrar(f"""
Você escolheu {state["personagem"]}.

A viagem para a ilha começa.
""")

    atualizar_status()

    return "fase2"


# ============================================================
# FASE 2
# ============================================================

def fase2():

    preparar_fase(2)

    mostrar("""
============================================================
🚢 FASE 2 - A VIAGEM
============================================================

O barco atravessa o mar durante horas.

A ilha aparece no horizonte.

Durante a viagem, ninguém fala muito sobre o passado.
""")

    mostrar(f"""
{state["personagem"]}:
— Por que todo mundo está evitando falar sobre essa ilha?

Um familiar responde:

— Porque o que aconteceu lá não foi algo normal.

{state["personagem"]}:
— E o que aconteceu?

Familiar:
— Quando chegarmos, você vai entender.

O barco chega ao porto.

A aventura começa.
""")

    return "fase3"


# ============================================================
# FASE 3
# ============================================================

def fase3():

    preparar_fase(3)

    mostrar("""
============================================================
🏝️ FASE 3 - CHEGADA
============================================================

A ilha parece pequena, mas existe uma grande floresta
ao redor da vila.

Alguns moradores observam vocês.

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
        "Escolha:",
        [
            "1) Perguntar sobre a ilha",
            "2) Perguntar sobre sua família",
            "3) Perguntar sobre os desaparecimentos"
        ]
    )

    if op.startswith("1"):

        mostrar("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")

        state["confianca_milo"] += 1

    elif op.startswith("2"):

        mostrar("""
Você:
— Vocês conhecem minha família?

Barbara:
— O sobrenome de vocês é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")

        state["pistas"] += 2

    else:

        mostrar("""
Você:
— É verdade que pessoas desapareceram?

Milo:
— Sim.

Barbara:
— E algumas nunca foram encontradas.
""")

        state["pistas"] += 1

    atualizar_status()

    return "fase4"


# ============================================================
# FASE 4
# ============================================================

def fase4():

    preparar_fase(4)

    mostrar("""
============================================================
🏘️ FASE 4 - A VILA
============================================================

Milo mostra a vila.

Existem três lugares importantes:

⛪ Uma igreja antiga.

🏚️ Uma casa abandonada.

🔦 Um farol.
""")

    op = escolher(
        "Para onde você vai?",
        [
            "1) Igreja",
            "2) Casa abandonada",
            "3) Farol"
        ]
    )

    if op.startswith("1"):
        return "fase5"

    if op.startswith("2"):
        return "fase6"

    return "fase7"


# ============================================================
# FASE 5
# ============================================================

def fase5():

    preparar_fase(5)

    mostrar("""
============================================================
⛪ FASE 5 - A IGREJA
============================================================

A igreja está abandonada.

Nas paredes existem símbolos estranhos.

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
        "O que fazer?",
        [
            "1) Examinar os símbolos",
            "2) Procurar documentos",
            "3) Fotografar os símbolos"
        ]
    )

    if op.startswith("1"):

        mostrar("Você percebe que os símbolos formam um mapa.")
        state["pistas"] += 2

    elif op.startswith("2"):

        pegar("livro antigo")
        state["pistas"] += 3

    else:

        pegar("fotografia dos símbolos")
        state["pistas"] += 1

    atualizar_status()

    return "fase8"


# ============================================================
# FASE 6
# ============================================================

def fase6():

    preparar_fase(6)

    mostrar("""
============================================================
🏚️ FASE 6 - CASA ABANDONADA
============================================================

A casa está coberta de poeira.

Mesmo assim, alguns objetos parecem ter sido usados
recentemente.

Milo:
— Eu não gosto desse lugar.

Barbara:
— Você nunca gosta de lugar nenhum.

Milo:
— Porque normalmente eu estou certo.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Procurar documentos",
            "2) Subir as escadas",
            "3) Ir ao porão"
        ]
    )

    if op.startswith("1"):

        pegar("documentos da família")
        state["pistas"] += 3

    elif op.startswith("2"):

        pegar("chave enferrujada")
        state["pistas"] += 2
        perder_sanidade()

    else:

        pegar("fotografia antiga")
        state["pistas"] += 3

    atualizar_status()

    return "fase8"


# ============================================================
# FASE 7
# ============================================================

def fase7():

    preparar_fase(7)

    mostrar("""
============================================================
🔦 FASE 7 - O FAROL
============================================================

No topo do farol existe uma caixa escondida.

Você encontra uma fotografia antiga.

Nela está parte da sua família.

Ao fundo aparece uma criatura que você não reconhece.
""")

    pegar("fotografia da criatura")

    state["pistas"] += 3

    mostrar("""
Milo:
— Isso estava na fotografia?

Barbara:
— Não deveria existir.
""")

    atualizar_status()

    return "fase8"


# ============================================================
# FASE 8
# ============================================================

def fase8():

    preparar_fase(8)

    mostrar("""
============================================================
🌙 FASE 8 - PRIMEIRA NOITE
============================================================

Durante a noite, vocês escutam três batidas.

TOC.

TOC.

TOC.

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
        "O que fazer?",
        [
            "1) Abrir a janela",
            "2) Ignorar",
            "3) Sair pela porta"
        ]
    )

    if op.startswith("1"):

        mostrar("""
Não existe ninguém do lado de fora.

Mas há marcas enormes no chão.
""")

        state["pistas"] += 2
        perder_sanidade()

    elif op.startswith("2"):

        mostrar("As batidas param depois de alguns minutos.")
        state["pistas"] += 1

    else:

        mostrar("""
Vocês saem.

Barbara:
— Olhem para o chão.

Existem pegadas enormes.
""")

        state["pistas"] += 3

    atualizar_status()

    return "fase9"


# ============================================================
# FASE 9
# ============================================================

def fase9():

    preparar_fase(9)

    mostrar("""
============================================================
🚨 FASE 9 - O DESAPARECIMENTO
============================================================

Na manhã seguinte, um morador desapareceu.

Os moradores estão assustados.

Milo:
— Ele estava aqui ontem.

Barbara:
— Então precisamos encontrá-lo.

Milo:
— Antes que seja tarde.
""")

    op = escolher(
        "Onde procurar?",
        [
            "1) Procurar na vila",
            "2) Procurar na floresta"
        ]
    )

    if op.startswith("1"):

        state["pistas"] += 1
        mostrar("Você encontra marcas perto da floresta.")

    else:

        state["pistas"] += 2
        mostrar("Vocês encontram pegadas enormes.")

    atualizar_status()

    return "fase10"


# ============================================================
# FASE 10
# ============================================================

def fase10():

    preparar_fase(10)

    mostrar("""
============================================================
🔎 FASE 10 - A INVESTIGAÇÃO
============================================================

Vocês seguem as pistas pela floresta.

Depois de algum tempo encontram um objeto pertencente
ao desaparecido.
""")

    pegar("objeto do desaparecido")

    mostrar("""
Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    state["pistas"] += 2

    atualizar_status()

    return "fase11"


# ============================================================
# FASE 11
# ============================================================

def fase11():

    preparar_fase(11)

    mostrar("""
============================================================
🌲 FASE 11 - A FLORESTA
============================================================

A floresta fica cada vez mais escura.

Vocês encontram uma trilha escondida.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Seguir a trilha",
            "2) Marcar o caminho e voltar",
            "3) Separar o grupo"
        ]
    )

    if op.startswith("1"):

        state["pistas"] += 2

    elif op.startswith("2"):

        state["pistas"] += 1

    else:

        mostrar("""
Milo:
— Não acho uma boa ideia.

Barbara:
— Concordo.

Você decide seguir sozinho.
""")

        perder_sanidade()

    atualizar_status()

    return "fase12"


# ============================================================
# FASE 12
# ============================================================

def fase12():

    preparar_fase(12)

    mostrar("""
============================================================
🔥 FASE 12 - ACAMPAMENTO
============================================================

Vocês montam um pequeno acampamento.

Durante a noite, conversam sobre a criatura.

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
        "O que fazer?",
        [
            "1) Conversar com Milo",
            "2) Conversar com Barbara",
            "3) Dormir"
        ]
    )

    if op.startswith("1"):

        state["confianca_milo"] += 2

    elif op.startswith("2"):

        state["confianca_barbara"] += 2

    else:

        mostrar("Você descansa e recupera um pouco da sanidade.")
        state["sanidade"] += 1

    atualizar_status()

    return "fase13"


# ============================================================
# FASE 13
# ============================================================

def fase13():

    preparar_fase(13)

    mostrar("""
============================================================
🐾 FASE 13 - PEGADAS
============================================================

Na manhã seguinte, vocês encontram pegadas gigantes.

Elas parecem ter sido feitas recentemente.

Barbara:
— Isso é grande demais.

Milo:
— E está indo naquela direção.

Você:
— Então vamos descobrir o que fez isso.
""")

    state["pistas"] += 3

    atualizar_status()

    return "fase14"


# ============================================================
# FASE 14
# ============================================================

def fase14():

    preparar_fase(14)

    mostrar("""
============================================================
🏚️ FASE 14 - A CABANA
============================================================

Uma pequena cabana aparece no meio da floresta.

Dentro há um diário.
""")

    pegar("diário")

    mostrar("""
No diário está escrito:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma forma de derrotar essa coisa.

Milo:
— Precisamos descobrir qual.
""")

    state["pistas"] += 3

    atualizar_status()

    return "fase15"


# ============================================================
# FASE 15
# ============================================================

def fase15():

    preparar_fase(15)

    mostrar("""
============================================================
📖 FASE 15 - O DIÁRIO
============================================================

Vocês leem o diário inteiro.

Ele fala sobre uma criatura que vive escondida
nas profundezas da ilha.

O diário também menciona:

"Quando a criatura for ferida pelo símbolo original,
ela ficará vulnerável."
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
Milo:
— Então precisamos encontrar esse símbolo.

Barbara:
— E alguma coisa capaz de usá-lo.
""")

    atualizar_status()

    return "fase16"


# ============================================================
# FASE 16
# ============================================================

def fase16():

    preparar_fase(16)

    mostrar("""
============================================================
🎒 FASE 16 - PREPARAÇÃO
============================================================

Vocês precisam encontrar equipamentos antes de continuar.
""")

    op = escolher(
        "O que procurar?",
        [
            "1) Procurar uma arma",
            "2) Procurar medicamentos",
            "3) Procurar o símbolo"
        ]
    )

    if op.startswith("1"):

        pegar("arma")
        state["pistas"] += 1

    elif op.startswith("2"):

        pegar("medicamento")

    else:

        pegar("símbolo antigo")
        state["pistas"] += 3

    atualizar_status()

    return "fase17"


# ============================================================
# FASE 17
# ============================================================

def fase17():

    preparar_fase(17)

    mostrar("""
============================================================
🌊 FASE 17 - O LAGO
============================================================

O mapa indica que o próximo símbolo está perto de um lago.

Barbara:
— Eu não gosto desse lugar.

Milo:
— Então somos dois.

Você:
— Precisamos continuar.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Procurar dentro da água",
            "2) Procurar ao redor do lago",
            "3) Ignorar o lago"
        ]
    )

    if op.startswith("1"):

        perder_vida()
        pegar("cristal")
        state["pistas"] += 2

    elif op.startswith("2"):

        pegar("cristal")
        state["pistas"] += 2

    else:

        state["pistas"] += 1

    atualizar_status()

    return "fase18"


# ============================================================
# FASE 18
# ============================================================

def fase18():

    preparar_fase(18)

    mostrar("""
============================================================
🕳️ FASE 18 - A CAVERNA
============================================================

O cristal aponta para uma caverna escondida.

Milo:
— Acho que estamos perto.

Barbara:
— Perto demais.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Entrar",
            "2) Procurar outra entrada"
        ]
    )

    if op.startswith("1"):

        state["pistas"] += 3

    else:

        state["pistas"] += 1

    atualizar_status()

    return "fase19"


# ============================================================
# FASE 19
# ============================================================

def fase19():

    preparar_fase(19)

    mostrar("""
============================================================
👹 FASE 19 - O PRIMEIRO ENCONTRO
============================================================

Um rugido ecoa pela caverna.

A criatura aparece por alguns segundos.

Ela é enorme e desaparece rapidamente.

Milo:
— CORRE!

Barbara:
— AGORA!

Vocês fogem antes que ela alcance o grupo.
""")

    perder_sanidade()

    return "fase20"


# ============================================================
# FASE 20
# ============================================================

def fase20():

    preparar_fase(20)

    mostrar("""
============================================================
🏃 FASE 20 - FUGA DO MONSTRO
============================================================

A criatura começa a perseguir vocês.
""")

    op = escolher(
        "Para onde correr?",
        [
            "1) Correr para a esquerda",
            "2) Correr para a direita",
            "3) Se esconder"
        ]
    )

    if op.startswith("1"):

        mostrar("Vocês encontram uma saída.")
        state["pistas"] += 1

    elif op.startswith("2"):

        mostrar("Vocês encontram uma sala escondida.")
        state["pistas"] += 2

    else:

        mostrar("Vocês conseguem se esconder.")
        state["sanidade"] += 1

    atualizar_status()

    return "fase21"


# ============================================================
# FASE 21
# ============================================================

def fase21():

    preparar_fase(21)

    mostrar("""
============================================================
🔎 FASE 21 - A FRAQUEZA
============================================================

Na sala escondida, vocês encontram uma inscrição.

Ela revela que o monstro pode ser ferido pelo símbolo
original da ilha.

Barbara:
— Então podemos derrotá-lo.

Milo:
— Sim.

Você:
— Mas precisamos chegar perto dele.
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    atualizar_status()

    return "fase22"


# ============================================================
# FASE 22
# ============================================================

def fase22():

    preparar_fase(22)

    mostrar("""
============================================================
🏚️ FASE 22 - O ESCONDERIJO
============================================================

Vocês descobrem que a criatura possui um esconderijo
abaixo da ilha.

Milo:
— É lá que ela fica.

Barbara:
— Então é lá que vamos.

Você:
— Vamos acabar com isso.
""")

    return "fase23"


# ============================================================
# FASE 23
# ============================================================

def fase23():

    preparar_fase(23)

    mostrar("""
============================================================
🆘 FASE 23 - O RESGATE
============================================================

Vocês encontram o morador desaparecido.

Ele está ferido, mas vivo.

Morador:
— Vocês precisam ir embora!

Você:
— O que aconteceu?

Morador:
— Ela está acordada.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Levar o homem embora",
            "2) Deixá-lo escondido"
        ]
    )

    if op.startswith("1"):

        mostrar("Vocês levam o homem para um local seguro.")

    else:

        mostrar("Vocês o escondem em uma área protegida.")

    state["pistas"] += 1

    atualizar_status()

    return "fase24"


# ============================================================
# FASE 24
# ============================================================

def fase24():

    preparar_fase(24)

    mostrar("""
============================================================
🚪 FASE 24 - A ENTRADA
============================================================

Vocês encontram uma porta enorme no subterrâneo.

Ela possui o símbolo original.
""")

    if "símbolo antigo" in state["inv"]:

        mostrar("""
O símbolo que vocês encontraram encaixa na porta.

Ela se abre.
""")

        state["pistas"] += 3

    else:

        mostrar("""
Vocês precisam forçar a porta.

Isso faz um grande barulho.
""")

        perder_vida()

    atualizar_status()

    return "fase25"


# ============================================================
# FASE 25
# ============================================================

def fase25():

    preparar_fase(25)

    mostrar("""
============================================================
📜 FASE 25 - O PASSADO DA FAMÍLIA
============================================================

Dentro do esconderijo existem documentos.

Eles revelam que sua família já encontrou a criatura
no passado.

Seu parente desaparecido tentou impedir que ela
fosse libertada.

Barbara:
— Então ele estava tentando proteger a ilha.

Milo:
— E ninguém contou isso para vocês.

Você:
— Agora eu sei por quê.
""")

    state["pistas"] += 4

    atualizar_status()

    return "fase26"


# ============================================================
# FASE 26
# ============================================================

def fase26():

    preparar_fase(26)

    mostrar("""
============================================================
⚔️ FASE 26 - PREPARAÇÃO
============================================================

Antes da batalha, vocês precisam decidir como agir.
""")

    op = escolher(
        "O que fazer?",
        [
            "1) Preparar a arma",
            "2) Preparar o símbolo",
            "3) Procurar mais informações"
        ]
    )

    if op.startswith("1"):

        if "arma" in state["inv"]:

            mostrar("A arma está pronta.")
            state["batalha"] += 1

        else:

            mostrar("Vocês não possuem uma arma adequada.")

    elif op.startswith("2"):

        if "símbolo antigo" in state["inv"]:

            mostrar("O símbolo está pronto.")
            state["batalha"] += 2

        else:

            mostrar("Vocês não encontraram o símbolo.")

    else:

        mostrar("""
Vocês descobrem uma informação importante:

A criatura fica mais fraca quando o símbolo é ativado.
""")

        state["monstro_fraqueza"] = True
        state["batalha"] += 2

    atualizar_status()

    return "fase27"


# ============================================================
# FASE 27
# ============================================================

def fase27():

    preparar_fase(27)

    mostrar("""
============================================================
👹 FASE 27 - O MONSTRO
============================================================

Vocês chegam à última sala.

A criatura está esperando.

Ela é muito maior do que parecia antes.

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
# FASE 28
# ============================================================

def fase28():

    preparar_fase(28)

    mostrar("""
============================================================
⚔️ FASE 28 - BATALHA CONTRA O MONSTRO
============================================================

A criatura ataca.

Vocês precisam agir rápido.
""")

    op = escolher(
        "Escolha uma ação:",
        [
            "1) Atacar o monstro",
            "2) Ativar o símbolo",
            "3) Ajudar Milo",
            "4) Ajudar Barbara"
        ]
    )

    if op.startswith("1"):

        if "arma" in state["inv"] and state["monstro_fraqueza"]:

            mostrar("""
Você ataca a criatura no ponto fraco.

Ela recua.
""")

            state["batalha"] += 3

        else:

            mostrar("""
Seu ataque não causa muito efeito.

A criatura contra-ataca.
""")

            perder_vida()

    elif op.startswith("2"):

        if "símbolo antigo" in state["inv"]:

            mostrar("""
Você ativa o símbolo.

A criatura começa a enfraquecer.
""")

            state["batalha"] += 4

        else:

            mostrar("""
Você tenta ativar o símbolo.

Mas não possui o objeto necessário.
""")

            perder_sanidade()

    elif op.startswith("3"):

        if state["milo_vivo"]:

            mostrar("""
Você salva Milo de um ataque.

Milo:
— Obrigado!

Ele consegue atacar a criatura.
""")

            state["confianca_milo"] += 2
            state["batalha"] += 2

        else:

            mostrar("Milo não está mais aqui.")

    else:

        if state["barbara_viva"]:

            mostrar("""
Você ajuda Barbara.

Barbara:
— Eu sabia que podia confiar em você!

Ela encontra uma abertura.
""")

            state["confianca_barbara"] += 2
            state["batalha"] += 2

        else:

            mostrar("Barbara não está mais aqui.")

    atualizar_status()

    return "fase29"


# ============================================================
# FASE 29
# ============================================================

def fase29():

    preparar_fase(29)

    mostrar("""
============================================================
🔥 FASE 29 - ÚLTIMA ESCOLHA
============================================================

A criatura está ferida.

Mas ainda não foi derrotada.

Você tem uma última oportunidade.

Milo:
— Se atacarmos juntos, talvez consigamos.

Barbara:
— Ou podemos tentar selar a criatura novamente.
""")

    op = escolher(
        "Qual será sua decisão?",
        [
            "1) Derrotar o monstro",
            "2) Selar o monstro",
            "3) Fugir"
        ]
    )

    if op.startswith("1"):

        if state["batalha"] >= 5:

            state["monstro_derrotado"] = True

        else:

            state["monstro_derrotado"] = False

            mostrar("""
Vocês atacam.

Mas não conseguiram enfraquecer a criatura o suficiente.
""")

    elif op.startswith("2"):

        state["monstro_derrotado"] = False
        state["batalha"] = max(state["batalha"], 3)

        mostrar("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

    else:

        state["monstro_derrotado"] = False
        state["vida"] = max(state["vida"], 1)

        mostrar("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

    atualizar_status()

    return "fase30"


# ============================================================
# FASE 30 - OS 5 FINAIS
# ============================================================

def fase30():

    limpar_tela()
    limpar_botoes()

    imagem.style.display = "block"

    vivos = companheiros_vivos()

    # ========================================================
    # FINAL 1 - PERFEITO
    # ========================================================

    if state["monstro_derrotado"] and len(vivos) >= 3:

        mudar_imagem("final_01.png")

        mostrar("""
============================================================
🌟 FINAL PERFEITO
============================================================

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
    # FINAL 2 - VITÓRIA
    # ========================================================

    elif state["monstro_derrotado"]:

        mudar_imagem("final_02.png")

        mostrar("""
============================================================
🌅 FINAL DA VITÓRIA
============================================================

A criatura foi derrotada.

Mas nem todos conseguiram sobreviver.

Os sobreviventes deixam a ilha sabendo que nunca
esquecerão aqueles que ficaram para trás.
""")

        mostrar(
            "Sobreviventes: " + ", ".join(vivos)
        )

    # ========================================================
    # FINAL 3 - SELAMENTO
    # ========================================================

    elif state["batalha"] >= 3:

        mudar_imagem("final_03.png")

        mostrar("""
============================================================
👁️ FINAL DO SELAMENTO
============================================================

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

        mudar_imagem("final_06.png")

        mostrar("""
============================================================
🏃 FINAL DA FUGA
============================================================

Vocês conseguem chegar ao barco.

A ilha fica para trás.

Mas, quando vocês olham para o mar...

A criatura aparece na costa.

Ela observa o barco partir.

Ela ainda está viva.
""")

    # ========================================================
    # FINAL 5 - ILHA
    # ========================================================

    else:

        mudar_imagem(
            "Gemini_Generated_Image_I0ib9910ib9910ib.png"
        )

        mostrar("""
============================================================
💀 FINAL DA ILHA
============================================================

A criatura vence.

Ninguém consegue escapar.

O segredo permanece enterrado na ilha.
""")

    mostrar("""
============================================================
🎮 FIM DO JOGO
============================================================
""")

    mostrar(
        "👤 Personagem: " + state["personagem"]
    )

    mostrar(
        "❤️ Vida: " + str(state["vida"])
    )

    mostrar(
        "🧠 Sanidade: " + str(state["sanidade"])
    )

    mostrar(
        "🔎 Pistas: " + str(state["pistas"])
    )

    mostrar(
        "🎒 Inventário: " + ", ".join(state["inv"])
    )

    mostrar("""
👥 SITUAÇÃO DOS PERSONAGENS:
""")

    mostrar(
        "Milo: " +
        ("VIVO" if state["milo_vivo"] else "MORTO")
    )

    mostrar(
        "Barbara: " +
        ("VIVA" if state["barbara_viva"] else "MORTA")
    )

    mostrar(
        "Olivier: " +
        ("VIVO" if state["olivier_vivo"] else "MORTO")
    )

    mostrar(
        "Amelie: " +
        ("VIVA" if state["amelie_viva"] else "MORTA")
    )

    atualizar_status()

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
# INICIAR
# ============================================================

cena = "fase1"

while cena != "fim":

    funcao = cenas[cena]

    cena = funcao()
