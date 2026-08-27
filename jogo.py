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
# FASE 1
# =========================================================

def fase1(event=None):
    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Olivier e Amelie estão viajando de barco em direção a uma pequena ilha.

Os dois encontraram documentos antigos relacionados à própria família.
Entre esses documentos havia referências a um parente que desapareceu
muitos anos atrás.

Enquanto o barco se aproxima da ilha, os dois observam a costa pela primeira vez.

Eles ainda não sabem o que encontrarão.

Na ilha, Milo e Barbara já vivem há muitos anos.
Os dois conhecem as histórias, os caminhos e os lugares antigos da região.

Agora Olivier e Amelie estão a caminho da ilha.

Escolha quem será o personagem principal:
""")

    criar_botao("🧑 Olivier", escolher_olivier)
    criar_botao("👩 Amelie", escolher_amelie)


def escolher_olivier(event):
    state["personagem"] = "Olivier"
    fase2()


def escolher_amelie(event):
    state["personagem"] = "Amelie"
    fase2()


# =========================================================
# FASE 2
# =========================================================

def fase2(event=None):
    preparar(2)

    mostrar("""
🚢 A VIAGEM

Você escolheu jogar como """ + state["personagem"] + """.

O barco continua avançando pelo mar.

Amelie e Olivier estão juntos durante a viagem.
Os dois observam a ilha ficando cada vez maior no horizonte.

O objetivo da viagem é descobrir o que aconteceu com o parente
desaparecido e entender por que a família deles aparece nos
documentos antigos encontrados.

O mar está relativamente tranquilo, mas existe uma sensação estranha.

Depois de algumas horas, o barco finalmente se aproxima da ilha.

A viagem está chegando ao fim.
""")

    criar_botao("🏝️ Continuar até a ilha", fase3)


# =========================================================
# FASE 3
# =========================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
🏝️ A CHEGADA À ILHA

O barco finalmente chega ao pequeno porto da ilha.

Amelie e Olivier desembarcam.

A ilha parece tranquila, mas é bem diferente do que eles imaginavam.

Pouco depois, eles encontram duas pessoas que já vivem naquele lugar.

São Milo e Barbara.

Milo e Barbara moram na ilha há anos e conhecem muito bem
a região, seus caminhos e suas histórias.

Milo observa os dois visitantes.

— Vocês devem ser as pessoas que estavam chegando.

Barbara olha para os documentos que eles trouxeram.

— Vieram procurar alguém da família?

A investigação está prestes a começar.
""")

    criar_botao("🗣️ Conversar com Milo", fase4_milo)
    criar_botao("🗣️ Conversar com Barbara", fase4_barbara)


# =========================================================
# FASE 4
# =========================================================

def fase4_milo(event):
    state["confianca_milo"] += 1
    state["pistas"] += 1

    preparar(4)

    mostrar("""
🗣️ MILO

Milo explica que sua família vive na ilha há gerações.

Por conhecer a ilha desde criança, ele sabe onde ficam
as trilhas, as casas antigas e alguns lugares que nem aparecem
nos mapas.

Ele também conta que alguns moradores desapareceram
ao longo dos anos.

— Se vocês estão procurando respostas, posso ajudar.

Milo menciona uma região antiga da ilha onde ninguém gosta de entrar.

Talvez seja lá que o mistério tenha começado.
""")

    criar_botao("➡️ Continuar", fase5)


def fase4_barbara(event):
    state["confianca_barbara"] += 1
    state["pistas"] += 1

    preparar(4)

    mostrar("""
🗣️ BARBARA

Barbara conta que sua família também vive na ilha há muitas gerações.

Ela conhece histórias sobre símbolos antigos encontrados pela região.

Segundo sua família, esses símbolos estavam relacionados
à proteção da ilha contra alguma coisa.

Barbara acredita que os documentos de Olivier e Amelie
podem estar ligados a essa história.

— Talvez sua família tenha deixado alguma coisa aqui.

A investigação continua.
""")

    criar_botao("➡️ Continuar", fase5)


# =========================================================
# FASE 5
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
🏘️ A VILA

Milo e Barbara mostram a vila para Amelie e Olivier.

Existem três lugares importantes:

⛪ Uma igreja antiga.

🏚️ Uma casa abandonada.

🔦 Um velho farol.

Cada lugar pode esconder uma pista diferente.

Onde vocês vão começar?
""")

    criar_botao("⛪ Ir para a igreja", fase6)
    criar_botao("🏚️ Ir para a casa abandonada", fase7)
    criar_botao("🔦 Ir para o farol", fase8)


# =========================================================
# FASE 6
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
⛪ A IGREJA

A igreja está abandonada há muitos anos.

Milo e Barbara conhecem o lugar.

Nas paredes existem símbolos antigos.

Barbara reconhece alguns deles.

— Minha família falava sobre esses símbolos.

Vocês começam a investigar.
""")

    criar_botao("🔎 Examinar os símbolos", fase6_simbolos)
    criar_botao("📖 Procurar documentos", fase6_documentos)


def fase6_simbolos(event):
    state["pistas"] += 2
    pegar("fotografia dos símbolos")

    mostrar("""
Os símbolos parecem formar um caminho.

Barbara percebe que alguns desenhos apontam para a floresta.

Você fotografa os símbolos para estudar depois.

Talvez eles sejam uma pista importante.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase9)


def fase6_documentos(event):
    state["pistas"] += 3
    pegar("livro antigo")

    mostrar("""
Atrás de um banco antigo vocês encontram um livro.

Ele fala sobre uma criatura que estaria escondida
nas profundezas da ilha.

Uma das páginas menciona um símbolo capaz de enfraquecê-la.

Essa informação pode ser muito importante.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase9)


# =========================================================
# FASE 7
# =========================================================

def fase7(event=None):
    preparar(7)

    mostrar("""
🏚️ A CASA ABANDONADA

Milo leva vocês até uma casa abandonada.

O antigo morador desapareceu muitos anos atrás.

Dentro existem documentos, fotografias e objetos.

Talvez alguma dessas coisas explique o passado da ilha.
""")

    criar_botao("📄 Procurar documentos", fase7_documentos)
    criar_botao("⬆️ Subir as escadas", fase7_escadas)
    criar_botao("⬇️ Investigar o porão", fase7_porao)


def fase7_documentos(event):
    state["pistas"] += 3
    pegar("documentos da família")

    mostrar("""
Entre os documentos aparece o sobrenome da família.

Barbara fica surpresa.

— Sua família realmente esteve aqui.

Agora existe uma ligação clara entre vocês e o passado da ilha.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase9)


def fase7_escadas(event):
    state["pistas"] += 2
    pegar("fotografia antiga")

    mostrar("""
No andar de cima vocês encontram uma fotografia.

Ela mostra algumas pessoas diante da floresta.

Uma delas parece ser o parente desaparecido.

Milo reconhece o lugar.

— Eu sei onde isso foi tirado.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase9)


def fase7_porao(event):
    state["pistas"] += 3
    pegar("fotografia antiga")

    mostrar("""
No porão existe uma caixa escondida.

Dentro dela há uma fotografia antiga.

No verso está escrito:

"Aquilo que está abaixo da ilha nunca deve ser despertado."

O segredo parece estar relacionado às cavernas.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase9)


# =========================================================
# FASE 8
# =========================================================

def fase8(event=None):
    preparar(8)

    state["pistas"] += 3
    pegar("fotografia da criatura")

    mostrar("""
🔦 O FAROL

O farol abandonado fica no alto de uma região rochosa.

Milo conhece o caminho e acompanha vocês.

No topo existe uma caixa antiga.

Dentro dela há uma fotografia.

Ao fundo aparece uma figura estranha.

Barbara fica assustada.

— Então as histórias podem ser verdadeiras.
""")

    atualizar_status()
    criar_botao("🌙 Continuar", fase9)


# =========================================================
# FASE 9
# =========================================================

def fase9(event=None):
    preparar(9)

    mostrar("""
🌙 A PRIMEIRA NOITE

A investigação demora mais do que esperavam.

A noite chega.

Milo e Barbara levam vocês para uma casa segura na vila.

Durante a madrugada, alguém bate na janela.

TOC.

TOC.

TOC.

Milo pede para ninguém abrir.

O que você faz?
""")

    criar_botao("🪟 Abrir a janela", fase9_janela)
    criar_botao("😶 Ignorar", fase9_ignorar)


def fase9_janela(event):
    perder_sanidade()
    state["pistas"] += 2

    mostrar("""
Você abre a janela.

Não há ninguém.

Mas existem marcas profundas no chão.

Milo reconhece as marcas.

— Eu já vi isso antes.

Barbara olha para a floresta.

— Então ela voltou.
""")

    criar_botao("🌅 Continuar", fase10)


def fase9_ignorar(event):
    state["pistas"] += 1

    mostrar("""
Vocês decidem ignorar as batidas.

Quando amanhece, encontram marcas no chão perto da casa.

Alguma coisa esteve ali durante a noite.
""")

    criar_botao("🌅 Continuar", fase10)


# =========================================================
# FASE 10
# =========================================================

def fase10(event=None):
    preparar(10)

    mostrar("""
🚨 O DESAPARECIMENTO

Na manhã seguinte, um morador desaparece.

Milo conhece o homem.

Barbara começa a procurar informações.

As marcas encontradas durante a noite podem estar relacionadas
ao desaparecimento.

Vocês precisam investigar.
""")

    criar_botao("🏘️ Procurar na vila", fase10_vila)
    criar_botao("🌲 Procurar na floresta", fase10_floresta)


def fase10_vila(event):
    state["pistas"] += 1

    mostrar("""
Vocês procuram pela vila.

Encontram marcas no chão.

Elas seguem para fora da vila.

Milo aponta para a floresta.

— Ele provavelmente foi para lá.
""")

    criar_botao("🔎 Continuar", fase11)


def fase10_floresta(event):
    state["pistas"] += 2

    mostrar("""
Vocês seguem as marcas diretamente para a floresta.

As pegadas parecem recentes.

Barbara encontra um objeto no caminho.

Talvez pertença ao homem desaparecido.
""")

    criar_botao("🔎 Continuar", fase11)


# =========================================================
# FASE 11
# =========================================================

def fase11(event=None):
    preparar(11)

    pegar("objeto do desaparecido")
    state["pistas"] += 2

    mostrar("""
🔎 A INVESTIGAÇÃO

As marcas continuam pela floresta.

Depois de algum tempo vocês encontram um objeto pertencente
ao desaparecido.

Milo reconhece.

— Isso é dele.

A trilha continua em direção a uma região mais afastada.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase12)


# =========================================================
# FASE 12
# =========================================================

def fase12(event=None):
    preparar(12)

    mostrar("""
🌲 A FLORESTA

Milo lidera o grupo.

Como mora na ilha desde criança, ele conhece muitos dos caminhos.

Uma trilha escondida leva até uma pequena cabana.

Vocês decidem investigar.
""")

    criar_botao("🥾 Seguir a trilha", fase13)


# =========================================================
# FASE 13
# =========================================================

def fase13(event=None):
    preparar(13)

    mostrar("""
🔥 O ACAMPAMENTO

A noite chega antes que vocês consigam voltar.

O grupo monta um pequeno acampamento.

Milo conta histórias que ouviu do avô.

Barbara explica que os símbolos antigos podem estar relacionados
à criatura.

Todos percebem que estão cada vez mais perto da verdade.
""")

    criar_botao("🌅 Continuar", fase14)


# =========================================================
# FASE 14
# =========================================================

def fase14(event=None):
    preparar(14)

    state["pistas"] += 2

    mostrar("""
🐾 AS PEGADAS

Na manhã seguinte, novas pegadas aparecem.

Elas são muito maiores que pegadas humanas.

Milo observa.

— Elas vão naquela direção.

Uma pequena cabana aparece entre as árvores.

Vocês seguem até lá.
""")

    atualizar_status()
    criar_botao("🏚️ Ir para a cabana", fase15)


# =========================================================
# FASE 15
# =========================================================

def fase15(event=None):
    preparar(15)

    pegar("diário")
    state["pistas"] += 3

    mostrar("""
📖 A CABANA

Dentro da cabana existem mapas e livros antigos.

Barbara encontra um diário.

Ele fala sobre uma criatura escondida nas profundezas da ilha.

Também menciona um símbolo capaz de enfraquecê-la.

Agora vocês possuem uma pista muito importante.
""")

    atualizar_status()
    criar_botao("📖 Ler o diário", fase16)


# =========================================================
# FASE 16
# =========================================================

def fase16(event=None):
    preparar(16)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
📖 O DIÁRIO

O diário revela que antigos moradores descobriram uma criatura
nas profundezas da ilha.

Eles descobriram que um símbolo antigo podia enfraquecê-la.

O símbolo foi escondido.

A última anotação diz que alguém da família precisaria
encontrar o símbolo novamente.

Talvez vocês sejam essa pessoa.
""")

    atualizar_status()
    criar_botao("🎒 Preparar equipamentos", fase17)


# =========================================================
# FASE 17
# =========================================================

def fase17(event=None):
    preparar(17)

    mostrar("""
🎒 PREPARAÇÃO

Agora vocês sabem que a criatura existe.

Antes de continuar, o grupo organiza tudo o que encontrou
durante a investigação.

Milo verifica os equipamentos.

Barbara revisa as pistas.

Vocês precisam decidir o que levar.
""")

    criar_botao("🎒 Organizar equipamentos", fase17_equipamentos)
    criar_botao("🔱 Preparar o símbolo", fase17_simbolo)


def fase17_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
Vocês organizam os equipamentos.

Milo verifica tudo.

Barbara guarda as pistas mais importantes.

O grupo está mais preparado.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase18)


def fase17_simbolo(event):
    pegar("símbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 3

    mostrar("""
Entre os objetos antigos vocês encontram o símbolo original.

Barbara reconhece o desenho.

— É exatamente o símbolo descrito no diário.

Milo percebe que ele pode ser a chave para enfrentar a criatura.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase18)


# =========================================================
# FASE 18
# =========================================================

def fase18(event=None):
    preparar(18)

    mostrar("""
🌊 O LAGO

As pistas levam vocês até um lago.

Perto da margem existe um pequeno cristal.

Barbara percebe que ele reage ao símbolo.

O cristal pode ser importante.
""")

    criar_botao("🔎 Pegar o cristal", fase18_cristal)
    criar_botao("➡️ Continuar", fase19)


def fase18_cristal(event):
    pegar("cristal")
    state["pistas"] += 2

    mostrar("""
Você pega o cristal.

Ele reage imediatamente ao símbolo antigo.

Uma luz percorre as paredes próximas.

A conexão entre o cristal e a criatura parece cada vez mais clara.
""")

    atualizar_status()
    criar_botao("🕳️ Continuar", fase19)


# =========================================================
# FASE 19
# =========================================================

def fase19(event=None):
    preparar(19)

    mostrar("""
🕳️ A CAVERNA

O caminho termina diante de uma enorme caverna.

Milo reconhece o lugar.

— Meu avô falava dessa caverna.

Nas paredes existem os mesmos símbolos encontrados na igreja.

Vocês entram.
""")

    criar_botao("🚪 Entrar na caverna", fase20)


# =========================================================
# FASE 20
# =========================================================

def fase20(event=None):
    preparar(20)

    perder_sanidade()

    mostrar("""
👹 O PRIMEIRO ENCONTRO

Um som estranho ecoa pela caverna.

Uma enorme silhueta aparece no fim do corredor.

Barbara reconhece os símbolos nas paredes.

Milo entende o que está acontecendo.

— A criatura existe.

Vocês ainda não estão preparados.

Precisam fugir e descobrir como enfrentá-la.
""")

    criar_botao("🏃 Fugir", fase21)


# =========================================================
# FASE 21
# =========================================================

def fase21(event=None):
    preparar(21)

    mostrar("""
🏃 A FUGA

O grupo corre pelos corredores.

Milo usa seu conhecimento da ilha para encontrar uma saída.

Depois de algum tempo vocês conseguem escapar.

Agora precisam descobrir a verdadeira fraqueza da criatura.
""")

    criar_botao("🔎 Descobrir a fraqueza", fase22)


# =========================================================
# FASE 22
# =========================================================

def fase22(event=None):
    preparar(22)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
🔎 A FRAQUEZA

Depois de comparar o diário, o símbolo e o cristal,
Barbara entende a mensagem.

A criatura pode ser enfraquecida.

O símbolo original é a chave.

Milo respira fundo.

— Então podemos tentar.

Vocês voltam para o esconderijo.
""")

    atualizar_status()
    criar_botao("🏚️ Ir para o esconderijo", fase23)


# =========================================================
# FASE 23
# =========================================================

def fase23(event=None):
    preparar(23)

    mostrar("""
🏚️ O ESCONDERIJO

As pistas levam vocês para uma região subterrânea.

Ali existem documentos antigos e inscrições.

Tudo indica que aquele lugar foi usado para esconder
informações sobre a criatura.

Uma grande porta está no final do corredor.

O segredo está atrás dela.
""")

    criar_botao("🚪 Abrir a porta", fase24)


# =========================================================
# FASE 24
# =========================================================

def fase24(event=None):
    preparar(24)

    mostrar("""
🆘 O RESGATE

Antes de chegar à sala principal, vocês encontram
o morador desaparecido.

Milo corre para ajudá-lo.

O homem explica que foi levado para a caverna.

Ele conseguiu escapar e encontrou aquele esconderijo.

— Ela está acordada — ele avisa.

Vocês precisam continuar.
""")

    criar_botao("🚶 Levar o homem embora", fase25)


# =========================================================
# FASE 25
# =========================================================

def fase25(event=None):
    preparar(25)

    state["pistas"] += 1

    mostrar("""
🚪 A ENTRADA

Milo ajuda o homem a sair.

Barbara encontra uma passagem segura.

Depois disso, vocês voltam para a entrada principal
do esconderijo.

Uma grande porta de pedra bloqueia o caminho.

No centro existe um símbolo.

Se vocês tiverem o símbolo antigo, a porta poderá ser aberta.
""")

    if "símbolo antigo" in state["inv"]:
        mostrar("""
O símbolo se encaixa perfeitamente.

A porta começa a abrir.

Uma passagem escura aparece.

Vocês estão muito perto do segredo.
""")
    else:
        mostrar("""
Vocês não possuem o símbolo original.

Mesmo assim conseguem encontrar uma passagem lateral.

Agora precisam continuar com cuidado.
""")

    criar_botao("🚪 Entrar", fase26)


# =========================================================
# FASE 26
# =========================================================

def fase26(event=None):
    preparar(26)

    state["pistas"] += 3

    mostrar("""
📜 O PASSADO

Dentro do esconderijo vocês encontram documentos.

Eles confirmam que o parente de Olivier ou Amelie esteve na ilha.

Ele descobriu a criatura e tentou impedir que ela voltasse
a ameaçar os moradores.

Uma anotação diz:

"Se alguém da minha família encontrar este lugar,
precisará terminar o que comecei."

Agora vocês entendem por que os documentos foram escondidos.
""")

    atualizar_status()
    criar_botao("⚔️ Continuar", fase27)


# =========================================================
# FASE 27
# =========================================================

def fase27(event=None):
    preparar(27)

    mostrar("""
⚔️ A PREPARAÇÃO FINAL

A criatura está próxima.

Milo e Barbara estão prontos para ajudar.

O símbolo antigo pode ser usado para enfraquecê-la.

O grupo se prepara para o confronto final.
""")

    criar_botao("🔱 Preparar o símbolo", fase27_simbolo)
    criar_botao("🎒 Organizar equipamentos", fase27_equipamentos)


def fase27_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["batalha"] += 3
        state["monstro_fraqueza"] = True

        mostrar("""
O símbolo começa a reagir.

O cristal brilha.

Barbara percebe que a criatura está sendo afetada
mesmo antes do confronto.

Vocês estão preparados.
""")
    else:
        mostrar("""
Vocês não conseguiram encontrar o símbolo original.

Mesmo assim precisam continuar.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase28)


def fase27_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    mostrar("""
Vocês organizam os equipamentos.

Milo verifica tudo.

Barbara guarda as pistas.

Agora o grupo está pronto.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase28)


# =========================================================
# FASE 28
# =========================================================

def fase28(event=None):
    preparar(28)

    mostrar("""
👹 O MONSTRO

O grupo chega à última sala.

A criatura está diante de vocês.

Os símbolos cobrem as paredes.

Milo reconhece o local.

— É aqui que tudo começou.

Barbara segura o símbolo.

Agora chegou a hora de decidir como enfrentar a criatura.
""")

    criar_botao("⚔️ Preparar o confronto", fase29)


# =========================================================
# FASE 29
# =========================================================

def fase29(event=None):
    preparar(29)

    mostrar("""
⚔️ O CONFRONTO

A criatura avança.

O símbolo pode ser usado para enfraquecê-la.

Milo e Barbara ajudam vocês.

Escolha uma estratégia.
""")

    criar_botao("🔱 Ativar o símbolo", fase29_simbolo)
    criar_botao("🛡️ Ajudar Milo", fase29_milo)
    criar_botao("🛡️ Ajudar Barbara", fase29_barbara)
    criar_botao("🏃 Recuar", fase29_recuar)


def fase29_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["batalha"] += 4
        state["monstro_fraqueza"] = True

        mostrar("""
Você ativa o símbolo antigo.

As paredes brilham.

A criatura perde força.

Milo grita:

— Continue!

A estratégia está funcionando.
""")
    else:
        perder_sanidade()

        mostrar("""
Você tenta ativar o símbolo, mas percebe que não o possui.

A criatura continua avançando.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase30)


def fase29_milo(event):
    state["confianca_milo"] += 2
    state["batalha"] += 2

    mostrar("""
Você ajuda Milo.

Ele reconhece uma inscrição antiga.

A descoberta ajuda o grupo a entender
como utilizar os símbolos.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase30)


def fase29_barbara(event):
    state["confianca_barbara"] += 2
    state["batalha"] += 2

    mostrar("""
Você ajuda Barbara.

Ela encontra uma inscrição escondida.

A informação confirma a fraqueza da criatura.

Agora vocês sabem o que fazer.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase30)


def fase29_recuar(event):
    perder_vida()

    mostrar("""
Vocês recuam.

A criatura avança.

Milo e Barbara ajudam o grupo a se reorganizar.

Agora não existe mais tempo para fugir da decisão.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase30)


# =========================================================
# FASE 30 — ESCOLHA DOS FINAIS
# =========================================================

def fase30(event=None):
    limpar()
    atualizar_status()

    mostrar("""
🔥 A ÚLTIMA ESCOLHA

A criatura está diante de vocês.

Depois de toda a investigação,
o segredo da ilha finalmente foi descoberto.

Agora você precisa tomar uma decisão.

Qual será?
""")

    criar_botao("⚔️ Derrotar o monstro", final_derrotar)
    criar_botao("🔒 Selar o monstro novamente", final_selar)
    criar_botao("🏃 Fugir da ilha", final_fugir)


# =========================================================
# FINAL 1 — DERROTAR
# =========================================================

def final_derrotar(event):
    state["escolheu_derrotar"] = True
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    if state["monstro_fraqueza"] and state["batalha"] >= 5:
        state["monstro_derrotado"] = True
    else:
        state["monstro_derrotado"] = False

    mostrar_final()


# =========================================================
# FINAL 3 — SELAR
# =========================================================

def final_selar(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = True
    state["escolheu_fugir"] = False
    state["monstro_derrotado"] = False

    mostrar_final()


# =========================================================
# FINAL 4 — FUGIR
# =========================================================

def final_fugir(event):
    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = True
    state["monstro_derrotado"] = False

    mostrar_final()


# =========================================================
# MOSTRAR O FINAL CORRETO
# =========================================================

def mostrar_final():
    limpar()
    atualizar_status()

    if state["escolheu_derrotar"] and state["monstro_derrotado"]:

        mostrar_imagem_final("final_01.png")

        mostrar("""
🌟 FINAL 1 — O MONSTRO FOI DERROTADO

O símbolo antigo começa a brilhar.

As inscrições da sala se iluminam.

A criatura perde completamente sua força.

Milo e Barbara permanecem ao lado de vocês.

Depois de tantos anos, o segredo da ilha finalmente chega ao fim.

Os documentos provam que o parente de Olivier ou Amelie
tentou proteger a ilha no passado.

Agora a verdade pode finalmente ser revelada.

🏝️ A ilha está livre da criatura.
""")

    elif state["escolheu_derrotar"]:

        mostrar_imagem_final("final_02.png")

        mostrar("""
🌅 FINAL 2 — A VITÓRIA INCOMPLETA

Vocês tentam derrotar a criatura.

A estratégia funciona parcialmente,
mas não é suficiente.

A criatura recua para as profundezas.

Milo consegue levar todos para um lugar seguro.

Vocês sobreviveram.

Mas o segredo ainda não terminou.

A criatura continua escondida.

Talvez um dia alguém consiga terminar
o que vocês começaram.
""")

    elif state["escolheu_selar"]:

        mostrar_imagem_final("final_03.png")

        mostrar("""
🔒 FINAL 3 — O SELAMENTO

Vocês decidem não destruir a criatura.

Barbara ativa os símbolos antigos.

Milo ajuda a manter o grupo seguro.

A passagem começa a se fechar.

A criatura desaparece novamente nas profundezas.

O segredo continua escondido.

A ilha está segura...

por enquanto.
""")

    elif state["escolheu_fugir"]:

        mostrar_imagem_final("final_06.png")

        mostrar("""
🏃 FINAL 4 — A FUGA

Vocês decidem abandonar a ilha.

Milo conhece o caminho de volta.

Barbara ajuda o grupo a chegar ao barco.

Olivier ou Amelie leva os documentos encontrados.

A ilha fica para trás.

Milo e Barbara permanecem lá,
porque aquela é a casa deles.

Vocês sobreviveram.

Mas nunca descobriram toda a verdade.

O segredo da ilha continua.
""")

    mostrar("""
🎮 FIM DO JOGO

Obrigado por jogar O Segredo na Ilha!
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

    state["escolheu_derrotar"] = False
    state["escolheu_selar"] = False
    state["escolheu_fugir"] = False

    state["batalha"] = 0

    fase1()


# =========================================================
# INICIAR O JOGO
# =========================================================

fase1()
