from js import document

tela = document.getElementById("jogo")
botoes = document.getElementById("botoes")
imagem = document.getElementById("imagem-fase")
status = document.getElementById("status")
video_final = document.getElementById("video-final")

# =========================================================
# ESTADO
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

    video_final.pause()
    video_final.currentTime = 0
    video_final.style.display = "none"


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
        # Impede dois cliques
        for b in botoes.querySelectorAll("button"):
            b.disabled = True

        # Apaga as opções antigas
        botoes.innerHTML = ""

        # Vai para a próxima parte
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
mas ninguém explica exatamente o que aconteceu.

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

Dentro existem três coisas:

um mapa antigo,
uma fotografia,
e uma chave enferrujada.

Você só pode levar uma delas.
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

O barco chega à ilha.

No porto você encontra Milo e Barbara.

Os dois parecem conhecer muito bem o lugar.

Milo diz que existe uma vila próxima.

Barbara diz que existem três caminhos:

a vila,
a floresta,
ou o farol.

Onde você vai primeiro?
""")

    criar_botao("🏘️ Ir para a vila", fase4_vila)
    criar_botao("🌲 Ir para a floresta", fase4_floresta)
    criar_botao("🔦 Ir para o farol", fase4_farol)


def fase4_vila(event=None):
    state["pistas"] += 1
    state["confianca_milo"] += 1
    fase5()


def fase4_floresta(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase6()


def fase4_farol(event=None):
    pegar("lanterna")
    state["pistas"] += 2
    fase7()


# =========================================================
# FASE 5
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
🏘️ A VILA

A vila parece tranquila.

Você pode conversar com os moradores,
investigar a igreja ou visitar a casa abandonada.

O que você escolhe?
""")

    criar_botao("🗣️ Conversar com moradores", fase5_moradores)
    criar_botao("⛪ Investigar a igreja", fase5_igreja)
    criar_botao("🏚️ Visitar casa abandonada", fase5_casa)


def fase5_moradores(event=None):
    state["pistas"] += 2
    state["confianca_milo"] += 1
    pegar("relato dos moradores")
    fase8()


def fase5_igreja(event=None):
    state["pistas"] += 1
    pegar("fotografia dos simbolos")
    fase8()


def fase5_casa(event=None):
    state["pistas"] += 2
    pegar("documentos da familia")
    fase8()


# =========================================================
# FASE 6
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
🌲 A FLORESTA

Você entra na floresta.

Depois de algum tempo encontra três caminhos.

Um segue para um rio.

Outro segue para uma cabana.

O terceiro parece levar para uma região
muito mais escura da floresta.
""")

    criar_botao("💧 Seguir para o rio", fase6_rio)
    criar_botao("🏚️ Procurar a cabana", fase6_cabana)
    criar_botao("🌑 Entrar na parte escura", fase6_escura)


def fase6_rio(event=None):
    pegar("cristal")
    state["pistas"] += 2
    fase8()


def fase6_cabana(event=None):
    pegar("diario")
    state["pistas"] += 3
    fase8()


def fase6_escura(event=None):
    perder_sanidade()
    state["batalha"] += 2
    state["pistas"] += 2
    fase8()


# =========================================================
# FASE 7
# =========================================================

def fase7(event=None):
    preparar(7)

    mostrar("""
🔦 O FAROL

Dentro do farol você encontra uma sala escondida.

Existem três objetos.

Um rádio antigo.

Um livro.

Uma caixa metálica.

Qual você investiga?
""")

    criar_botao("📻 Ligar o rádio", fase7_radio)
    criar_botao("📖 Ler o livro", fase7_livro)
    criar_botao("📦 Abrir a caixa", fase7_caixa)


def fase7_radio(event=None):
    state["pistas"] += 2
    perder_sanidade()
    fase8()


def fase7_livro(event=None):
    pegar("livro antigo")
    state["pistas"] += 3
    fase8()


def fase7_caixa(event=None):
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

E um barulho vindo da floresta.

Você precisa decidir o que investigar.
""")

    criar_botao("🪟 Janela", fase8_janela)
    criar_botao("🏠 Telhado", fase8_telhado)
    criar_botao("🌲 Floresta", fase8_floresta)


def fase8_janela(event=None):
    state["pistas"] += 2
    pegar("marca estranha")
    fase9()


def fase8_telhado(event=None):
    state["batalha"] += 1
    state["pistas"] += 1
    fase9()


def fase8_floresta(event=None):
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

Barbara quer investigar primeiro.

Você precisa decidir quem acompanhar.
""")

    criar_botao("🧑 Acompanhar Milo", fase9_milo)
    criar_botao("👩 Acompanhar Barbara", fase9_barbara)
    criar_botao("🔎 Investigar sozinho", fase9_sozinho)


def fase9_milo(event=None):
    state["confianca_milo"] += 2
    state["pistas"] += 2
    fase10()


def fase9_barbara(event=None):
    state["confianca_barbara"] += 2
    state["pistas"] += 2
    fase10()


def fase9_sozinho(event=None):
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

E uma mensagem escrita em uma pedra.

Qual pista investigar primeiro?
""")

    criar_botao("🐾 Pegadas", fase10_pegadas)
    criar_botao("🧥 Tecido", fase10_tecido)
    criar_botao("🪨 Mensagem", fase10_mensagem)


def fase10_pegadas(event=None):
    state["pistas"] += 2
    fase11()


def fase10_tecido(event=None):
    pegar("tecido misterioso")
    state["pistas"] += 1
    fase11()


def fase10_mensagem(event=None):
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

A trilha se divide novamente.

Uma direção leva até uma ponte.

Outra leva até uma cachoeira.

Outra parece seguir para uma caverna.
""")

    criar_botao("🌉 Ponte", fase11_ponte)
    criar_botao("💧 Cachoeira", fase11_cachoeira)
    criar_botao("🕳️ Caverna", fase11_caverna)


def fase11_ponte(event=None):
    state["pistas"] += 1
    fase12()


def fase11_cachoeira(event=None):
    pegar("cristal")
    state["pistas"] += 2
    fase12()


def fase11_caverna(event=None):
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

Durante o acampamento, vocês discutem
o que fazer.

Milo quer continuar pela floresta.

Barbara quer voltar à vila.

Você pode escolher a estratégia.
""")

    criar_botao("🌲 Continuar pela floresta", fase12_floresta)
    criar_botao("🏘️ Voltar à vila", fase12_vila)
    criar_botao("📚 Estudar as pistas", fase12_pistas)


def fase12_floresta(event=None):
    state["batalha"] += 2
    state["pistas"] += 1
    fase13()


def fase12_vila(event=None):
    state["pistas"] += 2
    state["confianca_milo"] += 1
    fase13()


def fase12_pistas(event=None):
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

As pegadas ficam maiores.

Vocês encontram três marcas diferentes.

Uma parece recente.

Outra parece antiga.

E a terceira possui um símbolo estranho.
""")

    criar_botao("🐾 Seguir a marca recente", fase13_recente)
    criar_botao("🕰️ Examinar a marca antiga", fase13_antiga)
    criar_botao("🔱 Examinar o símbolo", fase13_simbolo)


def fase13_recente(event=None):
    state["pistas"] += 2
    fase14()


def fase13_antiga(event=None):
    pegar("fragmento antigo")
    state["pistas"] += 2
    fase14()


def fase13_simbolo(event=None):
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

Dentro da cabana existem três lugares para procurar.

Uma estante.

Um baú.

Um porão.

Onde você vai procurar?
""")

    criar_botao("📚 Estante", fase14_estante)
    criar_botao("📦 Baú", fase14_bau)
    criar_botao("⬇️ Porão", fase14_porao)


def fase14_estante(event=None):
    pegar("diario")
    state["pistas"] += 2
    fase15()


def fase14_bau(event=None):
    pegar("medicamento")
    ganhar_vida()
    state["pistas"] += 1
    fase15()


def fase14_porao(event=None):
    pegar("documentos da familia")
    state["pistas"] += 3
    perder_sanidade()
    fase15()


# =========================================================
# FASE 15
# =========================================================

def fase15(event=None):
    preparar(15)

    state["monstro_fraqueza"] = True

    mostrar("""
📖 O DIÁRIO

As páginas finalmente revelam a verdade.

A criatura pode ser enfraquecida pelo símbolo original.

Porém, o diário apresenta três possibilidades.

Usar o símbolo.

Usar o cristal.

Ou tentar destruir a entrada do esconderijo.
""")

    criar_botao("🔱 Usar o símbolo", fase15_simbolo)
    criar_botao("💎 Estudar o cristal", fase15_cristal)
    criar_botao("🪨 Estudar a entrada", fase15_entrada)


def fase15_simbolo(event=None):
    state["monstro_fraqueza"] = True
    state["batalha"] += 3
    state["pistas"] += 2
    fase16()


def fase15_cristal(event=None):
    pegar("cristal")
    state["batalha"] += 2
    state["pistas"] += 3
    fase16()


def fase15_entrada(event=None):
    state["pistas"] += 3
    state["batalha"] += 1
    fase16()


# =========================================================
# FASE 16
# =========================================================

def fase16(event=None):
    preparar(16)

    mostrar("""
🎒 PREPARAÇÃO

Antes de continuar, você pode escolher
como preparar o grupo.

Equipamentos.

Medicamentos.

Ou estudar novamente as pistas.
""")

    criar_botao("⚔️ Equipamentos", fase16_equipamentos)
    criar_botao("💊 Medicamentos", fase16_medicamentos)
    criar_botao("🔎 Estudar pistas", fase16_pistas)


def fase16_equipamentos(event=None):
    pegar("equipamento")
    state["batalha"] += 3
    fase17()


def fase16_medicamentos(event=None):
    pegar("medicamento")
    ganhar_vida()
    fase17()


def fase16_pistas(event=None):
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

No lago vocês encontram um cristal brilhando.

Mas também existem marcas nas pedras.

E uma passagem escondida.

O que investigar?
""")

    criar_botao("💎 Pegar o cristal", fase17_cristal)
    criar_botao("🪨 Examinar as pedras", fase17_pedras)
    criar_botao("🚪 Entrar na passagem", fase17_passagem)


def fase17_cristal(event=None):
    pegar("cristal")
    state["batalha"] += 2
    state["pistas"] += 2
    fase18()


def fase17_pedras(event=None):
    state["pistas"] += 3
    fase18()


def fase17_passagem(event=None):
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

    criar_botao("🔱 Caminho dos símbolos", fase18_simbolos)
    criar_botao("⚔️ Caminho das batalhas", fase18_batalha)
    criar_botao("🌑 Caminho escuro", fase18_escuro)


def fase18_simbolos(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    fase19()


def fase18_batalha(event=None):
    state["batalha"] += 3
    perder_vida()
    fase19()


def fase18_escuro(event=None):
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

Você não consegue ver claramente o que é.

Milo quer fugir.

Barbara quer observar.

Você precisa decidir.
""")

    criar_botao("🏃 Fugir", fase19_fugir)
    criar_botao("🔎 Observar", fase19_observar)
    criar_botao("⚔️ Enfrentar", fase19_enfrentar)


def fase19_fugir(event=None):
    state["batalha"] += 1
    fase20()


def fase19_observar(event=None):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True
    perder_sanidade()
    fase20()


def fase19_enfrentar(event=None):
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

A criatura se aproxima.

Vocês precisam escapar.

Há três possibilidades.

Uma ponte antiga.

Um túnel.

Ou uma escada.
""")

    criar_botao("🌉 Ponte", fase20_ponte)
    criar_botao("🕳️ Túnel", fase20_tunel)
    criar_botao("🪜 Escada", fase20_escada)


def fase20_ponte(event=None):
    perder_vida()
    fase21()


def fase20_tunel(event=None):
    state["pistas"] += 2
    fase21()


def fase20_escada(event=None):
    ganhar_sanidade()
    fase21()


# =========================================================
# FASE 21
# =========================================================

def fase21(event=None):
    preparar(21)

    mostrar("""
🔎 A VERDADE

Depois da fuga, vocês conseguem entender
uma parte importante do diário.

A criatura possui uma fraqueza.

Agora vocês precisam descobrir como
usar essa informação.
""")

    criar_botao("🔱 Estudar o símbolo", fase21_simbolo)
    criar_botao("💎 Estudar o cristal", fase21_cristal)
    criar_botao("📖 Estudar o diário", fase21_diario)


def fase21_simbolo(event=None):
    state["monstro_fraqueza"] = True
    state["batalha"] += 3
    state["pistas"] += 2
    fase22()


def fase21_cristal(event=None):
    if "cristal" in state["inv"]:
        state["monstro_fraqueza"] = True
        state["batalha"] += 3
    else:
        state["pistas"] += 1

    fase22()


def fase21_diario(event=None):
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

Vocês encontram a entrada do esconderijo.

Antes de entrar, existem três maneiras
de se preparar.

Milo pode ajudar.

Barbara pode ajudar.

Ou você pode entrar sozinho.
""")

    criar_botao("🧑 Pedir ajuda ao Milo", fase22_milo)
    criar_botao("👩 Pedir ajuda à Barbara", fase22_barbara)
    criar_botao("🚪 Entrar sozinho", fase22_sozinho)


def fase22_milo(event=None):
    state["confianca_milo"] += 2
    state["batalha"] += 2
    fase23()


def fase22_barbara(event=None):
    state["confianca_barbara"] += 2
    state["pistas"] += 2
    fase23()


def fase22_sozinho(event=None):
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

Existem três maneiras de ajudá-lo.
""")

    criar_botao("🩹 Cuidar dele", fase23_cuidar)
    criar_botao("🏃 Tirar ele imediatamente", fase23_fugir)
    criar_botao("🔎 Perguntar o que aconteceu", fase23_perguntar)


def fase23_cuidar(event=None):
    ganhar_vida()
    state["pistas"] += 1
    fase24()


def fase23_fugir(event=None):
    state["batalha"] += 1
    fase24()


def fase23_perguntar(event=None):
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

Vocês finalmente chegam à última sala.

A criatura está escondida nas profundezas.

Você possui todas as pistas que conseguiu
reunir durante a aventura.

Agora existem várias possibilidades.

O que você fará?
""")

    criar_botao("⚔️ Preparar para lutar", fase26)
    criar_botao("🔱 Usar o símbolo", fase27)
    criar_botao("💎 Usar o cristal", fase28)
    criar_botao("🔒 Tentar selar", fase29)
    criar_botao("🏃 Fugir", final_fugir)


# =========================================================
# FASE 25
# =========================================================
# Essa fase funciona como uma pausa antes
# das decisões finais.

def fase25(event=None):
    fase24()


# =========================================================
# FASE 26
# =========================================================

def fase26(event=None):
    preparar(26)

    mostrar("""
⚔️ CONFRONTO

Você decide enfrentar a criatura diretamente.

A batalha é difícil.

Você precisa confiar nas pistas encontradas
durante toda a investigação.
""")

    criar_botao("⚔️ Atacar", luta_atacar)
    criar_botao("🔎 Procurar fraqueza", luta_fraqueza)
    criar_botao("🛡️ Defender", luta_defender)


def luta_atacar(event=None):
    state["batalha"] += 2
    perder_vida()

    if state["batalha"] >= 8 and state["monstro_fraqueza"]:
        state["monstro_derrotado"] = True

    fase30()


def luta_fraqueza(event=None):
    state["pistas"] += 2
    state["batalha"] += 2

    if state["monstro_fraqueza"] and state["pistas"] >= 8:
        state["monstro_derrotado"] = True

    fase30()


def luta_defender(event=None):
    state["batalha"] += 1
    ganhar_sanidade()

    if state["batalha"] >= 10 and state["monstro_fraqueza"]:
        state["monstro_derrotado"] = True

    fase30()


# =========================================================
# FASE 27
# =========================================================

def fase27(event=None):
    preparar(27)

    state["monstro_fraqueza"] = True
    state["batalha"] += 4
    state["pistas"] += 2

    mostrar("""
🔱 O SÍMBOLO ORIGINAL

Você levanta o símbolo antigo.

A criatura reage imediatamente.

As paredes começam a brilhar.

Agora você precisa decidir como terminar
o confronto.
""")

    criar_botao("⚔️ Usar toda a força", simbolo_forca)
    criar_botao("🔱 Repetir os símbolos", simbolo_ritual)


def simbolo_forca(event=None):
    state["batalha"] += 3
    state["monstro_derrotado"] = True
    fase30()


def simbolo_ritual(event=None):
    state["pistas"] += 3
    state["batalha"] += 2
    state["monstro_derrotado"] = True
    fase30()


# =========================================================
# FASE 28
# =========================================================

def fase28(event=None):
    preparar(28)

    mostrar("""
💎 O CRISTAL

O cristal começa a emitir uma luz forte.

Você percebe que ele reage ao símbolo.

Como você vai utilizá-lo?
""")

    criar_botao("💎 Aproximar do símbolo", cristal_simbolo)
    criar_botao("💎 Jogar contra a criatura", cristal_monstro)
    criar_botao("💎 Colocar no chão", cristal_chao)


def cristal_simbolo(event=None):
    if "cristal" in state["inv"] and state["monstro_fraqueza"]:
        state["monstro_derrotado"] = True
        state["batalha"] += 4
        state["pistas"] += 2
    else:
        state["batalha"] += 1

    fase30()


def cristal_monstro(event=None):
    if "cristal" in state["inv"]:
        state["batalha"] += 3
        state["monstro_derrotado"] = state["batalha"] >= 8
    else:
        perder_vida()

    fase30()


def cristal_chao(event=None):
    state["pistas"] += 2
    state["batalha"] += 2
    fase30()


# =========================================================
# FASE 29
# =========================================================

def fase29(event=None):
    preparar(29)

    mostrar("""
🔒 O SELAMENTO

Você decide tentar selar a criatura.

Os símbolos começam a brilhar.

Agora existem três maneiras de completar
o ritual.
""")

    criar_botao("🔱 Usar o símbolo", selar_simbolo)
    criar_botao("💎 Usar o cristal", selar_cristal)
    criar_botao("📖 Seguir o diário", selar_diario)


def selar_simbolo(event=None):
    state["monstro_derrotado"] = False
    state["final"] = "selar"
    fase30()


def selar_cristal(event=None):
    state["monstro_derrotado"] = False
    state["final"] = "selar"
    state["pistas"] += 2
    fase30()


def selar_diario(event=None):
    state["monstro_derrotado"] = False
    state["final"] = "selar"
    state["pistas"] += 3
    fase30()


# =========================================================
# FUGIR
# =========================================================

def final_fugir(event=None):
    state["final"] = "fugir"
    state["monstro_derrotado"] = False
    fase30()


# =========================================================
# FASE 30 - FINAIS
# =========================================================

def fase30(event=None):
    limpar()
    atualizar_status()

    # FINAL 1
    if state["monstro_derrotado"]:
        state["final"] = "derrotar"

        mostrar_imagem_final("final_01.png")

        mostrar("""
🌟 FINAL 1 — O SEGREDO REVELADO

Você conseguiu derrotar a criatura.

O símbolo antigo e as pistas encontradas
durante sua investigação finalmente fizeram
sentido.

A criatura desaparece.

A ilha está livre.

Milo e Barbara observam o local em silêncio.

Depois de tantos anos, o segredo da ilha
finalmente foi descoberto.

Os documentos mostram que sua família
esteve ligada à proteção daquele lugar.

Você decide levar as provas para a vila.

A verdade finalmente será conhecida.

🏝️ A ilha está livre.
🌟 VOCÊ CONSEGUIU O MELHOR FINAL!
""")

        criar_botao(
            "▶️ ASSISTIR AO VÍDEO FINAL",
            assistir_video
        )

    # FINAL 2
    elif state["final"] == "derrotar":
        mostrar_imagem_final("final_02.png")

        mostrar("""
🌅 FINAL 2 — VITÓRIA PARCIAL

Você tentou derrotar a criatura.

O confronto foi difícil.

Mesmo sem conseguir usar todas as pistas,
vocês conseguem impedir que ela saia
do esconderijo.

A ilha está mais segura.

Mas muitas perguntas continuam sem resposta.

Talvez outra pessoa precise continuar
a investigação no futuro.
""")

    # FINAL 3
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

    # FINAL 6
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
# COMEÇAR
# =========================================================

fase1()
