from js import document

# ============================================================
# O SEGREDO NA ILHA
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

    "batalha": 0,

    "escolheu_derrotar": False,
    "escolheu_selar": False,
    "escolheu_fugir": False
}


# ============================================================
# FUNÇÕES BÁSICAS
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
        "❤️ Vida: " + str(state["vida"]) +
        " | 🧠 Sanidade: " + str(state["sanidade"]) +
        " | 🔎 Pistas: " + str(state["pistas"]) +
        " | 🎒 Itens: " + str(len(state["inv"]))
    )


def mostrar_imagem(numero):
    imagem.src = "fase_" + str(numero).zfill(2) + ".png"
    imagem.style.display = "block"


def mostrar_final(nome):
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
    botao.onclick = funcao
    botoes.appendChild(botao)


def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)


def perder_vida(qtd=1):
    state["vida"] = max(0, state["vida"] - qtd)
    atualizar_status()


def perder_sanidade(qtd=1):
    state["sanidade"] = max(0, state["sanidade"] - qtd)
    atualizar_status()


def ganhar_sanidade(qtd=1):
    state["sanidade"] = min(5, state["sanidade"] + qtd)
    atualizar_status()


# ============================================================
# FASE 1 - ESCOLHA DO PERSONAGEM
# ============================================================

def fase1(event=None):
    preparar(1)

    mostrar("""
    🏝️ O SEGREDO NA ILHA

    Uma antiga história está prestes a começar.

    Você está prestes a viajar para uma pequena ilha,
    onde existem histórias sobre desaparecimentos,
    símbolos antigos e acontecimentos que ninguém
    consegue explicar.

    Antes de começar a viagem, você precisa escolher
    quem será o personagem principal da história.

    Você poderá jogar como:

    👩 AMELIE
    ou
    🧑 OLIVIER

    A escolha muda a forma como a história é contada,
    mas os dois personagens estão viajando juntos.
    """)

    criar_botao("👩 Ser Amelie", escolher_amelie)
    criar_botao("🧑 Ser Olivier", escolher_olivier)


def escolher_amelie(event=None):
    state["personagem"] = "Amelie"
    fase2()


def escolher_olivier(event=None):
    state["personagem"] = "Olivier"
    fase2()


# ============================================================
# FASE 2 - A VIAGEM
# ============================================================

def fase2(event=None):
    preparar(2)

    mostrar("""
    🚢 A VIAGEM

    O barco atravessa o mar enquanto a ilha começa
    a aparecer no horizonte.

    Você está viajando ao lado de seu irmão, seguindo
    documentos antigos encontrados pela família.

    Esses documentos mencionavam uma pessoa da família
    que desapareceu muitos anos atrás.

    Quanto mais vocês pesquisaram, mais perguntas
    apareceram.

    Por que aquela pessoa esteve na ilha?

    O que ela descobriu?

    E por que ninguém fala sobre isso?

    O barco continua avançando.

    A ilha está cada vez mais próxima.
    """)

    criar_botao("🔎 Ler novamente os documentos", fase3_documentos)
    criar_botao("🌊 Observar a ilha", fase3_observar)


def fase3_documentos(event=None):
    state["pistas"] += 1
    pegar("documentos da família")
    fase3()


def fase3_observar(event=None):
    state["sanidade"] = max(0, state["sanidade"] - 0)
    fase3()


# ============================================================
# FASE 3 - CHEGADA À ILHA
# ============================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
    🏝️ A CHEGADA À ILHA

    Finalmente, o barco chega à ilha.

    Você e seu irmão desembarcam no pequeno porto.

    A ilha parece tranquila à primeira vista.

    Algumas casas aparecem ao longe e uma pequena
    vila se espalha pela região.

    Duas pessoas estão esperando vocês no porto.

    São Milo e Barbara.

    Eles já vivem na ilha há bastante tempo e conhecem
    praticamente todos os lugares da região.

    Milo se aproxima.

    — Vocês finalmente chegaram.

    Barbara observa os documentos que vocês carregam.

    — Imagino que tenham vindo procurar respostas.

    A investigação começa.
    """)

    criar_botao("🗣️ Falar com Milo", fase4_milo)
    criar_botao("🗣️ Falar com Barbara", fase4_barbara)


# ============================================================
# FASE 4 - CONHECENDO A VILA
# ============================================================

def fase4_milo(event=None):
    state["confianca_milo"] += 1
    state["pistas"] += 1
    fase4()


def fase4_barbara(event=None):
    state["confianca_barbara"] += 1
    state["pistas"] += 1
    fase4()


def fase4(event=None):
    preparar(4)

    mostrar("""
    🏘️ CONHECENDO A VILA

    Milo e Barbara levam vocês para conhecer a vila.

    Como moram ali há anos, eles sabem quais lugares
    são importantes para a história da ilha.

    Milo aponta para uma construção antiga.

    — Aquela é a igreja.

    Barbara aponta para uma casa abandonada.

    — Aquela casa está vazia há muitos anos.

    Mais distante, no alto de uma região rochosa,
    existe um velho farol.

    — E aquele é o farol — explica Milo.

    Existem vários lugares para investigar.
    """)

    criar_botao("⛪ Investigar a igreja", fase5_igreja)
    criar_botao("🏚️ Investigar a casa abandonada", fase6_casa)
    criar_botao("🔦 Investigar o farol", fase7_farol)


# ============================================================
# FASE 5 - A IGREJA
# ============================================================

def fase5_igreja(event=None):
    preparar(5)

    mostrar("""
    ⛪ A IGREJA

    A antiga igreja está praticamente abandonada.

    O interior é silencioso e algumas partes da construção
    parecem muito antigas.

    Nas paredes existem símbolos desenhados.

    Barbara reconhece alguns deles.

    — Minha família já contou histórias sobre esses símbolos.

    Milo observa uma parte da parede.

    — Talvez exista alguma coisa escondida aqui.

    Você precisa escolher como investigar.
    """)

    criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
    criar_botao("📖 Procurar livros antigos", fase5_livros)


def fase5_simbolos(event=None):
    state["pistas"] += 2
    pegar("fotografia dos símbolos")
    fase6_casa()


def fase5_livros(event=None):
    state["pistas"] += 2
    pegar("livro antigo")
    fase6_casa()


# ============================================================
# FASE 6 - CASA ABANDONADA
# ============================================================

def fase6_casa(event=None):
    preparar(6)

    mostrar("""
    🏚️ A CASA ABANDONADA

    A casa está coberta de poeira.

    Milo explica que ninguém mora ali há muitos anos.

    Segundo os moradores, o antigo dono desapareceu
    sem deixar muitas explicações.

    Dentro da casa existem vários cômodos.

    Talvez alguma coisa tenha sido deixada para trás.
    """)

    criar_botao("📄 Procurar documentos", fase6_documentos)
    criar_botao("📷 Procurar fotografias", fase6_fotos)
    criar_botao("⬇️ Investigar o porão", fase6_porao)


def fase6_documentos(event=None):
    state["pistas"] += 2
    pegar("documentos da família")
    fase7_farol()


def fase6_fotos(event=None):
    state["pistas"] += 2
    pegar("fotografia antiga")
    fase7_farol()


def fase6_porao(event=None):
    state["pistas"] += 3
    pegar("chave enferrujada")
    fase7_farol()


# ============================================================
# FASE 7 - FAROL
# ============================================================

def fase7_farol(event=None):
    preparar(7)

    mostrar("""
    🔦 O FAROL

    O farol fica afastado da vila.

    Milo conhece o caminho e acompanha vocês até lá.

    O lugar parece abandonado há décadas.

    No topo do farol existe uma pequena sala.

    Dentro dela vocês encontram uma caixa antiga.

    Barbara abre a caixa com cuidado.

    Há uma fotografia mostrando uma figura estranha
    próxima à região da floresta.

    Ninguém sabe exatamente o que aquela figura é.

    Mas uma coisa fica clara:

    alguma coisa estranha realmente aconteceu naquela ilha.
    """)

    state["pistas"] += 2
    pegar("fotografia da criatura")

    criar_botao("🌙 Voltar para a vila", fase8_noite)


# ============================================================
# FASE 8 - PRIMEIRA NOITE
# ============================================================

def fase8_noite(event=None):
    preparar(8)

    mostrar("""
    🌙 A PRIMEIRA NOITE

    A noite chega.

    Milo e Barbara levam vocês para uma casa onde
    vocês podem passar a noite.

    O dia foi cansativo e todos tentam descansar.

    No meio da madrugada...

    TOC.

    TOC.

    TOC.

    Alguém bate na janela.

    Milo olha para vocês.

    — Não abram.

    O som continua.

    O que você faz?
    """)

    criar_botao("🪟 Olhar pela janela", fase8_janela)
    criar_botao("😶 Ignorar as batidas", fase8_ignorar)


def fase8_janela(event=None):
    state["pistas"] += 1
    perder_sanidade()
    fase9_desaparecimento()


def fase8_ignorar(event=None):
    state["pistas"] += 1
    fase9_desaparecimento()


# ============================================================
# FASE 9 - DESAPARECIMENTO
# ============================================================

def fase9_desaparecimento(event=None):
    preparar(9)

    mostrar("""
    🚨 O DESAPARECIMENTO

    Na manhã seguinte, a vila está agitada.

    Um dos moradores desapareceu durante a noite.

    Milo conhece o homem.

    — Ele nunca faria isso sem avisar ninguém.

    Barbara começa a procurar informações.

    Vocês percebem que as marcas encontradas perto
    da casa podem estar relacionadas ao desaparecimento.

    É hora de procurar pistas.
    """)

    criar_botao("🏘️ Procurar informações na vila", fase10_vila)
    criar_botao("🐾 Seguir as marcas", fase10_marcas)


# ============================================================
# FASE 10 - PROCURANDO PISTAS
# ============================================================

def fase10_vila(event=None):
    state["pistas"] += 2
    pegar("objeto do desaparecido")
    fase11_floresta()


def fase10_marcas(event=None):
    state["pistas"] += 2
    pegar("objeto do desaparecido")
    fase11_floresta()


def fase11_floresta(event=None):
    preparar(11)

    mostrar("""
    🌲 TRILHA NA FLORESTA

    As pistas levam vocês para dentro da floresta.

    Milo vai na frente porque conhece aquela região.

    A vegetação fica cada vez mais fechada.

    Barbara percebe marcas nas árvores.

    Elas parecem indicar que alguém passou por ali
    recentemente.

    Depois de algum tempo, vocês encontram uma trilha
    escondida.

    A trilha continua para dentro da floresta.
    """)

    criar_botao("🌲 Seguir a trilha", fase12_acampamento)
    criar_botao("🔎 Examinar as marcas", fase12_examinar)


# ============================================================
# FASE 12 - ACAMPAMENTO
# ============================================================

def fase12_acampamento(event=None):
    preparar(12)

    mostrar("""
    🔥 ACAMPAMENTO

    A noite chega antes que vocês consigam voltar.

    O grupo decide montar um pequeno acampamento.

    Milo conta histórias que ouviu de sua família.

    Barbara explica que algumas dessas histórias
    falam sobre uma criatura escondida nas profundezas
    da ilha.

    Durante a conversa, vocês percebem algo estranho
    entre as árvores.

    Um barulho.

    Depois silêncio.

    Ninguém consegue descobrir o que foi.
    """)

    criar_botao("🔦 Investigar o barulho", fase13_pegadas)
    criar_botao("🔥 Permanecer no acampamento", fase13_pegadas)


def fase12_examinar(event=None):
    state["pistas"] += 1
    fase12_acampamento()


# ============================================================
# FASE 13 - PEGADAS GIGANTES
# ============================================================

def fase13_pegadas(event=None):
    preparar(13)

    state["pistas"] += 2

    mostrar("""
    🐾 PEGADAS GIGANTES

    Quando amanhece, vocês encontram pegadas enormes
    próximas ao acampamento.

    Elas não parecem pertencer a nenhum animal comum.

    Milo se abaixa para observar.

    — Eu nunca vi pegadas assim.

    Barbara compara as marcas com os desenhos encontrados
    anteriormente.

    Elas parecem seguir em direção a uma região ainda
    mais afastada da floresta.

    A trilha termina perto de uma pequena cabana.
    """)

    criar_botao("🏚️ Seguir as pegadas até a cabana", fase14_cabana)
    criar_botao("🔎 Fotografar as pegadas", fase14_cabana)


# ============================================================
# FASE 14 - CABANA
# ============================================================

def fase14_cabana(event=None):
    preparar(14)

    mostrar("""
    🏚️ A CABANA

    A cabana está escondida entre as árvores.

    Dentro existem mapas, caixas e vários livros antigos.

    Parece que alguém passou muito tempo estudando
    os acontecimentos da ilha.

    Barbara encontra um diário.

    A capa está muito desgastada.

    Milo reconhece o sobrenome escrito nela.

    — Esse nome aparece em histórias antigas da ilha.

    O diário pode finalmente explicar o que está acontecendo.
    """)

    criar_botao("📖 Pegar o diário", fase15_diario)
    criar_botao("🔎 Examinar os mapas", fase15_mapas)


def fase15_mapas(event=None):
    state["pistas"] += 2
    pegar("mapa antigo")
    fase15_diario()


def fase15_diario(event=None):
    preparar(15)

    state["pistas"] += 3
    pegar("diário")

    mostrar("""
    📖 O DIÁRIO

    O diário conta a história de uma criatura que vive
    nas profundezas da ilha.

    Anos atrás, algumas pessoas descobriram a criatura
    e tentaram impedir que ela alcançasse a superfície.

    Elas descobriram que símbolos antigos poderiam
    enfraquecê-la.

    Uma passagem chama a atenção:

    "O segredo está escondido abaixo da ilha."

    Outra anotação fala sobre um símbolo que seria
    necessário para enfrentar a criatura.

    Agora vocês sabem que o perigo é real.

    E sabem que precisam se preparar.
    """)

    state["monstro_fraqueza"] = True

    criar_botao("🎒 Procurar equipamentos", fase16_preparacao)
    criar_botao("🔎 Procurar o símbolo antigo", fase16_preparacao)


# ============================================================
# FASE 16 - PREPARAÇÃO
# ============================================================

def fase16_preparacao(event=None):
    preparar(16)

    mostrar("""
    🎒 PREPARAÇÃO

    Antes de entrar nas profundezas da ilha,
    vocês precisam se preparar.

    Milo verifica os equipamentos.

    Barbara organiza os documentos e as pistas.

    Vocês precisam decidir o que levar para a jornada.
    """)

    criar_botao("🗡️ Preparar equipamentos", fase16_equipamentos)
    criar_botao("🔱 Procurar o símbolo", fase16_simbolo)
    criar_botao("📚 Organizar as pistas", fase16_pistas)


def fase16_equipamentos(event=None):
    pegar("equipamento")
    state["batalha"] += 2
    fase17_lago()


def fase16_simbolo(event=None):
    pegar("símbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 3
    state["pistas"] += 2
    fase17_lago()


def fase16_pistas(event=None):
    state["pistas"] += 2
    fase17_lago()


# ============================================================
# FASE 17 - LAGO
# ============================================================

def fase17_lago(event=None):
    preparar(17)

    mostrar("""
    🌊 O LAGO

    As pistas levam vocês até um lago escondido.

    A água está completamente parada.

    Perto da margem existe um pequeno cristal.

    Barbara percebe que o cristal possui o mesmo símbolo
    encontrado nos documentos.

    Talvez ele tenha alguma ligação com a criatura.

    O que vocês fazem?
    """)

    criar_botao("💎 Pegar o cristal", fase17_cristal)
    criar_botao("🔎 Examinar o lago", fase17_lago_examinar)


def fase17_cristal(event=None):
    pegar("cristal")
    state["pistas"] += 2
    state["batalha"] += 2
    fase18_caverna()


def fase17_lago_examinar(event=None):
    state["pistas"] += 1
    fase18_caverna()


# ============================================================
# FASE 18 - CAVERNA
# ============================================================

def fase18_caverna(event=None):
    preparar(18)

    mostrar("""
    🕳️ A CAVERNA

    Depois do lago, vocês encontram a entrada de uma
    enorme caverna.

    Milo reconhece o lugar.

    — Meu avô falava dessa caverna.

    Nas paredes existem símbolos iguais aos encontrados
    na igreja e no diário.

    O ar parece diferente lá dentro.

    Quanto mais vocês avançam, mais escuro fica.

    No fundo da caverna existe uma passagem.
    """)

    criar_botao("🔦 Entrar na passagem", fase19_encontro)
    criar_botao("🔎 Examinar os símbolos", fase19_encontro)


# ============================================================
# FASE 19 - PRIMEIRO ENCONTRO
# ============================================================

def fase19_encontro(event=None):
    preparar(19)

    perder_sanidade()

    mostrar("""
    👹 PRIMEIRO ENCONTRO

    Um som ecoa pelas paredes.

    Todos param.

    Algo se move no fundo da caverna.

    Uma enorme silhueta aparece por alguns segundos.

    Barbara reconhece os símbolos nas paredes.

    — É ela...

    Milo percebe que vocês ainda não estão preparados.

    A criatura se aproxima.

    Não há tempo para enfrentá-la.

    Vocês precisam escapar e descobrir uma forma
    de derrotá-la.
    """)

    criar_botao("🏃 Fugir da caverna", fase20_fuga)


# ============================================================
# FASE 20 - FUGA
# ============================================================

def fase20_fuga(event=None):
    preparar(20)

    mostrar("""
    🏃 FUGA

    Vocês correm pelos corredores da caverna.

    Milo usa seu conhecimento da ilha para encontrar
    um caminho de saída.

    Barbara segura os documentos e o diário.

    Depois de muito esforço, vocês conseguem escapar.

    Agora vocês sabem que a criatura existe.

    Também sabem que existe uma forma de enfrentá-la.

    O grupo volta para a região segura da ilha.

    Tudo o que descobriram aponta para uma decisão final.
    """)

    criar_botao("⚔️ Enfrentar a criatura", final_escolha)
    criar_botao("🔒 Tentar selar a criatura", final_escolha)
    criar_botao("🏃 Abandonar a ilha", final_escolha)


# ============================================================
# ESCOLHA FINAL
# ============================================================

def final_escolha(event=None):
    texto = event.target.innerText

    if "Enfrentar" in texto:
        state["escolheu_derrotar"] = True
        state["escolheu_selar"] = False
        state["escolheu_fugir"] = False

    elif "selar" in texto:
        state["escolheu_derrotar"] = False
        state["escolheu_selar"] = True
        state["escolheu_fugir"] = False

    elif "Abandonar" in texto:
        state["escolheu_derrotar"] = False
        state["escolheu_selar"] = False
        state["escolheu_fugir"] = True

    fase_final()


# ============================================================
# FINAIS
# ============================================================

def fase_final(event=None):
    limpar()
    atualizar_status()

    # FINAL 1
    if (
        state["escolheu_derrotar"]
        and state["monstro_fraqueza"]
        and state["pistas"] >= 10
        and state["batalha"] >= 5
        and state["milo_vivo"]
        and state["barbara_viva"]
    ):

        mostrar_final("final_01.png")

        mostrar("""
        🌟 FINAL 1 — O FINAL PERFEITO

        Depois de tudo que descobriram, vocês finalmente
        entendem como usar os símbolos.

        O símbolo antigo reage ao cristal.

        A criatura perde sua força.

        Milo e Barbara conseguem ajudar vocês durante
        o confronto.

        Depois de anos de mistério, a ameaça finalmente
        chega ao fim.

        Os documentos encontrados revelam a verdade
        sobre o passado da família.

        O segredo da ilha foi descoberto.

        Milo e Barbara continuam vivendo na ilha,
        agora sem precisar temer a criatura.

        A ilha está finalmente livre.

        🏝️ O SEGREDO FOI REVELADO.
        """)

    # FINAL 2
    elif state["escolheu_derrotar"]:

        mostrar_final("final_02.png")

        mostrar("""
        🌅 FINAL 2 — VITÓRIA COM PERDAS

        Vocês decidem enfrentar a criatura.

        A batalha é difícil.

        Mesmo sem possuir todas as pistas necessárias,
        o grupo consegue enfraquecê-la.

        A criatura é derrotada, mas a vitória tem um preço.

        O grupo sai da caverna cansado e abalado.

        Algumas pistas importantes foram destruídas
        durante o confronto.

        Vocês venceram.

        Mas talvez nunca consigam descobrir toda
        a história da ilha.

        A ameaça acabou.

        Porém, algumas perguntas permanecerão
        sem resposta.
        """)

    # FINAL 3
    elif state["escolheu_selar"]:

        mostrar_final("final_03.png")

        mostrar("""
        🔒 FINAL 3 — O SELAMENTO

        Vocês percebem que destruir a criatura pode
        trazer consequências ainda maiores.

        Barbara utiliza os símbolos antigos.

        Milo encontra o mecanismo escondido na caverna.

        O cristal começa a brilhar.

        A passagem para as profundezas começa
        lentamente a se fechar.

        A criatura desaparece novamente.

        O segredo permanece escondido.

        A ilha está segura.

        Mas ninguém sabe por quanto tempo.

        Talvez, no futuro, alguém encontre novamente
        a passagem.

        🔒 A criatura foi selada.
        """)

    # FINAL 6
    elif state["escolheu_fugir"]:

        mostrar_final("final_06.png")

        mostrar("""
        🌊 FINAL 6 — O SEGREDO CONTINUA

        Vocês decidem não enfrentar a criatura.

        Milo e Barbara ajudam vocês a encontrar
        o caminho de volta.

        O barco deixa a ilha.

        Enquanto vocês se afastam, a ilha fica
        cada vez menor no horizonte.

        Os documentos estão com vocês.

        As pistas também.

        Mas muitas perguntas continuam sem resposta.

        O que realmente é a criatura?

        Quem a colocou ali?

        E por que sua família estava envolvida?

        Talvez um dia vocês voltem.

        Por enquanto...

        o segredo continua.

        🏝️ O SEGREDO DA ILHA PERMANECE.
        """)

    mostrar("""
    🎮 FIM DO JOGO

    Obrigado por jogar
    O SEGREDO NA ILHA!
    """)

    criar_botao("🔄 Jogar novamente", reiniciar)


# ============================================================
# REINICIAR
# ============================================================

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

    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    fase1()


# ============================================================
# INICIAR JOGO
# ============================================================

fase1()
