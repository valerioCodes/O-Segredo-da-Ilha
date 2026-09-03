from js import document

tela = document.getElementById("jogo")
botoes = document.getElementById("botoes")
imagem = document.getElementById("imagem-fase")
status = document.getElementById("status")
video_final = document.getElementById("video-final")


# =========================================================
# ESTADO DO JOGO
# =========================================================

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

    "batalha": 0,
    "final": ""
}


# =========================================================
# SISTEMA
# =========================================================

def limpar():
    botoes.innerHTML = ""
    tela.innerHTML = ""

    try:
        video_final.pause()
        video_final.currentTime = 0
        video_final.style.display = "none"
    except:
        pass


def mostrar(texto):
    div = document.createElement("div")
    div.className = "texto-jogo"
    div.innerHTML = str(texto).replace("\n", "<br>")
    tela.appendChild(div)


def atualizar_status():
    status.innerHTML = (
        "❤️ Vida: " + str(state["vida"]) +
        " | 🧠 Sanidade: " + str(state["sanidade"]) +
        " | 🔎 Pistas: " + str(state["pistas"]) +
        " | 🎒 Itens: " + str(len(state["inv"])) +
        " | ⚔️ Força: " + str(state["batalha"])
    )


def mostrar_imagem(numero):
    if numero <= 20:
        imagem.src = "fase_" + str(numero).zfill(2) + ".png"
        imagem.style.display = "block"
    else:
        imagem.style.display = "none"


def mostrar_imagem_final(nome):
    imagem.src = nome
    imagem.style.display = "block"


def preparar(numero):
    limpar()
    atualizar_status()
    mostrar_imagem(numero)


def criar_botao(texto, funcao):
    botao = document.createElement("button")
    botao.className = "opcao"
    botao.innerText = texto

    def clicar(event):
        for b in botoes.querySelectorAll("button"):
            b.disabled = True

        botoes.innerHTML = ""
        funcao(event)

    botao.onclick = clicar
    botoes.appendChild(botao)


def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)


def perder_vida(qtd=1):
    state["vida"] = max(0, state["vida"] - qtd)
    atualizar_status()


def ganhar_vida(qtd=1):
    state["vida"] = min(5, state["vida"] + qtd)
    atualizar_status()


def perder_sanidade(qtd=1):
    state["sanidade"] = max(0, state["sanidade"] - qtd)
    atualizar_status()


def ganhar_sanidade(qtd=1):
    state["sanidade"] = min(5, state["sanidade"] + qtd)
    atualizar_status()


# =========================================================
# FASE 1
# =========================================================

def fase1(event=None):
    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Você recebeu uma carta misteriosa convidando-o
para visitar uma ilha distante.

Sua família já esteve nesse lugar no passado,
mas ninguém explica o que aconteceu.

Antes da viagem, você precisa escolher
quem será o protagonista.
""")

    criar_botao("👩 Amelie", escolher_amelie)
    criar_botao("🧑 Olivier", escolher_olivier)


def escolher_amelie(event=None):
    state["personagem"] = "Amelie"
    state["batalha"] += 1
    fase2()


def escolher_olivier(event=None):
    state["personagem"] = "Olivier"
    state["pistas"] += 1
    fase2()


# =========================================================
# FASE 2
# =========================================================

def fase2(event=None):
    preparar(2)

    mostrar("""
🚢 A VIAGEM

Durante a viagem, você encontra uma pequena caixa
entre seus pertences.

Dentro existem:

🗺️ um mapa antigo
📷 uma fotografia
🔑 uma chave enferrujada

Você só pode escolher uma.
""")

    criar_botao("🗺️ Pegar o mapa", escolha_mapa)
    criar_botao("📷 Pegar a fotografia", escolha_foto)
    criar_botao("🔑 Pegar a chave", escolha_chave)


def escolha_mapa(event=None):
    pegar("mapa antigo")
    state["pistas"] += 2
    fase3()


def escolha_foto(event=None):
    pegar("fotografia antiga")
    state["pistas"] += 1
    state["confianca_barbara"] += 1
    fase3()


def escolha_chave(event=None):
    pegar("chave enferrujada")
    state["pistas"] += 1
    state["batalha"] += 1
    fase3()


# =========================================================
# FASE 3
# =========================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
🏝️ A CHEGADA

O barco finalmente chega à ilha.

No porto você encontra Milo e Barbara.

À sua frente existem vários caminhos.

Você precisa decidir por onde começar.
""")

    criar_botao("🏘️ Ir para a vila", fase4)
    criar_botao("🌲 Ir para a floresta", fase4_floresta)
    criar_botao("🔦 Ir para o farol", fase4_farol)


def fase4_floresta(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase4()


def fase4_farol(event=None):
    pegar("lanterna")
    state["pistas"] += 2
    fase4()


# =========================================================
# FASE 4
# =========================================================

def fase4(event=None):
    preparar(4)

    mostrar("""
🏘️ A VILA

A vila parece tranquila demais.

Você pode conversar com os moradores,
investigar a igreja ou visitar uma casa abandonada.

O que você escolhe?
""")

    criar_botao("🗣️ Conversar com moradores", fase5)
    criar_botao("⛪ Investigar a igreja", fase5_igreja)
    criar_botao("🏚️ Visitar a casa abandonada", fase5_casa)


def fase5_igreja(event=None):
    state["pistas"] += 1
    pegar("fotografia dos simbolos")
    fase5()


def fase5_casa(event=None):
    state["pistas"] += 2
    pegar("documentos da familia")
    fase5()


# =========================================================
# FASE 5
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
⛪ A IGREJA

Dentro da igreja você encontra símbolos antigos
nas paredes.

Há três lugares interessantes para investigar.
""")

    criar_botao("📖 Procurar livros", fase6)
    criar_botao("🔱 Examinar os símbolos", fase6_simbolos)
    criar_botao("🚪 Procurar uma passagem", fase6_passagem)


def fase6_simbolos(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    pegar("simbolo antigo")
    fase6()


def fase6_passagem(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase6()


# =========================================================
# FASE 6
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
🏚️ A CASA ABANDONADA

A casa está coberta de poeira.

Você encontra diferentes lugares para investigar.
""")

    criar_botao("📚 Procurar na estante", fase7)
    criar_botao("📦 Abrir o baú", fase7_bau)
    criar_botao("⬇️ Descer ao porão", fase7_porao)


def fase7_bau(event=None):
    pegar("chave enferrujada")
    state["pistas"] += 1
    fase7()


def fase7_porao(event=None):
    pegar("documentos da familia")
    state["pistas"] += 3
    perder_sanidade()
    fase7()


# =========================================================
# FASE 7
# =========================================================

def fase7(event=None):
    preparar(7)

    mostrar("""
🔦 O FAROL

Dentro do farol existe uma sala escondida.

Você encontra três objetos.
""")

    criar_botao("📻 Ligar o rádio", fase8_radio)
    criar_botao("📖 Ler o livro", fase8_livro)
    criar_botao("📦 Abrir a caixa", fase8_caixa)


def fase8_radio(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase8()


def fase8_livro(event=None):
    pegar("livro antigo")
    state["pistas"] += 3
    fase8()


def fase8_caixa(event=None):
    pegar("simbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 2
    fase8()


# =========================================================
# FASE 8
# =========================================================

def fase8(event=None):
    preparar(8)

    mostrar("""
🌙 PRIMEIRA NOITE

Durante a noite você escuta três sons.

Batidas na janela.

Passos no telhado.

Um barulho vindo da floresta.

O que você investiga?
""")

    criar_botao("🪟 Janela", fase9_janela)
    criar_botao("🏠 Telhado", fase9_telhado)
    criar_botao("🌲 Floresta", fase9_floresta)


def fase9_janela(event=None):
    state["pistas"] += 2
    pegar("marca estranha")
    fase9()


def fase9_telhado(event=None):
    state["batalha"] += 1
    state["pistas"] += 1
    fase9()


def fase9_floresta(event=None):
    perder_sanidade()
    state["pistas"] += 3
    fase9()


# =========================================================
# FASE 9
# =========================================================

def fase9(event=None):
    preparar(9)

    mostrar("""
🚨 O DESAPARECIMENTO

Na manhã seguinte, um morador desapareceu.

Milo quer procurar imediatamente.

Barbara prefere investigar primeiro.

Você decide quem acompanhar.
""")

    criar_botao("🧑 Acompanhar Milo", fase10_milo)
    criar_botao("👩 Acompanhar Barbara", fase10_barbara)
    criar_botao("🔎 Investigar sozinho", fase10_sozinho)


def fase10_milo(event=None):
    state["confianca_milo"] += 2
    state["pistas"] += 2
    fase10()


def fase10_barbara(event=None):
    state["confianca_barbara"] += 2
    state["pistas"] += 2
    fase10()


def fase10_sozinho(event=None):
    state["pistas"] += 3
    perder_sanidade()
    fase10()


# =========================================================
# FASE 10
# =========================================================

def fase10(event=None):
    preparar(10)

    mostrar("""
🔎 A INVESTIGAÇÃO

Vocês encontram três pistas.

Pegadas.

Um pedaço de tecido.

Uma mensagem escrita em uma pedra.

Qual investigar?
""")

    criar_botao("🐾 Pegadas", fase11_pegadas)
    criar_botao("🧥 Tecido", fase11_tecido)
    criar_botao("🪨 Mensagem", fase11_mensagem)


def fase11_pegadas(event=None):
    state["pistas"] += 2
    fase11()


def fase11_tecido(event=None):
    pegar("tecido misterioso")
    state["pistas"] += 1
    fase11()


def fase11_mensagem(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase11()


# =========================================================
# FASE 11
# =========================================================

def fase11(event=None):
    preparar(11)

    mostrar("""
🥾 A TRILHA

A trilha se divide.

Você pode seguir por uma ponte,
pela cachoeira ou por uma caverna.
""")

    criar_botao("🌉 Ponte", fase12_ponte)
    criar_botao("💧 Cachoeira", fase12_cachoeira)
    criar_botao("🕳️ Caverna", fase12_caverna)


def fase12_ponte(event=None):
    state["pistas"] += 1
    fase12()


def fase12_cachoeira(event=None):
    pegar("cristal")
    state["pistas"] += 2
    fase12()


def fase12_caverna(event=None):
    perder_sanidade()
    state["batalha"] += 2
    state["pistas"] += 2
    fase12()


# =========================================================
# FASE 12
# =========================================================

def fase12(event=None):
    preparar(12)

    mostrar("""
🔥 O ACAMPAMENTO

Durante o acampamento, o grupo discute
qual deve ser o próximo passo.

Você precisa escolher uma estratégia.
""")

    criar_botao("🌲 Continuar pela floresta", fase13_floresta)
    criar_botao("🏘️ Voltar à vila", fase13_vila)
    criar_botao("📚 Estudar as pistas", fase13_pistas)


def fase13_floresta(event=None):
    state["batalha"] += 2
    state["pistas"] += 1
    fase13()


def fase13_vila(event=None):
    state["pistas"] += 2
    state["confianca_milo"] += 1
    fase13()


def fase13_pistas(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase13()


# =========================================================
# FASE 13
# =========================================================

def fase13(event=None):
    preparar(13)

    mostrar("""
🐾 PEGADAS GIGANTES

As pegadas ficam cada vez maiores.

Você encontra três marcas diferentes.

Uma recente.

Uma antiga.

E uma com um símbolo estranho.
""")

    criar_botao("🐾 Seguir a marca recente", fase14_recente)
    criar_botao("🕰️ Examinar a marca antiga", fase14_antiga)
    criar_botao("🔱 Examinar o símbolo", fase14_simbolo)


def fase14_recente(event=None):
    state["pistas"] += 2
    fase14()


def fase14_antiga(event=None):
    pegar("fragmento antigo")
    state["pistas"] += 2
    fase14()


def fase14_simbolo(event=None):
    pegar("simbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 2
    fase14()


# =========================================================
# FASE 14
# =========================================================

def fase14(event=None):
    preparar(14)

    mostrar("""
🏚️ A CABANA

Dentro da cabana existem vários lugares
para procurar.
""")

    criar_botao("📚 Procurar na estante", fase15_estante)
    criar_botao("📦 Abrir o baú", fase15_bau)
    criar_botao("⬇️ Ir para o porão", fase15_porao)


def fase15_estante(event=None):
    pegar("diario")
    state["pistas"] += 2
    fase15()


def fase15_bau(event=None):
    pegar("medicamento")
    ganhar_vida()
    state["pistas"] += 1
    fase15()


def fase15_porao(event=None):
    pegar("documentos da familia")
    state["pistas"] += 3
    perder_sanidade()
    fase15()


# =========================================================
# FASE 15
# =========================================================

def fase15(event=None):
    preparar(15)

    mostrar("""
📖 O DIÁRIO

As páginas finalmente revelam uma parte
da verdade.

A criatura pode ser enfraquecida
pelo símbolo original.

Você decide o que estudar primeiro.
""")

    criar_botao("🔱 Estudar o símbolo", fase16_simbolo)
    criar_botao("💎 Estudar o cristal", fase16_cristal)
    criar_botao("🗺️ Estudar o mapa", fase16_mapa)


def fase16_simbolo(event=None):
    state["monstro_fraqueza"] = True
    state["batalha"] += 3
    state["pistas"] += 2
    fase16()


def fase16_cristal(event=None):
    pegar("cristal")
    state["batalha"] += 2
    state["pistas"] += 3
    fase16()


def fase16_mapa(event=None):
    state["pistas"] += 3
    fase16()


# =========================================================
# FASE 16
# =========================================================

def fase16(event=None):
    preparar(16)

    mostrar("""
🎒 PREPARAÇÃO

Antes de continuar, você precisa preparar
o grupo para o que vem pela frente.
""")

    criar_botao("⚔️ Pegar equipamentos", fase17_equipamentos)
    criar_botao("💊 Procurar medicamentos", fase17_medicamentos)
    criar_botao("🔎 Estudar novamente as pistas", fase17_pistas)


def fase17_equipamentos(event=None):
    pegar("equipamento")
    state["batalha"] += 3
    fase17()


def fase17_medicamentos(event=None):
    pegar("medicamento")
    ganhar_vida()
    fase17()


def fase17_pistas(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase17()


# =========================================================
# FASE 17
# =========================================================

def fase17(event=None):
    preparar(17)

    mostrar("""
💎 O LAGO

No lago existe um cristal brilhando.

Também existem marcas nas pedras
e uma passagem escondida.

O que você investiga?
""")

    criar_botao("💎 Pegar o cristal", fase18_cristal)
    criar_botao("🪨 Examinar as pedras", fase18_pedras)
    criar_botao("🚪 Entrar na passagem", fase18_passagem)


def fase18_cristal(event=None):
    pegar("cristal")
    state["batalha"] += 2
    state["pistas"] += 2
    fase18()


def fase18_pedras(event=None):
    state["pistas"] += 3
    fase18()


def fase18_passagem(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase18()


# =========================================================
# FASE 18
# =========================================================

def fase18(event=None):
    preparar(18)

    mostrar("""
🕳️ A CAVERNA

Dentro da caverna existem três caminhos.

Um possui símbolos.

Outro possui marcas de batalha.

O último está completamente escuro.
""")

    criar_botao("🔱 Caminho dos símbolos", fase19_simbolos)
    criar_botao("⚔️ Caminho das batalhas", fase19_batalha)
    criar_botao("🌑 Caminho escuro", fase19_escuro)


def fase19_simbolos(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase19()


def fase19_batalha(event=None):
    state["batalha"] += 3
    perder_vida()
    fase19()


def fase19_escuro(event=None):
    perder_sanidade()
    state["pistas"] += 2
    fase19()


# =========================================================
# FASE 19
# =========================================================

def fase19(event=None):
    preparar(19)

    mostrar("""
👹 PRIMEIRO ENCONTRO

Uma presença aparece no final da caverna.

Você não consegue enxergar claramente
o que está diante de vocês.

O que fazer?
""")

    criar_botao("🏃 Fugir", fase20_fugir)
    criar_botao("🔎 Observar", fase20_observar)
    criar_botao("⚔️ Enfrentar", fase20_enfrentar)


def fase20_fugir(event=None):
    state["batalha"] += 1
    fase20()


def fase20_observar(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    perder_sanidade()
    fase20()


def fase20_enfrentar(event=None):
    state["batalha"] += 3
    perder_vida()
    fase20()


# =========================================================
# FASE 20
# =========================================================

def fase20(event=None):
    preparar(20)

    mostrar("""
🏃 A FUGA

A criatura começa a se aproximar.

Vocês precisam escapar rapidamente.

Existem três caminhos.
""")

    criar_botao("🌉 Atravessar a ponte", fase21_ponte)
    criar_botao("🕳️ Entrar no túnel", fase21_tunel)
    criar_botao("🪜 Subir a escada", fase21_escada)


def fase21_ponte(event=None):
    perder_vida()
    fase21()


def fase21_tunel(event=None):
    state["pistas"] += 2
    fase21()


def fase21_escada(event=None):
    ganhar_sanidade()
    fase21()


# =========================================================
# FASE 21
# =========================================================

def fase21(event=None):
    preparar(21)

    mostrar("""
🔎 A VERDADE

Depois da fuga, vocês entendem melhor
o diário.

A criatura possui uma fraqueza.

Agora você precisa descobrir como
usar essa informação.
""")

    criar_botao("🔱 Estudar o símbolo", fase22_simbolo)
    criar_botao("💎 Estudar o cristal", fase22_cristal)
    criar_botao("📖 Estudar o diário", fase22_diario)


def fase22_simbolo(event=None):
    state["monstro_fraqueza"] = True
    state["batalha"] += 3
    state["pistas"] += 2
    fase22()


def fase22_cristal(event=None):
    if "cristal" in state["inv"]:
        state["monstro_fraqueza"] = True
        state["batalha"] += 3
    else:
        state["pistas"] += 1

    fase22()


def fase22_diario(event=None):
    state["monstro_fraqueza"] = True
    state["pistas"] += 3
    fase22()


# =========================================================
# FASE 22
# =========================================================

def fase22(event=None):
    preparar(22)

    mostrar("""
🏚️ O ESCONDERIJO

Finalmente vocês encontram a entrada
do esconderijo da criatura.

Antes de entrar, você precisa decidir
como agir.
""")

    criar_botao("🧑 Pedir ajuda ao Milo", fase23_milo)
    criar_botao("👩 Pedir ajuda à Barbara", fase23_barbara)
    criar_botao("🚪 Entrar sozinho", fase23_sozinho)


def fase23_milo(event=None):
    state["confianca_milo"] += 2
    state["batalha"] += 2
    fase23()


def fase23_barbara(event=None):
    state["confianca_barbara"] += 2
    state["pistas"] += 2
    fase23()


def fase23_sozinho(event=None):
    state["batalha"] += 1
    perder_sanidade()
    fase23()


# =========================================================
# FASE 23
# =========================================================

def fase23(event=None):
    preparar(23)

    mostrar("""
🆘 O RESGATE

Dentro do esconderijo vocês encontram
o morador desaparecido.

Ele está assustado.

Você precisa decidir como ajudá-lo.
""")

    criar_botao("🩹 Cuidar dele", fase24_cuidar)
    criar_botao("🏃 Tirar ele dali", fase24_fugir)
    criar_botao("🔎 Perguntar o que aconteceu", fase24_perguntar)


def fase24_cuidar(event=None):
    ganhar_vida()
    state["pistas"] += 1
    fase24()


def fase24_fugir(event=None):
    state["batalha"] += 1
    fase24()


def fase24_perguntar(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase24()


# =========================================================
# FASE 24
# =========================================================

def fase24(event=None):
    preparar(24)

    mostrar("""
⚔️ A ENTRADA FINAL

Vocês chegam à última parte do esconderijo.

A criatura está nas profundezas.

Você precisa decidir como entrar.
""")

    criar_botao("⚔️ Entrar preparado", fase25)
    criar_botao("🔎 Procurar outra entrada", fase25_outra)
    criar_botao("👥 Entrar com o grupo", fase25_grupo)


def fase25_outra(event=None):
    state["pistas"] += 2
    fase25()


def fase25_grupo(event=None):
    state["confianca_milo"] += 1
    state["confianca_barbara"] += 1
    fase25()


# =========================================================
# FASE 25
# =========================================================

def fase25(event=None):
    preparar(25)

    mostrar("""
🚪 A CÂMARA FINAL

A porta se abre lentamente.

Do outro lado existem quatro possibilidades.

Uma passagem iluminada.

Uma sala cheia de símbolos.

Uma escada para baixo.

E uma porta marcada com o símbolo da ilha.

Qual caminho você escolhe?
""")

    criar_botao("💡 Passagem iluminada", fase26_luz)
    criar_botao("🔱 Sala dos símbolos", fase26_simbolos)
    criar_botao("⬇️ Escada para baixo", fase26_escada)
    criar_botao("🚪 Porta da ilha", fase26_porta)


def fase26_luz(event=None):
    state["sanidade"] = min(5, state["sanidade"] + 1)
    fase26()


def fase26_simbolos(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase26()


def fase26_escada(event=None):
    state["batalha"] += 2
    fase26()


def fase26_porta(event=None):
    state["pistas"] += 2
    fase26()


# =========================================================
# FASE 26
# =========================================================

def fase26(event=None):
    preparar(26)

    mostrar("""
⚔️ O CONFRONTO

A criatura finalmente aparece.

Você percebe que ainda existem várias
formas de enfrentar a situação.

Escolha sua estratégia.
""")

    criar_botao("⚔️ Atacar", luta_atacar)
    criar_botao("🔎 Procurar a fraqueza", luta_fraqueza)
    criar_botao("🛡️ Defender o grupo", luta_defender)
    criar_botao("🔱 Usar o símbolo", luta_simbolo)


def luta_atacar(event=None):
    state["batalha"] += 3
    perder_vida()
    fase27()


def luta_fraqueza(event=None):
    state["pistas"] += 2
    state["batalha"] += 2

    if state["monstro_fraqueza"]:
        state["batalha"] += 2

    fase27()


def luta_defender(event=None):
    state["batalha"] += 1
    ganhar_sanidade()
    fase27()


def luta_simbolo(event=None):
    state["monstro_fraqueza"] = True
    state["batalha"] += 4
    state["pistas"] += 2
    fase27()


# =========================================================
# FASE 27
# =========================================================

def fase27(event=None):
    preparar(27)

    mostrar("""
🔱 O SÍMBOLO ORIGINAL

O símbolo antigo começa a brilhar.

A criatura recua.

Você precisa decidir como utilizar
o símbolo.
""")

    criar_botao("⚔️ Usar toda a força", fase28_forca)
    criar_botao("🔱 Fazer o ritual", fase28_ritual)
    criar_botao("👥 Pedir ajuda ao grupo", fase28_grupo)


def fase28_forca(event=None):
    state["batalha"] += 4
    fase28()


def fase28_ritual(event=None):
    state["pistas"] += 3
    state["batalha"] += 2
    state["monstro_fraqueza"] = True
    fase28()


def fase28_grupo(event=None):
    state["confianca_milo"] += 1
    state["confianca_barbara"] += 1
    state["batalha"] += 2
    fase28()


# =========================================================
# FASE 28
# =========================================================

def fase28(event=None):
    preparar(28)

    mostrar("""
💎 O CRISTAL

O cristal começa a emitir uma luz intensa.

Ele parece reagir ao símbolo antigo.

Como você vai utilizá-lo?
""")

    criar_botao("💎 Aproximar do símbolo", fase29_simbolo)
    criar_botao("💎 Usar contra a criatura", fase29_criatura)
    criar_botao("💎 Colocar no chão", fase29_chao)
    criar_botao("💎 Guardar o cristal", fase29_guardar)


def fase29_simbolo(event=None):
    if "cristal" in state["inv"]:
        state["monstro_fraqueza"] = True
        state["batalha"] += 4
        state["pistas"] += 2
    else:
        state["pistas"] += 1

    fase29()


def fase29_criatura(event=None):
    if "cristal" in state["inv"]:
        state["batalha"] += 4
    else:
        perder_vida()

    fase29()


def fase29_chao(event=None):
    state["pistas"] += 3
    state["batalha"] += 2
    fase29()


def fase29_guardar(event=None):
    state["pistas"] += 1
    fase29()


# =========================================================
# FASE 29
# =========================================================

def fase29(event=None):
    preparar(29)

    mostrar("""
🔒 O ÚLTIMO RITUAL

A sala começa a tremer.

Você entende que precisa tomar
uma decisão definitiva.

O que fazer?
""")

    criar_botao("⚔️ Derrotar a criatura", final_derrotar)
    criar_botao("🔒 Selar a criatura", final_selar)
    criar_botao("💎 Usar o cristal para encerrar tudo", final_cristal)
    criar_botao("🏃 Fugir da ilha", final_fugir)


def final_derrotar(event=None):
    if state["monstro_fraqueza"] and (
        state["batalha"] >= 8 or state["pistas"] >= 10
    ):
        state["monstro_derrotado"] = True
        state["final"] = "derrotar"
    else:
        state["final"] = "derrotar_parcial"

    fase30()


def final_selar(event=None):
    state["final"] = "selar"
    state["monstro_derrotado"] = False
    fase30()


def final_cristal(event=None):
    if "cristal" in state["inv"] and state["monstro_fraqueza"]:
        state["monstro_derrotado"] = True
        state["final"] = "derrotar"
    else:
        state["final"] = "selar"

    fase30()


def final_fugir(event=None):
    state["final"] = "fugir"
    state["monstro_derrotado"] = False
    fase30()


# =========================================================
# FASE 30 — FINAIS
# =========================================================

def fase30(event=None):
    limpar()
    atualizar_status()

    # =====================================================
    # FINAL 1
    # =====================================================

    if state["monstro_derrotado"]:
        state["final"] = "derrotar"

        mostrar_imagem_final("final_01.png")

        mostrar("""
🌟 FINAL 1 — O SEGREDO REVELADO

Você conseguiu derrotar a criatura.

Todas as pistas encontradas durante
a investigação finalmente fizeram sentido.

O símbolo antigo e o cristal revelam
a verdade escondida na ilha.

A criatura desaparece.

A ilha está livre.

Milo e Barbara observam tudo em silêncio.

Os documentos mostram que sua família
esteve ligada à proteção daquele lugar.

Depois de tantos anos,
o segredo da ilha finalmente foi descoberto.

🏝️ A ilha está livre.

🌟 VOCÊ CONSEGUIU O MELHOR FINAL!
""")

        criar_botao(
            "▶️ ASSISTIR AO VÍDEO FINAL",
            assistir_video
        )

    # =====================================================
    # FINAL 2
    # =====================================================

    elif state["final"] == "derrotar_parcial":
        mostrar_imagem_final("final_02.png")

        mostrar("""
🌅 FINAL 2 — VITÓRIA PARCIAL

Você enfrentou a criatura.

O confronto foi difícil.

Mesmo sem conseguir reunir todas
as informações necessárias,
vocês conseguem impedir que ela
continue avançando.

A ilha está mais segura.

Mas muitas perguntas continuam
sem resposta.

Talvez alguém precise continuar
a investigação no futuro.
""")

    # =====================================================
    # FINAL 3
    # =====================================================

    elif state["final"] == "selar":
        mostrar_imagem_final("final_03.png")

        mostrar("""
🔒 FINAL 3 — O SELAMENTO

Você decide não destruir a criatura.

Em vez disso, usa os símbolos antigos
para selá-la novamente.

O ritual funciona.

A passagem começa a desaparecer.

A criatura volta para as profundezas.

A ilha está segura.

Mas a criatura não foi destruída.

Algum dia, alguém poderá precisar
voltar para aquele lugar.
""")

    # =====================================================
    # FINAL 6
    # =====================================================

    elif state["final"] == "fugir":
        mostrar_imagem_final("final_06.png")

        mostrar("""
🏃 FINAL 6 — FUGA

Você decide fugir da ilha.

Milo ajuda todos a chegar ao barco.

Barbara leva consigo algumas das pistas.

O barco se afasta lentamente.

A ilha desaparece no horizonte.

Vocês sobreviveram.

Mas o segredo continua escondido.

A criatura ainda está lá.

E talvez algum dia alguém volte
para descobrir a verdade.
""")

    # =====================================================
    # FIM
    # =====================================================

    mostrar("""
🎮 FIM DO JOGO

🏝️ O SEGREDO NA ILHA

Obrigado por jogar!
""")

    criar_botao("🔄 Jogar novamente", reiniciar)


# =========================================================
# VÍDEO
# =========================================================

def assistir_video(event=None):
    video_final.style.display = "block"
    video_final.currentTime = 0

    promessa = video_final.play()

    if promessa:
        promessa.catch(
            lambda erro: print(
                "Não foi possível iniciar o vídeo:",
                erro
            )
        )


# =========================================================
# REINICIAR
# =========================================================

def reiniciar(event=None):

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
    state["final"] = ""

    fase1()


# =========================================================
# COMEÇAR O JOGO
# =========================================================

fase1()
