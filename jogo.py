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

Tudo começa com uma viagem.

Olivier e Amelie estão em um barco seguindo em direção
a uma pequena ilha cercada pelo mar.

Os dois decidiram ir até lá por causa de documentos
antigos relacionados à família.

Entre os documentos existe uma história sobre um parente
que desapareceu misteriosamente muitos anos atrás.

Enquanto o barco se aproxima da ilha, a paisagem começa
a mudar.

A ilha parece tranquila, mas existe alguma coisa estranha
naquele lugar.

Agora você precisa escolher quem será o personagem
principal da história.
""")

    criar_botao("👨 Olivier", escolher_olivier)
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
🚢 A VIAGEM DE BARCO

Você escolheu jogar como """ + state["personagem"] + """.

O barco continua avançando pelo mar.

Amelie e Olivier observam a ilha ficando cada vez maior
no horizonte.

O vento sopra forte e o barco balança levemente.

Nenhum dos dois sabe exatamente o que encontrará quando
chegar lá.

Os documentos antigos mencionavam a ilha, mas muitas
informações estavam incompletas.

Depois de algum tempo, finalmente é possível enxergar
o pequeno porto.

A viagem está chegando ao fim.

Vocês estão prestes a pisar na ilha.
""")

    criar_botao("🏝️ Continuar até a ilha", fase3)


# =========================================================
# FASE 3
# =========================================================

def fase3(event=None):
    preparar(3)

    mostrar("""
🏝️ A CHEGADA

O barco finalmente chega à ilha.

Olivier e Amelie desembarcam no pequeno porto.

A ilha parece tranquila.

Casas antigas aparecem ao longe e uma pequena vila
fica próxima da praia.

Duas pessoas estão esperando por vocês.

São Milo e Barbara.

Ao contrário de Olivier e Amelie, Milo e Barbara já
moram na ilha há bastante tempo.

Eles conhecem a vila, as trilhas, o farol, a floresta
e as histórias antigas daquele lugar.

Milo se aproxima.

— Vocês finalmente chegaram.

Barbara observa os documentos que vocês trouxeram.

— Vieram procurar respostas sobre a família, não é?

A investigação começa.
""")

    criar_botao("🗣️ Conversar com Milo", fase4_milo)
    criar_botao("🗣️ Conversar com Barbara", fase4_barbara)


def fase4_milo(event):
    state["confianca_milo"] += 1
    state["pistas"] += 1
    fase4()


def fase4_barbara(event):
    state["confianca_barbara"] += 1
    state["pistas"] += 1
    fase4()


# =========================================================
# FASE 4
# =========================================================

def fase4(event=None):
    preparar(4)

    mostrar("""
🏘️ A VILA

Milo e Barbara mostram a vila para vocês.

Eles explicam que a ilha possui vários lugares antigos
que quase ninguém visita mais.

Existe uma igreja abandonada.

Existe uma casa que ficou vazia depois que o antigo
morador desapareceu.

E existe um velho farol no alto das pedras.

Segundo Milo, todos esses lugares possuem alguma ligação
com o passado da ilha.

Barbara acredita que os documentos da família podem
ajudar a descobrir a verdade.

Por onde vocês vão começar?
""")

    criar_botao("⛪ Ir para a igreja", fase5)
    criar_botao("🏚️ Ir para a casa abandonada", fase6)
    criar_botao("🔦 Ir para o farol", fase7)


# =========================================================
# FASE 5
# =========================================================

def fase5(event=None):
    preparar(5)

    mostrar("""
⛪ A IGREJA ABANDONADA

A igreja está abandonada há muitos anos.

Milo explica que quase ninguém entra ali.

Barbara percebe vários símbolos desenhados nas paredes.

Alguns deles parecem muito antigos.

Ela reconhece alguns símbolos porque sua família já havia
contado histórias sobre eles.

Existe alguma coisa escondida naquele lugar.

O que vocês procuram?
""")

    criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
    criar_botao("📖 Procurar documentos", fase5_documentos)


def fase5_simbolos(event):
    state["pistas"] += 2
    pegar("fotografia dos símbolos")

    limpar()

    mostrar("""
🔎 OS SÍMBOLOS

Barbara observa cuidadosamente os desenhos.

Alguns símbolos parecem formar um caminho.

Milo percebe que determinados sinais apontam para
a direção da floresta.

Você tira uma fotografia para poder analisar os símbolos
mais tarde.

Talvez essa seja uma das pistas deixadas pelos antigos
moradores da ilha.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase8)


def fase5_documentos(event):
    state["pistas"] += 3
    pegar("livro antigo")

    limpar()

    mostrar("""
📖 O LIVRO ANTIGO

Atrás de um banco velho vocês encontram um livro.

As páginas estão amareladas e algumas palavras estão
quase apagadas.

O livro fala sobre uma criatura que estaria escondida
nas profundezas da ilha.

Uma das páginas menciona um símbolo capaz de enfraquecer
a criatura.

Essa descoberta pode ser muito importante.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase8)


# =========================================================
# FASE 6
# =========================================================

def fase6(event=None):
    preparar(6)

    mostrar("""
🏚️ A CASA ABANDONADA

Milo leva vocês até uma casa abandonada.

Segundo ele, o antigo morador desapareceu muitos anos
atrás e nunca voltou.

Dentro da casa existem móveis velhos, fotografias,
documentos e objetos cobertos de poeira.

Alguma coisa ali pode explicar o passado da ilha.
""")

    criar_botao("📄 Procurar documentos", fase6_documentos)
    criar_botao("⬆️ Subir as escadas", fase6_escadas)
    criar_botao("⬇️ Investigar o porão", fase6_porao)


def fase6_documentos(event):
    state["pistas"] += 3
    pegar("documentos da família")

    limpar()

    mostrar("""
📄 OS DOCUMENTOS

Entre os documentos antigos aparece o sobrenome da família.

Barbara fica surpresa.

— Então sua família realmente esteve aqui.

Os papéis mostram que alguém da família esteve envolvido
com os acontecimentos misteriosos da ilha.

Agora existe uma ligação clara entre vocês e o passado.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase8)


def fase6_escadas(event):
    state["pistas"] += 2
    pegar("fotografia antiga")

    limpar()

    mostrar("""
📸 A FOTOGRAFIA

No andar de cima vocês encontram uma fotografia antiga.

Ela mostra algumas pessoas diante da floresta.

Uma delas parece ser o parente desaparecido.

Milo observa a fotografia por alguns segundos.

— Eu conheço esse lugar.

A fotografia pode indicar o próximo destino.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase8)


def fase6_porao(event):
    state["pistas"] += 3
    pegar("fotografia antiga")

    limpar()

    mostrar("""
🕯️ O PORÃO

No porão existe uma caixa escondida.

Dentro dela há uma fotografia antiga.

No verso está escrito:

"Aquilo que está abaixo da ilha nunca deve ser despertado."

O aviso deixa todos em silêncio.

Barbara acredita que a mensagem pode estar relacionada
às cavernas da ilha.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase8)


# =========================================================
# FASE 7
# =========================================================

def fase7(event=None):
    preparar(7)

    state["pistas"] += 3
    pegar("fotografia da criatura")

    mostrar("""
🔦 O FAROL

O farol abandonado fica no alto de uma região rochosa.

Milo conhece o caminho e acompanha vocês.

No topo existe uma caixa antiga.

Dentro dela existe uma fotografia estranha.

Ao fundo aparece uma figura que ninguém consegue
identificar direito.

Barbara fica preocupada.

— Então as histórias podem ser verdadeiras.

A fotografia é mais uma pista.
""")

    atualizar_status()
    criar_botao("🌙 Continuar", fase8)


# =========================================================
# FASE 8
# =========================================================

def fase8(event=None):
    preparar(8)

    mostrar("""
🌙 A PRIMEIRA NOITE

A investigação demora mais do que vocês esperavam.

Quando a noite chega, Milo e Barbara levam vocês
para uma casa segura na vila.

Durante a madrugada, alguém bate na janela.

TOC.

TOC.

TOC.

Milo pede para ninguém abrir.

O que você faz?
""")

    criar_botao("🪟 Abrir a janela", fase8_janela)
    criar_botao("😶 Ignorar", fase8_ignorar)


def fase8_janela(event):
    perder_sanidade()
    state["pistas"] += 2

    limpar()

    mostrar("""
🪟 A JANELA

Você abre a janela.

Não existe ninguém do lado de fora.

Porém, existem marcas profundas no chão.

Milo observa as marcas.

— Eu já vi isso antes.

Barbara olha para a floresta.

— Então ela voltou.

Ninguém sabe exatamente o que deixou aquelas marcas.
""")

    atualizar_status()
    criar_botao("🌅 Continuar", fase9)


def fase8_ignorar(event):
    state["pistas"] += 1

    limpar()

    mostrar("""
😶 O SILÊNCIO

Vocês decidem não abrir a janela.

Quando amanhece, encontram marcas no chão perto da casa.

Alguma coisa esteve ali durante a noite.

Milo acredita que as marcas podem estar relacionadas
ao mistério que vocês estão investigando.
""")

    atualizar_status()
    criar_botao("🌅 Continuar", fase9)


# =========================================================
# FASE 9
# =========================================================

def fase9(event=None):
    preparar(9)

    mostrar("""
🚨 O DESAPARECIMENTO

Na manhã seguinte, um morador da ilha desaparece.

Milo conhece o homem e fica preocupado.

Barbara começa a procurar informações.

As marcas encontradas durante a noite podem estar
relacionadas ao desaparecimento.

Vocês precisam descobrir para onde ele foi.
""")

    criar_botao("🏘️ Procurar na vila", fase9_vila)
    criar_botao("🌲 Procurar na floresta", fase9_floresta)


def fase9_vila(event):
    state["pistas"] += 1

    limpar()

    mostrar("""
🏘️ A VILA

Vocês procuram pela vila.

Depois de algum tempo encontram marcas no chão.

As marcas seguem para fora da vila.

Milo aponta para a floresta.

— Ele provavelmente foi para lá.

A investigação continua.
""")

    atualizar_status()
    criar_botao("🔎 Continuar", fase10)


def fase9_floresta(event):
    state["pistas"] += 2

    limpar()

    mostrar("""
🌲 A FLORESTA

Vocês seguem as marcas diretamente para a floresta.

As pegadas parecem recentes.

Barbara encontra um objeto no caminho.

Talvez ele pertença ao morador desaparecido.

Vocês decidem continuar seguindo a trilha.
""")

    atualizar_status()
    criar_botao("🔎 Continuar", fase10)


# =========================================================
# FASE 10
# =========================================================

def fase10(event=None):
    preparar(10)

    pegar("objeto do desaparecido")
    state["pistas"] += 2

    mostrar("""
🔎 A INVESTIGAÇÃO

As marcas continuam pela floresta.

Depois de algum tempo vocês encontram um objeto
pertencente ao morador desaparecido.

Milo reconhece o objeto imediatamente.

— Isso é dele.

A trilha continua em direção a uma região mais afastada.

Vocês decidem seguir.
""")

    atualizar_status()
    criar_botao("🌲 Continuar", fase11)


# =========================================================
# FASE 11
# =========================================================

def fase11(event=None):
    preparar(11)

    mostrar("""
🌲 A FLORESTA

Milo lidera o grupo.

Como mora na ilha desde criança, ele conhece muitos
dos caminhos escondidos.

Uma trilha estreita aparece entre as árvores.

No final dela existe uma pequena cabana.

Talvez o desaparecido tenha passado por lá.

Vocês se aproximam.
""")

    criar_botao("🥾 Seguir a trilha", fase12)


# =========================================================
# FASE 12
# =========================================================

def fase12(event=None):
    preparar(12)

    mostrar("""
🔥 O ACAMPAMENTO

A noite chega antes que vocês consigam voltar.

O grupo decide montar um pequeno acampamento.

Milo conta histórias que ouviu de seu avô sobre a ilha.

Barbara explica que os símbolos antigos podem estar
relacionados à criatura.

Todos percebem que estão cada vez mais perto da verdade.

Mas ninguém sabe o que encontrará quando chegar
às profundezas da ilha.
""")

    criar_botao("🌅 Continuar", fase13)


# =========================================================
# FASE 13
# =========================================================

def fase13(event=None):
    preparar(13)

    state["pistas"] += 2

    mostrar("""
🐾 AS PEGADAS

Na manhã seguinte, novas pegadas aparecem perto
do acampamento.

Elas são muito maiores do que pegadas humanas.

Milo observa atentamente.

— Elas vão naquela direção.

Entre as árvores aparece uma pequena cabana.

Vocês seguem as pegadas até lá.
""")

    atualizar_status()
    criar_botao("🏚️ Ir para a cabana", fase14)


# =========================================================
# FASE 14
# =========================================================

def fase14(event=None):
    preparar(14)

    pegar("diário")
    state["pistas"] += 3

    mostrar("""
📖 A CABANA

Dentro da cabana existem mapas, livros e objetos antigos.

Barbara encontra um diário.

As anotações falam sobre uma criatura escondida
nas profundezas da ilha.

Também existe uma referência a um símbolo capaz
de enfraquecê-la.

Agora vocês possuem uma pista muito importante.

O diário pode revelar o que aconteceu no passado.
""")

    atualizar_status()
    criar_botao("📖 Ler o diário", fase15)


# =========================================================
# FASE 15
# =========================================================

def fase15(event=None):
    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
📖 O DIÁRIO

O diário revela que antigos moradores descobriram
uma criatura nas profundezas da ilha.

Eles tentaram impedir que ela chegasse à superfície.

Depois de muito tempo, descobriram que um símbolo antigo
era capaz de enfraquecer a criatura.

O símbolo foi escondido para que ninguém pudesse
usá-lo de maneira errada.

A última anotação diz que alguém da família precisaria
encontrar o símbolo novamente.

Talvez vocês tenham chegado à ilha justamente para isso.
""")

    atualizar_status()
    criar_botao("🎒 Preparar equipamentos", fase16)


# =========================================================
# FASE 16
# =========================================================

def fase16(event=None):
    preparar(16)

    mostrar("""
🎒 PREPARAÇÃO

Agora vocês sabem que a criatura existe.

Antes de continuar, o grupo organiza tudo o que encontrou.

Milo verifica os equipamentos.

Barbara revisa as pistas.

O símbolo pode ser a chave para enfrentar a criatura.

Vocês precisam decidir o que preparar.
""")

    criar_botao("🎒 Organizar equipamentos", fase16_equipamentos)
    criar_botao("🔱 Procurar o símbolo", fase16_simbolo)


def fase16_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    limpar()

    mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam os equipamentos encontrados.

Milo verifica tudo cuidadosamente.

Barbara guarda as pistas mais importantes.

O grupo está mais preparado para continuar.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase17)


def fase16_simbolo(event):
    pegar("símbolo antigo")
    state["monstro_fraqueza"] = True
    state["batalha"] += 3

    limpar()

    mostrar("""
🔱 O SÍMBOLO ANTIGO

Entre os objetos antigos vocês encontram um símbolo.

Barbara reconhece imediatamente o desenho.

— É exatamente o símbolo descrito no diário.

Milo percebe que ele pode ser a chave para enfrentar
a criatura.

Agora vocês possuem uma das coisas mais importantes
da investigação.
""")

    atualizar_status()
    criar_botao("🌊 Continuar", fase17)


# =========================================================
# FASE 17
# =========================================================

def fase17(event=None):
    preparar(17)

    mostrar("""
🌊 O LAGO

As pistas levam vocês até um lago escondido.

Perto da margem existe um pequeno cristal.

Barbara percebe que o cristal reage ao símbolo antigo.

Talvez ele tenha alguma relação com a criatura.

O que vocês fazem?
""")

    criar_botao("🔎 Pegar o cristal", fase17_cristal)
    criar_botao("➡️ Continuar", fase18)


def fase17_cristal(event):
    pegar("cristal")
    state["pistas"] += 2

    limpar()

    mostrar("""
💎 O CRISTAL

Você pega o cristal.

Ele reage imediatamente ao símbolo antigo.

Uma luz percorre as pedras próximas.

Barbara observa surpresa.

— O cristal e o símbolo estão conectados.

A ligação entre os objetos e a criatura parece cada
vez mais clara.
""")

    atualizar_status()
    criar_botao("🕳️ Continuar", fase18)


# =========================================================
# FASE 18
# =========================================================

def fase18(event=None):
    preparar(18)

    mostrar("""
🕳️ A CAVERNA

O caminho termina diante de uma enorme caverna.

Milo reconhece o lugar.

— Meu avô falava dessa caverna.

Nas paredes existem os mesmos símbolos encontrados
na igreja.

A entrada parece levar para o interior da ilha.

Vocês respiram fundo e entram.
""")

    criar_botao("🚪 Entrar na caverna", fase19)


# =========================================================
# FASE 19
# =========================================================

def fase19(event=None):
    preparar(19)

    perder_sanidade()

    mostrar("""
👹 O PRIMEIRO ENCONTRO

Um som estranho ecoa pela caverna.

O grupo para.

Uma enorme silhueta aparece no fim do corredor.

Barbara reconhece os símbolos nas paredes.

Milo finalmente entende o que está acontecendo.

— A criatura existe.

Vocês percebem que ainda não estão preparados.

A única opção é fugir e descobrir como enfrentá-la.
""")

    criar_botao("🏃 Fugir", fase20)


# =========================================================
# FASE 20
# =========================================================

def fase20(event=None):
    preparar(20)

    mostrar("""
🏃 A FUGA

O grupo corre pelos corredores da caverna.

Milo usa seu conhecimento da ilha para encontrar
uma saída.

Depois de algum tempo vocês conseguem escapar.

Todos estão cansados, mas conseguiram sair.

Agora vocês sabem que a criatura realmente existe.

E precisam descobrir sua verdadeira fraqueza.
""")

    criar_botao("🔎 Descobrir a fraqueza", fase21)


# =========================================================
# FASE 21
# =========================================================

def fase21(event=None):
    preparar(21)

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

Agora o grupo sabe que existe uma maneira de enfrentar
a criatura.

Vocês voltam para o esconderijo.
""")

    atualizar_status()
    criar_botao("🏚️ Ir para o esconderijo", fase22)


# =========================================================
# FASE 22
# =========================================================

def fase22(event=None):
    preparar(22)

    mostrar("""
🏚️ O ESCONDERIJO

As pistas levam vocês para uma região subterrânea.

Ali existem documentos antigos e inscrições nas paredes.

Tudo indica que aquele lugar foi usado para esconder
informações sobre a criatura.

Uma grande porta está no final do corredor.

O segredo está atrás dela.
""")

    criar_botao("🚪 Abrir a porta", fase23)


# =========================================================
# FASE 23
# =========================================================

def fase23(event=None):
    preparar(23)

    mostrar("""
🆘 O RESGATE

Antes de chegar à sala principal, vocês encontram
o morador desaparecido.

Milo corre para ajudá-lo.

O homem explica que foi levado para a região subterrânea.

Ele conseguiu escapar e encontrou aquele esconderijo.

— Ela está acordada — ele avisa.

O grupo percebe que não existe mais tempo a perder.

É preciso continuar.
""")

    criar_botao("🚶 Levar o homem para fora", fase24)


# =========================================================
# FASE 24
# =========================================================

def fase24(event=None):
    preparar(24)

    state["pistas"] += 1

    mostrar("""
🚪 A ENTRADA

Milo ajuda o homem a sair.

Barbara encontra uma passagem segura.

Depois disso, vocês voltam para a entrada principal
do esconderijo.

Uma grande porta de pedra bloqueia o caminho.

No centro existe um símbolo.

Se vocês tiverem o símbolo antigo, a porta poderá
ser aberta.
""")

    if "símbolo antigo" in state["inv"]:
        mostrar("""
🔱 O SÍMBOLO

O símbolo se encaixa perfeitamente.

A porta começa a abrir lentamente.

Uma passagem escura aparece.

Vocês estão muito perto do segredo.
""")
    else:
        mostrar("""
⚠️ A PASSAGEM

Vocês não possuem o símbolo original.

Mesmo assim conseguem encontrar uma passagem lateral.

Agora precisam continuar com cuidado.
""")

    criar_botao("🚪 Entrar", fase25)


# =========================================================
# FASE 25
# =========================================================

def fase25(event=None):
    preparar(25)

    state["pistas"] += 3

    mostrar("""
📜 O PASSADO

Dentro do esconderijo vocês encontram documentos antigos.

Eles confirmam que o parente de """ + state["personagem"] + """
esteve na ilha.

Ele descobriu a criatura e tentou impedir que ela voltasse
a ameaçar os moradores.

Uma anotação diz que alguém da família precisaria
terminar o que ele começou.

Agora vocês entendem por que os documentos foram escondidos.

O passado da família está diretamente ligado ao segredo
da ilha.
""")

    atualizar_status()
    criar_botao("⚔️ Continuar", fase26)


# =========================================================
# FASE 26
# =========================================================

def fase26(event=None):
    preparar(26)

    mostrar("""
⚔️ A PREPARAÇÃO FINAL

A criatura está próxima.

Milo e Barbara estão prontos para ajudar.

O símbolo antigo pode ser usado para enfraquecê-la.

O grupo se prepara para o confronto final.

Agora é preciso decidir como se preparar.
""")

    criar_botao("🔱 Preparar o símbolo", fase26_simbolo)
    criar_botao("🎒 Organizar equipamentos", fase26_equipamentos)


def fase26_simbolo(event):
    if "símbolo antigo" in state["inv"]:
        state["batalha"] += 3
        state["monstro_fraqueza"] = True

        limpar()

        mostrar("""
🔱 O SÍMBOLO ESTÁ PRONTO

O símbolo começa a reagir.

O cristal também começa a brilhar.

Barbara percebe que a criatura está sendo afetada
mesmo antes do confronto.

Vocês estão preparados.
""")
    else:
        limpar()

        mostrar("""
⚠️ O SÍMBOLO NÃO FOI ENCONTRADO

Vocês não conseguiram encontrar o símbolo original.

Mesmo assim precisam continuar.

Talvez ainda exista outra maneira de enfrentar
a criatura.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase27)


def fase26_equipamentos(event):
    pegar("equipamento")
    state["batalha"] += 2

    limpar()

    mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam os equipamentos.

Milo verifica tudo.

Barbara guarda as pistas.

Agora o grupo está pronto para enfrentar
o que existe naquela sala.
""")

    atualizar_status()
    criar_botao("👹 Continuar", fase27)


# =========================================================
# FASE 27
# =========================================================

def fase27(event=None):
    preparar(27)

    mostrar("""
👹 O MONSTRO

O grupo chega à última sala.

A criatura está diante de vocês.

Os símbolos cobrem as paredes.

Milo reconhece o local.

— É aqui que tudo começou.

Barbara segura o símbolo.

Depois de tudo o que vocês descobriram,
chegou a hora de enfrentar a criatura.

Mas primeiro é preciso escolher uma estratégia.
""")

    criar_botao("⚔️ Preparar o confronto", fase28)


# =========================================================
# FASE 28
# =========================================================

def fase28(event=None):
    preparar(28)

    mostrar("""
⚔️ O CONFRONTO

A criatura avança.

O símbolo pode ser usado para enfraquecê-la.

Milo e Barbara ajudam vocês.

Cada escolha pode mudar o resultado do confronto.

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

        limpar()

        mostrar("""
🔱 O SÍMBOLO É ATIVADO

Você ativa o símbolo antigo.

As paredes começam a brilhar.

O cristal reage.

A criatura perde parte de sua força.

Milo grita:

— Continue!

A estratégia está funcionando.
""")
    else:
        perder_sanidade()

        limpar()

        mostrar("""
⚠️ O SÍMBOLO NÃO ESTÁ COM VOCÊ

Você tenta ativar o símbolo, mas percebe que não
possui o objeto original.

A criatura continua avançando.

Vocês precisam pensar em outra maneira de continuar.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_milo(event):
    state["confianca_milo"] += 2
    state["batalha"] += 2

    limpar()

    mostrar("""
🛡️ AJUDANDO MILO

Você ajuda Milo a observar as inscrições.

Ele reconhece uma escrita antiga.

A descoberta ajuda o grupo a entender como utilizar
os símbolos.

Milo ganha confiança e continua ajudando vocês.

A criatura ainda está diante do grupo.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_barbara(event):
    state["confianca_barbara"] += 2
    state["batalha"] += 2

    limpar()

    mostrar("""
🛡️ AJUDANDO BARBARA

Você ajuda Barbara a procurar uma inscrição escondida.

Ela encontra uma informação importante.

A descoberta confirma a fraqueza da criatura.

Agora vocês sabem melhor o que fazer.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


def fase28_recuar(event):
    perder_vida()

    limpar()

    mostrar("""
🏃 RECUANDO

Vocês recuam.

A criatura avança.

Milo e Barbara ajudam o grupo a se reorganizar.

Todos percebem que não existe mais tempo para fugir
da decisão.

O confronto final está chegando.
""")

    atualizar_status()
    criar_botao("🔥 Decisão final", fase29)


# =========================================================
# FASE 29
# =========================================================

def fase29(event=None):
    preparar(29)

    mostrar("""
🔥 A ÚLTIMA ESCOLHA

A criatura está diante de vocês.

Depois de toda a investigação, o segredo da ilha
finalmente foi descoberto.

Agora você precisa tomar uma decisão.

O que você fará?
""")

    criar_botao("⚔️ Derrotar o monstro", final_derrotar)
    criar_botao("🔒 Selar o monstro novamente", final_selar)
    criar_botao("🏃 Fugir da ilha", final_fugir)


# =========================================================
# DECISÕES DOS FINAIS
# =========================================================

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


# =========================================================
# FASE 30 — FINAIS
# =========================================================

def fase30(event=None):
    limpar()
    atualizar_status()

    # FINAL 1 — DERROTOU O MONSTRO
    if state["escolheu_derrotar"] and state["monstro_derrotado"]:

        mostrar_imagem_final("final_01.png")

        mostrar("""
🌟 FINAL 1 — O MONSTRO FOI DERROTADO

O símbolo antigo começa a brilhar.

As inscrições da sala se iluminam.

O cristal reage ao símbolo.

A criatura perde completamente sua força.

Milo e Barbara permanecem ao lado de vocês.

Depois de tantos anos, o segredo da ilha finalmente
chega ao fim.

Os documentos provam que o parente de """ + state["personagem"] + """
esteve envolvido com os acontecimentos da ilha.

A verdade finalmente pode ser revelada.

Milo e Barbara continuam na ilha, o lugar que sempre
foi a casa deles.

Olivier e Amelie conseguem voltar levando consigo
as provas encontradas.

🏝️ A ilha está livre da criatura.

✨ VOCÊ CONSEGUIU O MELHOR FINAL!
""")

    # FINAL 2 — TENTOU DERROTAR, MAS NÃO CONSEGUIU
    elif state["escolheu_derrotar"]:

        mostrar_imagem_final("final_02.png")

        mostrar("""
🌅 FINAL 2 — A VITÓRIA INCOMPLETA

Vocês tentam derrotar a criatura.

A estratégia funciona parcialmente.

A criatura perde força, mas não é derrotada.

Milo consegue levar todos para um lugar seguro.

Vocês sobreviveram.

Porém, o segredo ainda não terminou.

A criatura continua escondida nas profundezas.

Talvez algum dia alguém consiga terminar
o que vocês começaram.

A ilha continua guardando seu segredo.
""")

    # FINAL 3 — SELAR
    elif state["escolheu_selar"]:

        mostrar_imagem_final("final_03.png")

        mostrar("""
🔒 FINAL 3 — O SELAMENTO

Vocês decidem não destruir a criatura.

Barbara ativa os símbolos antigos.

Milo ajuda a manter o grupo seguro.

O cristal começa a brilhar.

A passagem começa a se fechar.

A criatura desaparece novamente nas profundezas.

O segredo continua escondido.

A ilha está segura...

por enquanto.

Milo e Barbara decidem continuar vivendo na ilha,
enquanto Olivier e Amelie deixam o local levando
as informações que descobriram.

🏝️ O segredo continua.
""")

    # FINAL 4 — FUGA
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

A criatura continua nas profundezas.

O segredo da ilha continua.
""")

    mostrar("""
🎮 FIM DO JOGO

Obrigado por jogar:

🏝️ O SEGREDO NA ILHA

Cada escolha pode levar a um resultado diferente.
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
# COMEÇAR O JOGO
# =========================================================

fase1()
