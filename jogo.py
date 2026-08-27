from js import document


# ============================================================
# ELEMENTOS DA PÁGINA
# ============================================================

tela = document.getElementById("jogo")
botoes = document.getElementById("botoes")
imagem = document.getElementById("imagem-fase")
status = document.getElementById("status")


# ============================================================
# ESTADO DO JOGO
# ============================================================

state = {
    "personagem": "",
    "vida": 5,
    "sanidade": 5,
    "pistas": 0,
    "inv": [],

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

def limpar():
    tela.innerHTML = ""
    botoes.innerHTML = ""


def mostrar(texto):
    div = document.createElement("div")
    div.className = "texto-jogo"
    div.innerHTML = str(texto).replace("\n", "<br>")
    tela.appendChild(div)


def atualizar_status():
    status.innerHTML = (
        f"❤️ Vida: {state['vida']} &nbsp;&nbsp; "
        f"🧠 Sanidade: {state['sanidade']} &nbsp;&nbsp; "
        f"🔎 Pistas: {state['pistas']} &nbsp;&nbsp; "
        f"🎒 Itens: {len(state['inv'])}"
    )


def imagem_fase(numero):
    imagem.src = f"fase_{numero:02d}.png"
    imagem.style.display = "block"


def mudar_imagem(nome):
    imagem.src = nome
    imagem.style.display = "block"


def botao(texto, funcao):
    b = document.createElement("button")

    b.className = "opcao"
    b.innerText = texto

    b.onclick = funcao

    botoes.appendChild(b)


def preparar(numero):
    limpar()
    atualizar_status()

    if numero <= 20:
        imagem_fase(numero)
    else:
        imagem.style.display = "none"


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

    atualizar_status()


def perder_sanidade(qtd=1):
    state["sanidade"] -= qtd

    if state["sanidade"] < 0:
        state["sanidade"] = 0

    atualizar_status()


# ============================================================
# FASE 1
# ============================================================

def fase1():

    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Há muitos anos, um membro da sua família desapareceu
misteriosamente em uma ilha distante.

Recentemente, documentos antigos foram encontrados.

Agora você precisa descobrir o que aconteceu.

ESCOLHA SEU PERSONAGEM:
""")

    botao(
        "🧑 Olivier",
        escolher_olivier
    )

    botao(
        "👩 Amelie",
        escolher_amelie
    )


def escolher_olivier(event):

    state["personagem"] = "Olivier"

    fase2()


def escolher_amelie(event):

    state["personagem"] = "Amelie"

    fase2()


# ============================================================
# FASE 2
# ============================================================

def fase2():

    preparar(2)

    mostrar("""
🚢 FASE 2 — A VIAGEM

O barco atravessa o mar.

Depois de algumas horas, a ilha aparece no horizonte.

Milo:
— Finalmente chegamos.

Barbara:
— Espero que vocês estejam preparados.

Você olha para a ilha.

Alguma coisa parece estar errada.
""")

    botao(
        "➡️ Continuar",
        continuar_fase3
    )


def continuar_fase3(event):
    fase3()


# ============================================================
# FASE 3
# ============================================================

def fase3():

    preparar(3)

    mostrar("""
🏝️ FASE 3 — CHEGADA

Vocês chegam à vila.

Milo e Barbara vêm encontrar vocês.

Milo:
— Vocês são os visitantes?

Barbara:
— Eu sabia que alguém viria.
""")

    botao(
        "🔎 Perguntar sobre a ilha",
        fase3_ilha
    )

    botao(
        "👨‍👩‍👧 Perguntar sobre sua família",
        fase3_familia
    )

    botao(
        "👻 Perguntar sobre desaparecimentos",
        fase3_desaparecimentos
    )


def fase3_ilha(event):

    state["confianca_milo"] += 1

    mostrar("""
Milo:
— Durante o dia a ilha parece tranquila.

Barbara:
— Durante a noite é outra história.
""")

    botao("➡️ Continuar", continuar_fase4)


def fase3_familia(event):

    state["pistas"] += 2

    mostrar("""
Barbara:
— O sobrenome da sua família é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")

    atualizar_status()

    botao("➡️ Continuar", continuar_fase4)


def fase3_desaparecimentos(event):

    state["pistas"] += 1

    mostrar("""
Milo:
— Sim. Pessoas desapareceram.

Barbara:
— Algumas nunca foram encontradas.
""")

    atualizar_status()

    botao("➡️ Continuar", continuar_fase4)


def continuar_fase4(event):
    fase4()


# ============================================================
# FASE 4
# ============================================================

def fase4():

    preparar(4)

    mostrar("""
🏘️ FASE 4 — A VILA

Existem três lugares importantes:

⛪ Igreja antiga
🏚️ Casa abandonada
🔦 Farol

Para onde você vai?
""")

    botao("⛪ Igreja", fase5)
    botao("🏚️ Casa abandonada", fase6)
    botao("🔦 Farol", fase7)


# ============================================================
# FASE 5
# ============================================================

def fase5():

    preparar(5)

    mostrar("""
⛪ FASE 5 — A IGREJA

A igreja está abandonada.

Nas paredes existem símbolos estranhos.

Milo:
— Eu já vi esses símbolos antes.
""")

    botao(
        "🔎 Examinar símbolos",
        fase5_simbolos
    )

    botao(
        "📖 Procurar documentos",
        fase5_documentos
    )

    botao(
        "📷 Fotografar símbolos",
        fase5_foto
    )


def fase5_simbolos(event):

    state["pistas"] += 2

    mostrar("""
Você percebe que os símbolos formam um mapa.
""")

    atualizar_status()

    botao("➡️ Continuar", fase8)


def fase5_documentos(event):

    pegar("livro antigo")

    state["pistas"] += 3

    atualizar_status()

    botao("➡️ Continuar", fase8)


def fase5_foto(event):

    pegar("fotografia dos símbolos")

    state["pistas"] += 1

    atualizar_status()

    botao("➡️ Continuar", fase8)


# ============================================================
# FASE 6
# ============================================================

def fase6():

    preparar(6)

    mostrar("""
🏚️ FASE 6 — CASA ABANDONADA

A casa está coberta de poeira.

Alguns objetos parecem ter sido usados recentemente.
""")

    botao(
        "📄 Procurar documentos",
        fase6_documentos
    )

    botao(
        "⬆️ Subir as escadas",
        fase6_escadas
    )

    botao(
        "⬇️ Ir ao porão",
        fase6_porao
    )


def fase6_documentos(event):

    pegar("documentos da família")

    state["pistas"] += 3

    botao("➡️ Continuar", fase8)


def fase6_escadas(event):

    pegar("chave enferrujada")

    state["pistas"] += 2

    perder_sanidade()

    botao("➡️ Continuar", fase8)


def fase6_porao(event):

    pegar("fotografia antiga")

    state["pistas"] += 3

    botao("➡️ Continuar", fase8)


# ============================================================
# FASE 7
# ============================================================

def fase7():

    preparar(7)

    mostrar("""
🔦 FASE 7 — O FAROL

No topo do farol existe uma caixa escondida.

Dentro dela existe uma fotografia.

Ao fundo aparece uma criatura desconhecida.
""")

    pegar("fotografia da criatura")

    state["pistas"] += 3

    atualizar_status()

    mostrar("""
Milo:
— Isso não deveria existir.

Barbara:
— Precisamos descobrir o que é.
""")

    botao("➡️ Continuar", fase8)


# ============================================================
# FASE 8
# ============================================================

def fase8():

    preparar(8)

    mostrar("""
🌙 FASE 8 — PRIMEIRA NOITE

Durante a noite vocês escutam:

TOC.

TOC.

TOC.

Milo:
— Não abre.

Barbara:
— E é isso que me assusta.
""")

    botao(
        "🪟 Abrir a janela",
        fase8_janela
    )

    botao(
        "😶 Ignorar",
        fase8_ignorar
    )

    botao(
        "🚪 Sair pela porta",
        fase8_porta
    )


def fase8_janela(event):

    state["pistas"] += 2

    perder_sanidade()

    mostrar("""
Não existe ninguém do lado de fora.

Mas existem marcas enormes no chão.
""")

    botao("➡️ Continuar", fase9)


def fase8_ignorar(event):

    state["pistas"] += 1

    mostrar("As batidas param depois de alguns minutos.")

    botao("➡️ Continuar", fase9)


def fase8_porta(event):

    state["pistas"] += 3

    mostrar("""
Vocês saem.

Existem pegadas enormes no chão.
""")

    botao("➡️ Continuar", fase9)


# ============================================================
# FASE 9
# ============================================================

def fase9():

    preparar(9)

    mostrar("""
🚨 FASE 9 — O DESAPARECIMENTO

Na manhã seguinte, um morador desapareceu.

Milo:
— Ele estava aqui ontem.

Barbara:
— Precisamos encontrá-lo.
""")

    botao(
        "🏘️ Procurar na vila",
        fase9_vila
    )

    botao(
        "🌲 Procurar na floresta",
        fase9_floresta
    )


def fase9_vila(event):

    state["pistas"] += 1

    mostrar("Você encontra marcas perto da floresta.")

    botao("➡️ Continuar", fase10)


def fase9_floresta(event):

    state["pistas"] += 2

    mostrar("Vocês encontram pegadas enormes.")

    botao("➡️ Continuar", fase10)


# ============================================================
# FASE 10
# ============================================================

def fase10():

    preparar(10)

    mostrar("""
🔎 FASE 10 — A INVESTIGAÇÃO

Vocês seguem as pistas.

Depois de algum tempo encontram um objeto
pertencente ao desaparecido.
""")

    pegar("objeto do desaparecido")

    state["pistas"] += 2

    mostrar("""
Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    botao("➡️ Continuar", fase11)


# ============================================================
# FASE 11
# ============================================================

def fase11():

    preparar(11)

    mostrar("""
🌲 FASE 11 — A FLORESTA

A floresta fica cada vez mais escura.

Vocês encontram uma trilha escondida.
""")

    botao("➡️ Seguir a trilha", fase11_trilha)
    botao("🪵 Marcar o caminho", fase11_marcar)
    botao("⚠️ Separar o grupo", fase11_separar)


def fase11_trilha(event):

    state["pistas"] += 2

    botao("➡️ Continuar", fase12)


def fase11_marcar(event):

    state["pistas"] += 1

    botao("➡️ Continuar", fase12)


def fase11_separar(event):

    perder_sanidade()

    mostrar("""
Milo:
— Não acho uma boa ideia.

Você decide continuar sozinho.
""")

    botao("➡️ Continuar", fase12)


# ============================================================
# FASE 12
# ============================================================

def fase12():

    preparar(12)

    mostrar("""
🔥 FASE 12 — ACAMPAMENTO

Vocês montam um pequeno acampamento.

Durante a noite conversam sobre a criatura.
""")

    botao("🗣️ Conversar com Milo", fase12_milo)
    botao("🗣️ Conversar com Barbara", fase12_barbara)
    botao("😴 Dormir", fase12_dormir)


def fase12_milo(event):

    state["confianca_milo"] += 2

    botao("➡️ Continuar", fase13)


def fase12_barbara(event):

    state["confianca_barbara"] += 2

    botao("➡️ Continuar", fase13)


def fase12_dormir(event):

    state["sanidade"] += 1

    atualizar_status()

    botao("➡️ Continuar", fase13)


# ============================================================
# FASE 13
# ============================================================

def fase13():

    preparar(13)

    state["pistas"] += 3

    mostrar("""
🐾 FASE 13 — PEGADAS

Na manhã seguinte vocês encontram pegadas gigantes.

Barbara:
— Isso é grande demais.

Milo:
— E está indo naquela direção.
""")

    atualizar_status()

    botao("➡️ Continuar", fase14)


# ============================================================
# FASE 14
# ============================================================

def fase14():

    preparar(14)

    mostrar("""
🏚️ FASE 14 — A CABANA

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
""")

    botao("➡️ Continuar", fase15)


# ============================================================
# FASE 15
# ============================================================

def fase15():

    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
📖 FASE 15 — O DIÁRIO

O diário fala sobre uma criatura que vive
nas profundezas da ilha.

Também diz:

"Quando a criatura for ferida pelo símbolo original,
ela ficará vulnerável."

Milo:
— Precisamos encontrar esse símbolo.
""")

    atualizar_status()

    botao("➡️ Continuar", fase16)


# ============================================================
# FASE 16
# ============================================================

def fase16():

    preparar(16)

    mostrar("""
🎒 FASE 16 — PREPARAÇÃO

Vocês precisam encontrar equipamentos.
""")

    botao("⚔️ Procurar uma arma", fase16_arma)
    botao("💊 Procurar medicamentos", fase16_medicamento)
    botao("🔱 Procurar o símbolo", fase16_simbolo)


def fase16_arma(event):

    pegar("arma")
    state["batalha"] += 1

    botao("➡️ Continuar", fase17)


def fase16_medicamento(event):

    pegar("medicamento")

    botao("➡️ Continuar", fase17)


def fase16_simbolo(event):

    pegar("símbolo antigo")

    state["pistas"] += 3

    botao("➡️ Continuar", fase17)


# ============================================================
# FASE 17
# ============================================================

def fase17():

    preparar(17)

    mostrar("""
🌊 FASE 17 — O LAGO

O mapa indica que o próximo símbolo está perto
de um lago.
""")

    botao("🌊 Procurar dentro da água", fase17_agua)
    botao("🔎 Procurar ao redor", fase17_redor)
    botao("➡️ Ignorar o lago", fase17_ignorar)


def fase17_agua(event):

    perder_vida()
    pegar("cristal")
    state["pistas"] += 2

    botao("➡️ Continuar", fase18)


def fase17_redor(event):

    pegar("cristal")
    state["pistas"] += 2

    botao("➡️ Continuar", fase18)


def fase17_ignorar(event):

    state["pistas"] += 1

    botao("➡️ Continuar", fase18)


# ============================================================
# FASE 18
# ============================================================

def fase18():

    preparar(18)

    mostrar("""
🕳️ FASE 18 — A CAVERNA

O cristal aponta para uma caverna escondida.

Milo:
— Acho que estamos perto.

Barbara:
— Perto demais.
""")

    botao("🚪 Entrar", fase18_entrar)
    botao("🔎 Procurar outra entrada", fase18_outra)


def fase18_entrar(event):

    state["pistas"] += 3

    botao("➡️ Continuar", fase19)


def fase18_outra(event):

    state["pistas"] += 1

    botao("➡️ Continuar", fase19)


# ============================================================
# FASE 19
# ============================================================

def fase19():

    preparar(19)

    perder_sanidade()

    mostrar("""
👹 FASE 19 — PRIMEIRO ENCONTRO

Um rugido ecoa pela caverna.

A criatura aparece por alguns segundos.

Milo:
— CORRE!

Barbara:
— AGORA!
""")

    botao("🏃 Fugir", fase20)


# ============================================================
# FASE 20
# ============================================================

def fase20():

    preparar(20)

    mostrar("""
🏃 FASE 20 — FUGA DO MONSTRO

A criatura começa a perseguir vocês.

Para onde correr?
""")

    botao("⬅️ Esquerda", fase20_esquerda)
    botao("➡️ Direita", fase20_direita)
    botao("🫣 Se esconder", fase20_esconder)


def fase20_esquerda(event):

    state["pistas"] += 1
    botao("➡️ Continuar", fase21)


def fase20_direita(event):

    state["pistas"] += 2
    botao("➡️ Continuar", fase21)


def fase20_esconder(event):

    state["sanidade"] += 1

    botao("➡️ Continuar", fase21)


# ============================================================
# FASE 21
# ============================================================

def fase21():

    preparar(21)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
🔎 FASE 21 — A FRAQUEZA

Vocês encontram uma inscrição.

Ela revela que o monstro pode ser ferido
pelo símbolo original da ilha.

Barbara:
— Então podemos derrotá-lo.
""")

    atualizar_status()

    botao("➡️ Continuar", fase22)


# ============================================================
# FASE 22
# ============================================================

def fase22():

    preparar(22)

    mostrar("""
🏚️ FASE 22 — O ESCONDERIJO

Vocês descobrem o esconderijo da criatura
abaixo da ilha.

Milo:
— É lá que ela fica.

Você:
— Então é lá que vamos.
""")

    botao("➡️ Continuar", fase23)


# ============================================================
# FASE 23
# ============================================================

def fase23():

    preparar(23)

    state["pistas"] += 1

    mostrar("""
🆘 FASE 23 — O RESGATE

Vocês encontram o morador desaparecido.

Ele está ferido, mas vivo.

Morador:
— Vocês precisam ir embora!

Você:
— O que aconteceu?

Morador:
— Ela está acordada.
""")

    botao("🚶 Levar o homem embora", fase24)
    botao("🫣 Deixá-lo escondido", fase24)


# ============================================================
# FASE 24
# ============================================================

def fase24():

    preparar(24)

    mostrar("""
🚪 FASE 24 — A ENTRADA

Vocês encontram uma porta enorme.

Ela possui o símbolo original.
""")

    if "símbolo antigo" in state["inv"]:

        state["pistas"] += 3

        mostrar("""
O símbolo encaixa na porta.

A porta se abre.
""")

    else:

        perder_vida()

        mostrar("""
Vocês precisam forçar a porta.

Um grande barulho ecoa pelo subterrâneo.
""")

    atualizar_status()

    botao("➡️ Entrar", fase25)


# ============================================================
# FASE 25
# ============================================================

def fase25():

    preparar(25)

    state["pistas"] += 4

    mostrar("""
📜 FASE 25 — O PASSADO DA FAMÍLIA

Dentro do esconderijo existem documentos.

Eles revelam que sua família já encontrou
a criatura no passado.

Seu parente desaparecido tentou impedir
que ela fosse libertada.

Barbara:
— Então ele estava tentando proteger a ilha.
""")

    atualizar_status()

    botao("➡️ Continuar", fase26)


# ============================================================
# FASE 26
# ============================================================

def fase26():

    preparar(26)

    mostrar("""
⚔️ FASE 26 — PREPARAÇÃO

Antes da batalha, vocês precisam decidir
como agir.
""")

    botao("⚔️ Preparar arma", fase26_arma)
    botao("🔱 Preparar símbolo", fase26_simbolo)
    botao("📖 Procurar informações", fase26_info)


def fase26_arma(event):

    if "arma" in state["inv"]:

        state["batalha"] += 1

        mostrar("A arma está pronta.")

    else:

        mostrar("Vocês não possuem uma arma.")

    botao("➡️ Continuar", fase27)


def fase26_simbolo(event):

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 2

        mostrar("O símbolo está pronto.")

    else:

        mostrar("Vocês não possuem o símbolo.")

    botao("➡️ Continuar", fase27)


def fase26_info(event):

    state["monstro_fraqueza"] = True
    state["batalha"] += 2

    mostrar("""
Vocês descobrem que a criatura fica
mais fraca quando o símbolo é ativado.
""")

    botao("➡️ Continuar", fase27)


# ============================================================
# FASE 27
# ============================================================

def fase27():

    preparar(27)

    mostrar("""
👹 FASE 27 — O MONSTRO

Vocês chegam à última sala.

A criatura está esperando.

Milo:
— É agora.

Barbara:
— Todo mundo pronto?

Milo:
— Não.

Barbara:
— Mas vamos mesmo assim.
""")

    botao("⚔️ Enfrentar", fase28)


# ============================================================
# FASE 28
# ============================================================

def fase28():

    preparar(28)

    mostrar("""
⚔️ FASE 28 — BATALHA

A criatura ataca.

Escolha uma ação:
""")

    botao("⚔️ Atacar", fase28_atacar)
    botao("🔱 Ativar símbolo", fase28_simbolo)
    botao("🛡️ Ajudar Milo", fase28_milo)
    botao("🛡️ Ajudar Barbara", fase28_barbara)


def fase28_atacar(event):

    if "arma" in state["inv"] and state["monstro_fraqueza"]:

        state["batalha"] += 3

        mostrar("Você ataca o ponto fraco da criatura.")

    else:

        perder_vida()

        mostrar("Seu ataque não causa muito efeito.")

    botao("➡️ Continuar", fase29)


def fase28_simbolo(event):

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 4

        state["monstro_fraqueza"] = True

        mostrar("""
Você ativa o símbolo.

A criatura começa a enfraquecer.
""")

    else:

        perder_sanidade()

        mostrar("Você não possui o símbolo necessário.")

    botao("➡️ Continuar", fase29)


def fase28_milo(event):

    if state["milo_vivo"]:

        state["confianca_milo"] += 2
        state["batalha"] += 2

        mostrar("""
Você ajuda Milo.

Milo:
— Obrigado!
""")

    botao("➡️ Continuar", fase29)


def fase28_barbara(event):

    if state["barbara_viva"]:

        state["confianca_barbara"] += 2
        state["batalha"] += 2

        mostrar("""
Você ajuda Barbara.

Barbara:
— Eu sabia que podia confiar em você!
""")

    botao("➡️ Continuar", fase29)


# ============================================================
# FASE 29
# ============================================================

def fase29():

    preparar(29)

    mostrar("""
🔥 FASE 29 — ÚLTIMA ESCOLHA

A criatura está ferida.

Mas ainda não foi derrotada.

Você tem uma última oportunidade.
""")

    botao("⚔️ Derrotar o monstro", fase29_derrotar)
    botao("🔒 Selar o monstro", fase29_selar)
    botao("🏃 Fugir", fase29_fugir)


def fase29_derrotar(event):

    if state["batalha"] >= 5:

        state["monstro_derrotado"] = True

    else:

        state["monstro_derrotado"] = False

        mostrar("""
Vocês atacam.

Mas não conseguiram enfraquecer
a criatura o suficiente.
""")

    fase30()


def fase29_selar(event):

    state["monstro_derrotado"] = False
    state["batalha"] = max(state["batalha"], 3)

    mostrar("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

    fase30()


def fase29_fugir(event):

    state["monstro_derrotado"] = False
    state["vida"] = max(state["vida"], 1)

    mostrar("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

    fase30()


# ============================================================
# FASE 30 — FINAIS
# ============================================================

def fase30():

    limpar()

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


    # FINAL 1
    if state["monstro_derrotado"] and len(vivos) >= 3:

        mudar_imagem("final_01.png")

        mostrar("""
🌟 FINAL PERFEITO

A criatura finalmente é derrotada.

Todos conseguem sair da câmara.

Todos sobrevivem.

O segredo da ilha foi descoberto.
""")

    # FINAL 2
    elif state["monstro_derrotado"]:

        mudar_imagem("final_02.png")

        mostrar("""
🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Nem todos conseguiram sobreviver.

Os sobreviventes deixam a ilha.
""")

        mostrar(
            "Sobreviventes: " + ", ".join(vivos)
        )

    # FINAL 3
    elif state["batalha"] >= 3:

        mudar_imagem("final_03.png")

        mostrar("""
👁️ FINAL DO SELAMENTO

A criatura é selada novamente.

A ilha está segura...

Por enquanto.
""")

    # FINAL 4
    elif state["vida"] > 0:

        mudar_imagem("final_06.png")

        mostrar("""
🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha fica para trás.

Mas a criatura ainda está viva.
""")

    # FINAL 5
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
        "🎒 Inventário: " +
        ", ".join(state["inv"])
    )

    botao(
        "🔄 Jogar novamente",
        reiniciar
    )


# ============================================================
# REINICIAR
# ============================================================

def reiniciar(event):

    state["personagem"] = ""
    state["vida"] = 5
    state["sanidade"] = 5
    state["pistas"] = 0
    state["inv"] = []

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
# COMEÇAR O JOGO
# ============================================================

fase1()
