from js import document


# ============================================================
# 🏝️ O SEGREDO NA ILHA
# VERSÃO PARA PYSCRIPT + GITHUB PAGES
# ============================================================


# ============================================================
# ELEMENTOS DO HTML
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

    # Mantém as quebras de linha
    bloco.innerHTML = str(texto).replace("\n", "<br>")

    tela.appendChild(bloco)

    # Faz a tela rolar para o final
    try:
        tela.scrollTop = tela.scrollHeight
    except:
        pass


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

    imagem.style.display = "block"
    imagem_fase(numero)

    atualizar_status()


# ============================================================
# BOTÕES
# ============================================================

def escolher(opcoes):
    limpar_botoes()

    for texto, funcao in opcoes:

        botao = document.createElement("button")

        botao.className = "opcao"

        botao.innerText = texto

        def clicar(evento, funcao=funcao):
            limpar_botoes()
            funcao()

        botao.addEventListener("click", clicar)

        botoes.appendChild(botao)


# ============================================================
# ITENS / STATUS
# ============================================================

def pegar(item):

    if item not in state["inv"]:
        state["inv"].append(item)

        mostrar(
            f"🎒 Você encontrou: {item}"
        )

    atualizar_status()


def perder_vida(qtd=1):

    state["vida"] -= qtd

    if state["vida"] < 0:
        state["vida"] = 0

    mostrar(
        f"❤️ Você perdeu {qtd} ponto(s) de vida."
    )

    atualizar_status()


def perder_sanidade(qtd=1):

    state["sanidade"] -= qtd

    if state["sanidade"] < 0:
        state["sanidade"] = 0

    mostrar(
        f"🧠 Você perdeu {qtd} ponto(s) de sanidade."
    )

    atualizar_status()


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

    escolher([
        ("👤 Olivier", escolher_olivier),
        ("👤 Amelie", escolher_amelie)
    ])


def escolher_olivier():

    state["personagem"] = "Olivier"

    mostrar("""
Você escolheu Olivier.

A viagem para a ilha começa.
""")

    atualizar_status()

    fase2()


def escolher_amelie():

    state["personagem"] = "Amelie"

    mostrar("""
Você escolheu Amelie.

A viagem para a ilha começa.
""")

    atualizar_status()

    fase2()


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

Você:

— Por que todo mundo está evitando falar sobre essa ilha?

Um familiar responde:

— Porque o que aconteceu lá não foi algo normal.

Você:

— E o que aconteceu?

Familiar:

— Quando chegarmos, você vai entender.

O barco chega ao porto.

A aventura começa.
""")

    escolher([
        ("➡️ Continuar", fase3)
    ])


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

    escolher([
        ("1️⃣ Perguntar sobre a ilha", fase3_ilha),
        ("2️⃣ Perguntar sobre sua família", fase3_familia),
        ("3️⃣ Perguntar sobre desaparecimentos", fase3_desaparecimentos)
    ])


def fase3_ilha():

    mostrar("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")

    state["confianca_milo"] += 1

    atualizar_status()

    fase4()


def fase3_familia():

    mostrar("""
Você:
— Vocês conhecem minha família?

Barbara:
— O sobrenome de vocês é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")

    state["pistas"] += 2

    atualizar_status()

    fase4()


def fase3_desaparecimentos():

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

    fase4()


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

    escolher([
        ("⛪ Igreja", fase5),
        ("🏚️ Casa abandonada", fase6),
        ("🔦 Farol", fase7)
    ])


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

    escolher([
        ("🔎 Examinar os símbolos", fase5_simbolos),
        ("📜 Procurar documentos", fase5_documentos),
        ("📷 Fotografar os símbolos", fase5_fotografia)
    ])


def fase5_simbolos():

    mostrar(
        "Você percebe que os símbolos formam um mapa."
    )

    state["pistas"] += 2

    atualizar_status()

    fase8()


def fase5_documentos():

    pegar("livro antigo")

    state["pistas"] += 3

    fase8()


def fase5_fotografia():

    pegar("fotografia dos símbolos")

    state["pistas"] += 1

    fase8()


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

    escolher([
        ("📜 Procurar documentos", fase6_documentos),
        ("🪜 Subir as escadas", fase6_escadas),
        ("⬇️ Ir ao porão", fase6_porao)
    ])


def fase6_documentos():

    pegar("documentos da família")

    state["pistas"] += 3

    fase8()


def fase6_escadas():

    pegar("chave enferrujada")

    state["pistas"] += 2

    perder_sanidade()

    fase8()


def fase6_porao():

    pegar("fotografia antiga")

    state["pistas"] += 3

    fase8()


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

    fase8()


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

    escolher([
        ("🪟 Abrir a janela", fase8_janela),
        ("😶 Ignorar", fase8_ignorar),
        ("🚪 Sair pela porta", fase8_porta)
    ])


def fase8_janela():

    mostrar("""
Não existe ninguém do lado de fora.

Mas há marcas enormes no chão.
""")

    state["pistas"] += 2

    perder_sanidade()

    fase9()


def fase8_ignorar():

    mostrar(
        "As batidas param depois de alguns minutos."
    )

    state["pistas"] += 1

    fase9()


def fase8_porta():

    mostrar("""
Vocês saem.

Barbara:
— Olhem para o chão.

Existem pegadas enormes.
""")

    state["pistas"] += 3

    fase9()


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

    escolher([
        ("🏘️ Procurar na vila", fase9_vila),
        ("🌲 Procurar na floresta", fase9_floresta)
    ])


def fase9_vila():

    state["pistas"] += 1

    mostrar(
        "Você encontra marcas perto da floresta."
    )

    fase10()


def fase9_floresta():

    state["pistas"] += 2

    mostrar(
        "Vocês encontram pegadas enormes."
    )

    fase10()


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

    state["pistas"] += 2

    mostrar("""
Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    fase11()


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

    escolher([
        ("🥾 Seguir a trilha", fase11_trilha),
        ("🪵 Marcar o caminho e voltar", fase11_marcar),
        ("👥 Separar o grupo", fase11_separar)
    ])


def fase11_trilha():

    state["pistas"] += 2

    fase12()


def fase11_marcar():

    state["pistas"] += 1

    fase12()


def fase11_separar():

    mostrar("""
Milo:
— Não acho uma boa ideia.

Barbara:
— Concordo.

Você decide seguir sozinho.
""")

    perder_sanidade()

    fase12()


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

    escolher([
        ("🗣️ Conversar com Milo", fase12_milo),
        ("🗣️ Conversar com Barbara", fase12_barbara),
        ("😴 Dormir", fase12_dormir)
    ])


def fase12_milo():

    state["confianca_milo"] += 2

    fase13()


def fase12_barbara():

    state["confianca_barbara"] += 2

    fase13()


def fase12_dormir():

    mostrar(
        "Você descansa e recupera um pouco da sanidade."
    )

    state["sanidade"] += 1

    atualizar_status()

    fase13()


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

    escolher([
        ("➡️ Seguir as pegadas", fase14)
    ])


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

    state["pistas"] += 3

    mostrar("""
No diário está escrito:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma forma de derrotar essa coisa.

Milo:
— Precisamos descobrir qual.
""")

    fase15()


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

    fase16()


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

    escolher([
        ("⚔️ Procurar uma arma", fase16_arma),
        ("💊 Procurar medicamentos", fase16_medicamento),
        ("🔱 Procurar o símbolo", fase16_simbolo)
    ])


def fase16_arma():

    pegar("arma")

    state["pistas"] += 1

    fase17()


def fase16_medicamento():

    pegar("medicamento")

    fase17()


def fase16_simbolo():

    pegar("símbolo antigo")

    state["pistas"] += 3

    fase17()


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

    escolher([
        ("🌊 Procurar dentro da água", fase17_agua),
        ("🔎 Procurar ao redor do lago", fase17_redor),
        ("➡️ Ignorar o lago", fase17_ignorar)
    ])


def fase17_agua():

    perder_vida()

    pegar("cristal")

    state["pistas"] += 2

    fase18()


def fase17_redor():

    pegar("cristal")

    state["pistas"] += 2

    fase18()


def fase17_ignorar():

    state["pistas"] += 1

    fase18()


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

    escolher([
        ("🕳️ Entrar", fase18_entrar),
        ("🔎 Procurar outra entrada", fase18_outra)
    ])


def fase18_entrar():

    state["pistas"] += 3

    fase19()


def fase18_outra():

    state["pistas"] += 1

    fase19()


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

    fase20()


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

    escolher([
        ("⬅️ Correr para a esquerda", fase20_esquerda),
        ("➡️ Correr para a direita", fase20_direita),
        ("🙈 Se esconder", fase20_esconder)
    ])


def fase20_esquerda():

    mostrar("Vocês encontram uma saída.")

    state["pistas"] += 1

    fase21()


def fase20_direita():

    mostrar("Vocês encontram uma sala escondida.")

    state["pistas"] += 2

    fase21()


def fase20_esconder():

    mostrar("Vocês conseguem se esconder.")

    state["sanidade"] += 1

    fase21()


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

    fase22()


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

    escolher([
        ("➡️ Continuar", fase23)
    ])


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

    escolher([
        ("🧑‍🦽 Levar o homem embora", fase23_levar),
        ("🙈 Deixá-lo escondido", fase23_esconder)
    ])


def fase23_levar():

    mostrar(
        "Vocês levam o homem para um local seguro."
    )

    state["pistas"] += 1

    fase24()


def fase23_esconder():

    mostrar(
        "Vocês o escondem em uma área protegida."
    )

    state["pistas"] += 1

    fase24()


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

    fase25()


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

    fase26()


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

    escolher([
        ("⚔️ Preparar a arma", fase26_arma),
        ("🔱 Preparar o símbolo", fase26_simbolo),
        ("📖 Procurar mais informações", fase26_informacoes)
    ])


def fase26_arma():

    if "arma" in state["inv"]:

        mostrar("A arma está pronta.")

        state["batalha"] += 1

    else:

        mostrar(
            "Vocês não possuem uma arma adequada."
        )

    fase27()


def fase26_simbolo():

    if "símbolo antigo" in state["inv"]:

        mostrar("O símbolo está pronto.")

        state["batalha"] += 2

    else:

        mostrar(
            "Vocês não encontraram o símbolo."
        )

    fase27()


def fase26_informacoes():

    mostrar("""
Vocês descobrem uma informação importante:

A criatura fica mais fraca quando o símbolo é ativado.
""")

    state["monstro_fraqueza"] = True
    state["batalha"] += 2

    fase27()


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

    escolher([
        ("⚔️ Entrar na batalha", fase28)
    ])


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

    escolher([
        ("⚔️ Atacar o monstro", fase28_atacar),
        ("🔱 Ativar o símbolo", fase28_simbolo),
        ("🛡️ Ajudar Milo", fase28_milo),
        ("🛡️ Ajudar Barbara", fase28_barbara)
    ])


def fase28_atacar():

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

    fase29()


def fase28_simbolo():

    if "símbolo antigo" in state["inv"]:

        mostrar("""
Você ativa o símbolo.

A criatura começa a enfraquecer.
""")

        state["batalha"] += 4
        state["monstro_fraqueza"] = True

    else:

        mostrar("""
Você tenta ativar o símbolo.

Mas não possui o objeto necessário.
""")

        perder_sanidade()

    fase29()


def fase28_milo():

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

    fase29()


def fase28_barbara():

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

    fase29()


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

    escolher([
        ("⚔️ Derrotar o monstro", final_derrotar),
        ("🔒 Selar o monstro", final_selar),
        ("🏃 Fugir", final_fugir)
    ])


def final_derrotar():

    if state["batalha"] >= 5:

        state["monstro_derrotado"] = True

        mostrar("""
Vocês atacam juntos.

A criatura finalmente cai.

VOCÊS CONSEGUIRAM!
""")

    else:

        state["monstro_derrotado"] = False

        mostrar("""
Vocês atacam.

Mas não conseguiram enfraquecer a criatura o suficiente.
""")

    fase30()


def final_selar():

    state["monstro_derrotado"] = False

    state["batalha"] = max(
        state["batalha"],
        3
    )

    mostrar("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

    fase30()


def final_fugir():

    state["monstro_derrotado"] = False

    state["vida"] = max(
        state["vida"],
        1
    )

    mostrar("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

    fase30()


# ============================================================
# FASE 30
# 5 FINAIS
# ============================================================

def fase30():

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
    # FINAL 2
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
    # FINAL 3
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
    # FINAL 4
    # ========================================================

    elif state["vida"] > 0:

        mudar_imagem("final_04.png")

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
    # FINAL 5
    # ========================================================

    else:

        mudar_imagem("final_05.png")

        mostrar("""
============================================================
🌑 FINAL DA ILHA
============================================================

A criatura vence.

Ninguém consegue escapar.

O segredo permanece enterrado na ilha.
""")


    # ========================================================
    # RESUMO
    # ========================================================

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


    escolher([
        ("🔄 Jogar novamente", reiniciar)
    ])


# ============================================================
# REINICIAR
# ============================================================

def reiniciar():

    state["personagem"] = ""
    state["vida"] = 5
    state["sanidade"] = 5
    state["inv"] = []
    state["pistas"] = 0

    state["milo_vivo"] = True
    state["barbara_viva"] = True
    state["olivier_vivo"] = True
    state["amelie_viva"] = True

    state["confianca_milo"] = 0
    state["confianca_barbara"] = 0

    state["monstro_fraqueza"] = False
    state["monstro_derrotado"] = False

    state["batalha"] = 0

    fase1()


# ============================================================
# INICIAR O JOGO
# ============================================================

fase1()
