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
# TELA
# ============================================================

def limpar():
    tela.innerHTML = ""
    botoes.innerHTML = ""


def mostrar(texto):
    div = document.createElement("div")
    div.className = "texto-jogo"
    div.innerHTML = str(texto).replace("\n", "<br>")
    tela.appendChild(div)


def imagem_fase(numero):
    imagem.src = f"fase_{numero:02d}.png"
    imagem.style.display = "block"


def mudar_imagem(nome):
    imagem.src = nome
    imagem.style.display = "block"


def atualizar_status():
    status.innerHTML = (
        f"❤️ Vida: {state['vida']} &nbsp;&nbsp;"
        f" 🧠 Sanidade: {state['sanidade']} &nbsp;&nbsp;"
        f" 🔎 Pistas: {state['pistas']} &nbsp;&nbsp;"
        f" 🎒 Itens: {len(state['inv'])}"
    )


# ============================================================
# BOTÕES
# ============================================================

def criar_botao(texto, funcao):

    botao = document.createElement("button")

    botao.className = "opcao"

    botao.innerText = texto

    botao.onclick = funcao

    botoes.appendChild(botao)


def preparar(numero):

    limpar()

    imagem_fase(numero)

    atualizar_status()


def pegar(item):

    if item not in state["inv"]:
        state["inv"].append(item)


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


def continuar(funcao):

    botoes.innerHTML = ""

    criar_botao("➡️ Continuar", funcao)


# ============================================================
# FASE 1
# ============================================================

def fase1():

    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Há muitos anos, um membro da sua família desapareceu
misteriosamente em uma ilha distante.

Agora vocês descobriram documentos antigos que podem
revelar o que aconteceu.

Escolha seu personagem:
""")

    criar_botao("👨 Olivier", escolher_olivier)
    criar_botao("👩 Amelie", escolher_amelie)


def escolher_olivier():

    state["personagem"] = "Olivier"

    fase2()


def escolher_amelie():

    state["personagem"] = "Amelie"

    fase2()


# ============================================================
# FASE 2
# ============================================================

def fase2():

    preparar(2)

    mostrar(f"""
🚢 FASE 2 — A VIAGEM

Você escolheu {state["personagem"]}.

O barco atravessa o mar durante horas.

A ilha aparece no horizonte.

Durante a viagem, ninguém fala muito sobre o passado.
""")

    continuar(fase3)


# ============================================================
# FASE 3
# ============================================================

def fase3():

    preparar(3)

    mostrar("""
🏝️ FASE 3 — CHEGADA

O barco finalmente chega à ilha.

Milo e Barbara esperam vocês no porto.

Milo:
— Vocês são os visitantes?

Barbara:
— Eu sabia que alguém viria.
""")

    criar_botao("❓ Perguntar sobre a ilha", fase3_ilha)
    criar_botao("👨‍👩‍👧 Perguntar sobre sua família", fase3_familia)
    criar_botao("🔎 Perguntar sobre desaparecimentos", fase3_desaparecimentos)


def fase3_ilha():

    state["confianca_milo"] += 1
    mostrar("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")

    continuar(fase4)


def fase3_familia():

    state["pistas"] += 2

    mostrar("""
Barbara:
— O sobrenome de vocês é conhecido aqui.

Milo:
— E não por um motivo muito bom.
""")

    atualizar_status()

    continuar(fase4)


def fase3_desaparecimentos():

    state["pistas"] += 1

    mostrar("""
Milo:
— Sim. Algumas pessoas desapareceram.

Barbara:
— E algumas nunca foram encontradas.
""")

    atualizar_status()

    continuar(fase4)


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

    criar_botao("⛪ Igreja", fase5)
    criar_botao("🏚️ Casa abandonada", fase6)
    criar_botao("🔦 Farol", fase7)


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
— Eu já vi esses símbolos.
""")

    criar_botao("🔎 Examinar símbolos", fase5_simbolos)
    criar_botao("📖 Procurar documentos", fase5_documentos)
    criar_botao("📸 Fotografar símbolos", fase5_foto)


def fase5_simbolos():

    state["pistas"] += 2

    mostrar("Os símbolos parecem formar um mapa.")

    atualizar_status()

    continuar(fase8)


def fase5_documentos():

    pegar("livro antigo")
    state["pistas"] += 3

    mostrar("Você encontrou um livro antigo.")

    atualizar_status()

    continuar(fase8)


def fase5_foto():

    pegar("fotografia dos símbolos")
    state["pistas"] += 1

    mostrar("Você fotografou os símbolos.")

    atualizar_status()

    continuar(fase8)


# ============================================================
# FASE 6
# ============================================================

def fase6():

    preparar(6)

    mostrar("""
🏚️ FASE 6 — CASA ABANDONADA

A casa está coberta de poeira.

Mas alguns objetos parecem ter sido usados recentemente.
""")

    criar_botao("📄 Procurar documentos", fase6_documentos)
    criar_botao("⬆️ Subir as escadas", fase6_escadas)
    criar_botao("⬇️ Ir ao porão", fase6_porao)


def fase6_documentos():

    pegar("documentos da família")
    state["pistas"] += 3

    mostrar("Você encontrou documentos antigos da família.")

    atualizar_status()

    continuar(fase8)


def fase6_escadas():

    pegar("chave enferrujada")
    state["pistas"] += 2
    perder_sanidade()

    mostrar("Você encontrou uma chave enferrujada.")

    continuar(fase8)


def fase6_porao():

    pegar("fotografia antiga")
    state["pistas"] += 3

    mostrar("Você encontrou uma fotografia antiga.")

    atualizar_status()

    continuar(fase8)


# ============================================================
# FASE 7
# ============================================================

def fase7():

    preparar(7)

    mostrar("""
🔦 FASE 7 — O FAROL

No topo do farol existe uma caixa escondida.

Dentro dela há uma fotografia.

Ao fundo aparece uma criatura misteriosa.
""")

    pegar("fotografia da criatura")

    state["pistas"] += 3

    atualizar_status()

    continuar(fase8)


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
— Isso me assusta.
""")

    criar_botao("🪟 Abrir a janela", fase8_janela)
    criar_botao("🚪 Ignorar", fase8_ignorar)
    criar_botao("🚶 Sair pela porta", fase8_porta)


def fase8_janela():

    state["pistas"] += 2
    perder_sanidade()

    mostrar("Não há ninguém lá fora. Mas existem marcas enormes.")

    continuar(fase9)


def fase8_ignorar():

    state["pistas"] += 1

    mostrar("As batidas param depois de alguns minutos.")

    atualizar_status()

    continuar(fase9)


def fase8_porta():

    state["pistas"] += 3

    mostrar("Existem pegadas enormes no chão.")

    atualizar_status()

    continuar(fase9)


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

    criar_botao("🏘️ Procurar na vila", fase9_vila)
    criar_botao("🌲 Procurar na floresta", fase9_floresta)


def fase9_vila():

    state["pistas"] += 1

    mostrar("Você encontrou marcas perto da floresta.")

    atualizar_status()

    continuar(fase10)


def fase9_floresta():

    state["pistas"] += 2

    mostrar("Vocês encontram pegadas enormes.")

    atualizar_status()

    continuar(fase10)


# ============================================================
# FASE 10
# ============================================================

def fase10():

    preparar(10)

    mostrar("""
🔎 FASE 10 — A INVESTIGAÇÃO

Vocês seguem as pistas pela floresta.

Encontram um objeto pertencente ao desaparecido.
""")

    pegar("objeto do desaparecido")

    state["pistas"] += 2

    atualizar_status()

    continuar(fase11)


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

    criar_botao("➡️ Seguir a trilha", fase11_trilha)
    criar_botao("🔙 Marcar caminho e voltar", fase11_voltar)
    criar_botao("⚠️ Separar o grupo", fase11_separar)


def fase11_trilha():

    state["pistas"] += 2

    atualizar_status()

    continuar(fase12)


def fase11_voltar():

    state["pistas"] += 1

    atualizar_status()

    continuar(fase12)


def fase11_separar():

    perder_sanidade()

    mostrar("Você decide seguir sozinho por alguns minutos.")

    continuar(fase12)


# ============================================================
# FASE 12
# ============================================================

def fase12():

    preparar(12)

    mostrar("""
🔥 FASE 12 — ACAMPAMENTO

Durante a noite vocês conversam sobre a criatura.

Milo:
— Acho que aquilo não é um animal.

Barbara:
— Então o que é?
""")

    criar_botao("🗣️ Conversar com Milo", fase12_milo)
    criar_botao("🗣️ Conversar com Barbara", fase12_barbara)
    criar_botao("😴 Dormir", fase12_dormir)


def fase12_milo():

    state["confianca_milo"] += 2

    atualizar_status()

    continuar(fase13)


def fase12_barbara():

    state["confianca_barbara"] += 2

    atualizar_status()

    continuar(fase13)


def fase12_dormir():

    state["sanidade"] += 1

    atualizar_status()

    continuar(fase13)


# ============================================================
# FASE 13
# ============================================================

def fase13():

    preparar(13)

    mostrar("""
🐾 FASE 13 — PEGADAS

Na manhã seguinte vocês encontram pegadas gigantes.

Barbara:
— Isso é grande demais.

Milo:
— E está indo naquela direção.
""")

    state["pistas"] += 3

    atualizar_status()

    continuar(fase14)


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
O diário diz:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma forma de derrotar essa coisa.
""")

    atualizar_status()

    continuar(fase15)


# ============================================================
# FASE 15
# ============================================================

def fase15():

    preparar(15)

    mostrar("""
📖 FASE 15 — O DIÁRIO

O diário fala sobre uma criatura que vive
nas profundezas da ilha.

Também menciona um símbolo original
capaz de deixá-la vulnerável.
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    atualizar_status()

    continuar(fase16)


# ============================================================
# FASE 16
# ============================================================

def fase16():

    preparar(16)

    mostrar("""
🎒 FASE 16 — PREPARAÇÃO

Vocês precisam encontrar equipamentos.
""")

    criar_botao("⚔️ Procurar uma arma", fase16_arma)
    criar_botao("💊 Procurar medicamentos", fase16_medicamento)
    criar_botao("🔱 Procurar o símbolo", fase16_simbolo)


def fase16_arma():

    pegar("arma")
    state["pistas"] += 1

    atualizar_status()

    continuar(fase17)


def fase16_medicamento():

    pegar("medicamento")

    atualizar_status()

    continuar(fase17)


def fase16_simbolo():

    pegar("símbolo antigo")
    state["pistas"] += 3

    atualizar_status()

    continuar(fase17)


# ============================================================
# FASE 17
# ============================================================

def fase17():

    preparar(17)

    mostrar("""
🌊 FASE 17 — O LAGO

O mapa indica que o próximo símbolo está perto de um lago.
""")

    criar_botao("🌊 Procurar dentro da água", fase17_agua)
    criar_botao("🔎 Procurar ao redor", fase17_redor)
    criar_botao("➡️ Ignorar o lago", fase17_ignorar)


def fase17_agua():

    perder_vida()
    pegar("cristal")
    state["pistas"] += 2

    atualizar_status()

    continuar(fase18)


def fase17_redor():

    pegar("cristal")
    state["pistas"] += 2

    atualizar_status()

    continuar(fase18)


def fase17_ignorar():

    state["pistas"] += 1

    atualizar_status()

    continuar(fase18)


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
""")

    criar_botao("🚶 Entrar", fase18_entrar)
    criar_botao("🔎 Procurar outra entrada", fase18_outra)


def fase18_entrar():

    state["pistas"] += 3

    atualizar_status()

    continuar(fase19)


def fase18_outra():

    state["pistas"] += 1

    atualizar_status()

    continuar(fase19)


# ============================================================
# FASE 19
# ============================================================

def fase19():

    preparar(19)

    mostrar("""
👹 FASE 19 — PRIMEIRO ENCONTRO

Um rugido ecoa pela caverna.

A criatura aparece por alguns segundos.

Milo:
— CORRE!

Barbara:
— AGORA!
""")

    perder_sanidade()

    continuar(fase20)


# ============================================================
# FASE 20
# ============================================================

def fase20():

    preparar(20)

    mostrar("""
🏃 FASE 20 — FUGA

A criatura começa a perseguir vocês.
""")

    criar_botao("⬅️ Correr para a esquerda", fase20_esquerda)
    criar_botao("➡️ Correr para a direita", fase20_direita)
    criar_botao("🙈 Se esconder", fase20_esconder)


def fase20_esquerda():

    state["pistas"] += 1

    continuar(fase21)


def fase20_direita():

    state["pistas"] += 2

    continuar(fase21)


def fase20_esconder():

    state["sanidade"] += 1

    atualizar_status()

    continuar(fase21)


# ============================================================
# FASE 21
# ============================================================

def fase21():

    preparar(21)

    mostrar("""
🔎 FASE 21 — A FRAQUEZA

Vocês encontram uma inscrição.

Ela revela que o monstro pode ser ferido pelo
símbolo original da ilha.
""")

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    atualizar_status()

    continuar(fase22)


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

Barbara:
— Então é lá que vamos.
""")

    continuar(fase23)


# ============================================================
# FASE 23
# ============================================================

def fase23():

    preparar(23)

    mostrar("""
🆘 FASE 23 — O RESGATE

Vocês encontram o morador desaparecido.

Ele está ferido, mas vivo.

Morador:
— Vocês precisam ir embora!

— Ela está acordada.
""")

    criar_botao("🚶 Levar o homem embora", fase23_levar)
    criar_botao("🙈 Deixá-lo escondido", fase23_esconder)


def fase23_levar():

    state["pistas"] += 1

    continuar(fase24)


def fase23_esconder():

    state["pistas"] += 1

    continuar(fase24)


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

        mostrar("O símbolo encaixa na porta. Ela se abre.")

        state["pistas"] += 3

    else:

        mostrar("Vocês precisam forçar a porta.")

        perder_vida()

    atualizar_status()

    continuar(fase25)


# ============================================================
# FASE 25
# ============================================================

def fase25():

    preparar(25)

    mostrar("""
📜 FASE 25 — O PASSADO DA FAMÍLIA

Dentro do esconderijo existem documentos.

Eles revelam que sua família já encontrou
a criatura no passado.

Seu parente tentou impedir que ela fosse libertada.
""")

    state["pistas"] += 4

    atualizar_status()

    continuar(fase26)


# ============================================================
# FASE 26
# ============================================================

def fase26():

    preparar(26)

    mostrar("""
⚔️ FASE 26 — PREPARAÇÃO

Antes da batalha vocês precisam decidir como agir.
""")

    criar_botao("⚔️ Preparar a arma", fase26_arma)
    criar_botao("🔱 Preparar o símbolo", fase26_simbolo)
    criar_botao("📖 Procurar informações", fase26_info)


def fase26_arma():

    if "arma" in state["inv"]:

        state["batalha"] += 1
        mostrar("A arma está pronta.")

    else:

        mostrar("Vocês não possuem uma arma.")

    atualizar_status()

    continuar(fase27)


def fase26_simbolo():

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 2
        mostrar("O símbolo está pronto.")

    else:

        mostrar("Vocês não encontraram o símbolo.")

    atualizar_status()

    continuar(fase27)


def fase26_info():

    state["monstro_fraqueza"] = True
    state["batalha"] += 2

    mostrar("Vocês descobrem que o símbolo enfraquece a criatura.")

    atualizar_status()

    continuar(fase27)


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
— Não deixem ela chegar perto.
""")

    continuar(fase28)


# ============================================================
# FASE 28
# ============================================================

def fase28():

    preparar(28)

    mostrar("""
⚔️ FASE 28 — BATALHA

A criatura ataca.

Vocês precisam agir rápido.
""")

    criar_botao("⚔️ Atacar o monstro", batalha_atacar)
    criar_botao("🔱 Ativar o símbolo", batalha_simbolo)
    criar_botao("🛡️ Ajudar Milo", batalha_milo)
    criar_botao("🛡️ Ajudar Barbara", batalha_barbara)


def batalha_atacar():

    if "arma" in state["inv"] and state["monstro_fraqueza"]:

        state["batalha"] += 3

        mostrar("Você ataca o ponto fraco da criatura.")

    else:

        perder_vida()

        mostrar("Seu ataque não causa muito efeito.")

    atualizar_status()

    continuar(fase29)


def batalha_simbolo():

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 4

        mostrar("O símbolo enfraquece a criatura.")

    else:

        perder_sanidade()

        mostrar("Você não possui o símbolo.")

    atualizar_status()

    continuar(fase29)


def batalha_milo():

    if state["milo_vivo"]:

        state["confianca_milo"] += 2
        state["batalha"] += 2

        mostrar("Você ajuda Milo.")

    continuar(fase29)


def batalha_barbara():

    if state["barbara_viva"]:

        state["confianca_barbara"] += 2
        state["batalha"] += 2

        mostrar("Você ajuda Barbara.")

    continuar(fase29)


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

    criar_botao("⚔️ Derrotar o monstro", final_derrotar)
    criar_botao("🔒 Selar o monstro", final_selar)
    criar_botao("🏃 Fugir", final_fugir)


def final_derrotar():

    if state["batalha"] >= 5:

        state["monstro_derrotado"] = True

    else:

        state["monstro_derrotado"] = False

        mostrar("Vocês não conseguiram enfraquecer a criatura o suficiente.")

    fase30()


def final_selar():

    state["monstro_derrotado"] = False
    state["batalha"] = max(state["batalha"], 3)

    fase30()


def final_fugir():

    state["monstro_derrotado"] = False

    fase30()


# ============================================================
# FASE 30 — FINAIS
# ============================================================

def fase30():

    limpar()

    atualizar_status()

    vivos = 0

    if state["milo_vivo"]:
        vivos += 1

    if state["barbara_viva"]:
        vivos += 1

    if state["personagem"] == "Olivier":

        if state["amelie_viva"]:
            vivos += 1

    else:

        if state["olivier_vivo"]:
            vivos += 1


    # FINAL 1

    if state["monstro_derrotado"] and vivos >= 3:

        mudar_imagem("final_01.png")

        mostrar("""
🌟 FINAL PERFEITO

A criatura finalmente foi derrotada.

Todos conseguem sair da câmara.

Milo:
— Nós realmente conseguimos.

Barbara:
— E ninguém morreu.

O segredo da ilha foi descoberto.
""")

    # FINAL 2

    elif state["monstro_derrotado"]:

        mudar_imagem("final_02.png")

        mostrar("""
🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Mas nem todos conseguiram sobreviver.

Os sobreviventes deixam a ilha.
""")

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

Mas a criatura continua viva.
""")

    # FINAL 5

    else:

        mudar_imagem("Gemini_Generated_Image_I0ib9910ib9910ib.png")

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

    mostrar(f"""
👤 Personagem: {state["personagem"]}

❤️ Vida: {state["vida"]}

🧠 Sanidade: {state["sanidade"]}

🔎 Pistas: {state["pistas"]}

🎒 Itens: {", ".join(state["inv"]) if state["inv"] else "Nenhum"}
""")


# ============================================================
# COMEÇAR O JOGO
# ============================================================

fase1()
