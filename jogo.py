from js import document

tela = document.getElementById("jogo")
botoes = document.getElementById("botoes")
imagem = document.getElementById("imagem-fase")
status = document.getElementById("status")
video_final = document.getElementById("video-final")


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


def limpar():
    tela.innerHTML = ""
    botoes.innerHTML = ""

    video_final.style.display = "none"
    video_final.pause()
    video_final.currentTime = 0


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


# =========================================================
# FASE 1 - ESCOLHA DO PERSONAGEM
# =========================================================

def fase1(event=None):
    preparar(1)

    mostrar("""
    🏝️ O SEGREDO NA ILHA

    Uma viagem misteriosa está prestes a começar.

    Você está prestes a viajar para uma pequena ilha
    cercada pelo mar.

    Há histórias antigas sobre aquele lugar e sobre
    acontecimentos que ninguém consegue explicar.

    Antes de começar a aventura, você precisa escolher
    quem será o personagem principal.

    Quem você quer ser?
    """)

    criar_botao("👩 Amelie", escolher_amelie)
    criar_botao("🧑 Olivier", escolher_olivier)


def escolher_amelie(event):
    state["personagem"] = "Amelie"
    fase2()


def escolher_olivier(event):
    state["personagem"] = "Olivier"
    fase2()


# =========================================================
# FASE 2 - A VIAGEM
# =========================================================

def fase2(event=None):
    preparar(2)

    mostrar("""
    🚢 A VIAGEM

    Você escolheu ser """ + state["personagem"] + """.

    O barco corta as águas enquanto a ilha se aproxima
    lentamente no horizonte.

    O mar está relativamente calmo, mas existe uma
    sensação estranha no ar.

    Durante a viagem, você observa os documentos
    que trouxe consigo.

    Eles contêm informações sobre sua família e sobre
    uma antiga ligação com aquela ilha.

    Quanto mais você lê, mais perguntas aparecem.

    Por que sua família esteve naquela ilha?

    O que aconteceu no passado?

    E por que ninguém fala sobre isso?

    Depois de algumas horas, a ilha finalmente
    aparece completamente diante de você.
    """)

    criar_botao("➡️ Continuar", fase3)


# =========================================================
# FASE 3 - CHEGADA NA ILHA
# =========================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
    🏝️ A CHEGADA NA ILHA

    O barco finalmente chega ao pequeno porto.

    Você desembarca e olha ao redor.

    A ilha parece tranquila, mas existe algo diferente
    naquele lugar.

    Perto do porto estão duas pessoas.

    São Milo e Barbara.

    Eles já moram na ilha há bastante tempo e conhecem
    praticamente todos os caminhos e histórias do lugar.

    Milo se aproxima primeiro.

    — Você deve ser """ + state["personagem"] + """.

    Barbara observa os documentos que você trouxe.

    — Então você veio descobrir o que aconteceu
    com sua família?

    Você percebe que talvez eles saibam mais do que
    estão contando.

    A investigação está apenas começando.
    """)

    criar_botao("➡️ Continuar", fase4)


# =========================================================
# FASE 4 - CONHECENDO A VILA
# =========================================================

def fase4(event=None):
    preparar(4)

    mostrar("""
    🏘️ CONHECENDO A VILA

    Milo e Barbara levam você para conhecer a vila.

    As casas são antigas e muitas parecem ter sido
    construídas há várias décadas.

    Enquanto caminham, Milo explica que a ilha possui
    alguns lugares que quase ninguém visita.

    Barbara aponta para três locais.

    Uma igreja antiga.

    Uma casa abandonada.

    E um velho farol.

    Segundo eles, cada um desses lugares pode guardar
    alguma pista sobre o passado da ilha.

    Por onde você quer começar?
    """)

    criar_botao("⛪ Ir para a igreja", fase5)
    criar_botao("🏚️ Ir para a casa abandonada", fase6)
    criar_botao("🔦 Ir para o farol", fase7)


# =========================================================
# FASE 5 - A IGREJA
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
    ⛪ A IGREJA

    A igreja antiga fica afastada das casas da vila.

    A porta range quando vocês entram.

    Lá dentro existem bancos cobertos de poeira,
    livros antigos e vários símbolos desenhados
    nas paredes.

    Barbara observa os símbolos com atenção.

    — Eu já vi desenhos parecidos antes.

    Milo se aproxima de uma das paredes.

    — Minha família conta histórias sobre esse lugar.

    Você percebe que existem várias coisas que podem
    ser investigadas.

    Talvez os símbolos escondam alguma informação.
    """)

    criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
    criar_botao("📖 Procurar livros antigos", fase5_livros)


def fase5_simbolos(event):
    state["pistas"] += 2
    pegar("fotografia dos simbolos")

    mostrar("""
    🔎 OS SÍMBOLOS

    Você examina cuidadosamente os símbolos.

    Alguns parecem formar uma sequência.

    Barbara percebe que determinados desenhos
    apontam na direção da floresta.

    Você tira uma fotografia para poder estudar
    tudo depois.

    Talvez esses símbolos sejam uma das primeiras
    pistas realmente importantes.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase5_livros(event):
    state["pistas"] += 2
    pegar("livro antigo")

    mostrar("""
    📖 OS LIVROS

    Entre vários livros antigos, você encontra
    um volume muito velho.

    As páginas falam sobre acontecimentos estranhos
    que ocorreram na ilha muitos anos atrás.

    Uma passagem fala sobre algo que vive nas
    profundezas da ilha.

    Você guarda o livro para investigar depois.

    A descoberta deixa todos preocupados.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================================================
# FASE 6 - CASA ABANDONADA
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
    🏚️ A CASA ABANDONADA

    A casa fica em uma parte mais afastada da vila.

    Milo explica que o antigo morador desapareceu
    muitos anos atrás.

    A porta está entreaberta.

    Dentro da casa existem móveis antigos,
    fotografias e caixas espalhadas pelo chão.

    Talvez alguma coisa ali possa explicar
    o que aconteceu.

    Onde você vai procurar?
    """)

    criar_botao("📄 Procurar documentos", fase6_documentos)
    criar_botao("🖼️ Procurar fotografias", fase6_fotos)
    criar_botao("⬇️ Investigar o porão", fase6_porao)


def fase6_documentos(event):
    state["pistas"] += 3
    pegar("documentos da familia")

    mostrar("""
    📄 OS DOCUMENTOS

    Você encontra uma caixa cheia de documentos.

    Entre os papéis aparece o sobrenome da sua família.

    Barbara fica surpresa.

    — Então sua família realmente esteve aqui.

    Alguns documentos falam sobre uma investigação
    que aconteceu muitos anos atrás.

    Agora existe uma ligação clara entre sua família
    e os acontecimentos da ilha.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase6_fotos(event):
    state["pistas"] += 2
    pegar("fotografia antiga")

    mostrar("""
    🖼️ A FOTOGRAFIA

    Entre vários objetos antigos você encontra
    uma fotografia.

    Nela aparecem algumas pessoas diante da floresta.

    Milo olha para a imagem e reconhece o lugar.

    — Eu sei onde essa fotografia foi tirada.

    O passado da ilha parece estar ficando
    cada vez mais próximo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase6_porao(event):
    state["pistas"] += 3
    pegar("fotografia antiga")

    mostrar("""
    ⬇️ O PORÃO

    O porão está completamente escuro.

    Depois de procurar por alguns minutos,
    você encontra uma caixa escondida.

    Dentro existe uma fotografia antiga.

    No verso existe uma mensagem avisando
    que algo nas profundezas da ilha jamais
    deveria ser despertado.

    A mensagem deixa todos em silêncio.

    Talvez as cavernas tenham alguma relação
    com o que está acontecendo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================================================
# FASE 7 - FAROL
# =========================================================

def fase7(event=None):
    preparar(7)

    state["pistas"] += 2
    pegar("fotografia da criatura")

    mostrar("""
    🔦 O FAROL

    O velho farol fica em uma região rochosa
    próxima ao mar.

    Milo conhece o caminho e leva você até o topo.

    Dentro de uma caixa antiga existe uma fotografia.

    Ao fundo da fotografia aparece uma figura estranha
    entre as árvores.

    Barbara observa a imagem atentamente.

    — Isso não parece uma pessoa.

    A descoberta faz você perceber que as histórias
    da ilha talvez sejam verdadeiras.

    Vocês guardam a fotografia e voltam para a vila.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================================================
# FASE 8 - PRIMEIRA NOITE
# =========================================================

def fase8(event=None):
    preparar(8)

    mostrar("""
    🌙 A PRIMEIRA NOITE

    A investigação levou mais tempo do que vocês
    esperavam.

    A noite chega.

    Milo e Barbara levam você para uma casa segura
    na vila.

    Tudo parece tranquilo.

    Até que, durante a madrugada...

    TOC.

    TOC.

    TOC.

    Alguém bate na janela.

    Milo olha para você.

    — Não abra.

    O que você faz?
    """)

    criar_botao("🪟 Abrir a janela", fase8_janela)
    criar_botao("😶 Ignorar as batidas", fase8_ignorar)


def fase8_janela(event):
    perder_sanidade()
    state["pistas"] += 2

    mostrar("""
    🪟 A JANELA

    Você abre a janela.

    Não existe ninguém do lado de fora.

    Porém, no chão existem marcas estranhas.

    Milo se aproxima e observa.

    — Eu já vi marcas assim antes.

    Barbara olha para a floresta.

    — Então ela voltou.

    Ninguém sabe exatamente o que isso significa.

    Mas alguma coisa esteve ali naquela noite.
    """)

    criar_botao("➡️ Continuar", fase9)


def fase8_ignorar(event):
    state["pistas"] += 1

    mostrar("""
    😶 O SILÊNCIO

    Vocês decidem não abrir a janela.

    Depois de alguns minutos,
    as batidas param.

    Quando amanhece, vocês encontram marcas
    estranhas no chão perto da casa.

    Alguma coisa esteve ali durante a noite.

    E agora vocês precisam descobrir o que foi.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase9)


# =========================================================
# FASE 9 - DESAPARECIMENTO
# =========================================================

def fase9(event=None):
    preparar(9)

    mostrar("""
    🚨 O DESAPARECIMENTO

    Na manhã seguinte, a vila acorda com uma notícia.

    Um dos moradores desapareceu.

    Milo conhece a pessoa e fica preocupado.

    Barbara começa a procurar informações.

    As marcas encontradas durante a noite podem
    estar relacionadas ao desaparecimento.

    Vocês precisam descobrir para onde o morador foi.
    """)

    criar_botao("🏘️ Procurar informações na vila", fase9_vila)
    criar_botao("🌲 Procurar diretamente na floresta", fase9_floresta)


def fase9_vila(event):
    state["pistas"] += 1

    mostrar("""
    🏘️ A VILA

    Vocês perguntam aos moradores se alguém viu
    alguma coisa durante a noite.

    Depois de conversar com algumas pessoas,
    vocês descobrem que o desaparecido foi visto
    perto da saída da vila.

    As marcas no chão também seguem naquela direção.

    Milo aponta para a floresta.

    — Devemos procurar lá.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase10)


def fase9_floresta(event):
    state["pistas"] += 2

    mostrar("""
    🌲 A FLORESTA

    Vocês seguem imediatamente para a floresta.

    As marcas no chão parecem recentes.

    Depois de caminhar um pouco, Barbara encontra
    um objeto abandonado.

    Milo reconhece o objeto.

    — Isso pertence ao homem desaparecido.

    A trilha continua pela floresta.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase10)


# =========================================================
# FASE 10 - PROCURANDO PISTAS
# =========================================================

def fase10(event=None):
    preparar(10)

    state["pistas"] += 2
    pegar("objeto do desaparecido")

    mostrar("""
    🔎 PROCURANDO PISTAS

    Vocês continuam seguindo os sinais deixados
    pelo morador desaparecido.

    O caminho fica cada vez mais afastado da vila.

    Entre as árvores, vocês encontram mais pistas.

    Milo reconhece o objeto encontrado.

    — Ele esteve aqui.

    Barbara percebe que as marcas seguem
    para uma região ainda mais afastada.

    A investigação continua.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase11)


# =========================================================
# FASE 11 - TRILHA NA FLORESTA
# =========================================================

def fase11(event=None):
    preparar(11)

    mostrar("""
    🌲 TRILHA NA FLORESTA

    Milo segue na frente porque conhece bem
    os caminhos da ilha.

    A trilha é estreita e cercada por árvores.

    Depois de algum tempo, vocês encontram
    uma pequena passagem entre as árvores.

    Barbara observa o chão.

    Existem marcas recentes.

    A trilha parece levar até uma cabana.

    Vocês continuam.
    """)

    criar_botao("🥾 Seguir pela trilha", fase12)


# =========================================================
# FASE 12 - ACAMPAMENTO
# =========================================================

def fase12(event=None):
    preparar(12)

    mostrar("""
    🔥 ACAMPAMENTO

    A noite chega antes que vocês consigam
    chegar à cabana.

    O grupo decide montar um pequeno acampamento.

    Milo conta histórias antigas que ouviu
    de sua família.

    Barbara fala sobre os símbolos encontrados
    na igreja e sobre as histórias antigas da ilha.

    Aos poucos, todos percebem que as pistas
    parecem estar conectadas.

    No dia seguinte, vocês continuarão a procura.
    """)

    criar_botao("➡️ Continuar", fase13)


# =========================================================
# FASE 13 - PEGADAS GIGANTES
# =========================================================

def fase13(event=None):
    preparar(13)

    state["pistas"] += 2

    mostrar("""
    🐾 PEGADAS GIGANTES

    Quando amanhece, vocês encontram novas pegadas.

    Dessa vez elas são enormes.

    Não parecem pertencer a nenhum animal
    que vocês conheçam.

    Milo se abaixa para examiná-las.

    — São muito maiores do que as marcas
    que encontramos antes.

    Barbara olha para a direção das pegadas.

    Elas levam até uma cabana escondida
    entre as árvores.

    Vocês decidem seguir.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar até a cabana", fase14)


# =========================================================
# FASE 14 - A CABANA
# =========================================================

def fase14(event=None):
    preparar(14)

    state["pistas"] += 3
    pegar("mapas antigos")

    mostrar("""
    🏚️ A CABANA

    A cabana parece abandonada há muitos anos.

    Dentro existem mapas, livros e objetos antigos.

    Barbara encontra um diário escondido.

    Algumas páginas falam sobre uma criatura
    que estaria escondida nas profundezas da ilha.

    Também existem desenhos dos mesmos símbolos
    encontrados na igreja.

    Tudo parece estar conectado.

    O diário pode conter respostas.
    """)

    atualizar_status()
    criar_botao("📖 Ler o diário", fase15)


# =========================================================
# FASE 15 - O DIÁRIO
# =========================================================

def fase15(event=None):
    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3
    pegar("diario")

    mostrar("""
    📖 O DIÁRIO

    O diário conta a história de antigos moradores
    que descobriram uma criatura nas profundezas
    da ilha.

    Eles descobriram que determinados símbolos
    poderiam enfraquecer a criatura.

    O diário também fala sobre um objeto antigo
    que foi escondido para impedir que a criatura
    recuperasse sua força.

    Uma das últimas páginas fala sobre uma família
    que tentou proteger a ilha.

    O sobrenome escrito na página é o mesmo
    da sua família.

    Agora você entende que sua chegada à ilha
    talvez não tenha sido uma coincidência.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase16)


# =========================================================
# FASE 16 - PREPARAÇÃO
# =========================================================

def fase16(event=None):
    preparar(16)

    mostrar("""
    🎒 PREPARAÇÃO

    Agora vocês sabem que existe algo escondido
    nas profundezas da ilha.

    Antes de continuar, o grupo precisa se preparar.

    Milo verifica os equipamentos.

    Barbara organiza todas as pistas encontradas.

    Você revisa os documentos e o diário.

    A próxima etapa será chegar até a região
    onde a criatura está escondida.

    Vocês estão preparados?
    """)

    criar_botao("🎒 Organizar equipamentos", fase16_equipamentos)
    criar_botao("🔱 Preparar o símbolo", fase16_simbolo)


def fase16_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
    🎒 EQUIPAMENTOS

    Vocês organizam tudo o que possuem.

    Milo verifica os equipamentos.

    Barbara guarda as pistas mais importantes.

    Agora o grupo está melhor preparado
    para continuar a investigação.

    O caminho leva até um lago escondido.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase17)


def fase16_simbolo(event):
    pegar("simbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 3

    mostrar("""
    🔱 O SÍMBOLO

    Entre os objetos encontrados,
    vocês conseguem reunir informações
    suficientes para identificar o símbolo antigo.

    Barbara reconhece o desenho.

    — É exatamente o símbolo descrito no diário.

    Milo acredita que ele pode ser usado
    contra a criatura.

    Agora vocês seguem em direção ao lago.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase17)


# =========================================================
# FASE 17 - O LAGO
# =========================================================

def fase17(event=None):
    preparar(17)

    mostrar("""
    🌊 O LAGO

    As pistas levam vocês até um lago escondido.

    A água está completamente parada.

    Perto da margem existe um pequeno cristal
    parcialmente escondido entre as pedras.

    Barbara percebe que o cristal parece reagir
    aos símbolos antigos.

    Talvez ele seja importante.
    """)

    criar_botao("🔎 Pegar o cristal", fase17_cristal)
    criar_botao("➡️ Continuar sem pegar", fase18)


def fase17_cristal(event):
    pegar("cristal")
    state["pistas"] += 2
    state["batalha"] += 2

    mostrar("""
    💎 O CRISTAL

    Você pega o cristal.

    Assim que ele toca sua mão,
    uma luz fraca aparece dentro dele.

    Barbara observa surpresa.

    — Ele está reagindo aos símbolos.

    A descoberta pode ajudar vocês
    no confronto que está por vir.

    Vocês continuam o caminho.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase18)


# =========================================================
# FASE 18 - A CAVERNA
# =========================================================

def fase18(event=None):
    preparar(18)

    mostrar("""
    🕳️ A CAVERNA

    Finalmente vocês chegam até uma enorme caverna.

    Milo reconhece o lugar.

    — Meu avô falava sobre essa caverna.

    Nas paredes existem símbolos antigos.

    Alguns são iguais aos encontrados
    na igreja e no diário.

    O caminho parece descer cada vez mais.

    Vocês entram cuidadosamente.
    """)

    criar_botao("🚪 Entrar na caverna", fase19)


# =========================================================
# FASE 19 - PRIMEIRO ENCONTRO
# =========================================================

def fase19(event=None):
    preparar(19)

    perder_sanidade()

    mostrar("""
    👹 PRIMEIRO ENCONTRO

    Um som estranho ecoa pela caverna.

    O chão começa a tremer.

    No final do corredor aparece uma enorme silhueta.

    Ninguém fala por alguns segundos.

    Barbara reconhece os símbolos nas paredes.

    Milo entende o que está acontecendo.

    — A criatura existe.

    Vocês ainda não sabem como enfrentá-la.

    A única opção é recuar e descobrir
    como derrotá-la.
    """)

    criar_botao("🏃 Fugir da caverna", fase20)


# =========================================================
# FASE 20 - FUGA
# =========================================================

def fase20(event=None):
    preparar(20)

    mostrar("""
    🏃 FUGA

    Vocês correm pelos corredores da caverna.

    Milo usa seu conhecimento da ilha
    para encontrar uma saída.

    Depois de muito esforço, vocês conseguem escapar.

    A criatura continua lá dentro.

    Mas agora vocês sabem que ela existe.

    O diário, os símbolos e o cristal podem revelar
    como enfrentá-la.

    A próxima etapa será descobrir a verdadeira
    fraqueza da criatura.
    """)

    criar_botao("➡️ Continuar", fase21)


# =========================================================
# FASE 21 - DESCOBRINDO A FRAQUEZA
# =========================================================

def fase21(event=None):
    limpar()
    atualizar_status()

    mostrar("""
    🔎 A FRAQUEZA

    Depois de comparar o diário, os símbolos
    e todas as pistas encontradas,

    Barbara finalmente entende a mensagem.

    A criatura pode ser enfraquecida pelo símbolo antigo.

    Milo concorda.

    — Então temos uma chance.

    Vocês decidem voltar para o esconderijo
    e preparar o confronto.

    A decisão final está cada vez mais próxima.
    """)

    state["monstro_fraqueza"] = True
    state["pistas"] += 2
    state["batalha"] += 2

    atualizar_status()

    criar_botao("➡️ Continuar", fase22)


# =========================================================
# FASE 22 - O ESCONDERIJO
# =========================================================

def fase22(event=None):
    limpar()
    atualizar_status()

    mostrar("""
    🏚️ O ESCONDERIJO

    As pistas levam vocês até uma região subterrânea.

    Ali existem inscrições antigas nas paredes.

    Tudo indica que aquele lugar foi usado
    por pessoas que tentaram impedir a criatura
    no passado.

    Vocês encontram uma grande passagem.

    No final dela está o caminho para a criatura.

    Mas antes de continuar,
    vocês encontram alguém.
    """)

    criar_botao("➡️ Continuar", fase23)


# =========================================================
# FASE 23 - O RESGATE
# =========================================================

def fase23(event=None):
    limpar()
    atualizar_status()

    mostrar("""
    🆘 O RESGATE

    No esconderijo vocês encontram o morador
    que havia desaparecido.

    Milo corre para ajudá-lo.

    O homem explica que foi levado para a região
    subterrânea, mas conseguiu escapar.

    Ele conta que a criatura está acordada.

    — Vocês precisam decidir o que fazer.

    Milo olha para você.

    Barbara segura o símbolo.

    A hora da decisão finalmente chegou.
    """)

    criar_botao("➡️ Continuar", fase24)


# =========================================================
# FASE 24 - ESCOLHA DO FINAL
# =========================================================

def fase24(event=None):
    limpar()
    atualizar_status()

    mostrar("""
    ⚔️ A DECISÃO FINAL

    Vocês chegam diante da criatura.

    Depois de toda a investigação,
    finalmente descobriram o segredo da ilha.

    Agora você precisa escolher.

    O que você fará?
    """)

    criar_botao("⚔️ Derrotar o monstro", final_derrotar)
    criar_botao("🔒 Selar o monstro novamente", final_selar)
    criar_botao("🏃 Fugir da ilha", final_fugir)


# =========================================================
# FINAL 1 - PERFEITO
# =========================================================

def final_derrotar(event):
    state["final"] = "derrotar"

    if state["monstro_fraqueza"] and state["batalha"] >= 5:
        state["monstro_derrotado"] = True
    else:
        state["monstro_derrotado"] = False

    fase25()


# =========================================================
# FINAL 3 - SELAMENTO
# =========================================================

def final_selar(event):
    state["final"] = "selar"
    state["monstro_derrotado"] = False

    fase25()


# =========================================================
# FINAL 6 - SEGREDO CONTINUA
# =========================================================

def final_fugir(event):
    state["final"] = "fugir"
    state["monstro_derrotado"] = False

    fase25()


# =========================================================
# FASE 25 - FINAIS
# =========================================================

def fase25(event=None):
    limpar()
    atualizar_status()

    # =====================================================
    # FINAL 1 - PERFEITO
    # =====================================================

    if state["final"] == "derrotar" and state["monstro_derrotado"]:

        mostrar_imagem_final("final_01.png")

        # O VÍDEO APARECE SOMENTE NO FINAL 1
        video_final.style.display = "block"
        video_final.currentTime = 0

        mostrar("""
        🌟 FINAL 1 — PERFEITO

        O símbolo antigo começa a brilhar.

        O cristal reage imediatamente.

        As inscrições das paredes se iluminam
        e a força da criatura começa a desaparecer.

        Você continua usando as pistas encontradas
        durante toda a investigação.

        Milo e Barbara ajudam até o último momento.

        Depois de tantos anos, a criatura finalmente
        é derrotada.

        Os documentos encontrados mostram que
        sua família esteve envolvida na história
        da ilha no passado.

        Agora a verdade pode finalmente ser revelada.

        A ilha está livre.

        Milo e Barbara podem continuar vivendo
        na ilha sem precisar temer a criatura.

        🏝️ O segredo finalmente chegou ao fim.
        """)

    # =====================================================
    # FINAL 2 - VITÓRIA COM PERDAS
    # =====================================================

    elif state["final"] == "derrotar":

        mostrar_imagem_final("final_02.png")

        mostrar("""
        🌅 FINAL 2 — VITÓRIA COM PERDAS

        Você decide enfrentar a criatura.

        A estratégia funciona, mas não perfeitamente.

        O grupo consegue enfraquecê-la e impedir
        que ela continue avançando.

        Porém, nem tudo acontece como planejado.

        Algumas pistas são destruídas durante
        o confronto.

        O esconderijo começa a desmoronar
        e vocês precisam sair rapidamente.

        Milo e Barbara ajudam o grupo a escapar.

        Vocês conseguiram vencer a ameaça,
        mas muitas respostas ficaram para trás.

        A ilha está mais segura.

        Porém, o passado ainda guarda alguns mistérios.

        🏝️ Vocês venceram, mas tiveram perdas.
        """)

    # =====================================================
    # FINAL 3 - SELAMENTO
    # =====================================================

    elif state["final"] == "selar":

        mostrar_imagem_final("final_03.png")

        mostrar("""
        🔒 FINAL 3 — O SELAMENTO

        Você decide não destruir a criatura.

        Barbara usa os símbolos antigos
        para iniciar o selamento.

        Milo ajuda a manter todos em segurança.

        O cristal reage aos símbolos.

        A passagem começa a se fechar.

        A criatura desaparece novamente
        nas profundezas da ilha.

        O grupo consegue escapar.

        A ilha está segura novamente.

        Mas a criatura não foi destruída.

        Ela continua existindo em algum lugar
        abaixo da ilha.

        Talvez um dia alguém precise enfrentar
        esse problema novamente.

        🔒 O segredo continua guardado.
        """)

    # =====================================================
    # FINAL 6 - SEGREDO CONTINUA
    # =====================================================

    elif state["final"] == "fugir":

        mostrar_imagem_final("final_06.png")

        mostrar("""
        🏃 FINAL 6 — O SEGREDO CONTINUA

        Você decide abandonar a ilha.

        Milo conhece o caminho de volta
        e ajuda todos a chegar ao barco.

        Barbara leva algumas das pistas encontradas.

        Você leva os documentos relacionados
        à sua família.

        O barco se afasta lentamente da ilha.

        Pela última vez, você olha para trás.

        A ilha fica cada vez menor no horizonte.

        Vocês sobreviveram.

        Mas a criatura continua lá.

        O mistério não foi resolvido.

        Milo e Barbara permanecem na ilha,
        porque aquele lugar é a casa deles.

        Talvez algum dia alguém volte
        para descobrir toda a verdade.

        🏝️ O segredo da ilha continua.
        """)

    mostrar("""
    🎮 FIM DO JOGO

    Obrigado por jogar
    O Segredo na Ilha!

    A aventura terminou.
    """)

    criar_botao("🔄 Jogar novamente", reiniciar)


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
