from js import document


# ============================================================
# ELEMENTOS DA TELA
# ============================================================

tela = document.getElementById("jogo")
imagem = document.getElementById("imagem-fase")
botoes = document.getElementById("botoes")
status = document.getElementById("status")


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
        f"❤️ Vida: {state['vida']} "
        f"&nbsp;&nbsp; "
        f"🧠 Sanidade: {state['sanidade']} "
        f"&nbsp;&nbsp; "
        f"🔎 Pistas: {state['pistas']} "
        f"&nbsp;&nbsp; "
        f"🎒 Itens: {len(state['inv'])}"
    )


def preparar_fase(numero):

    limpar_tela()
    limpar_botoes()

    if numero <= 20:
        imagem_fase(numero)
    else:
        imagem.style.display = "none"

    atualizar_status()


# ============================================================
# BOTÕES
# ============================================================

def criar_botao(texto, funcao):

    botao = document.createElement("button")

    botao.className = "opcao"

    botao.innerText = texto

    botao.onclick = funcao

    botoes.appendChild(botao)


# ============================================================
# INVENTÁRIO
# ============================================================

def pegar(item):

    if item not in state["inv"]:

        state["inv"].append(item)

        mostrar("🎒 Você encontrou: " + item)

        atualizar_status()


# ============================================================
# VIDA
# ============================================================

def perder_vida(qtd=1):

    state["vida"] -= qtd

    if state["vida"] < 0:
        state["vida"] = 0

    atualizar_status()

    mostrar(
        "❤️ Você perdeu "
        + str(qtd)
        + " ponto(s) de vida."
    )


# ============================================================
# SANIDADE
# ============================================================

def perder_sanidade(qtd=1):

    state["sanidade"] -= qtd

    if state["sanidade"] < 0:
        state["sanidade"] = 0

    atualizar_status()

    mostrar(
        "🧠 Você perdeu "
        + str(qtd)
        + " ponto(s) de sanidade."
    )


# ============================================================
# COMPANHEIROS
# ============================================================

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
🏝️ O SEGREDO NA ILHA

Há muitos anos, um membro da sua família desapareceu
misteriosamente em uma ilha distante.

O caso nunca foi solucionado.

Recentemente, sua família encontrou documentos antigos
que podem revelar o que aconteceu.

Por isso, vocês decidiram viajar até a ilha.

Antes de começar, escolha seu personagem:
""")

    criar_botao(
        "👨 Olivier",
        escolher_olivier
    )

    criar_botao(
        "👩 Amelie",
        escolher_amelie
    )


def escolher_olivier(event=None):

    state["personagem"] = "Olivier"

    mostrar("""
Você escolheu Olivier.

A viagem para a ilha começa.
""")

    criar_botao(
        "➡️ Continuar",
        fase2
    )


def escolher_amelie(event=None):

    state["personagem"] = "Amelie"

    mostrar("""
Você escolheu Amelie.

A viagem para a ilha começa.
""")

    criar_botao(
        "➡️ Continuar",
        fase2
    )


# ============================================================
# FASE 2
# ============================================================

def fase2(event=None):

    preparar_fase(2)

    mostrar(f"""
🚢 FASE 2 - A VIAGEM

O barco atravessa o mar durante horas.

A ilha aparece no horizonte.

Durante a viagem, ninguém fala muito sobre o passado.

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

    criar_botao(
        "➡️ Chegar na ilha",
        fase3
    )


# ============================================================
# FASE 3
# ============================================================

def fase3(event=None):

    preparar_fase(3)

    mostrar("""
🏝️ FASE 3 - CHEGADA

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

    mostrar("Escolha o que perguntar:")

    criar_botao(
        "1️⃣ Perguntar sobre a ilha",
        fase3_ilha
    )

    criar_botao(
        "2️⃣ Perguntar sobre sua família",
        fase3_familia
    )

    criar_botao(
        "3️⃣ Perguntar sobre desaparecimentos",
        fase3_desaparecimentos
    )


def fase3_ilha(event=None):

    state["confianca_milo"] += 1

    mostrar("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")

    atualizar_status()

    criar_botao("➡️ Continuar", fase4)


def fase3_familia(event=None):

    state["pistas"] += 2

    mostrar("""
Você:
— Vocês conhecem minha família?

Barbara:
— O sobrenome de vocês é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")

    atualizar_status()

    criar_botao("➡️ Continuar", fase4)


def fase3_desaparecimentos(event=None):

    state["pistas"] += 1

    mostrar("""
Você:
— É verdade que pessoas desapareceram?

Milo:
— Sim.

Barbara:
— E algumas nunca foram encontradas.
""")

    atualizar_status()

    criar_botao("➡️ Continuar", fase4)


# ============================================================
# FASE 4
# ============================================================

def fase4(event=None):

    preparar_fase(4)

    mostrar("""
🏘️ FASE 4 - A VILA

Milo mostra a vila.

Existem três lugares importantes:

⛪ Uma igreja antiga.

🏚️ Uma casa abandonada.

🔦 Um farol.
""")

    criar_botao("⛪ Igreja", fase5)

    criar_botao("🏚️ Casa abandonada", fase6)

    criar_botao("🔦 Farol", fase7)


# ============================================================
# FASE 5
# ============================================================

def fase5(event=None):

    preparar_fase(5)

    mostrar("""
⛪ FASE 5 - A IGREJA

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

    criar_botao(
        "🔎 Examinar os símbolos",
        fase5_simbolos
    )

    criar_botao(
        "📜 Procurar documentos",
        fase5_documentos
    )

    criar_botao(
        "📷 Fotografar os símbolos",
        fase5_fotografia
    )


def fase5_simbolos(event=None):

    state["pistas"] += 2

    mostrar(
        "Você percebe que os símbolos formam um mapa."
    )

    atualizar_status()

    criar_botao("➡️ Continuar", fase8)


def fase5_documentos(event=None):

    pegar("livro antigo")

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase8)


def fase5_fotografia(event=None):

    pegar("fotografia dos símbolos")

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase8)


# ============================================================
# FASE 6
# ============================================================

def fase6(event=None):

    preparar_fase(6)

    mostrar("""
🏚️ FASE 6 - CASA ABANDONADA

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

    criar_botao(
        "📜 Procurar documentos",
        fase6_documentos
    )

    criar_botao(
        "⬆️ Subir as escadas",
        fase6_escadas
    )

    criar_botao(
        "⬇️ Ir ao porão",
        fase6_porao
    )


def fase6_documentos(event=None):

    pegar("documentos da família")

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase8)


def fase6_escadas(event=None):

    pegar("chave enferrujada")

    state["pistas"] += 2

    perder_sanidade()

    criar_botao("➡️ Continuar", fase8)


def fase6_porao(event=None):

    pegar("fotografia antiga")

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase8)


# ============================================================
# FASE 7
# ============================================================

def fase7(event=None):

    preparar_fase(7)

    mostrar("""
🔦 FASE 7 - O FAROL

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

    criar_botao("➡️ Continuar", fase8)


# ============================================================
# FASE 8
# ============================================================

def fase8(event=None):

    preparar_fase(8)

    mostrar("""
🌙 FASE 8 - PRIMEIRA NOITE

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

    criar_botao(
        "🪟 Abrir a janela",
        fase8_janela
    )

    criar_botao(
        "🤫 Ignorar",
        fase8_ignorar
    )

    criar_botao(
        "🚪 Sair pela porta",
        fase8_porta
    )


def fase8_janela(event=None):

    mostrar("""
Não existe ninguém do lado de fora.

Mas há marcas enormes no chão.
""")

    state["pistas"] += 2

    perder_sanidade()

    criar_botao("➡️ Continuar", fase9)


def fase8_ignorar(event=None):

    mostrar(
        "As batidas param depois de alguns minutos."
    )

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase9)


def fase8_porta(event=None):

    mostrar("""
Vocês saem.

Barbara:
— Olhem para o chão.

Existem pegadas enormes.
""")

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase9)


# ============================================================
# FASE 9
# ============================================================

def fase9(event=None):

    preparar_fase(9)

    mostrar("""
🚨 FASE 9 - O DESAPARECIMENTO

Na manhã seguinte, um morador desapareceu.

Os moradores estão assustados.

Milo:
— Ele estava aqui ontem.

Barbara:
— Então precisamos encontrá-lo.

Milo:
— Antes que seja tarde.
""")

    criar_botao(
        "🏘️ Procurar na vila",
        fase9_vila
    )

    criar_botao(
        "🌲 Procurar na floresta",
        fase9_floresta
    )


def fase9_vila(event=None):

    state["pistas"] += 1

    mostrar(
        "Você encontra marcas perto da floresta."
    )

    atualizar_status()

    criar_botao("➡️ Continuar", fase10)


def fase9_floresta(event=None):

    state["pistas"] += 2

    mostrar(
        "Vocês encontram pegadas enormes."
    )

    atualizar_status()

    criar_botao("➡️ Continuar", fase10)


# ============================================================
# FASE 10
# ============================================================

def fase10(event=None):

    preparar_fase(10)

    mostrar("""
🔎 FASE 10 - A INVESTIGAÇÃO

Vocês seguem as pistas pela floresta.

Depois de algum tempo encontram um objeto pertencente
ao desaparecido.
""")

    pegar("objeto do desaparecido")

    state["pistas"] += 2

    mostrar("""
Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    atualizar_status()

    criar_botao("➡️ Continuar", fase11)


# ============================================================
# FASE 11
# ============================================================

def fase11(event=None):

    preparar_fase(11)

    mostrar("""
🌲 FASE 11 - A FLORESTA

A floresta fica cada vez mais escura.

Vocês encontram uma trilha escondida.
""")

    criar_botao(
        "🌲 Seguir a trilha",
        fase11_trilha
    )

    criar_botao(
        "🪧 Marcar o caminho e voltar",
        fase11_voltar
    )

    criar_botao(
        "🚶 Separar o grupo",
        fase11_separar
    )


def fase11_trilha(event=None):

    state["pistas"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase12)


def fase11_voltar(event=None):

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase12)


def fase11_separar(event=None):

    mostrar("""
Milo:
— Não acho uma boa ideia.

Barbara:
— Concordo.

Você decide seguir sozinho.
""")

    perder_sanidade()

    criar_botao("➡️ Continuar", fase12)


# ============================================================
# FASE 12
# ============================================================

def fase12(event=None):

    preparar_fase(12)

    mostrar("""
🔥 FASE 12 - ACAMPAMENTO

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

    criar_botao(
        "🗣️ Conversar com Milo",
        fase12_milo
    )

    criar_botao(
        "🗣️ Conversar com Barbara",
        fase12_barbara
    )

    criar_botao(
        "😴 Dormir",
        fase12_dormir
    )


def fase12_milo(event=None):

    state["confianca_milo"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase13)


def fase12_barbara(event=None):

    state["confianca_barbara"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase13)


def fase12_dormir(event=None):

    state["sanidade"] += 1

    mostrar(
        "Você descansa e recupera um pouco da sanidade."
    )

    atualizar_status()

    criar_botao("➡️ Continuar", fase13)


# ============================================================
# FASE 13
# ============================================================

def fase13(event=None):

    preparar_fase(13)

    mostrar("""
🐾 FASE 13 - PEGADAS

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

    criar_botao("➡️ Continuar", fase14)


# ============================================================
# FASE 14
# ============================================================

def fase14(event=None):

    preparar_fase(14)

    mostrar("""
🏚️ FASE 14 - A CABANA

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

    criar_botao("➡️ Continuar", fase15)


# ============================================================
# FASE 15
# ============================================================

def fase15(event=None):

    preparar_fase(15)

    mostrar("""
📖 FASE 15 - O DIÁRIO

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

    criar_botao("➡️ Continuar", fase16)


# ============================================================
# FASE 16
# ============================================================

def fase16(event=None):

    preparar_fase(16)

    mostrar("""
🎒 FASE 16 - PREPARAÇÃO

Vocês precisam encontrar equipamentos antes de continuar.
""")

    criar_botao(
        "⚔️ Procurar uma arma",
        fase16_arma
    )

    criar_botao(
        "💊 Procurar medicamentos",
        fase16_medicamento
    )

    criar_botao(
        "🔱 Procurar o símbolo",
        fase16_simbolo
    )


def fase16_arma(event=None):

    pegar("arma")

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase17)


def fase16_medicamento(event=None):

    pegar("medicamento")

    atualizar_status()

    criar_botao("➡️ Continuar", fase17)


def fase16_simbolo(event=None):

    pegar("símbolo antigo")

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase17)


# ============================================================
# FASE 17
# ============================================================

def fase17(event=None):

    preparar_fase(17)

    mostrar("""
🌊 FASE 17 - O LAGO

O mapa indica que o próximo símbolo está perto de um lago.

Barbara:
— Eu não gosto desse lugar.

Milo:
— Então somos dois.

Você:
— Precisamos continuar.
""")

    criar_botao(
        "🌊 Procurar dentro da água",
        fase17_agua
    )

    criar_botao(
        "🔎 Procurar ao redor do lago",
        fase17_redor
    )

    criar_botao(
        "🚶 Ignorar o lago",
        fase17_ignorar
    )


def fase17_agua(event=None):

    perder_vida()

    pegar("cristal")

    state["pistas"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase18)


def fase17_redor(event=None):

    pegar("cristal")

    state["pistas"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase18)


def fase17_ignorar(event=None):

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase18)


# ============================================================
# FASE 18
# ============================================================

def fase18(event=None):

    preparar_fase(18)

    mostrar("""
🕳️ FASE 18 - A CAVERNA

O cristal aponta para uma caverna escondida.

Milo:
— Acho que estamos perto.

Barbara:
— Perto demais.
""")

    criar_botao(
        "🕳️ Entrar",
        fase18_entrar
    )

    criar_botao(
        "🔎 Procurar outra entrada",
        fase18_outra
    )


def fase18_entrar(event=None):

    state["pistas"] += 3

    atualizar_status()

    criar_botao("➡️ Continuar", fase19)


def fase18_outra(event=None):

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase19)


# ============================================================
# FASE 19
# ============================================================

def fase19(event=None):

    preparar_fase(19)

    mostrar("""
👹 FASE 19 - O PRIMEIRO ENCONTRO

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

    criar_botao("➡️ Continuar", fase20)


# ============================================================
# FASE 20
# ============================================================

def fase20(event=None):

    preparar_fase(20)

    mostrar("""
🏃 FASE 20 - FUGA DO MONSTRO

A criatura começa a perseguir vocês.
""")

    criar_botao(
        "⬅️ Correr para a esquerda",
        fase20_esquerda
    )

    criar_botao(
        "➡️ Correr para a direita",
        fase20_direita
    )

    criar_botao(
        "🙈 Se esconder",
        fase20_esconder
    )


def fase20_esquerda(event=None):

    mostrar("Vocês encontram uma saída.")

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase21)


def fase20_direita(event=None):

    mostrar("Vocês encontram uma sala escondida.")

    state["pistas"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase21)


def fase20_esconder(event=None):

    mostrar("Vocês conseguem se esconder.")

    state["sanidade"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase21)


# ============================================================
# FASE 21
# ============================================================

def fase21(event=None):

    preparar_fase(21)

    mostrar("""
🔎 FASE 21 - A FRAQUEZA

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

    criar_botao("➡️ Continuar", fase22)


# ============================================================
# FASE 22
# ============================================================

def fase22(event=None):

    preparar_fase(22)

    mostrar("""
🏚️ FASE 22 - O ESCONDERIJO

Vocês descobrem que a criatura possui um esconderijo
abaixo da ilha.

Milo:
— É lá que ela fica.

Barbara:
— Então é lá que vamos.

Você:
— Vamos acabar com isso.
""")

    criar_botao("➡️ Continuar", fase23)


# ============================================================
# FASE 23
# ============================================================

def fase23(event=None):

    preparar_fase(23)

    mostrar("""
🆘 FASE 23 - O RESGATE

Vocês encontram o morador desaparecido.

Ele está ferido, mas vivo.

Morador:
— Vocês precisam ir embora!

Você:
— O que aconteceu?

Morador:
— Ela está acordada.
""")

    criar_botao(
        "🚶 Levar o homem embora",
        fase23_levar
    )

    criar_botao(
        "🫥 Deixá-lo escondido",
        fase23_esconder
    )


def fase23_levar(event=None):

    mostrar(
        "Vocês levam o homem para um local seguro."
    )

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase24)


def fase23_esconder(event=None):

    mostrar(
        "Vocês o escondem em uma área protegida."
    )

    state["pistas"] += 1

    atualizar_status()

    criar_botao("➡️ Continuar", fase24)


# ============================================================
# FASE 24
# ============================================================

def fase24(event=None):

    preparar_fase(24)

    mostrar("""
🚪 FASE 24 - A ENTRADA

Vocês encontram uma porta enorme no subterrâneo.

Ela possui o símbolo original.
""")

    if "símbolo antigo" in state["inv"]:

        mostrar("""
O símbolo que vocês encontraram encaixa na porta.

Ela se abre.
""")

        state["pistas"] += 3

        atualizar_status()

        criar_botao("➡️ Entrar", fase25)

    else:

        mostrar("""
Vocês precisam forçar a porta.

Isso faz um grande barulho.
""")

        perder_vida()

        criar_botao("➡️ Continuar", fase25)


# ============================================================
# FASE 25
# ============================================================

def fase25(event=None):

    preparar_fase(25)

    mostrar("""
📜 FASE 25 - O PASSADO DA FAMÍLIA

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

    criar_botao("➡️ Continuar", fase26)


# ============================================================
# FASE 26
# ============================================================

def fase26(event=None):

    preparar_fase(26)

    mostrar("""
⚔️ FASE 26 - PREPARAÇÃO

Antes da batalha, vocês precisam decidir como agir.
""")

    criar_botao(
        "⚔️ Preparar a arma",
        fase26_arma
    )

    criar_botao(
        "🔱 Preparar o símbolo",
        fase26_simbolo
    )

    criar_botao(
        "📖 Procurar mais informações",
        fase26_informacoes
    )


def fase26_arma(event=None):

    if "arma" in state["inv"]:

        mostrar("A arma está pronta.")

        state["batalha"] += 1

    else:

        mostrar(
            "Vocês não possuem uma arma adequada."
        )

    atualizar_status()

    criar_botao("➡️ Continuar", fase27)


def fase26_simbolo(event=None):

    if "símbolo antigo" in state["inv"]:

        mostrar("O símbolo está pronto.")

        state["batalha"] += 2

    else:

        mostrar(
            "Vocês não encontraram o símbolo."
        )

    atualizar_status()

    criar_botao("➡️ Continuar", fase27)


def fase26_informacoes(event=None):

    mostrar("""
Vocês descobrem uma informação importante:

A criatura fica mais fraca quando o símbolo é ativado.
""")

    state["monstro_fraqueza"] = True
    state["batalha"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase27)


# ============================================================
# FASE 27
# ============================================================

def fase27(event=None):

    preparar_fase(27)

    mostrar("""
👹 FASE 27 - O MONSTRO

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

    criar_botao("⚔️ Enfrentar a criatura", fase28)


# ============================================================
# FASE 28
# ============================================================

def fase28(event=None):

    preparar_fase(28)

    mostrar("""
⚔️ FASE 28 - BATALHA CONTRA O MONSTRO

A criatura ataca.

Vocês precisam agir rápido.
""")

    criar_botao(
        "⚔️ Atacar o monstro",
        fase28_atacar
    )

    criar_botao(
        "🔱 Ativar o símbolo",
        fase28_simbolo
    )

    criar_botao(
        "🛡️ Ajudar Milo",
        fase28_milo
    )

    criar_botao(
        "🛡️ Ajudar Barbara",
        fase28_barbara
    )


def fase28_atacar(event=None):

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

    atualizar_status()

    criar_botao("➡️ Continuar", fase29)


def fase28_simbolo(event=None):

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

    atualizar_status()

    criar_botao("➡️ Continuar", fase29)


def fase28_milo(event=None):

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

    atualizar_status()

    criar_botao("➡️ Continuar", fase29)


def fase28_barbara(event=None):

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

    criar_botao("➡️ Continuar", fase29)


# ============================================================
# FASE 29
# ============================================================

def fase29(event=None):

    preparar_fase(29)

    mostrar("""
🔥 FASE 29 - ÚLTIMA ESCOLHA

A criatura está ferida.

Mas ainda não foi derrotada.

Você tem uma última oportunidade.

Milo:
— Se atacarmos juntos, talvez consigamos.

Barbara:
— Ou podemos tentar selar a criatura novamente.
""")

    criar_botao(
        "⚔️ Derrotar o monstro",
        fase29_derrotar
    )

    criar_botao(
        "🔒 Selar o monstro",
        fase29_selar
    )

    criar_botao(
        "🏃 Fugir",
        fase29_fugir
    )


def fase29_derrotar(event=None):

    if state["batalha"] >= 5:

        state["monstro_derrotado"] = True

        mostrar("""
Vocês atacam juntos.

A criatura finalmente é derrotada!
""")

    else:

        state["monstro_derrotado"] = False

        mostrar("""
Vocês atacam.

Mas não conseguiram enfraquecer a criatura o suficiente.
""")

    atualizar_status()

    criar_botao("➡️ Descobrir o final", fase30)


def fase29_selar(event=None):

    state["monstro_derrotado"] = False

    state["batalha"] = max(
        state["batalha"],
        3
    )

    mostrar("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

    atualizar_status()

    criar_botao("➡️ Descobrir o final", fase30)


def fase29_fugir(event=None):

    state["monstro_derrotado"] = False

    state["vida"] = max(
        state["vida"],
        1
    )

    mostrar("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

    atualizar_status()

    criar_botao("➡️ Descobrir o final", fase30)


# ============================================================
# FASE 30 - FINAIS
# ============================================================

def fase30(event=None):

    limpar_tela()
    limpar_botoes()

    imagem.style.display = "block"

    vivos = companheiros_vivos()

    # ========================================================
    # FINAL 1
    # ========================================================

    if state["monstro_derrotado"] and len(vivos) >= 3:

        mudar_imagem("final_01.png")

        mostrar("""
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
    # FINAL 2
    # ========================================================

    elif state["monstro_derrotado"]:

        mudar_imagem("final_02.png")

        mostrar("""
🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Mas nem todos conseguiram sobreviver.

Os sobreviventes deixam a ilha sabendo que nunca
esquecerão aqueles que ficaram para trás.
""")

        mostrar(
            "Sobreviventes: " + ", ".join(vivos)
        )

    # ========================================================
    # FINAL 3
    # ========================================================

    elif state["batalha"] >= 3:

        mudar_imagem("final_03.png")

        mostrar("""
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
    # FINAL 4
    # ========================================================

    elif state["vida"] > 0:

        mudar_imagem("final_06.png")

        mostrar("""
🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha fica para trás.

Mas, quando vocês olham para o mar...

A criatura aparece na costa.

Ela observa o barco partir.

Ela ainda está viva.
""")

    # ========================================================
    # FINAL 5
    # ========================================================

    else:

        mudar_imagem(
            "Gemini_Generated_Image_I0ib9910ib9910ib.png"
        )

        mostrar("""
💀 FINAL DA ILHA

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
        "👤 Personagem: " +
        state["personagem"]
    )

    mostrar(
        "❤️ Vida: " +
        str(state["vida"])
    )

    mostrar(
        "🧠 Sanidade: " +
        str(state["sanidade"])
    )

    mostrar(
        "🔎 Pistas: " +
        str(state["pistas"])
    )

    if len(state["inv"]) > 0:

        mostrar(
            "🎒 Inventário: " +
            ", ".join(state["inv"])
        )

    else:

        mostrar(
            "🎒 Inventário: vazio"
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


# ============================================================
# INICIAR O JOGO
# ============================================================

atualizar_status()

fase1()
