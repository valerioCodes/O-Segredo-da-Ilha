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
    "batalha": 0,
    "escolheu_derrotar": False,
    "escolheu_selar": False,
    "escolheu_fugir": False
}


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


def mostrar_imagem_fase(numero):
    imagem.src = "fase_" + str(numero).zfill(2) + ".png"
    imagem.style.display = "block"


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


# =========================================================
# FASE 1 - ESCOLHA DO PERSONAGEM
# =========================================================

def fase1(event=None):
    preparar(1)

    mostrar("""
    🏝️ O SEGREDO NA ILHA

    Tudo começa antes da chegada à ilha.

    Olivier e Amelie estão viajando juntos em um barco
    em direção a uma pequena ilha.

    Eles decidiram viajar até lá por causa de documentos
    antigos relacionados à família.

    O lugar parece tranquilo de longe, mas existem muitas
    histórias estranhas sobre aquela ilha.

    Enquanto o barco se aproxima, os dois observam
    a costa pela primeira vez.

    Agora você precisa escolher quem será o personagem
    principal da história.

    Quem você quer controlar?
    """)

    criar_botao("👨 Ser Olivier", escolher_olivier)
    criar_botao("👩 Ser Amelie", escolher_amelie)


def escolher_olivier(event):
    state["personagem"] = "Olivier"
    fase2()


def escolher_amelie(event):
    state["personagem"] = "Amelie"
    fase2()


# =========================================================
# FASE 2 - A VIAGEM
# =========================================================

def fase2(event=None):
    preparar(2)

    mostrar("""
    🚢 FASE 2 — A VIAGEM

    O barco continua avançando pelo mar.

    Olivier e Amelie estão cada vez mais próximos da ilha.

    O vento está forte e o céu começa a ficar nublado.

    Durante a viagem, os dois conversam sobre os
    documentos que encontraram antes de partir.

    Eles sabem que um parente da família desapareceu
    muitos anos atrás.

    Talvez a ilha esconda respostas.

    Enquanto observam o caminho, você pode escolher
    o que fazer durante a viagem.
    """)

    criar_botao("📜 Ler os documentos antigos", viagem_documentos)
    criar_botao("🌊 Observar a ilha de longe", viagem_observar)
    criar_botao("🗣️ Conversar sobre o desaparecimento", viagem_conversar)


def viagem_documentos(event):
    state["pistas"] += 2
    pegar("documentos da família")

    mostrar("""
    📜 DOCUMENTOS

    Você decide revisar os documentos.

    Entre as páginas existem referências a uma ilha
    isolada e a uma pessoa que desapareceu muitos anos
    atrás.

    Algumas anotações parecem ter sido escritas às
    pressas.

    Uma frase chama sua atenção:

    "Não confie em tudo que encontrar na ilha."

    Essa pode ser uma pista importante.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar viagem", fase3)


def viagem_observar(event):
    state["pistas"] += 1

    mostrar("""
    🌊 OBSERVANDO A ILHA

    Você observa a ilha pela janela do barco.

    É possível ver algumas casas próximas à costa,
    uma região de floresta e, mais distante, a silhueta
    de um antigo farol.

    A ilha parece muito maior do que vocês imaginavam.

    Algo naquele lugar dá a sensação de que existem
    histórias escondidas por todos os lados.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar viagem", fase3)


def viagem_conversar(event):
    state["pistas"] += 1

    mostrar("""
    🗣️ UMA CONVERSA

    Você conversa sobre o desaparecimento.

    A família nunca recebeu uma explicação clara
    sobre o que aconteceu.

    A única coisa que ficou foram os documentos.

    Talvez descobrir o que aconteceu naquela ilha
    seja a única maneira de entender o passado.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar viagem", fase3)


# =========================================================
# FASE 3 - CHEGADA NA ILHA
# =========================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
    🏝️ FASE 3 — CHEGADA NA ILHA

    Depois de horas de viagem, o barco finalmente
    chega à ilha.

    Olivier e Amelie desembarcam.

    Na região do porto, duas pessoas esperam por eles.

    São Milo e Barbara.

    Diferente dos visitantes, Milo e Barbara já moram
    na ilha há anos.

    Eles conhecem a vila, as trilhas e os lugares
    antigos da região.

    Milo se aproxima para receber vocês.

    Barbara observa os documentos que trouxeram.

    Agora começa oficialmente a investigação.
    """)

    criar_botao("🗣️ Conversar com Milo", chegada_milo)
    criar_botao("🗣️ Conversar com Barbara", chegada_barbara)
    criar_botao("🔎 Observar o porto", chegada_porto)


def chegada_milo(event):
    state["confianca_milo"] += 1
    state["pistas"] += 1

    mostrar("""
    🗣️ MILO

    Milo explica que conhece praticamente todos
    os caminhos da ilha.

    Ele conta que algumas regiões são evitadas
    pelos moradores.

    Quando você menciona o desaparecimento,
    Milo fica mais sério.

    — Essa história é mais antiga do que parece.

    Talvez Milo saiba mais do que está contando.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase4)


def chegada_barbara(event):
    state["confianca_barbara"] += 1
    state["pistas"] += 1

    mostrar("""
    🗣️ BARBARA

    Barbara observa os documentos com atenção.

    Ela reconhece alguns nomes antigos.

    Segundo ela, algumas famílias da ilha guardam
    histórias que nunca foram registradas nos mapas.

    Barbara acredita que os documentos podem estar
    relacionados a essas histórias.

    — Talvez vocês tenham vindo até aqui por um motivo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase4)


def chegada_porto(event):
    state["pistas"] += 1

    mostrar("""
    🔎 O PORTO

    Antes de sair, você observa o porto.

    Existem caixas antigas, barcos pequenos e
    algumas marcas estranhas próximas à areia.

    Milo explica que algumas dessas marcas aparecem
    depois de tempestades.

    Mesmo assim, alguma coisa parece diferente.

    Você decide guardar essa informação.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase4)


# =========================================================
# FASE 4 - CONHECENDO A VILA
# =========================================================

def fase4(event=None):
    preparar(4)

    mostrar("""
    🏘️ FASE 4 — CONHECENDO A VILA

    Milo e Barbara levam vocês para conhecer a vila.

    O lugar é pequeno e cercado pela floresta.

    Durante o caminho, vocês descobrem três lugares
    que podem ajudar na investigação:

    ⛪ Uma igreja antiga.
    🏚️ Uma casa abandonada.
    🔦 Um velho farol.

    Cada lugar pode esconder uma pista diferente.

    Escolha por onde começar.
    """)

    criar_botao("⛪ Investigar a igreja", fase5)
    criar_botao("🏚️ Investigar a casa abandonada", fase6)
    criar_botao("🔦 Investigar o farol", fase7)


# =========================================================
# FASE 5 - IGREJA
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
    ⛪ FASE 5 — A IGREJA

    A igreja antiga está praticamente abandonada.

    As portas rangem quando vocês entram.

    Nas paredes existem símbolos que parecem muito
    antigos.

    Barbara reconhece alguns deles.

    Milo explica que os moradores mais antigos
    evitavam falar sobre aqueles desenhos.

    O lugar pode esconder mais de uma pista.
    """)

    criar_botao("🔎 Examinar os símbolos", igreja_simbolos)
    criar_botao("📖 Procurar livros", igreja_livros)
    criar_botao("🚪 Procurar uma passagem escondida", igreja_passagem)


def igreja_simbolos(event):
    state["pistas"] += 2
    pegar("fotografia dos símbolos")

    mostrar("""
    🔎 OS SÍMBOLOS

    Você examina cuidadosamente os símbolos.

    Alguns deles parecem formar um caminho.

    Barbara percebe que os desenhos apontam para
    uma região da floresta.

    Você tira uma fotografia para guardar a pista.

    Talvez esses símbolos sejam importantes mais tarde.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase6)


def igreja_livros(event):
    state["pistas"] += 2
    pegar("livro antigo")

    mostrar("""
    📖 OS LIVROS

    Em uma estante velha você encontra um livro.

    Ele fala sobre histórias antigas da ilha.

    Uma das páginas menciona uma criatura escondida
    em uma região subterrânea.

    O texto também fala sobre um símbolo capaz
    de enfraquecê-la.

    Você guarda o livro.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase6)


def igreja_passagem(event):
    state["pistas"] += 3
    pegar("chave enferrujada")

    mostrar("""
    🚪 A PASSAGEM

    Atrás de uma parede existe uma pequena passagem.

    Dentro dela vocês encontram uma chave enferrujada.

    Ninguém sabe qual porta ela abre.

    Mesmo assim, parece ser um objeto importante.

    Você guarda a chave.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase6)


# =========================================================
# FASE 6 - CASA ABANDONADA
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
    🏚️ FASE 6 — A CASA ABANDONADA

    A casa abandonada fica afastada da vila.

    Milo conhece o antigo morador.

    Segundo ele, a pessoa desapareceu há muitos anos.

    Dentro da casa existem documentos, fotografias
    e objetos antigos.

    Há vários lugares que podem ser investigados.
    """)

    criar_botao("📄 Procurar documentos", casa_documentos)
    criar_botao("⬆️ Subir as escadas", casa_escadas)
    criar_botao("⬇️ Investigar o porão", casa_porao)


def casa_documentos(event):
    state["pistas"] += 3
    pegar("documentos da família")

    mostrar("""
    📄 OS DOCUMENTOS

    Entre os documentos você encontra novamente
    o sobrenome da família.

    Barbara fica surpresa.

    — Então sua família realmente esteve aqui.

    A ligação entre a família e a ilha está ficando
    cada vez mais clara.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase7)


def casa_escadas(event):
    state["pistas"] += 2
    pegar("fotografia antiga")

    mostrar("""
    📸 A FOTOGRAFIA

    No andar de cima existe uma fotografia antiga.

    Ela mostra algumas pessoas diante da floresta.

    Uma delas pode ser o parente desaparecido.

    Milo reconhece o lugar da fotografia.

    — Eu sei onde isso foi tirado.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase7)


def casa_porao(event):
    state["pistas"] += 3
    pegar("fotografia antiga")

    mostrar("""
    ⬇️ O PORÃO

    No porão vocês encontram uma caixa escondida.

    Dentro existe uma fotografia.

    No verso está escrito que algo escondido
    abaixo da ilha nunca deveria ser despertado.

    A mensagem aumenta ainda mais o mistério.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase7)


# =========================================================
# FASE 7 - FAROL
# =========================================================

def fase7(event=None):
    preparar(7)

    mostrar("""
    🔦 FASE 7 — O FAROL

    O velho farol fica no alto de uma região rochosa.

    Milo acompanha vocês pelo caminho.

    O lugar está abandonado há muito tempo.

    Dentro do farol existem vários objetos antigos.

    Vocês podem investigar diferentes partes do lugar.
    """)

    criar_botao("📦 Abrir a caixa antiga", farol_caixa)
    criar_botao("🔭 Subir até o topo", farol_topo)
    criar_botao("📸 Procurar fotografias", farol_fotos)


def farol_caixa(event):
    state["pistas"] += 2
    pegar("fotografia da criatura")

    mostrar("""
    📦 A CAIXA

    Dentro de uma caixa antiga existe uma fotografia.

    Ao fundo aparece uma figura estranha.

    Barbara observa a imagem em silêncio.

    — Isso não parece ser uma pessoa.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def farol_topo(event):
    state["pistas"] += 2

    mostrar("""
    🔭 O TOPO DO FAROL

    Do alto do farol vocês conseguem observar
    praticamente toda a ilha.

    A floresta parece muito maior vista dali.

    Você percebe uma região escura entre as árvores.

    Talvez seja uma entrada para algum lugar.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


def farol_fotos(event):
    state["pistas"] += 3
    pegar("fotografia da criatura")

    mostrar("""
    📸 AS FOTOGRAFIAS

    Vocês encontram fotografias antigas.

    Algumas mostram pessoas investigando a floresta.

    Em uma delas aparece uma sombra estranha.

    A imagem pode estar relacionada ao desaparecimento.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase8)


# =========================================================
# FASE 8 - PRIMEIRA NOITE
# =========================================================

def fase8(event=None):
    preparar(8)

    mostrar("""
    🌙 FASE 8 — A PRIMEIRA NOITE

    Depois de um dia inteiro investigando,
    vocês voltam para a vila.

    Milo e Barbara oferecem um lugar seguro
    para passar a noite.

    Durante a madrugada...

    TOC.

    TOC.

    TOC.

    Alguém bate na janela.

    O grupo fica em silêncio.

    O que você faz?
    """)

    criar_botao("🪟 Abrir a janela", noite_janela)
    criar_botao("😶 Ignorar as batidas", noite_ignorar)
    criar_botao("🔎 Procurar outra saída", noite_saida)


def noite_janela(event):
    perder_sanidade()
    state["pistas"] += 2

    mostrar("""
    🪟 A JANELA

    Você abre a janela.

    Não há ninguém.

    Porém, existem marcas estranhas no chão.

    Milo reconhece aquelas marcas.

    — Eu já vi isso antes.

    Barbara olha para a floresta.

    — Então ela voltou.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase9)


def noite_ignorar(event):
    state["pistas"] += 1

    mostrar("""
    😶 IGNORAR

    Vocês decidem não abrir.

    Quando amanhece, encontram marcas no chão
    próximas da casa.

    Alguma coisa esteve ali durante a noite.

    Ninguém sabe o que era.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase9)


def noite_saida(event):
    state["pistas"] += 2

    mostrar("""
    🔎 INVESTIGAR

    Em vez de abrir a janela, vocês procuram
    outra maneira de observar o lado de fora.

    Uma pequena marca aparece perto da porta.

    A marca parece ter sido feita recentemente.

    Vocês decidem investigar pela manhã.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase9)


# =========================================================
# FASE 9 - DESAPARECIMENTO
# =========================================================

def fase9(event=None):
    preparar(9)

    mostrar("""
    🚨 FASE 9 — O DESAPARECIMENTO

    Na manhã seguinte, um morador desaparece.

    Milo conhece a pessoa.

    Barbara começa a procurar informações.

    As marcas encontradas durante a noite podem
    estar relacionadas ao desaparecimento.

    Vocês precisam decidir por onde procurar.
    """)

    criar_botao("🏘️ Procurar informações na vila", desaparecimento_vila)
    criar_botao("🌲 Procurar marcas na floresta", desaparecimento_floresta)
    criar_botao("🏠 Investigar a casa do desaparecido", desaparecimento_casa)


def desaparecimento_vila(event):
    state["pistas"] += 1

    mostrar("""
    🏘️ A VILA

    Vocês conversam com alguns moradores.

    Uma pessoa diz ter visto o desaparecido
    caminhando em direção à floresta.

    Agora existe uma direção para seguir.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase10)


def desaparecimento_floresta(event):
    state["pistas"] += 2

    mostrar("""
    🌲 A FLORESTA

    Vocês encontram marcas no chão.

    Elas seguem para fora da vila.

    Milo reconhece o caminho.

    — Ele provavelmente passou por aqui.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase10)


def desaparecimento_casa(event):
    state["pistas"] += 2
    pegar("objeto do desaparecido")

    mostrar("""
    🏠 A CASA DO DESAPARECIDO

    Dentro da casa vocês encontram um objeto
    que parece ter sido levado às pressas.

    Barbara acredita que ele pode ajudar
    a descobrir para onde a pessoa foi.

    A investigação continua.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase10)


# =========================================================
# FASE 10 - PROCURANDO PISTAS
# =========================================================

def fase10(event=None):
    preparar(10)

    mostrar("""
    🔎 FASE 10 — PROCURANDO PISTAS

    A investigação continua.

    Vocês seguem as informações encontradas
    durante a procura pelo desaparecido.

    Existem diferentes maneiras de procurar pistas.

    Cada descoberta pode ajudar a entender
    o que está acontecendo na ilha.
    """)

    criar_botao("👣 Seguir as marcas", pistas_marcas)
    criar_botao("📜 Comparar os documentos", pistas_documentos)
    criar_botao("🔎 Procurar objetos escondidos", pistas_objetos)


def pistas_marcas(event):
    state["pistas"] += 2

    mostrar("""
    👣 AS MARCAS

    Vocês seguem as marcas pelo chão.

    Elas continuam em direção à floresta.

    Algumas são muito maiores do que pegadas humanas.

    A descoberta deixa o grupo preocupado.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase11)


def pistas_documentos(event):
    state["pistas"] += 3

    mostrar("""
    📜 OS DOCUMENTOS

    Você compara os documentos encontrados.

    As informações parecem apontar para a mesma
    região da ilha.

    Uma antiga referência à floresta aparece
    várias vezes.

    Agora vocês têm uma direção mais clara.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase11)


def pistas_objetos(event):
    state["pistas"] += 2

    mostrar("""
    🔎 OS OBJETOS

    Vocês procuram entre as árvores.

    Encontram pequenas marcas e um objeto antigo.

    Barbara acredita que alguém esteve naquela
    região recentemente.

    A trilha continua.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase11)


# =========================================================
# FASE 11 - TRILHA NA FLORESTA
# =========================================================

def fase11(event=None):
    preparar(11)

    mostrar("""
    🌲 FASE 11 — TRILHA NA FLORESTA

    A trilha entra cada vez mais fundo na floresta.

    Milo conhece alguns caminhos.

    Mesmo assim, existem trechos que ele nunca
    tinha explorado.

    O grupo precisa escolher como continuar.
    """)

    criar_botao("🥾 Seguir a trilha principal", trilha_principal)
    criar_botao("🌿 Procurar um caminho alternativo", trilha_alternativa)
    criar_botao("🗺️ Usar as informações do mapa", trilha_mapa)


def trilha_principal(event):
    state["pistas"] += 2

    mostrar("""
    🥾 TRILHA PRINCIPAL

    Vocês seguem as marcas diretamente.

    Depois de algum tempo, encontram sinais
    de que alguém passou por ali.

    A trilha continua até uma região mais aberta.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase12)


def trilha_alternativa(event):
    state["pistas"] += 2

    mostrar("""
    🌿 CAMINHO ALTERNATIVO

    O caminho é mais difícil, mas leva vocês
    até uma parte diferente da floresta.

    Ali existem árvores muito antigas.

    No chão, vocês encontram símbolos parecidos
    com os da igreja.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase12)


def trilha_mapa(event):
    state["pistas"] += 3

    mostrar("""
    🗺️ O MAPA

    Vocês usam o mapa encontrado anteriormente.

    Uma marca antiga indica uma região próxima
    a uma pequena clareira.

    Milo confirma que o local existe.

    Vocês seguem naquela direção.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase12)


# =========================================================
# FASE 12 - ACAMPAMENTO
# =========================================================

def fase12(event=None):
    preparar(12)

    mostrar("""
    🔥 FASE 12 — ACAMPAMENTO

    A noite chega antes que vocês consigam voltar.

    O grupo monta um pequeno acampamento.

    Milo conta histórias que ouviu de sua família.

    Barbara organiza as pistas encontradas.

    O grupo está cansado, mas precisa continuar
    investigando.
    """)

    criar_botao("🔥 Conversar com Milo", acampamento_milo)
    criar_botao("📖 Revisar as pistas com Barbara", acampamento_barbara)
    criar_botao("🌲 Vigiar a floresta", acampamento_vigiar)


def acampamento_milo(event):
    state["confianca_milo"] += 2
    state["pistas"] += 1

    mostrar("""
    🔥 MILO CONTA O QUE SABE

    Milo conta histórias que ouviu quando era criança.

    Segundo ele, existiam lugares da ilha
    que os moradores antigos evitavam.

    Ele nunca soube se as histórias eram verdadeiras.

    Agora começa a acreditar nelas.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase13)


def acampamento_barbara(event):
    state["confianca_barbara"] += 2
    state["pistas"] += 2

    mostrar("""
    📖 BARBARA ORGANIZA AS PISTAS

    Barbara coloca as informações lado a lado.

    Os símbolos, os documentos e as fotografias
    parecem estar relacionados.

    Ela acredita que existe uma história maior
    por trás de tudo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase13)


def acampamento_vigiar(event):
    state["pistas"] += 2

    mostrar("""
    🌲 VIGIANDO A FLORESTA

    Você decide ficar de olho na floresta.

    Durante a noite, um barulho distante chama
    sua atenção.

    Quando vocês verificam pela manhã,
    encontram novas marcas no chão.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase13)


# =========================================================
# FASE 13 - PEGADAS GIGANTES
# =========================================================

def fase13(event=None):
    preparar(13)

    mostrar("""
    🐾 FASE 13 — PEGADAS GIGANTES

    Pela manhã, novas pegadas aparecem.

    Dessa vez não existe dúvida.

    Elas são muito maiores que pegadas humanas.

    Milo observa o chão em silêncio.

    Barbara tenta comparar as marcas com
    as fotografias antigas.

    Existem diferentes maneiras de investigar.
    """)

    criar_botao("👣 Medir as pegadas", pegadas_medir)
    criar_botao("📸 Fotografar as pegadas", pegadas_fotografar)
    criar_botao("🔎 Seguir as pegadas", pegadas_seguir)


def pegadas_medir(event):
    state["pistas"] += 2

    mostrar("""
    👣 MEDINDO AS PEGADAS

    As marcas são grandes demais para pertencer
    a qualquer pessoa.

    Milo percebe que elas seguem em direção
    a uma parte mais profunda da floresta.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase14)


def pegadas_fotografar(event):
    state["pistas"] += 2
    pegar("fotografia das pegadas")

    mostrar("""
    📸 FOTOGRAFIA

    Você registra as pegadas.

    Barbara compara a imagem com uma fotografia
    encontrada anteriormente.

    Os padrões parecem semelhantes.

    Existe alguma coisa naquela floresta.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase14)


def pegadas_seguir(event):
    state["pistas"] += 3

    mostrar("""
    🔎 SEGUINDO AS PEGADAS

    Vocês decidem seguir as marcas.

    Depois de algum tempo, uma pequena cabana
    aparece entre as árvores.

    Talvez seja ali que esteja a próxima resposta.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase14)


# =========================================================
# FASE 14 - CABANA
# =========================================================

def fase14(event=None):
    preparar(14)

    mostrar("""
    🏚️ FASE 14 — A CABANA

    A cabana parece abandonada.

    A porta está entreaberta.

    Dentro existem mapas, livros e objetos antigos.

    O lugar parece ter sido usado por alguém
    que investigava a ilha.

    Vocês podem procurar diferentes coisas.
    """)

    criar_botao("📖 Procurar um diário", cabana_diario)
    criar_botao("🗺️ Procurar mapas", cabana_mapas)
    criar_botao("📦 Procurar objetos", cabana_objetos)


def cabana_diario(event):
    state["pistas"] += 3
    pegar("diário")

    mostrar("""
    📖 O DIÁRIO

    Vocês encontram um diário antigo.

    As páginas falam sobre uma criatura escondida
    nas profundezas da ilha.

    O diário também menciona símbolos antigos.

    Talvez finalmente exista uma explicação
    para tudo.
    """)

    atualizar_status()
    criar_botao("➡️ Ler o diário", fase15)


def cabana_mapas(event):
    state["pistas"] += 2

    mostrar("""
    🗺️ OS MAPAS

    Os mapas mostram várias regiões da ilha.

    Uma área subterrânea está marcada com um símbolo.

    Barbara acredita que aquele lugar pode ser
    importante para a investigação.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase15)


def cabana_objetos(event):
    state["pistas"] += 2
    pegar("objeto antigo")

    mostrar("""
    📦 OS OBJETOS

    Entre caixas antigas vocês encontram objetos
    que parecem ter sido usados durante pesquisas.

    Um deles possui o mesmo símbolo encontrado
    anteriormente.

    A ligação está ficando cada vez mais forte.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase15)


# =========================================================
# FASE 15 - O DIÁRIO
# =========================================================

def fase15(event=None):
    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 2

    mostrar("""
    📖 FASE 15 — O DIÁRIO

    O diário revela informações importantes.

    Antigos moradores descobriram uma criatura
    nas profundezas da ilha.

    Eles descobriram que certos símbolos poderiam
    enfraquecê-la.

    O diário também fala sobre alguém da família
    de Olivier e Amelie.

    Essa pessoa tentou impedir que a criatura
    voltasse a ameaçar a ilha.

    Agora vocês sabem que precisam se preparar.
    """)

    atualizar_status()

    criar_botao("📖 Ler as últimas páginas", diario_final)
    criar_botao("🔎 Procurar o símbolo mencionado", diario_simbolo)
    criar_botao("🗺️ Estudar o mapa junto com o diário", diario_mapa)


def diario_final(event):
    state["pistas"] += 2

    mostrar("""
    📖 ÚLTIMAS PÁGINAS

    As últimas páginas explicam que o símbolo
    pode enfraquecer a criatura.

    Porém, ele precisa ser encontrado antes
    do confronto.

    A informação pode ser decisiva.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase16)


def diario_simbolo(event):
    state["pistas"] += 3
    pegar("símbolo antigo")
    state["monstro_fraqueza"] = True

    mostrar("""
    🔱 O SÍMBOLO

    Entre as páginas existe um desenho detalhado.

    Barbara reconhece o símbolo.

    Depois de procurar entre os objetos da cabana,
    vocês encontram uma versão antiga dele.

    Agora possuem uma ferramenta importante
    para o futuro confronto.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase16)


def diario_mapa(event):
    state["pistas"] += 3

    mostrar("""
    🗺️ MAPA E DIÁRIO

    Quando vocês colocam o mapa ao lado do diário,
    percebem que os símbolos indicam uma direção.

    O caminho leva até uma região próxima
    a um lago.

    Talvez seja o próximo passo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase16)


# =========================================================
# FASE 16 - PREPARAÇÃO
# =========================================================

def fase16(event=None):
    preparar(16)

    mostrar("""
    🎒 FASE 16 — PREPARAÇÃO

    Agora vocês sabem que existe alguma coisa
    escondida nas profundezas da ilha.

    Antes de continuar, precisam se preparar.

    Milo e Barbara ajudam a organizar tudo
    que foi encontrado.

    Você pode escolher como se preparar.
    """)

    criar_botao("🎒 Organizar equipamentos", preparacao_equipamentos)
    criar_botao("🔱 Preparar o símbolo", preparacao_simbolo)
    criar_botao("📜 Revisar todas as pistas", preparacao_pistas)


def preparacao_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
    🎒 EQUIPAMENTOS

    Vocês organizam os equipamentos.

    Milo verifica tudo cuidadosamente.

    Barbara separa os documentos e objetos
    mais importantes.

    O grupo está mais preparado.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase17)


def preparacao_simbolo(event):
    if "símbolo antigo" not in state["inv"]:
        pegar("símbolo antigo")

    state["monstro_fraqueza"] = True
    state["batalha"] += 3

    mostrar("""
    🔱 O SÍMBOLO

    Vocês preparam o símbolo antigo.

    Barbara explica que ele pode ser usado
    contra a criatura.

    O objeto parece reagir aos símbolos
    encontrados durante a investigação.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase17)


def preparacao_pistas(event):
    state["pistas"] += 2

    mostrar("""
    📜 REVISANDO AS PISTAS

    Vocês colocam todas as pistas juntas.

    Fotografias, documentos, símbolos e mapas
    finalmente começam a fazer sentido.

    O caminho parece levar até um lago.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase17)


# =========================================================
# FASE 17 - LAGO
# =========================================================

def fase17(event=None):
    preparar(17)

    mostrar("""
    🌊 FASE 17 — O LAGO

    As pistas levam vocês até um lago escondido
    entre as árvores.

    O lugar está completamente silencioso.

    Próximo à margem existem objetos antigos.

    Vocês podem investigar o lago de diferentes formas.
    """)

    criar_botao("💎 Procurar algo na margem", lago_margem)
    criar_botao("🔎 Examinar os símbolos nas pedras", lago_pedras)
    criar_botao("🌊 Investigar a água", lago_agua)


def lago_margem(event):
    state["pistas"] += 2
    pegar("cristal")

    mostrar("""
    💎 O CRISTAL

    Próximo à margem vocês encontram um pequeno cristal.

    Quando ele se aproxima do símbolo antigo,
    começa a brilhar.

    Talvez exista uma ligação entre os dois.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase18)


def lago_pedras(event):
    state["pistas"] += 3

    mostrar("""
    🔎 AS PEDRAS

    Existem símbolos gravados nas pedras.

    Barbara percebe que são muito parecidos
    com os desenhos da igreja.

    Um deles indica uma passagem subterrânea.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase18)


def lago_agua(event):
    state["pistas"] += 2
    pegar("cristal")

    mostrar("""
    🌊 A ÁGUA

    Ao investigar a água, vocês percebem
    um brilho no fundo.

    Depois de procurar com cuidado,
    encontram um pequeno cristal.

    Ele parece reagir ao símbolo antigo.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase18)


# =========================================================
# FASE 18 - CAVERNA
# =========================================================

def fase18(event=None):
    preparar(18)

    mostrar("""
    🕳️ FASE 18 — A CAVERNA

    O caminho termina diante de uma enorme caverna.

    Milo reconhece o lugar.

    — Meu avô falava dessa caverna.

    Nas paredes existem símbolos antigos.

    O grupo sabe que está chegando cada vez
    mais perto da verdade.

    Como vocês vão entrar?
    """)

    criar_botao("🔦 Entrar pela entrada principal", caverna_principal)
    criar_botao("🕳️ Procurar outra entrada", caverna_alternativa)
    criar_botao("🔎 Examinar os símbolos antes", caverna_simbolos)


def caverna_principal(event):
    state["pistas"] += 2

    mostrar("""
    🔦 ENTRADA PRINCIPAL

    Vocês entram pela abertura principal.

    O corredor é escuro e silencioso.

    Quanto mais avançam, mais antigos ficam
    os símbolos nas paredes.

    Um som distante ecoa pela caverna.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase19)


def caverna_alternativa(event):
    state["pistas"] += 3

    mostrar("""
    🕳️ OUTRA ENTRADA

    Vocês encontram uma passagem lateral.

    Ela parece ter sido construída por pessoas
    que conheciam muito bem a caverna.

    O caminho leva para uma área mais profunda.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase19)


def caverna_simbolos(event):
    state["pistas"] += 3
    state["monstro_fraqueza"] = True

    mostrar("""
    🔎 OS SÍMBOLOS

    Barbara examina os símbolos.

    Alguns deles explicam como o símbolo antigo
    pode ser usado.

    Agora vocês possuem uma informação muito
    importante para o confronto.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase19)


# =========================================================
# FASE 19 - PRIMEIRO ENCONTRO
# =========================================================

def fase19(event=None):
    preparar(19)

    perder_sanidade()

    mostrar("""
    👹 FASE 19 — PRIMEIRO ENCONTRO

    Um som estranho ecoa pela caverna.

    O grupo para.

    Uma enorme silhueta aparece no final
    do corredor.

    Barbara reconhece os símbolos nas paredes.

    Milo entende o que está acontecendo.

    — A criatura existe.

    Vocês ainda não estão preparados
    para enfrentá-la.

    É preciso decidir como reagir.
    """)

    criar_botao("🏃 Tentar fugir imediatamente", encontro_fugir)
    criar_botao("🔎 Observar a criatura", encontro_observar)
    criar_botao("🔱 Mostrar o símbolo", encontro_simbolo)


def encontro_fugir(event):
    state["batalha"] += 1

    mostrar("""
    🏃 FUGIR

    Vocês decidem não arriscar.

    Milo encontra um caminho de saída.

    O grupo corre pelos corredores
    até conseguir se afastar.

    A criatura continua na caverna.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase20)


def encontro_observar(event):
    state["pistas"] += 2
    state["batalha"] += 1

    mostrar("""
    🔎 OBSERVAR

    Vocês observam a criatura sem se aproximar.

    Barbara percebe que ela reage aos símbolos
    nas paredes.

    Essa informação pode ajudar mais tarde.

    Quando a criatura se aproxima,
    vocês recuam.
    """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase20)


def encontro_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["monstro_fraqueza"] = True
        state["batalha"] += 3

        mostrar("""
        🔱 O SÍMBOLO

        Você mostra o símbolo antigo.

        A criatura reage imediatamente.

        Ela recua.

        Barbara percebe que o símbolo realmente
        pode enfraquecê-la.

        Agora vocês sabem que existe uma maneira
        de enfrentá-la.
        """)
    else:
        perder_sanidade()

        mostrar("""
        🔱 O SÍMBOLO

        Você tenta usar o símbolo.

        Porém, percebe que ainda não possui
        o símbolo original.

        A criatura continua avançando.

        Vocês precisam fugir.
        """)

    atualizar_status()
    criar_botao("➡️ Continuar", fase20)


# =========================================================
# FASE 20 - FUGA
# =========================================================

def fase20(event=None):
    preparar(20)

    mostrar("""
    🏃 FASE 20 — FUGA

    Depois do primeiro encontro,
    vocês conseguem escapar da caverna.

    Milo conhece um caminho de volta.

    Barbara organiza as últimas pistas.

    Agora vocês sabem que a criatura existe.

    Também sabem que existe uma forma
    de enfrentá-la.

    Antes de chegar ao final da história,
    você precisa decidir o que fará com
    tudo o que descobriu.
    """)

    criar_botao("⚔️ Enfrentar a criatura", preparar_derrota)
    criar_botao("🔒 Preparar um novo selamento", preparar_selamento)
    criar_botao("🏃 Abandonar a ilha", preparar_fuga)


def preparar_derrota(event):
    state["escolheu_derrotar"] = True
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    fase_final()


def preparar_selamento(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = True
    state["escolheu_fugir"] = False

    fase_final()


def preparar_fuga(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = True

    fase_final()


# =========================================================
# FINAIS
# =========================================================

def fase_final(event=None):
    limpar()
    atualizar_status()

    # FINAL 1
    if state["escolheu_derrotar"]:

        if state["monstro_fraqueza"] and state["pistas"] >= 10:
            mostrar_imagem_final("final_01.png")

            mostrar("""
            🌟 FINAL 1 — PERFEITO

            Vocês finalmente conseguem enfrentar
            a criatura.

            Todas as pistas encontradas durante
            a investigação foram importantes.

            O símbolo antigo enfraquece a criatura
            e permite que vocês terminem aquilo
            que a família havia começado muitos anos atrás.

            Milo e Barbara ajudam durante o confronto.

            Depois de tantos anos, o segredo da ilha
            finalmente chega ao fim.

            A criatura é derrotada.

            A ilha está livre.

            Olivier e Amelie finalmente descobrem
            a verdade sobre o passado da família.

            🏝️ O segredo foi revelado.

            ❤️ Todos conseguiram sobreviver.
            """)

        else:
            mostrar_imagem_final("final_02.png")

            mostrar("""
            🌅 FINAL 2 — VITÓRIA COM PERDAS

            Vocês decidem enfrentar a criatura.

            Mesmo sem possuir todas as informações,
            conseguem encontrar uma maneira de
            enfraquecê-la.

            O confronto é difícil.

            Nem tudo acontece como planejado.

            Algumas coisas são perdidas durante
            o confronto.

            Mesmo assim, a criatura é finalmente
            derrotada.

            A ilha está livre, mas o grupo nunca
            esquecerá o preço pago para chegar até aqui.

            🏝️ Vocês venceram.

            Mas foi uma vitória com perdas.
            """)

    # FINAL 3
    elif state["escolheu_selar"]:

        mostrar_imagem_final("final_03.png")

        mostrar("""
        🔒 FINAL 3 — O SELAMENTO

        Vocês decidem que destruir a criatura
        não é a melhor escolha.

        Barbara utiliza os símbolos antigos.

        Milo ajuda a encontrar o caminho correto.

        O grupo consegue realizar o antigo ritual
        de selamento.

        A passagem começa a se fechar.

        A criatura desaparece novamente
        nas profundezas da ilha.

        O lugar fica silencioso.

        A ilha está segura...

        por enquanto.

        🔒 O segredo foi selado novamente.
        """)

    # FINAL 6
    elif state["escolheu_fugir"]:

        mostrar_imagem_final("final_06.png")

        mostrar("""
        🏃 FINAL 6 — O SEGREDO CONTINUA

        Vocês decidem abandonar a ilha.

        Milo conhece o caminho de volta.

        Barbara ajuda o grupo a encontrar
        uma rota segura.

        Olivier e Amelie levam consigo
        os documentos encontrados.

        A ilha fica para trás.

        Milo e Barbara permanecem lá,
        porque aquela é a casa deles.

        Vocês sobreviveram.

        Porém, a criatura continua escondida.

        A verdade nunca foi completamente revelada.

        🏝️ O segredo da ilha continua.
        """)

    mostrar("""
    🎮 FIM DO JOGO

    Obrigado por jogar:

    🏝️ O SEGREDO NA ILHA
    """)

    criar_botao("🔄 Jogar novamente", reiniciar)


# =========================================================
# REINICIAR
# =========================================================

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

    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    fase1()


# =========================================================
# INICIAR JOGO
# =========================================================

fase1()
