# ============================================================
# 🏝️ O SEGREDO NA ILHA
# RPG DE ESCOLHAS - 30 FASES
# VERSÃO PYSCRIPT PARA GITHUB PAGES
# ============================================================

from js import document
from pyodide.ffi import create_proxy
import asyncio


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
# ELEMENTOS DA PÁGINA
# ============================================================

area = document.getElementById("jogo")
botoes = document.getElementById("botoes")
status = document.getElementById("status")

def mudar_imagem(nome):
    imagem = document.getElementById("imagem-fase")
    imagem.src = nome
    imagem.style.display = "block"

# ============================================================
# MOSTRAR TEXTO
# ============================================================

def mostrar(texto):
    bloco = document.createElement("pre")

    bloco.textContent = str(texto)

    bloco.className = "texto-jogo"

    area.appendChild(bloco)

    area.scrollTop = area.scrollHeight


# ============================================================
# LIMPAR BOTÕES
# ============================================================

def limpar_botoes():
    botoes.innerHTML = ""


# ============================================================
# ATUALIZAR STATUS
# ============================================================

def atualizar_status():

    status.textContent = (
        f"❤️ Vida: {state['vida']}    "
        f"🧠 Sanidade: {state['sanidade']}    "
        f"🔎 Pistas: {state['pistas']}    "
        f"🎒 Itens: {len(state['inv'])}"
    )


# ============================================================
# ESCOLHER
# ============================================================

async def escolher(pergunta, opcoes):

    mostrar("\n" + pergunta)

    limpar_botoes()

    loop = asyncio.get_running_loop()

    resultado = loop.create_future()

    def escolher_botao(valor):

        if not resultado.done():
            resultado.set_result(valor)

    for opcao in opcoes:

        botao = document.createElement("button")

        botao.textContent = opcao

        botao.className = "opcao"

        valor = opcao

        proxy = create_proxy(
            lambda evento, v=valor:
            escolher_botao(v)
        )

        botao.addEventListener("click", proxy)

        botoes.appendChild(botao)

    resposta = await resultado

    limpar_botoes()

    return resposta


# ============================================================
# INVENTÁRIO
# ============================================================

def pegar(item):

    if item not in state["inv"]:

        state["inv"].append(item)

        mostrar(
            f"\n🎒 Você encontrou: {item}"
        )

        atualizar_status()


# ============================================================
# PERDER VIDA
# ============================================================

def perder_vida(qtd=1):

    state["vida"] -= qtd

    mostrar(
        f"\n❤️ Vida: {state['vida']}"
    )

    atualizar_status()

    return state["vida"] <= 0


# ============================================================
# PERDER SANIDADE
# ============================================================

def perder_sanidade(qtd=1):

    state["sanidade"] -= qtd

    mostrar(
        f"\n🧠 Sanidade: {state['sanidade']}"
    )

    atualizar_status()

    return state["sanidade"] <= 0


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

async def fase1():

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

    resposta = await escolher(
        "👤 Escolha seu personagem:",
        [
            "🧑 Olivier",
            "👩 Amelie"
        ]
    )

    if "Olivier" in resposta:

        state["personagem"] = "Olivier"

    else:

        state["personagem"] = "Amelie"

    mostrar(f"""
Você escolheu {state["personagem"]}.

A viagem para a ilha começa...
""")

    atualizar_status()

    return "fase2"


# ============================================================
# FASE 2
# ============================================================

def fase2():

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

🏝️ A aventura começa.
""")

    return "fase3"


# ============================================================
# FASE 3
# ============================================================

async def fase3():

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

    resposta = await escolher(
        "O que você quer perguntar?",
        [
            "1️⃣ Perguntar sobre a ilha",
            "2️⃣ Perguntar sobre sua família",
            "3️⃣ Perguntar sobre os desaparecimentos"
        ]
    )

    if resposta.startswith("1"):

        mostrar("""
Milo:
— A ilha é tranquila durante o dia.

Barbara:
— Durante a noite é outra história.
""")

        state["confianca_milo"] += 1

    elif resposta.startswith("2"):

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

async def fase4():

    mostrar("""
============================================================
🏘️ FASE 4 - A VILA
============================================================

Milo mostra a vila.

Existem três lugares importantes:

⛪ Uma igreja antiga.

🏚️ Uma casa abandonada.

🔦 Um farol.

Milo:
— Se querem descobrir alguma coisa, comecem por esses
lugares.

Barbara:
— Mas tomem cuidado.

Você:
— Por quê?

Barbara:
— Porque alguns lugares não gostam de visitantes.
""")

    resposta = await escolher(
        "Para onde você vai?",
        [
            "1️⃣ Igreja",
            "2️⃣ Casa abandonada",
            "3️⃣ Farol"
        ]
    )

    if resposta.startswith("1"):
        return "fase5"

    if resposta.startswith("2"):
        return "fase6"

    return "fase7"


# ============================================================
# FASE 5
# ============================================================

async def fase5():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Examinar os símbolos",
            "2️⃣ Procurar documentos",
            "3️⃣ Fotografar os símbolos"
        ]
    )

    if resposta.startswith("1"):

        mostrar("""
Você percebe que os símbolos formam um mapa.
""")

        state["pistas"] += 2

    elif resposta.startswith("2"):

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

async def fase6():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Procurar documentos",
            "2️⃣ Subir as escadas",
            "3️⃣ Ir ao porão"
        ]
    )

    if resposta.startswith("1"):

        pegar("documentos da família")

        state["pistas"] += 3

    elif resposta.startswith("2"):

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

    mostrar("""
============================================================
🔦 FASE 7 - O FAROL
============================================================

No topo do farol existe uma caixa escondida.

Você encontra uma fotografia antiga.

Nela está parte da sua família.

Ao fundo aparece uma criatura que você não reconhece.

Milo:
— Isso estava na fotografia?

Barbara:
— Não deveria existir.
""")

    pegar("fotografia da criatura")

    state["pistas"] += 3

    atualizar_status()

    return "fase8"


# ============================================================
# FASE 8
# ============================================================

async def fase8():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Abrir a janela",
            "2️⃣ Ignorar",
            "3️⃣ Sair pela porta"
        ]
    )

    if resposta.startswith("1"):

        mostrar("""
Não existe ninguém do lado de fora.

Mas há marcas enormes no chão.
""")

        state["pistas"] += 2

        perder_sanidade()

    elif resposta.startswith("2"):

        mostrar("""
As batidas param depois de alguns minutos.
""")

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

async def fase9():

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

    resposta = await escolher(
        "Onde procurar?",
        [
            "1️⃣ Procurar na vila",
            "2️⃣ Procurar na floresta"
        ]
    )

    if resposta.startswith("1"):

        state["pistas"] += 1

        mostrar(
            "Você encontra marcas de sangue perto da floresta."
        )

    else:

        state["pistas"] += 2

        mostrar(
            "Vocês encontram pegadas enormes."
        )

    atualizar_status()

    return "fase10"


# ============================================================
# FASE 10
# ============================================================

def fase10():

    mostrar("""
============================================================
🔎 FASE 10 - A INVESTIGAÇÃO
============================================================

Vocês seguem as pistas pela floresta.

Depois de algum tempo encontram um objeto pertencente
ao desaparecido.

Barbara:
— Ele esteve aqui.

Milo:
— E alguma coisa levou ele.
""")

    pegar("objeto do desaparecido")

    state["pistas"] += 2

    atualizar_status()

    return "fase11"


# ============================================================
# FASE 11
# ============================================================

async def fase11():

    mostrar("""
============================================================
🌲 FASE 11 - A FLORESTA
============================================================

A floresta fica cada vez mais escura.

Vocês encontram uma trilha escondida.
""")

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Seguir a trilha",
            "2️⃣ Marcar o caminho e voltar",
            "3️⃣ Separar o grupo"
        ]
    )

    if resposta.startswith("1"):

        state["pistas"] += 2

    elif resposta.startswith("2"):

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

async def fase12():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Conversar com Milo",
            "2️⃣ Conversar com Barbara",
            "3️⃣ Dormir"
        ]
    )

    if resposta.startswith("1"):

        state["confianca_milo"] += 2

    elif resposta.startswith("2"):

        state["confianca_barbara"] += 2

    else:

        mostrar(
            "Você descansa e recupera um pouco da sanidade."
        )

        state["sanidade"] += 1

    atualizar_status()

    return "fase13"


# ============================================================
# FASE 13
# ============================================================

def fase13():

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

    mostrar("""
============================================================
🏚️ FASE 14 - A CABANA
============================================================

Uma pequena cabana aparece no meio da floresta.

Dentro há um diário.

Vocês encontram uma mensagem:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma forma de matar essa coisa.

Milo:
— Precisamos descobrir qual.
""")

    pegar("diário")

    state["pistas"] += 3

    atualizar_status()

    return "fase15"


# ============================================================
# FASE 15
# ============================================================

def fase15():

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

Milo:
— Então precisamos encontrar esse símbolo.

Barbara:
— E alguma coisa capaz de usá-lo.
""")

    state["monstro_fraqueza"] = True

    state["pistas"] += 3

    atualizar_status()

    return "fase16"


# ============================================================
# FASE 16
# ============================================================

async def fase16():

    mostrar("""
============================================================
🎒 FASE 16 - PREPARAÇÃO
============================================================

Vocês precisam encontrar equipamentos antes de continuar.
""")

    resposta = await escolher(
        "O que procurar?",
        [
            "1️⃣ Procurar uma arma",
            "2️⃣ Procurar medicamentos",
            "3️⃣ Procurar o símbolo"
        ]
    )

    if resposta.startswith("1"):

        pegar("arma")

        state["pistas"] += 1

    elif resposta.startswith("2"):

        pegar("medicamento")

        mostrar(
            "❤️ Vocês encontram medicamentos."
        )

    else:

        pegar("símbolo antigo")

        state["pistas"] += 3

    atualizar_status()

    return "fase17"


# ============================================================
# FASE 17
# ============================================================

async def fase17():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Procurar dentro da água",
            "2️⃣ Procurar ao redor do lago",
            "3️⃣ Ignorar o lago"
        ]
    )

    if resposta.startswith("1"):

        perder_vida()

        pegar("cristal")

        state["pistas"] += 2

    elif resposta.startswith("2"):

        pegar("cristal")

        state["pistas"] += 2

    else:

        state["pistas"] += 1

    atualizar_status()

    return "fase18"


# ============================================================
# FASE 18
# ============================================================

async def fase18():

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

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Entrar",
            "2️⃣ Procurar outra entrada"
        ]
    )

    if resposta.startswith("1"):

        state["pistas"] += 3

    else:

        state["pistas"] += 1

    atualizar_status()

    return "fase19"


# ============================================================
# FASE 19
# ============================================================

def fase19():

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

    atualizar_status()

    return "fase20"


# ============================================================
# FASE 20
# ============================================================

async def fase20():

    mostrar("""
============================================================
🏃 FASE 20 - FUGA DO MONSTRO
============================================================

A criatura começa a perseguir vocês.
""")

    resposta = await escolher(
        "Para onde correr?",
        [
            "1️⃣ Correr para a esquerda",
            "2️⃣ Correr para a direita",
            "3️⃣ Se esconder"
        ]
    )

    if resposta.startswith("1"):

        mostrar(
            "Vocês encontram uma saída."
        )

        state["pistas"] += 1

    elif resposta.startswith("2"):

        mostrar(
            "Vocês encontram uma sala escondida."
        )

        state["pistas"] += 2

    else:

        mostrar(
            "Vocês conseguem se esconder."
        )

        state["sanidade"] += 1

    atualizar_status()

    return "fase21"


# ============================================================
# FASE 21
# ============================================================

def fase21():

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

async def fase23():

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

    resposta = await escolher(
        "O que fazer com o homem?",
        [
            "1️⃣ Levar o homem embora",
            "2️⃣ Deixá-lo escondido"
        ]
    )

    if resposta.startswith("1"):

        mostrar(
            "Vocês levam o homem para um local seguro."
        )

    else:

        mostrar(
            "Vocês o escondem em uma área protegida."
        )

    state["pistas"] += 1

    atualizar_status()

    return "fase24"


# ============================================================
# FASE 24
# ============================================================

def fase24():

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

async def fase26():

    mostrar("""
============================================================
⚔️ FASE 26 - PREPARAÇÃO
============================================================

Antes da batalha, vocês precisam decidir como agir.
""")

    resposta = await escolher(
        "Como se preparar?",
        [
            "1️⃣ Preparar a arma",
            "2️⃣ Preparar o símbolo",
            "3️⃣ Procurar mais informações"
        ]
    )

    if resposta.startswith("1"):

        if "arma" in state["inv"]:

            mostrar(
                "A arma está pronta."
            )

            state["batalha"] += 1

        else:

            mostrar(
                "Vocês não possuem uma arma adequada."
            )

    elif resposta.startswith("2"):

        if "símbolo antigo" in state["inv"]:

            mostrar(
                "O símbolo está pronto."
            )

            state["batalha"] += 2

        else:

            mostrar(
                "Vocês não encontraram o símbolo."
            )

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

async def fase28():

    mostrar("""
============================================================
⚔️ FASE 28 - BATALHA CONTRA O MONSTRO
============================================================

A criatura ataca.

Vocês precisam agir rápido.
""")

    resposta = await escolher(
        "O que você faz?",
        [
            "1️⃣ Atacar o monstro",
            "2️⃣ Ativar o símbolo",
            "3️⃣ Ajudar Milo",
            "4️⃣ Ajudar Barbara"
        ]
    )

    if resposta.startswith("1"):

        if (
            "arma" in state["inv"]
            and state["monstro_fraqueza"]
        ):

            mostrar("""
Você ataca a criatura no ponto fraco.

Ela grita e recua.
""")

            state["batalha"] += 3

        else:

            mostrar("""
Seu ataque não causa muito efeito.

A criatura contra-ataca.
""")

            perder_vida()

    elif resposta.startswith("2"):

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

    elif resposta.startswith("3"):

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

            mostrar(
                "Milo não está mais aqui."
            )

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

            mostrar(
                "Barbara não está mais aqui."
            )

    atualizar_status()

    return "fase29"


# ============================================================
# FASE 29
# ============================================================

async def fase29():

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

    resposta = await escolher(
        "Qual é sua decisão?",
        [
            "1️⃣ Derrotar o monstro",
            "2️⃣ Selar o monstro",
            "3️⃣ Fugir"
        ]
    )

    if resposta.startswith("1"):

        if state["batalha"] >= 5:

            state["monstro_derrotado"] = True

        else:

            mostrar("""
Vocês atacam.

Mas não conseguiram enfraquecer a criatura o suficiente.
""")

    elif resposta.startswith("2"):

        mostrar("""
Vocês conseguem selar a criatura novamente.

Mas ela não foi destruída.
""")

    else:

        mostrar("""
Vocês decidem fugir.

A ilha começa a desmoronar.
""")

    return "fase30"


# ============================================================
# FASE 30
# ============================================================

def fase30():

    mostrar("""
============================================================
🏁 FASE 30 - O FINAL
============================================================
""")

    vivos = companheiros_vivos()

    if (
        state["monstro_derrotado"]
        and len(vivos) >= 3
    ):

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

    elif state["monstro_derrotado"]:

mudar_imagem("final_01.png")
        
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

    elif state["batalha"] >= 3:

mudar_imagem("final_02.png")
        
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

    elif state["vida"] > 0:

mudar_imagem("final_03.png")
        
mostrar("""
🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha fica para trás.

Mas, quando vocês olham para o mar...

A criatura aparece na costa.

Ela observa o barco partir.

Ela ainda está viva.
""")

    else:

mudar_imagem("final_06.png")
      
mostrar("""
💀 FINAL DA ILHA

A criatura vence.

Ninguém consegue escapar.

O segredo permanece enterrado na ilha.
""")

mudar_imagem("Gemini_Generated_Image_I0ib9910ib9910ib.png")
    
mostrar("""
============================================================
                    🎮 FIM DO JOGO
============================================================

👤 Personagem:
""" + state["personagem"] + """

❤️ Vida:
""" + str(state["vida"]) + """

🧠 Sanidade:
""" + str(state["sanidade"]) + """

🔎 Pistas:
""" + str(state["pistas"]) + """

🎒 Inventário:
""" + ", ".join(state["inv"]) + """

👥 SITUAÇÃO DOS PERSONAGENS:

Milo:
""" + ("VIVO" if state["milo_vivo"] else "MORTO") + """

Barbara:
""" + ("VIVA" if state["barbara_viva"] else "MORTA") + """

Olivier:
""" + ("VIVO" if state["olivier_vivo"] else "MORTO") + """

Amelie:
""" + ("VIVA" if state["amelie_viva"] else "MORTA") + """

============================================================
                  🏝️ FIM DO JOGO
============================================================
""")

    limpar_botoes()

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
# INICIAR O JOGO
# ============================================================

async def iniciar_jogo():

    limpar_botoes()

    atualizar_status()

    cena = "fase1"

    while cena != "fim":

        funcao = cenas[cena]

        resultado = funcao()

        if hasattr(resultado, "__await__"):

            cena = await resultado

        else:

            cena = resultado

        atualizar_status()


asyncio.ensure_future(
    iniciar_jogo()
)
