from js import document

tela = document.getElementById("jogo")
botoes = document.getElementById("botoes")
imagem = document.getElementById("imagem-fase")
status = document.getElementById("status")


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

    "escolheu_derrotar": False,
    "escolheu_selar": False,
    "escolheu_fugir": False,

    "batalha": 0
}


# =========================
# FUNÇÕES BÁSICAS
# =========================

def limpar():
    tela.innerHTML = ""
    botoes.innerHTML = ""


def mostrar(texto):
    div = document.createElement("div")
    div.className = "texto-jogo"
    div.innerText = str(texto)
    tela.appendChild(div)


def atualizar_status():
    status.innerHTML = (
        "❤️ Vida: " + str(state["vida"]) +
        " | 🧠 Sanidade: " + str(state["sanidade"]) +
        " | 🔎 Pistas: " + str(state["pistas"]) +
        " | 🎒 Itens: " + str(len(state["inv"]))
    )


def mostrar_imagem_fase(numero):
    if numero >= 1 and numero <= 20:
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
    mostrar_imagem_fase(numero)


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


# =========================
# FASE 1
# ESCOLHA DO PERSONAGEM
# =========================

def fase1(event=None):
    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Tudo começa antes da chegada à ilha.

Olivier e Amelie estão viajando juntos de barco
em direção a uma pequena ilha.

Eles decidiram fazer essa viagem depois de encontrar
documentos antigos relacionados à família.

Os documentos mencionavam acontecimentos estranhos
e o desaparecimento de uma pessoa muitos anos atrás.

Enquanto o barco se aproxima da ilha, os dois
observam o horizonte.

A viagem está apenas começando.

Agora você precisa escolher quem será o personagem
principal da história.

Você será Olivier ou Amelie?
""")

    criar_botao("🧑 Ser Olivier", escolher_olivier)
    criar_botao("👩 Ser Amelie", escolher_amelie)


def escolher_olivier(event):
    state["personagem"] = "Olivier"
    fase2()


def escolher_amelie(event):
    state["personagem"] = "Amelie"
    fase2()


# =========================
# FASE 2
# A VIAGEM
# =========================

def fase2(event=None):
    preparar(2)

    mostrar("""
🚢 A VIAGEM

O barco continua avançando pelo mar.

Olivier e Amelie permanecem no convés enquanto
a ilha começa a aparecer no horizonte.

A viagem parece tranquila, mas os documentos
encontrados antes da partida deixam os dois
com muitas perguntas.

Por que a família esteve naquela ilha?

O que aconteceu com a pessoa desaparecida?

E por que alguns registros falavam sobre
lugares que não aparecem nos mapas?

O barco continua se aproximando.

Em pouco tempo, vocês finalmente chegarão.
""")

    criar_botao("🏝️ Continuar viagem", fase3)


# =========================
# FASE 3
# CHEGADA À ILHA
# =========================

def fase3(event=None):
    preparar(3)

    mostrar("""
🏝️ CHEGADA À ILHA

Depois de horas de viagem, o barco finalmente
chega ao pequeno porto da ilha.

Olivier e Amelie desembarcam.

A ilha parece tranquila à primeira vista.

Perto do porto, duas pessoas aguardam a chegada.

São Milo e Barbara.

Os dois já moram na ilha há muito tempo
e conhecem muito bem a região.

Milo se aproxima para receber os visitantes.

Barbara observa os documentos que vocês trouxeram.

Talvez eles possam ajudar a descobrir
o que aconteceu no passado.

A investigação começa agora.
""")

    criar_botao("👋 Conversar com Milo", fase4_milo)
    criar_botao("👋 Conversar com Barbara", fase4_barbara)


# =========================
# FASE 4
# CONHECENDO A VILA
# =========================

def fase4_milo(event):
    state["confianca_milo"] += 1
    state["pistas"] += 1
    fase4()


def fase4_barbara(event):
    state["confianca_barbara"] += 1
    state["pistas"] += 1
    fase4()


def fase4(event=None):
    preparar(4)

    mostrar("""
🏘️ CONHECENDO A VILA

Milo e Barbara acompanham Olivier e Amelie
durante uma caminhada pela vila.

Eles explicam que vivem naquela ilha há muitos anos.

Milo conhece as trilhas e os lugares mais afastados.

Barbara conhece as histórias antigas que foram
passadas de geração em geração.

Enquanto caminham, vocês percebem que existem
três lugares que podem ter alguma relação
com os documentos da família.

Uma igreja antiga.

Uma casa abandonada.

E um velho farol.

Cada lugar pode esconder uma pista.

Onde vocês querem começar?
""")

    criar_botao("⛪ Ir para a igreja", fase5)
    criar_botao("🏚️ Ir para a casa abandonada", fase6)
    criar_botao("🔦 Ir para o farol", fase7)


# =========================
# FASE 5
# A IGREJA
# =========================

def fase5(event=None):
    preparar(5)

    mostrar("""
⛪ A IGREJA

A antiga igreja está praticamente abandonada.

Milo explica que poucas pessoas entram ali atualmente.

Nas paredes existem símbolos muito antigos.

Barbara reconhece alguns deles.

Ela conta que sua família já ouviu histórias
sobre aqueles desenhos.

Talvez eles tenham alguma relação com
o mistério da ilha.

O que vocês procuram?
""")

    criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
    criar_botao("📖 Procurar documentos", fase5_documentos)


def fase5_simbolos(event):
    state["pistas"] += 2
    pegar("fotografia dos símbolos")

    mostrar("""
🔎 OS SÍMBOLOS

Vocês examinam cuidadosamente os símbolos
nas paredes da igreja.

Alguns deles parecem formar uma sequência.

Barbara percebe que determinados desenhos
apontam para a região da floresta.

Você registra os símbolos para poder estudá-los depois.

Talvez essa seja uma das primeiras pistas
realmente importantes.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase5_documentos(event):
    state["pistas"] += 3
    pegar("livro antigo")

    mostrar("""
📖 DOCUMENTOS ANTIGOS

Atrás de um banco antigo vocês encontram
um livro bastante velho.

As páginas falam sobre uma criatura
que estaria escondida nas profundezas da ilha.

Uma anotação menciona um símbolo capaz
de enfraquecê-la.

Vocês guardam o livro.

Essa descoberta pode ser importante no futuro.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================
# FASE 6
# CASA ABANDONADA
# =========================

def fase6(event=None):
    preparar(6)

    mostrar("""
🏚️ A CASA ABANDONADA

Milo leva vocês até uma antiga casa
que está abandonada há muitos anos.

Segundo ele, o antigo morador desapareceu
sem deixar muitas explicações.

Dentro da casa existem móveis antigos,
papéis e objetos esquecidos.

O lugar parece guardar parte da história
da ilha.

Onde vocês vão procurar?
""")

    criar_botao("📄 Procurar documentos", fase6_documentos)
    criar_botao("⬆️ Subir as escadas", fase6_escadas)
    criar_botao("⬇️ Investigar o porão", fase6_porao)


def fase6_documentos(event):
    state["pistas"] += 3
    pegar("documentos da família")

    mostrar("""
📄 OS DOCUMENTOS

Entre vários papéis antigos vocês encontram
o sobrenome da família.

Barbara fica surpresa.

A família de Olivier e Amelie realmente
esteve naquela ilha no passado.

Agora existe uma ligação muito mais clara
entre os documentos e o mistério.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase6_escadas(event):
    state["pistas"] += 2
    pegar("fotografia antiga")

    mostrar("""
📷 A FOTOGRAFIA

No andar de cima vocês encontram uma fotografia.

Ela mostra algumas pessoas diante da floresta.

Uma delas parece ser o parente desaparecido.

Milo observa a imagem por alguns segundos.

Ele reconhece o local.

A fotografia pode indicar o próximo lugar
que vocês devem investigar.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def fase6_porao(event):
    state["pistas"] += 3
    pegar("fotografia antiga")

    mostrar("""
⬇️ O PORÃO

No porão existe uma caixa escondida.

Dentro dela vocês encontram uma fotografia antiga.

No verso existe uma mensagem alertando
sobre algo que estaria escondido abaixo da ilha.

A descoberta deixa todos preocupados.

Talvez o segredo esteja ligado às cavernas.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================
# FASE 7
# FAROL
# =========================

def fase7(event=None):
    preparar(7)

    state["pistas"] += 3
    pegar("fotografia da criatura")

    mostrar("""
🔦 O FAROL

O velho farol fica em uma região mais afastada
da vila.

Milo conhece o caminho e acompanha vocês.

No topo do farol existe uma caixa antiga.

Dentro dela há uma fotografia.

Ao fundo aparece uma figura estranha.

Barbara observa a fotografia com atenção.

As histórias antigas da ilha talvez não sejam
apenas histórias.

Alguma coisa realmente pode estar escondida
naquele lugar.
""")

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================
# FASE 8
# PRIMEIRA NOITE
# =========================

def fase8(event=None):
    preparar(8)

    mostrar("""
🌙 A PRIMEIRA NOITE

Depois de passar o dia investigando,
a noite finalmente chega.

Milo e Barbara levam vocês para uma casa segura
na vila.

Durante a madrugada, vocês escutam três batidas
na janela.

TOC.

TOC.

TOC.

Milo pede para ninguém abrir.

O som continua por alguns segundos.

O que vocês fazem?
""")

    criar_botao("🪟 Abrir a janela", fase8_janela)
    criar_botao("😶 Ignorar as batidas", fase8_ignorar)


def fase8_janela(event):
    perder_sanidade()
    state["pistas"] += 2

    mostrar("""
🪟 A JANELA

Você abre a janela.

Não há ninguém do lado de fora.

Mas existem marcas profundas no chão.

Milo observa as marcas e fica sério.

Ele já viu sinais parecidos antes.

Barbara olha para a floresta.

Alguma coisa passou por ali durante a noite.
""")

    criar_botao("🌅 Continuar", fase9)


def fase8_ignorar(event):
    state["pistas"] += 1

    mostrar("""
😶 AS BATIDAS

Vocês decidem não abrir a janela.

Quando amanhece, encontram marcas no chão
perto da casa.

Alguma coisa esteve ali durante a noite.

Agora vocês precisam descobrir o que aconteceu.
""")

    criar_botao("🌅 Continuar", fase9)


# =========================
# FASE 9
# DESAPARECIMENTO
# =========================

def fase9(event=None):
    preparar(9)

    mostrar("""
🚨 O DESAPARECIMENTO

Na manhã seguinte, um morador da ilha desaparece.

Milo conhece a pessoa e fica preocupado.

Barbara começa a procurar informações
entre os moradores.

As marcas encontradas durante a noite
podem estar relacionadas ao desaparecimento.

Vocês precisam descobrir para onde ele foi.
""")

    criar_botao("🏘️ Procurar na vila", fase9_vila)
    criar_botao("🌲 Procurar na floresta", fase9_floresta)


def fase9_vila(event):
    state["pistas"] += 1

    mostrar("""
🏘️ PROCURANDO NA VILA

Vocês procuram informações pela vila.

Depois de algum tempo encontram marcas
que seguem para fora das casas.

Milo observa o caminho.

As marcas seguem em direção à floresta.

Vocês decidem continuar por lá.
""")

    criar_botao("🔎 Continuar", fase10)


def fase9_floresta(event):
    state["pistas"] += 2

    mostrar("""
🌲 PROCURANDO NA FLORESTA

Vocês seguem as marcas pela floresta.

Elas parecem recentes.

Barbara encontra um objeto no caminho.

Milo reconhece imediatamente.

O objeto provavelmente pertence
ao morador desaparecido.
""")

    criar_botao("🔎 Continuar", fase10)


# =========================
# FASE 10
# PROCURANDO PISTAS
# =========================

def fase10(event=None):
    preparar(10)

    pegar("objeto do desaparecido")
    state["pistas"] += 2

    mostrar("""
🔎 PROCURANDO PISTAS

A investigação continua.

Vocês encontram um objeto pertencente
ao morador desaparecido.

Milo confirma que o objeto é dele.

A trilha continua pela floresta.

Quanto mais vocês avançam,
mais distante a vila fica.

Parece que estão chegando a uma região
que quase ninguém visita.
""")

    atualizar_status()
    criar_botao("🌲 Seguir a trilha", fase11)


# =========================
# FASE 11
# TRILHA NA FLORESTA
# =========================

def fase11(event=None):
    preparar(11)

    mostrar("""
🌲 TRILHA NA FLORESTA

Milo assume a liderança.

Como mora na ilha há muitos anos,
ele conhece caminhos que não aparecem
nos mapas.

A trilha fica cada vez mais fechada.

Entre as árvores vocês encontram sinais
de que alguém passou por ali recentemente.

Depois de algum tempo aparece uma pequena
cabana escondida.

Talvez ela contenha mais respostas.
""")

    criar_botao("🥾 Continuar pela trilha", fase12)


# =========================
# FASE 12
# ACAMPAMENTO
# =========================

def fase12(event=None):
    preparar(12)

    mostrar("""
🔥 ACAMPAMENTO

A noite chega antes que vocês consigam
voltar para a vila.

O grupo decide montar um pequeno acampamento.

Milo conta histórias que ouviu de seu avô
sobre a parte mais antiga da ilha.

Barbara explica que os símbolos encontrados
podem estar ligados à criatura mencionada
nos documentos.

Todos percebem que estão cada vez mais
perto da verdade.

Mas ainda existem muitas perguntas.
""")

    criar_botao("🌅 Continuar pela manhã", fase13)


# =========================
# FASE 13
# PEGADAS GIGANTES
# =========================

def fase13(event=None):
    preparar(13)

    state["pistas"] += 2

    mostrar("""
🐾 PEGADAS GIGANTES

Quando amanhece, novas pegadas aparecem
próximas ao acampamento.

Elas são muito maiores do que pegadas humanas.

Milo se abaixa para examiná-las.

Ele percebe que elas seguem em direção
a uma área ainda mais afastada.

Entre as árvores existe uma pequena cabana.

Talvez seja o lugar que vocês estavam procurando.
""")

    atualizar_status()
    criar_botao("🏚️ Ir até a cabana", fase14)


# =========================
# FASE 14
# A CABANA
# =========================

def fase14(event=None):
    preparar(14)

    pegar("diário")
    state["pistas"] += 3

    mostrar("""
🏚️ A CABANA

Dentro da cabana vocês encontram mapas,
livros antigos e vários objetos.

Barbara encontra um diário escondido.

As anotações parecem ter sido feitas
por alguém que investigava a criatura.

O diário pode revelar o que aconteceu
com o antigo morador da ilha.

Vocês decidem ler as anotações.
""")

    atualizar_status()
    criar_botao("📖 Ler o diário", fase15)


# =========================
# FASE 15
# O DIÁRIO
# =========================

def fase15(event=None):
    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
📖 O DIÁRIO

O diário revela uma história assustadora.

Anos atrás, alguns moradores descobriram
uma criatura escondida nas profundezas da ilha.

Eles descobriram que existia um símbolo antigo
capaz de enfraquecê-la.

O símbolo acabou sendo escondido.

A última parte do diário menciona
a família de Olivier e Amelie.

Talvez alguém da família tenha tentado
proteger a ilha no passado.

Agora vocês sabem que precisam encontrar
o símbolo.
""")

    atualizar_status()
    criar_botao("🎒 Preparar equipamentos", fase16)


# =========================
# FASE 16
# PREPARAÇÃO
# =========================

def fase16(event=None):
    preparar(16)

    mostrar("""
🎒 PREPARAÇÃO

Agora vocês sabem que existe uma criatura
e também conhecem uma possível fraqueza.

Antes de continuar, o grupo organiza
tudo o que encontrou.

Milo verifica os equipamentos.

Barbara revisa as pistas.

Vocês precisam decidir como se preparar
para continuar a investigação.
""")

    criar_botao("🎒 Organizar equipamentos", fase16_equipamentos)
    criar_botao("🔱 Preparar o símbolo", fase16_simbolo)


def fase16_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam os equipamentos.

Milo verifica se tudo está pronto.

Barbara guarda as pistas mais importantes.

O grupo está mais preparado para continuar.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase17)


def fase16_simbolo(event):
    pegar("símbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 3

    mostrar("""
🔱 O SÍMBOLO

Entre os objetos antigos vocês encontram
o símbolo descrito no diário.

Barbara reconhece imediatamente o desenho.

Milo percebe que aquilo pode ser a chave
para enfrentar a criatura.

Agora vocês têm uma vantagem importante.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase17)


# =========================
# FASE 17
# O LAGO
# =========================

def fase17(event=None):
    preparar(17)

    mostrar("""
🌊 O LAGO

As pistas levam vocês até um lago escondido.

A água está completamente parada.

Perto da margem existe um pequeno cristal.

Barbara percebe que ele reage aos símbolos
encontrados durante a investigação.

Talvez o cristal tenha alguma ligação
com a criatura.
""")

    criar_botao("🔎 Pegar o cristal", fase17_cristal)
    criar_botao("➡️ Continuar sem pegar", fase18)


def fase17_cristal(event):
    pegar("cristal")
    state["pistas"] += 2

    mostrar("""
💎 O CRISTAL

Você pega o cristal.

Ele reage imediatamente ao símbolo antigo.

Uma pequena luz aparece por alguns segundos.

Barbara acredita que o cristal pode ajudar
a enfraquecer a criatura.

Vocês guardam o objeto e continuam.
""")

    atualizar_status()
    criar_botao("🕳️ Continuar", fase18)


# =========================
# FASE 18
# A CAVERNA
# =========================

def fase18(event=None):
    preparar(18)

    mostrar("""
🕳️ A CAVERNA

O caminho termina diante de uma enorme caverna.

Milo reconhece o lugar.

Seu avô costumava falar sobre aquela região.

Nas paredes existem os mesmos símbolos
encontrados na igreja.

Tudo parece estar conectado.

Vocês entram na caverna.

O segredo da ilha pode estar muito próximo.
""")

    criar_botao("🚪 Entrar na caverna", fase19)


# =========================
# FASE 19
# PRIMEIRO ENCONTRO
# =========================

def fase19(event=None):
    preparar(19)

    perder_sanidade()

    mostrar("""
👹 PRIMEIRO ENCONTRO

Um som estranho ecoa pela caverna.

O grupo para imediatamente.

Uma enorme silhueta aparece
no final do corredor.

Barbara reconhece os símbolos
nas paredes.

Milo finalmente entende
o que aquelas histórias significavam.

A criatura realmente existe.

Vocês ainda não estão preparados
para enfrentá-la.

A única opção é fugir e descobrir
como derrotá-la.
""")

    criar_botao("🏃 Fugir da caverna", fase20)


# =========================
# FASE 20
# FUGA
# =========================

def fase20(event=None):
    preparar(20)

    mostrar("""
🏃 FUGA

O grupo corre pelos corredores da caverna.

Milo usa seu conhecimento da região
para encontrar uma saída.

Depois de muito esforço,
vocês conseguem escapar.

Agora sabem que a criatura existe.

Mas ainda precisam descobrir
como enfrentá-la.

A investigação ainda não terminou.

O verdadeiro confronto está chegando.
""")

    criar_botao("🔎 Descobrir a fraqueza", fase21)


# =========================
# FASE 21
# DESCOBRINDO A FRAQUEZA
# =========================

def fase21(event=None):
    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    limpar()
    atualizar_status()

    mostrar("""
🔎 A FRAQUEZA

Depois de comparar o diário,
os símbolos e o cristal,
Barbara finalmente entende a mensagem.

A criatura pode ser enfraquecida.

O símbolo antigo é a chave.

Milo respira fundo.

— Então podemos tentar.

Agora vocês precisam voltar
para o esconderijo da criatura.
""")

    criar_botao("🏚️ Ir para o esconderijo", fase22)


# =========================
# FASE 22
# ESCONDERIJO
# =========================

def fase22(event=None):
    limpar()
    atualizar_status()

    mostrar("""
🏚️ O ESCONDERIJO

As pistas levam vocês até uma região
subterrânea escondida.

Existem documentos e inscrições antigas
nas paredes.

Tudo indica que aquele lugar foi usado
para esconder informações sobre a criatura.

No final do corredor existe uma enorme
porta de pedra.

O segredo está atrás dela.
""")

    criar_botao("🚪 Abrir a porta", fase23)


# =========================
# FASE 23
# RESGATE
# =========================

def fase23(event=None):
    limpar()
    atualizar_status()

    mostrar("""
🆘 O RESGATE

Antes de chegar à sala principal,
vocês encontram o morador desaparecido.

Milo corre para ajudá-lo.

O homem conta que foi levado para aquela região.

Ele conseguiu escapar e encontrou
o esconderijo por acaso.

Antes de sair, ele avisa:

— Ela está acordada.

Vocês precisam continuar.
""")

    criar_botao("🚶 Continuar com cuidado", fase24)


# =========================
# FASE 24
# ENTRADA DO ESCONDERIJO
# =========================

def fase24(event=None):
    limpar()
    atualizar_status()

    state["pistas"] += 1

    mostrar("""
🚪 A ENTRADA

Milo ajuda o homem a sair.

Barbara encontra uma passagem segura.

Depois disso, vocês voltam para a entrada
principal do esconderijo.

Uma enorme porta de pedra bloqueia o caminho.

No centro existe um símbolo.

Se vocês tiverem encontrado o símbolo antigo,
talvez consigam abrir a porta.
""")

    if "símbolo antigo" in state["inv"]:
        mostrar("""
🔱 O SÍMBOLO

O símbolo se encaixa perfeitamente na porta.

As inscrições começam a brilhar.

A porta lentamente se abre.

Uma passagem escura aparece.

Vocês estão muito perto do segredo.
""")
    else:
        mostrar("""
⚠️ UMA PASSAGEM ALTERNATIVA

Vocês não possuem o símbolo original.

Mesmo assim, Barbara encontra
uma pequena passagem lateral.

O grupo decide continuar por ela.
""")

    criar_botao("🚪 Entrar", fase25)


# =========================
# FASE 25
# O PASSADO
# =========================

def fase25(event=None):
    limpar()
    atualizar_status()

    state["pistas"] += 3

    mostrar("""
📜 O PASSADO

Dentro do esconderijo vocês encontram
documentos muito antigos.

Eles confirmam que o parente de Olivier
ou Amelie esteve na ilha.

Ele descobriu a existência da criatura
e tentou impedir que ela voltasse
a ameaçar os moradores.

Uma anotação chama a atenção de vocês:

A família deveria terminar
o que havia começado.

Agora vocês entendem por que
os documentos foram escondidos.

A história da família está ligada
ao segredo da ilha.
""")

    criar_botao("⚔️ Continuar", fase26)


# =========================
# FASE 26
# PREPARAÇÃO FINAL
# =========================

def fase26(event=None):
    limpar()
    atualizar_status()

    mostrar("""
⚔️ PREPARAÇÃO FINAL

A criatura está próxima.

Milo e Barbara estão prontos para ajudar.

O símbolo antigo pode ser usado
para enfraquecê-la.

O grupo se prepara para o confronto final.

Agora não há mais como voltar atrás.
""")

    criar_botao("🔱 Preparar o símbolo", fase26_simbolo)
    criar_botao("🎒 Organizar equipamentos", fase26_equipamentos)


def fase26_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["batalha"] += 3
        state["monstro_fraqueza"] = True

        mostrar("""
🔱 O SÍMBOLO REAGE

O símbolo começa a brilhar.

O cristal também reage.

Barbara percebe que a criatura
está sendo afetada.

Vocês estão preparados para o confronto.
""")
    else:
        mostrar("""
⚠️ SEM O SÍMBOLO

Vocês procuram pelo símbolo,
mas não o possuem.

Mesmo assim precisam continuar.

A criatura está esperando.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase27)


def fase26_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam tudo o que possuem.

Milo verifica os equipamentos.

Barbara guarda as pistas.

O grupo está pronto.

Agora só falta enfrentar a criatura.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase27)


# =========================
# FASE 27
# O MONSTRO
# =========================

def fase27(event=None):
    limpar()
    atualizar_status()

    mostrar("""
👹 O MONSTRO

O grupo chega à última sala.

A criatura está diante de vocês.

Os símbolos cobrem as paredes.

Milo reconhece aquele lugar.

— É aqui que tudo começou.

Barbara segura o símbolo.

Agora chegou a hora de enfrentar
a criatura e decidir o destino da ilha.
""")

    criar_botao("⚔️ Preparar o confronto", fase28)


# =========================
# FASE 28
# O CONFRONTO
# =========================

def fase28(event=None):
    limpar()
    atualizar_status()

    mostrar("""
⚔️ O CONFRONTO

A criatura avança.

O símbolo pode ser usado
para enfraquecê-la.

Milo e Barbara ajudam vocês.

Cada decisão pode mudar
o resultado do confronto.

Escolha uma estratégia.
""")

    criar_botao("🔱 Ativar o símbolo", fase28_simbolo)
    criar_botao("🛡️ Ajudar Milo", fase28_milo)
    criar_botao("🛡️ Ajudar Barbara", fase28_barbara)
    criar_botao("🏃 Recuar", fase28_recuar)


def fase28_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["batalha"] += 4
        state["monstro_fraqueza"] = True

        mostrar("""
🔱 O SÍMBOLO É ATIVADO

Você ativa o símbolo antigo.

As paredes começam a brilhar.

A criatura perde força.

Milo grita para continuar.

A estratégia está funcionando.
""")
    else:
        perder_sanidade()

        mostrar("""
⚠️ O SÍMBOLO NÃO ESTÁ COM VOCÊ

Você tenta ativar o símbolo,
mas percebe que não o possui.

A criatura continua avançando.

O grupo precisa continuar.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_milo(event):
    state["confianca_milo"] += 2
    state["batalha"] += 2

    mostrar("""
🛡️ AJUDANDO MILO

Você ajuda Milo a observar
as inscrições da parede.

Ele reconhece uma marca antiga.

A descoberta ajuda o grupo
a entender melhor a criatura.

Agora vocês têm uma chance maior
de vencer.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_barbara(event):
    state["confianca_barbara"] += 2
    state["batalha"] += 2

    mostrar("""
🛡️ AJUDANDO BARBARA

Você ajuda Barbara a procurar
uma inscrição escondida.

Ela encontra uma informação
que confirma a fraqueza da criatura.

Agora o grupo sabe como agir.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_recuar(event):
    perder_vida()

    mostrar("""
🏃 RECUAR

Vocês recuam por alguns instantes.

A criatura avança.

Milo e Barbara ajudam o grupo
a se reorganizar.

Agora não existe mais tempo
para continuar recuando.

É hora de decidir.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


# =========================
# FASE 29
# ÚLTIMA ESCOLHA
# =========================

def fase29(event=None):
    limpar()
    atualizar_status()

    mostrar("""
🔥 A ÚLTIMA ESCOLHA

Depois de toda a investigação,
vocês finalmente descobriram
o segredo da ilha.

A criatura está diante de vocês.

Agora você precisa tomar
a decisão final.

O que você fará?
""")

    criar_botao("⚔️ Derrotar o monstro", final_derrotar)
    criar_botao("🔒 Selar o monstro novamente", final_selar)
    criar_botao("🏃 Fugir da ilha", final_fugir)


# =========================
# FINAIS
# =========================

def final_derrotar(event):
    state["escolheu_derrotar"] = True
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    if state["monstro_fraqueza"] and state["batalha"] >= 5:
        state["monstro_derrotado"] = True
    else:
        state["monstro_derrotado"] = False

    fase30()


def final_selar(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = True
    state["escolheu_fugir"] = False
    state["monstro_derrotado"] = False

    fase30()


def final_fugir(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = True
    state["monstro_derrotado"] = False

    fase30()


# =========================
# FASE 30
# FINAIS
# =========================

def fase30(event=None):
    limpar()
    atualizar_status()

    # FINAL 1 - PERFEITO
    if state["escolheu_derrotar"] and state["monstro_derrotado"]:

        mostrar_imagem_final("final_01.png")

        mostrar("""
🌟 FINAL 1 — FINAL PERFEITO

O símbolo antigo começa a brilhar.

As inscrições da sala se iluminam.

A criatura perde completamente sua força.

Milo e Barbara permanecem ao lado de vocês.

Depois de tantos anos, o segredo da ilha
finalmente chega ao fim.

Os documentos encontrados confirmam
a ligação da família com a ilha.

A verdade finalmente foi descoberta.

🏝️ A ilha está livre da criatura.

Olivier e Amelie conseguem voltar para casa
sabendo exatamente o que aconteceu.

Milo e Barbara continuam na ilha,
agora sem precisar temer a criatura.

O mistério finalmente terminou.
""")

    # FINAL 2 - VITÓRIA COM PERDAS
    elif state["escolheu_derrotar"]:

        mostrar_imagem_final("final_02.png")

        mostrar("""
🌅 FINAL 2 — VITÓRIA COM PERDAS

Vocês decidem enfrentar a criatura.

A estratégia funciona parcialmente.

Depois de uma longa luta,
a criatura finalmente é derrotada.

Mas a vitória teve um preço.

Nem tudo saiu como vocês esperavam.

O grupo consegue sobreviver,
mas algumas coisas foram perdidas durante
o confronto.

Milo e Barbara ajudam vocês a sair
do esconderijo.

A ilha está livre da criatura.

Porém, a lembrança de tudo que aconteceu
ficará para sempre com vocês.

Vocês venceram.

Mas foi uma vitória com perdas.
""")

    # FINAL 3 - SELAMENTO
    elif state["escolheu_selar"]:

        mostrar_imagem_final("final_03.png")

        mostrar("""
🔒 FINAL 3 — SELAMENTO

Vocês decidem não destruir a criatura.

Barbara ativa os símbolos antigos.

Milo ajuda a manter todos em segurança.

A passagem começa lentamente a se fechar.

A criatura desaparece novamente
nas profundezas da ilha.

O segredo continua escondido.

A ilha está segura.

Mas a criatura não foi destruída.

Ela apenas foi selada novamente.

Talvez um dia alguém encontre
aquele lugar outra vez.

Por enquanto, porém,
o segredo permanece protegido.
""")

    # FINAL 6 - SEGREDO CONTINUA
    elif state["escolheu_fugir"]:

        mostrar_imagem_final("final_06.png")

        mostrar("""
🏃 FINAL 6 — O SEGREDO CONTINUA

Vocês decidem abandonar a ilha.

Milo conhece o caminho de volta.

Barbara ajuda o grupo a chegar
até o barco.

Olivier ou Amelie leva consigo
os documentos encontrados.

A ilha começa a ficar para trás.

Milo e Barbara permanecem na ilha,
porque aquele lugar é a casa deles.

Vocês sobreviveram.

Mas nunca descobriram toda a verdade.

A criatura continua escondida.

O segredo da ilha continua.

Talvez um dia alguém volte
para descobrir o que realmente aconteceu.
""")

    mostrar("""
🎮 FIM DO JOGO

Obrigado por jogar
O SEGREDO NA ILHA! 🏝️

Será que você conseguiu descobrir
todos os finais?
""")

    criar_botao("🔄 Jogar novamente", reiniciar)


# =========================
# REINICIAR
# =========================

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

    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    state["batalha"] = 0

    fase1()


# =========================
# COMEÇAR O JOGO
# =========================

fase1()
