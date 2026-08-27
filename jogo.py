from js import document


# ============================================================
# ELEMENTOS DA PÁGINA
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

    "acao_final": ""
}


# ============================================================
# FUNÇÕES DA TELA
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
        f"❤️ Vida: {state['vida']} &nbsp;&nbsp; "
        f"🧠 Sanidade: {state['sanidade']} &nbsp;&nbsp; "
        f"🔎 Pistas: {state['pistas']} &nbsp;&nbsp; "
        f"🎒 Itens: {len(state['inv'])}"
    )


def imagem_fase(numero):
    imagem.src = f"fase_{numero:02d}.png"
    imagem.style.display = "block"


def mudar_imagem(nome):
    imagem.src = nome
    imagem.style.display = "block"


def botao(texto, funcao):
    b = document.createElement("button")
    b.className = "opcao"
    b.innerText = texto
    b.onclick = funcao
    botoes.appendChild(b)


def preparar(numero):
    limpar()
    atualizar_status()

    if numero <= 20:
        imagem_fase(numero)
    else:
        imagem.style.display = "none"


def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)
        atualizar_status()


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


# ============================================================
# FASE 1
# ============================================================

def fase1():

    preparar(1)

    mostrar("""
🏝️ O SEGREDO NA ILHA

Há muitos anos, alguém da sua família desapareceu
sem deixar nenhuma explicação.

Durante muito tempo, todos acreditaram que o caso
jamais seria solucionado.

Até que documentos antigos apareceram.

Entre mapas, fotografias e anotações havia várias
referências a uma pequena ilha afastada do continente.

Tudo indicava que o desaparecimento tinha acontecido ali.

Agora, você decide descobrir a verdade.

Mas existe uma coisa que ninguém contou:

algumas pessoas que foram até a ilha nunca voltaram.

Escolha quem vai enfrentar esse mistério:
""")

    botao("🧑 Olivier", escolher_olivier)
    botao("👩 Amelie", escolher_amelie)


def escolher_olivier(event):
    state["personagem"] = "Olivier"
    fase2()


def escolher_amelie(event):
    state["personagem"] = "Amelie"
    fase2()


# ============================================================
# FASE 2
# ============================================================

def fase2():

    preparar(2)

    mostrar("""
🚢 FASE 2 — A VIAGEM

O barco atravessa um mar cada vez mais agitado.

A ilha surge lentamente no horizonte.

Quanto mais vocês se aproximam, mais silencioso
fica o ambiente.

Milo observa a ilha por alguns segundos.

Milo:
— Finalmente chegamos.

Barbara:
— Eu não gosto desse lugar.

Você pergunta o que há de errado.

Barbara apenas olha para a ilha.

Barbara:
— Algumas coisas são melhores quando continuam escondidas.

Uma sensação estranha percorre você.

Mesmo assim, não há mais como voltar atrás.
""")

    botao("🏝️ Chegar à ilha", fase3)


# ============================================================
# FASE 3
# ============================================================

def fase3():

    preparar(3)

    mostrar("""
🏝️ FASE 3 — A CHEGADA

O barco finalmente chega à vila.

As casas parecem antigas e algumas estão abandonadas.

Milo e Barbara esperam vocês no pequeno porto.

Milo:
— Vocês são os visitantes?

Barbara:
— Eu sabia que alguém acabaria vindo.

Você percebe que os dois parecem saber muito mais
sobre a ilha do que estão contando.

Talvez seja melhor fazer algumas perguntas.
""")

    botao("🔎 Perguntar sobre a ilha", fase3_ilha)
    botao("👨‍👩‍👧 Perguntar sobre sua família", fase3_familia)
    botao("👻 Perguntar sobre desaparecimentos", fase3_desaparecimentos)


def fase3_ilha(event):

    state["confianca_milo"] += 1

    mostrar("""
Milo:
— Durante o dia, a ilha parece tranquila.

Ele olha para a floresta.

Milo:
— Mas quando o sol desaparece, as coisas mudam.

Barbara:
— É por isso que ninguém deve ficar andando por aí
durante a noite.

Você começa a perceber que a ilha possui uma história
que os moradores preferem não contar.
""")

    atualizar_status()
    fase4()


def fase3_familia(event):

    state["pistas"] += 2

    mostrar("""
Barbara fica em silêncio por alguns segundos.

Barbara:
— O sobrenome da sua família é conhecido aqui.

Milo:
— Seu parente esteve nesta ilha muitos anos atrás.

Você pergunta o que aconteceu com ele.

Barbara:
— Ele estava procurando alguma coisa.

Milo:
— E nunca conseguiu voltar.

A resposta deixa ainda mais perguntas do que respostas.
""")

    atualizar_status()
    fase4()


def fase3_desaparecimentos(event):

    state["pistas"] += 1

    mostrar("""
Milo:
— Sim. Pessoas desapareceram.

Barbara:
— Algumas desapareceram há décadas.

Milo:
— Outras desapareceram recentemente.

Você pergunta se existe alguma ligação.

Barbara olha para a floresta.

Barbara:
— Todos encontraram a mesma coisa antes de desaparecer.

Você pergunta o que era.

Ela não responde.
""")

    atualizar_status()
    fase4()


# ============================================================
# FASE 4
# ============================================================

def fase4():

    preparar(4)

    mostrar("""
🏘️ FASE 4 — A VILA

Depois de conversar com Milo e Barbara,
vocês começam a investigar a vila.

Três lugares chamam sua atenção:

⛪ Uma igreja antiga
🏚️ Uma casa abandonada
🔦 Um farol construído perto dos penhascos

Talvez um desses lugares esconda alguma pista
sobre o passado da ilha.

Onde você vai investigar?
""")

    botao("⛪ Ir para a igreja", fase5)
    botao("🏚️ Investigar a casa abandonada", fase6)
    botao("🔦 Ir até o farol", fase7)


# ============================================================
# FASE 5
# ============================================================

def fase5():

    preparar(5)

    mostrar("""
⛪ FASE 5 — A IGREJA

A porta da igreja está aberta.

O interior está coberto de poeira.

Nas paredes existem símbolos antigos que parecem
ter sido desenhados há centenas de anos.

Milo se aproxima.

Milo:
— Eu já vi esses símbolos antes.

Você pergunta onde.

Milo:
— Nos documentos sobre os desaparecimentos.

Talvez esses símbolos sejam uma pista importante.
""")

    botao("🔎 Examinar os símbolos", fase5_simbolos)
    botao("📖 Procurar documentos", fase5_documentos)
    botao("📷 Fotografar os símbolos", fase5_foto)


def fase5_simbolos(event):

    state["pistas"] += 2

    mostrar("""
Você examina cuidadosamente os símbolos.

Depois de algum tempo percebe algo estranho.

Eles não estão espalhados aleatoriamente.

Quando observados juntos, parecem formar um mapa.

Uma parte do mapa aponta para a floresta.

Outra aponta para as profundezas da ilha.

Você guarda essa informação.

Talvez esteja começando a entender o que aconteceu.
""")

    atualizar_status()
    fase8()


def fase5_documentos(event):

    pegar("livro antigo")
    state["pistas"] += 3

    mostrar("""
Atrás de um armário você encontra um livro antigo.

As páginas estão amareladas, mas ainda podem ser lidas.

O livro fala sobre uma criatura que, segundo os antigos
moradores, vivia nas profundezas da ilha.

A última página foi arrancada.

Mesmo assim, algumas informações ainda podem ser úteis.
""")

    atualizar_status()
    fase8()


def fase5_foto(event):

    pegar("fotografia dos símbolos")
    state["pistas"] += 1

    mostrar("""
Você fotografa os símbolos.

A fotografia pode ajudar a comparar os desenhos
com os documentos encontrados anteriormente.

Barbara observa a parede.

Barbara:
— Se esses símbolos ainda estão aqui,
talvez o que eles protegem também esteja.
""")

    atualizar_status()
    fase8()


# ============================================================
# FASE 6
# ============================================================

def fase6():

    preparar(6)

    mostrar("""
🏚️ FASE 6 — A CASA ABANDONADA

A casa parece estar abandonada há muitos anos.

A madeira range quando vocês entram.

Apesar da aparência antiga, alguns objetos parecem
ter sido mexidos recentemente.

Isso significa que alguém esteve aqui.

Talvez essa pessoa soubesse alguma coisa sobre a ilha.
""")

    botao("📄 Procurar documentos", fase6_documentos)
    botao("⬆️ Subir as escadas", fase6_escadas)
    botao("⬇️ Explorar o porão", fase6_porao)


def fase6_documentos(event):

    pegar("documentos da família")
    state["pistas"] += 3

    mostrar("""
Em uma gaveta você encontra documentos antigos.

Eles pertencem à sua família.

Entre eles existe uma anotação dizendo:

"Não confie no que a ilha mostra durante a noite."

Você sente um arrepio.

A família realmente esteve envolvida nesse mistério.
""")

    atualizar_status()
    fase8()


def fase6_escadas(event):

    pegar("chave enferrujada")
    state["pistas"] += 2
    perder_sanidade()

    mostrar("""
No andar de cima existe um quarto completamente vazio.

No chão você encontra uma chave enferrujada.

Quando você a pega, escuta um barulho vindo
do corredor.

Você olha.

Não há ninguém.

Mesmo assim, decide sair dali.
""")

    atualizar_status()
    fase8()


def fase6_porao(event):

    pegar("fotografia antiga")
    state["pistas"] += 3

    mostrar("""
O porão está completamente escuro.

Entre caixas antigas você encontra uma fotografia.

Nela aparece um grupo de pessoas diante da ilha.

Entre elas está seu parente desaparecido.

No verso da fotografia existe uma data muito antiga
e uma única frase:

"Ele encontrou a entrada."
""")

    atualizar_status()
    fase8()


# ============================================================
# FASE 7
# ============================================================

def fase7():

    preparar(7)

    mostrar("""
🔦 FASE 7 — O FAROL

O farol está abandonado.

Você sobe lentamente as escadas.

No topo existe uma pequena caixa escondida.

Dentro dela há uma fotografia antiga.

Ao fundo da fotografia aparece uma criatura
que você não consegue identificar.

Milo fica pálido.

Milo:
— Isso não deveria existir.

Barbara:
— Então agora sabemos que as histórias eram verdadeiras.

Você guarda a fotografia.

A investigação acabou de ficar muito mais perigosa.
""")

    pegar("fotografia da criatura")
    state["pistas"] += 3

    atualizar_status()

    fase8()


# ============================================================
# FASE 8
# ============================================================

def fase8():

    preparar(8)

    mostrar("""
🌙 FASE 8 — A PRIMEIRA NOITE

A noite chega.

Vocês estão reunidos em uma casa quando escutam:

TOC.

...

TOC.

...

TOC.

Ninguém se mexe.

Milo:
— Não abra.

Barbara:
— Não sabemos o que está lá fora.

O som continua.

Você precisa decidir o que fazer.
""")

    botao("🪟 Abrir a janela", fase8_janela)
    botao("😶 Ignorar as batidas", fase8_ignorar)
    botao("🚪 Sair pela porta", fase8_porta)


def fase8_janela(event):

    state["pistas"] += 2
    perder_sanidade()

    mostrar("""
Você abre lentamente a janela.

Não existe ninguém do lado de fora.

Mas existem marcas enormes no chão.

Elas parecem pegadas.

Milo:
— Feche isso.

Você fecha a janela.

Agora você sabe que alguma coisa está andando
pela vila durante a noite.
""")

    atualizar_status()
    fase9()


def fase8_ignorar(event):

    state["pistas"] += 1

    mostrar("""
Vocês decidem não responder.

Depois de alguns minutos, as batidas param.

O silêncio volta.

Mas ninguém consegue dormir.

Pela manhã, vocês descobrem que as marcas
apareceram ao redor da casa.
""")

    atualizar_status()
    fase9()


def fase8_porta(event):

    state["pistas"] += 3

    mostrar("""
Vocês saem cuidadosamente pela porta.

No chão existem pegadas enormes.

Elas atravessam a vila e desaparecem na direção
da floresta.

Milo:
— Então é para lá que ela foi.

Vocês decidem investigar pela manhã.
""")

    atualizar_status()
    fase9()


# ============================================================
# FASE 9
# ============================================================

def fase9():

    preparar(9)

    mostrar("""
🚨 FASE 9 — O DESAPARECIMENTO

Na manhã seguinte, uma notícia assusta a vila.

Um morador desapareceu.

Milo:
— Ele estava aqui ontem.

Barbara:
— Precisamos encontrá-lo antes que seja tarde.

As últimas marcas foram encontradas perto da floresta.

Você precisa escolher onde procurar primeiro.
""")

    botao("🏘️ Procurar na vila", fase9_vila)
    botao("🌲 Procurar na floresta", fase9_floresta)


def fase9_vila(event):

    state["pistas"] += 1

    mostrar("""
Você procura pelas casas próximas.

Atrás de uma construção encontra marcas no chão.

Elas seguem até a entrada da floresta.

Não há dúvida.

O desaparecido passou por ali.
""")

    atualizar_status()
    fase10()


def fase9_floresta(event):

    state["pistas"] += 2

    mostrar("""
Vocês seguem as pegadas pela floresta.

Depois de algum tempo encontram marcas enormes
afundadas no solo.

Parece que alguma coisa pesada passou por ali.

A trilha continua para dentro da mata.
""")

    atualizar_status()
    fase10()


# ============================================================
# FASE 10
# ============================================================

def fase10():

    preparar(10)

    mostrar("""
🔎 FASE 10 — A INVESTIGAÇÃO

A trilha leva vocês cada vez mais para dentro da floresta.

Depois de algum tempo encontram um objeto
pertencente ao morador desaparecido.

Milo:
— Ele esteve aqui.

Barbara:
— E alguma coisa o levou.

Agora vocês sabem que o desaparecimento
não foi um acidente.

Existe algo vivendo naquela floresta.
""")

    pegar("objeto do desaparecido")
    state["pistas"] += 2

    atualizar_status()
    fase11()


# ============================================================
# FASE 11
# ============================================================

def fase11():

    preparar(11)

    mostrar("""
🌲 FASE 11 — A FLORESTA

A floresta fica cada vez mais escura.

As árvores escondem completamente o céu.

Depois de algum tempo, vocês encontram uma trilha
que parece ter sido aberta recentemente.

Milo:
— Devemos ter cuidado.

Você precisa decidir como continuar.
""")

    botao("➡️ Seguir a trilha", fase11_trilha)
    botao("🪵 Marcar o caminho", fase11_marcar)
    botao("⚠️ Separar o grupo", fase11_separar)


def fase11_trilha(event):

    state["pistas"] += 2

    mostrar("""
Vocês seguem juntos pela trilha.

Quanto mais avançam, mais antigas ficam as árvores.

No chão aparecem marcas que parecem ter sido
feitas por alguma criatura enorme.

Mesmo assim, vocês continuam.
""")

    atualizar_status()
    fase12()


def fase11_marcar(event):

    state["pistas"] += 1

    mostrar("""
Vocês marcam algumas árvores para não se perder.

A trilha continua por vários metros.

Isso dá uma pequena sensação de segurança.

Pelo menos, agora vocês sabem como voltar.
""")

    atualizar_status()
    fase12()


def fase11_separar(event):

    perder_sanidade()

    mostrar("""
Você decide seguir sozinho.

Milo:
— Não acho uma boa ideia.

A floresta fica silenciosa.

Por alguns segundos você pensa ter ouvido
algo se movimentando atrás das árvores.

Você decide voltar para o grupo.

Separar-se não parece mais uma boa ideia.
""")

    atualizar_status()
    fase12()


# ============================================================
# FASE 12
# ============================================================

def fase12():

    preparar(12)

    mostrar("""
🔥 FASE 12 — O ACAMPAMENTO

A noite começa a cair.

Vocês montam um pequeno acampamento.

A fogueira ilumina apenas uma pequena parte
da floresta.

O assunto inevitavelmente volta para a criatura.

Talvez conversar seja a melhor maneira de entender
o que está acontecendo.
""")

    botao("🗣️ Conversar com Milo", fase12_milo)
    botao("🗣️ Conversar com Barbara", fase12_barbara)
    botao("😴 Dormir", fase12_dormir)


def fase12_milo(event):

    state["confianca_milo"] += 2

    mostrar("""
Você conversa com Milo.

Ele revela que seu próprio avô pesquisava
as histórias sobre a criatura.

Milo:
— Ele dizia que ela não era invencível.

Você pergunta qual era a fraqueza.

Milo:
— Nunca descobrimos.

Talvez vocês ainda possam descobrir.
""")

    atualizar_status()
    fase13()


def fase12_barbara(event):

    state["confianca_barbara"] += 2

    mostrar("""
Barbara conta que já ouviu histórias sobre a criatura
desde criança.

Barbara:
— Os antigos moradores falavam de um símbolo.

Você pergunta qual símbolo.

Barbara:
— O símbolo original da ilha.

Talvez essa seja a chave para derrotar a criatura.
""")

    atualizar_status()
    fase13()


def fase12_dormir(event):

    state["sanidade"] += 1

    if state["sanidade"] > 5:
        state["sanidade"] = 5

    mostrar("""
Você decide descansar.

Por algumas horas, consegue esquecer o medo.

Quando acorda, a fogueira ainda está acesa.

Pelo menos sua mente está um pouco mais tranquila.
""")

    atualizar_status()
    fase13()


# ============================================================
# FASE 13
# ============================================================

def fase13():

    preparar(13)

    state["pistas"] += 3

    mostrar("""
🐾 FASE 13 — AS PEGADAS

Na manhã seguinte, vocês encontram pegadas gigantes.

Elas são muito maiores do que qualquer animal
que deveria existir naquela ilha.

Barbara:
— Isso é grande demais.

Milo:
— E está indo naquela direção.

As pegadas levam até uma região ainda mais isolada
da floresta.

Vocês seguem o caminho.
""")

    atualizar_status()
    fase14()


# ============================================================
# FASE 14
# ============================================================

def fase14():

    preparar(14)

    mostrar("""
🏚️ FASE 14 — A CABANA

Depois de seguir as pegadas, vocês encontram
uma pequena cabana escondida entre as árvores.

A porta está aberta.

Dentro existe uma mesa coberta de papéis.

Sobre ela está um diário.

As anotações parecem pertencer a alguém
que investigava a criatura.

Uma frase chama imediatamente sua atenção:

"ELE NÃO PODE SER MORTO COM ARMAS COMUNS."

Barbara:
— Então existe uma maneira de derrotá-lo.
""")

    pegar("diário")
    state["pistas"] += 3

    atualizar_status()
    fase15()


# ============================================================
# FASE 15
# ============================================================

def fase15():

    preparar(15)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
📖 FASE 15 — O DIÁRIO

Vocês passam alguns minutos lendo o diário.

Ele conta a história de uma criatura que vive
nas profundezas da ilha.

Segundo o autor, ela pode ser ferida apenas
por um objeto ligado ao símbolo original.

Uma anotação chama atenção:

"Quando a criatura for atingida pelo símbolo original,
ela ficará vulnerável."

Milo:
— Então precisamos encontrar esse símbolo.

Agora vocês sabem que a criatura possui uma fraqueza.

Só falta descobrir onde está o símbolo.
""")

    atualizar_status()
    fase16()


# ============================================================
# FASE 16
# ============================================================

def fase16():

    preparar(16)

    mostrar("""
🎒 FASE 16 — A PREPARAÇÃO

Vocês sabem que encontrar a criatura será perigoso.

Antes de continuar, precisam decidir
o que procurar.

Talvez uma arma ajude.

Talvez medicamentos sejam necessários.

Ou talvez o mais importante seja encontrar
o símbolo original.
""")

    botao("⚔️ Procurar uma arma", fase16_arma)
    botao("💊 Procurar medicamentos", fase16_medicamento)
    botao("🔱 Procurar o símbolo", fase16_simbolo)


def fase16_arma(event):

    pegar("arma")
    state["batalha"] += 1

    mostrar("""
Você encontra uma arma antiga abandonada.

Ela pode não ser suficiente para derrotar a criatura,
mas pode ajudar caso algo dê errado.

Você a guarda para a viagem.
""")

    atualizar_status()
    fase17()


def fase16_medicamento(event):

    pegar("medicamento")

    mostrar("""
Vocês encontram alguns medicamentos esquecidos
em uma caixa.

Eles podem ser úteis se alguém se machucar.

Você guarda os medicamentos.
""")

    atualizar_status()
    fase17()


def fase16_simbolo(event):

    pegar("símbolo antigo")
    state["pistas"] += 3

    mostrar("""
Depois de procurar entre os objetos antigos,
vocês finalmente encontram um símbolo.

Ele corresponde exatamente aos desenhos
encontrados na igreja.

Milo:
— É ele.

Vocês finalmente possuem uma possível arma
contra a criatura.
""")

    atualizar_status()
    fase17()


# ============================================================
# FASE 17
# ============================================================

def fase17():

    preparar(17)

    mostrar("""
🌊 FASE 17 — O LAGO

O mapa indica que o próximo ponto da investigação
fica perto de um lago.

A água está completamente parada.

No centro existe algo refletindo a luz.

Talvez seja importante.

Você precisa decidir como procurar.
""")

    botao("🌊 Procurar dentro da água", fase17_agua)
    botao("🔎 Procurar ao redor", fase17_redor)
    botao("➡️ Ignorar o lago", fase17_ignorar)


def fase17_agua(event):

    perder_vida()
    pegar("cristal")
    state["pistas"] += 2

    mostrar("""
Você entra na água para procurar.

O fundo é mais profundo do que parecia.

Depois de alguns segundos, encontra um cristal.

Ao sair da água, percebe que se machucou durante
a busca.

Mesmo assim, o cristal parece importante.
""")

    atualizar_status()
    fase18()


def fase17_redor(event):

    pegar("cristal")
    state["pistas"] += 2

    mostrar("""
Vocês procuram ao redor do lago.

Perto de algumas pedras encontram um cristal.

Ele parece reagir quando é aproximado
do símbolo antigo.

Milo:
— Isso não é uma coincidência.
""")

    atualizar_status()
    fase18()


def fase17_ignorar(event):

    state["pistas"] += 1

    mostrar("""
Vocês decidem não perder tempo no lago.

Continuam seguindo o mapa.

Depois de alguns minutos encontram uma passagem
que leva para uma região subterrânea.
""")

    atualizar_status()
    fase18()


# ============================================================
# FASE 18
# ============================================================

def fase18():

    preparar(18)

    mostrar("""
🕳️ FASE 18 — A CAVERNA

O caminho leva até uma caverna escondida.

O cristal parece apontar para dentro dela.

Milo:
— Acho que estamos perto.

Barbara:
— Perto demais.

O ar dentro da caverna é frio.

Alguma coisa está fazendo um som distante.

Você precisa decidir por onde entrar.
""")

    botao("🚪 Entrar pela entrada principal", fase18_entrar)
    botao("🔎 Procurar outra entrada", fase18_outra)


def fase18_entrar(event):

    state["pistas"] += 3

    mostrar("""
Vocês entram pela passagem principal.

Nas paredes existem os mesmos símbolos
encontrados na igreja.

Isso confirma que a caverna está ligada
ao antigo mistério da ilha.

O caminho continua para baixo.
""")

    atualizar_status()
    fase19()


def fase18_outra(event):

    state["pistas"] += 1

    mostrar("""
Vocês procuram outra entrada.

Depois de algum tempo encontram uma passagem estreita.

Ela parece menos perigosa, mas leva ao mesmo lugar.

Vocês continuam.
""")

    atualizar_status()
    fase19()


# ============================================================
# FASE 19
# ============================================================

def fase19():

    preparar(19)

    perder_sanidade()

    mostrar("""
👹 FASE 19 — O PRIMEIRO ENCONTRO

Um rugido ecoa pela caverna.

As paredes parecem tremer.

Então vocês veem a criatura.

Ela aparece apenas por alguns segundos
antes de desaparecer novamente na escuridão.

Milo:
— CORRE!

Barbara:
— AGORA!

Vocês não estão preparados para enfrentá-la.

A única opção é fugir.
""")

    atualizar_status()
    fase20()


# ============================================================
# FASE 20
# ============================================================

def fase20():

    preparar(20)

    mostrar("""
🏃 FASE 20 — A FUGA

A criatura começa a perseguir vocês.

Os corredores da caverna parecem todos iguais.

Cada segundo aumenta o desespero.

Você precisa escolher rapidamente para onde correr.
""")

    botao("⬅️ Correr para a esquerda", fase20_esquerda)
    botao("➡️ Correr para a direita", fase20_direita)
    botao("🫣 Se esconder", fase20_esconder)


def fase20_esquerda(event):

    state["pistas"] += 1

    mostrar("""
Vocês correm para a esquerda.

O caminho parece terminar em uma parede,
mas vocês encontram uma pequena passagem.

Por pouco conseguem escapar.

A criatura fica para trás.
""")

    atualizar_status()
    fase21()


def fase20_direita(event):

    state["pistas"] += 2

    mostrar("""
Vocês correm para a direita.

O corredor leva até uma área escondida da caverna.

Ali existem inscrições antigas.

Talvez vocês tenham encontrado algo importante.
""")

    atualizar_status()
    fase21()


def fase20_esconder(event):

    state["sanidade"] += 1

    if state["sanidade"] > 5:
        state["sanidade"] = 5

    mostrar("""
Vocês encontram uma pequena abertura na parede
e conseguem se esconder.

A criatura passa pelo corredor sem perceber vocês.

Depois que o som desaparece, vocês respiram aliviados.

Por enquanto estão seguros.
""")

    atualizar_status()
    fase21()


# ============================================================
# FASE 21
# ============================================================

def fase21():

    preparar(21)

    state["monstro_fraqueza"] = True
    state["pistas"] += 3

    mostrar("""
🔎 FASE 21 — A FRAQUEZA

Nas paredes da caverna vocês encontram uma inscrição.

Depois de comparar os símbolos com o diário,
vocês finalmente entendem a mensagem.

A criatura não pode ser derrotada por força comum.

O símbolo original pode enfraquecê-la.

Milo:
— Então essa é a nossa chance.

Barbara:
— Agora precisamos encontrar o esconderijo dela.

Vocês continuam pela caverna.
""")

    atualizar_status()
    fase22()


# ============================================================
# FASE 22
# ============================================================

def fase22():

    preparar(22)

    mostrar("""
🏚️ FASE 22 — O ESCONDERIJO

Depois de seguir as inscrições, vocês encontram
uma passagem escondida.

Ela leva para uma enorme área subterrânea.

Ali existem marcas nas paredes e no chão.

Milo:
— É aqui.

Barbara:
— É o esconderijo da criatura.

O silêncio é assustador.

Vocês sabem que estão cada vez mais perto
da resposta que procuravam.
""")

    fase23()


# ============================================================
# FASE 23
# ============================================================

def fase23():

    preparar(23)

    state["pistas"] += 1

    mostrar("""
🆘 FASE 23 — O RESGATE

Antes de entrar mais fundo no esconderijo,
vocês encontram alguém.

É o morador desaparecido.

Ele está ferido, mas ainda está consciente.

Morador:
— Vocês precisam ir embora!

Você:
— O que aconteceu?

Morador:
— Eu entrei aqui procurando respostas.

Ele olha para o fundo da caverna.

Morador:
— Ela está acordada.

Vocês precisam decidir o que fazer com ele.
""")

    botao("🚶 Levar o homem embora", fase23_levar)
    botao("🫣 Deixá-lo escondido", fase23_esconder)


def fase23_levar(event):

    mostrar("""
Vocês ajudam o homem a se levantar.

Ele está fraco, mas consegue andar.

Milo:
— Vamos levá-lo para um lugar seguro.

Depois de encontrar uma área protegida,
vocês voltam para continuar a investigação.

Não podem deixar o mistério sem resposta.
""")

    fase24()


def fase23_esconder(event):

    mostrar("""
Vocês encontram um lugar seguro dentro da caverna.

O homem permanece escondido enquanto vocês
continuam a investigação.

Barbara:
— Voltaremos para buscá-lo.

Vocês seguem em direção à entrada do esconderijo.
""")

    fase24()


# ============================================================
# FASE 24
# ============================================================

def fase24():

    preparar(24)

    mostrar("""
🚪 FASE 24 — A ENTRADA

Uma enorme porta bloqueia o caminho.

No centro dela existe exatamente o mesmo símbolo
encontrado na igreja.

Agora tudo começa a fazer sentido.

A igreja, o diário, o mapa e a caverna
fazem parte do mesmo mistério.

A porta parece reconhecer o símbolo original.
""")

    if "símbolo antigo" in state["inv"]:

        state["pistas"] += 3

        mostrar("""
Você aproxima o símbolo da porta.

Os desenhos começam a brilhar.

Um mecanismo antigo é ativado.

A enorme porta começa a se abrir.

Vocês encontraram a entrada verdadeira.
""")

    else:

        perder_vida()

        mostrar("""
Vocês não possuem o símbolo.

Milo procura outra maneira de abrir a porta.

Depois de algum esforço, vocês conseguem forçá-la.

Um enorme barulho ecoa pelo subterrâneo.

Talvez a criatura tenha ouvido.
""")

    atualizar_status()

    fase25()


# ============================================================
# FASE 25
# ============================================================

def fase25():

    preparar(25)

    state["pistas"] += 4

    mostrar("""
📜 FASE 25 — O PASSADO DA FAMÍLIA

Dentro do esconderijo existem dezenas de documentos.

Você começa a procurar entre eles.

Então encontra algo que reconhece.

O sobrenome da sua família.

Os documentos revelam que seu parente esteve
na ilha anos atrás.

Ele descobriu a existência da criatura.

E tentou impedir que ela fosse libertada.

Barbara:
— Então ele não desapareceu por acaso.

Milo:
— Ele estava tentando proteger todo mundo.

Agora você entende por que sua família
guardou aquele segredo durante tanto tempo.
""")

    atualizar_status()
    fase26()


# ============================================================
# FASE 26
# ============================================================

def fase26():

    preparar(26)

    mostrar("""
⚔️ FASE 26 — A PREPARAÇÃO

Vocês estão diante do local onde a criatura
está escondida.

Antes de entrar, precisam se preparar.

A próxima decisão pode determinar o resultado
de toda a investigação.

Como vocês vão se preparar?
""")

    botao("⚔️ Preparar a arma", fase26_arma)
    botao("🔱 Preparar o símbolo", fase26_simbolo)
    botao("📖 Procurar mais informações", fase26_info)


def fase26_arma(event):

    if "arma" in state["inv"]:

        state["batalha"] += 1

        mostrar("""
Você verifica a arma.

Ela está pronta.

Milo:
— Não sabemos se vai funcionar.

Você:
— Mas é melhor ter alguma coisa do que nada.

Vocês se preparam para entrar.
""")

    else:

        mostrar("""
Vocês procuram uma arma.

Infelizmente, nenhuma está disponível.

Mesmo assim, precisam continuar.
""")

    atualizar_status()
    fase27()


def fase26_simbolo(event):

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 2

        mostrar("""
Você segura o símbolo antigo.

Ele começa a emitir um brilho fraco.

Barbara:
— É isso que pode derrotar a criatura.

Agora vocês sabem que possuem uma chance.
""")

    else:

        mostrar("""
Vocês procuram pelo símbolo antigo.

Infelizmente, ele não está com vocês.

Talvez seja necessário enfrentar a criatura
sem ele.
""")

    atualizar_status()
    fase27()


def fase26_info(event):

    state["monstro_fraqueza"] = True
    state["batalha"] += 2

    mostrar("""
Vocês revisam todos os documentos encontrados.

Finalmente descobrem mais uma informação.

A criatura fica mais vulnerável quando
o símbolo original é ativado.

Milo:
— Agora sabemos exatamente o que fazer.

Vocês estão prontos.
""")

    atualizar_status()
    fase27()


# ============================================================
# FASE 27
# ============================================================

def fase27():

    preparar(27)

    mostrar("""
👹 FASE 27 — O MONSTRO

Vocês chegam à última sala.

A criatura está esperando.

Ela é muito maior do que parecia nas histórias.

Por alguns segundos, ninguém fala.

Milo:
— É agora.

Barbara:
— Todo mundo pronto?

Milo:
— Não.

Barbara:
— Mas vamos mesmo assim.

A criatura começa a avançar.

Não existe mais como fugir do confronto.
""")

    fase28()


# ============================================================
# FASE 28
# ============================================================

def fase28():

    preparar(28)

    mostrar("""
⚔️ FASE 28 — A BATALHA

A criatura ataca.

O chão treme.

Vocês precisam trabalhar juntos para sobreviver.

Escolha uma ação:
""")

    botao("⚔️ Atacar", fase28_atacar)
    botao("🔱 Ativar o símbolo", fase28_simbolo)
    botao("🛡️ Ajudar Milo", fase28_milo)
    botao("🛡️ Ajudar Barbara", fase28_barbara)


def fase28_atacar(event):

    if "arma" in state["inv"] and state["monstro_fraqueza"]:

        state["batalha"] += 3

        mostrar("""
Você usa a arma contra o ponto fraco da criatura.

O golpe funciona.

A criatura recua pela primeira vez.

Milo:
— Funcionou!

Agora vocês sabem que ela pode ser derrotada.
""")

    else:

        perder_vida()

        mostrar("""
Você tenta atacar.

O golpe não causa o efeito esperado.

A criatura reage e você acaba se machucando.

Ainda assim, vocês continuam lutando.
""")

    atualizar_status()
    fase29()


def fase28_simbolo(event):

    if "símbolo antigo" in state["inv"]:

        state["batalha"] += 4
        state["monstro_fraqueza"] = True

        mostrar("""
Você ergue o símbolo antigo.

Uma luz atravessa a sala.

A criatura recua imediatamente.

As inscrições nas paredes começam a brilhar.

Barbara:
— Agora!

A criatura está enfraquecida.

Essa pode ser a única oportunidade.
""")

    else:

        perder_sanidade()

        mostrar("""
Você tenta ativar o símbolo.

Mas percebe que não o possui.

A criatura avança.

Por pouco vocês conseguem escapar.
""")

    atualizar_status()
    fase29()


def fase28_milo(event):

    if state["milo_vivo"]:

        state["confianca_milo"] += 2
        state["batalha"] += 2

        mostrar("""
Você ajuda Milo a se posicionar.

Milo consegue evitar o ataque da criatura.

Milo:
— Obrigado!

Vocês percebem que trabalhar juntos
aumenta suas chances de sobreviver.
""")

    atualizar_status()
    fase29()


def fase28_barbara(event):

    if state["barbara_viva"]:

        state["confianca_barbara"] += 2
        state["batalha"] += 2

        mostrar("""
Você ajuda Barbara.

Ela consegue ativar uma das inscrições
na parede.

Barbara:
— Eu sabia que podia confiar em você!

A criatura parece enfraquecer ainda mais.
""")

    atualizar_status()
    fase29()


# ============================================================
# FASE 29
# ============================================================

def fase29():

    preparar(29)

    mostrar("""
🔥 FASE 29 — A ÚLTIMA ESCOLHA

A criatura está ferida.

Ela ainda é perigosa, mas vocês finalmente
descobriram como enfrentá-la.

Agora existe apenas uma decisão.

O que vocês vão fazer?
""")

    botao("⚔️ Derrotar o monstro", fase29_derrotar)
    botao("🔒 Selar o monstro", fase29_selar)
    botao("🏃 Fugir da ilha", fase29_fugir)


def fase29_derrotar(event):

    state["acao_final"] = "derrotar"

    if state["batalha"] >= 5 and state["monstro_fraqueza"]:

        state["monstro_derrotado"] = True

        mostrar("""
Você reúne toda a coragem que consegue.

O símbolo é ativado.

A criatura perde a força.

Vocês atacam juntos.

Depois de uma última tentativa,
a criatura finalmente cai.

O silêncio toma conta da caverna.

A ameaça que assombrou a ilha durante gerações
finalmente chegou ao fim.
""")

    else:

        state["monstro_derrotado"] = False

        mostrar("""
Vocês tentam derrotar a criatura.

Mas ela ainda está forte demais.

O ataque não é suficiente.

Mesmo assim, vocês conseguem sobreviver
e precisam decidir como escapar.
""")

    fase30()


def fase29_selar(event):

    state["acao_final"] = "selar"
    state["monstro_derrotado"] = False

    if state["batalha"] < 3:
        state["batalha"] = 3

    mostrar("""
Vocês percebem que derrotar a criatura
pode ser impossível naquele momento.

Então decidem usar o símbolo para selá-la novamente.

As inscrições começam a brilhar.

A criatura desaparece atrás da enorme porta.

O silêncio volta.

A ilha está segura.

Mas ninguém sabe por quanto tempo.
""")

    fase30()


def fase29_fugir(event):

    state["acao_final"] = "fugir"
    state["monstro_derrotado"] = False

    if state["vida"] < 1:
        state["vida"] = 1

    mostrar("""
Vocês percebem que continuar lutando
pode custar suas vidas.

Então decidem fugir.

Correm pelos corredores da caverna
enquanto a ilha começa a tremer.

Por pouco conseguem chegar à superfície.

O barco ainda está esperando.

Vocês deixam a ilha para trás.

Mas a criatura continua viva.
""")

    fase30()


# ============================================================
# FASE 30 — FINAIS
# ============================================================

def fase30():

    limpar()

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


    # ========================================================
    # FINAL 1 — PERFEITO
    # ========================================================

    if state["acao_final"] == "derrotar" and state["monstro_derrotado"] and len(vivos) >= 3:

        mudar_imagem("final_01.png")

        mostrar("""
🌟 FINAL PERFEITO

A criatura finalmente foi derrotada.

Todos conseguem sair da câmara subterrânea.

Milo olha para a ilha pela última vez.

Barbara:
— Depois de tantos anos, acabou.

Você segura os documentos encontrados
e percebe que finalmente descobriu a verdade
sobre o desaparecimento da sua família.

Todos sobrevivem.

O segredo da ilha foi descoberto.

E, dessa vez, ninguém precisará esconder a verdade.
""")

    # ========================================================
    # FINAL 2 — VITÓRIA
    # ========================================================

    elif state["acao_final"] == "derrotar" and state["monstro_derrotado"]:

        mudar_imagem("final_02.png")

        mostrar("""
🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Mas a batalha teve um preço.

Nem todos conseguiram sair da ilha.

Os sobreviventes chegam ao barco
e deixam aquele lugar para trás.

Enquanto a ilha desaparece no horizonte,
você percebe que a verdade finalmente foi descoberta.

O segredo terminou.

Mas as lembranças daquela noite
nunca serão esquecidas.
""")

        mostrar(
            "👥 Sobreviventes: " + ", ".join(vivos)
        )


    # ========================================================
    # FINAL 3 — SELAMENTO
    # ========================================================

    elif state["acao_final"] == "selar":

        mudar_imagem("final_03.png")

        mostrar("""
👁️ FINAL DO SELAMENTO

A criatura não foi destruída.

Mas o símbolo conseguiu prendê-la novamente
nas profundezas da ilha.

A porta se fecha.

Os símbolos desaparecem.

Por alguns minutos, tudo parece tranquilo.

Barbara:
— Nós conseguimos.

Milo:
— Conseguimos por enquanto.

Você olha para a entrada da caverna.

A ilha está segura...

Por enquanto.

Algum dia alguém poderá encontrar aquela porta
novamente.

E talvez cometa o mesmo erro.
""")


    # ========================================================
    # FINAL 4 — FUGA
    # ========================================================

    elif state["acao_final"] == "fugir":

        mudar_imagem("final_06.png")

        mostrar("""
🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha começa a ficar distante.

Ninguém fala durante a viagem.

Você olha para trás.

A ilha parece completamente normal.

Mas você sabe a verdade.

A criatura continua lá.

O segredo não foi destruído.

Apenas ficou para trás.

Talvez um dia alguém volte.

E, quando isso acontecer,
a história poderá começar novamente.
""")


    # ========================================================
    # FINAL 5 — DERROTA
    # ========================================================

    else:

        mudar_imagem(
            "Gemini_Generated_Image_I0ib9910ib9910ib.png"
        )

        mostrar("""
💀 FINAL DA ILHA

A criatura consegue resistir.

Vocês não conseguiram encontrar uma maneira
de derrotá-la.

A ilha permanece em silêncio.

O segredo continua escondido
nas profundezas da caverna.

Durante muitos anos,
ninguém saberá o que realmente aconteceu.

A ilha continua esperando.

E o mistério permanece enterrado.
""")


    # ========================================================
    # INFORMAÇÕES FINAIS
    # ========================================================

    mostrar("""
============================================================

🎮 FIM DO JOGO

============================================================
""")

    mostrar(
        "👤 Personagem: " + state["personagem"]
    )

    mostrar(
        "❤️ Vida: " + str(state["vida"])
    )

    mostrar(
        "🧠 Sanidade: " + str(state["sanidade"])
    )

    mostrar(
        "🔎 Pistas: " + str(state["pistas"])
    )

    mostrar(
        "🎒 Inventário: " +
        (", ".join(state["inv"]) if state["inv"] else "Nenhum item")
    )

    botao(
        "🔄 Jogar novamente",
        reiniciar
    )


# ============================================================
# REINICIAR
# ============================================================

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

    state["acao_final"] = ""

    fase1()


# ============================================================
# COMEÇAR O JOGO
# ============================================================

fase1()
