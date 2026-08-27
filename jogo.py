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

```
"milo_vivo": True,
"barbara_viva": True,
"olivier_vivo": True,
"amelie_viva": True,

"confianca_milo": 0,
"confianca_barbara": 0,

"monstro_fraqueza": False,
"monstro_derrotado": False,
"batalha": 0
```

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
f"❤️ Vida: {state['vida']}   "
f" 🧠 Sanidade: {state['sanidade']}   "
f" 🔎 Pistas: {state['pistas']}   "
f" 🎒 Itens: {len(state['inv'])}"
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

```
if numero <= 20:
    imagem_fase(numero)
else:
    imagem.style.display = "none"
```

def pegar(item):
if item not in state["inv"]:
state["inv"].append(item)
mostrar(f"🎒 Você encontrou: {item}")
atualizar_status()

def perder_vida(qtd=1):
state["vida"] -= qtd

```
if state["vida"] < 0:
    state["vida"] = 0

atualizar_status()
```

def perder_sanidade(qtd=1):
state["sanidade"] -= qtd

```
if state["sanidade"] < 0:
    state["sanidade"] = 0

atualizar_status()
```

def ganhar_sanidade(qtd=1):
state["sanidade"] += qtd

```
if state["sanidade"] > 5:
    state["sanidade"] = 5

atualizar_status()
```

# ============================================================

# FASE 1 — CHEGADA DOS VISITANTES

# ============================================================

def fase1():

```
preparar(1)

mostrar("""
```

🏝️ O SEGREDO NA ILHA

Durante muitos anos, uma pequena ilha permaneceu
afastada do restante do mundo.

Existem histórias antigas sobre pessoas que desapareceram,
lugares abandonados e acontecimentos que ninguém da região
gosta de comentar.

Recentemente, Olivier e Amelie encontraram documentos
relacionados à própria família.

Os documentos mencionavam uma ilha distante e um parente
que havia desaparecido muitos anos atrás.

Depois de descobrir essas informações, os dois decidiram
viajar até a ilha para descobrir a verdade.

O barco se aproxima lentamente da costa.

Ao longe, é possível ver algumas casas, uma igreja antiga
e um enorme farol.

Antes de desembarcar, você precisa decidir quem vai assumir
a investigação.

ESCOLHA SEU PERSONAGEM:
""")

```
botao("🧑 Olivier", escolher_olivier)
botao("👩 Amelie", escolher_amelie)
```

def escolher_olivier(event):
state["personagem"] = "Olivier"
fase2()

def escolher_amelie(event):
state["personagem"] = "Amelie"
fase2()

# ============================================================

# FASE 2 — A VIAGEM

# ============================================================

def fase2():

```
preparar(2)

mostrar("""
```

🚢 FASE 2 — A VIAGEM

O barco continua avançando pelo mar.

Olivier observa os documentos da família pela última vez.

Amelie olha pela janela e percebe que a ilha está ficando
cada vez maior.

A viagem foi longa e silenciosa.

Ninguém sabe exatamente o que aconteceu com o parente que
desapareceu anos atrás, mas os documentos deixam claro que
ele esteve naquela ilha.

Quando o barco finalmente se aproxima do pequeno porto,
duas pessoas aparecem esperando na praia.

São Milo e Barbara.

Eles não são visitantes.

Os dois nasceram e vivem na ilha há anos e conhecem muito
bem os caminhos, as histórias e os lugares abandonados.

Milo faz um sinal para que o barco se aproxime.

— Vocês finalmente chegaram.

Barbara observa os documentos que vocês carregam.

— Então vocês vieram por causa da família de vocês...

A expressão dela muda.

— Talvez seja melhor conversarmos antes de vocês
começarem a explorar a ilha.
""")

```
botao("➡️ Desembarcar", fase3)
```

# ============================================================

# FASE 3 — OS MORADORES

# ============================================================

def fase3():

```
preparar(3)

mostrar("""
```

🏝️ FASE 3 — OS MORADORES DA ILHA

Depois de desembarcar, vocês caminham pela vila.

Milo e Barbara seguem na frente.

Eles conhecem cada rua e cada caminho da região.

Milo explica que poucas pessoas vivem na ilha atualmente.

— A maioria das famílias foi embora há muitos anos.

Barbara olha para as casas antigas.

— Principalmente depois dos desaparecimentos.

Vocês percebem que os moradores evitam falar sobre
determinados lugares.

Olivier/Amelie decide fazer algumas perguntas.

O que você quer descobrir primeiro?
""")

```
botao("🔎 Perguntar sobre a ilha", fase3_ilha)
botao("👨‍👩‍👧 Perguntar sobre sua família", fase3_familia)
botao("👻 Perguntar sobre os desaparecimentos", fase3_desaparecimentos)
```

def fase3_ilha(event):

```
state["confianca_milo"] += 1

mostrar("""
```

Milo respira fundo antes de responder.

— Durante o dia, a ilha parece normal.

Ele aponta para a floresta.

— Mas quando escurece, algumas coisas mudam.

Barbara completa:

— É por isso que os moradores evitam sair depois da noite.

Milo olha para vocês.

— Se vocês realmente querem descobrir o que aconteceu,
precisam tomar cuidado.
""")

```
botao("🏝️ Continuar investigação", fase4)
```

def fase3_familia(event):

```
state["pistas"] += 2

mostrar("""
```

Barbara pega os documentos das mãos de vocês e observa
o sobrenome escrito neles.

— Eu já vi esse nome antes.

Milo fica em silêncio por alguns segundos.

— Sua família esteve aqui.

Barbara continua:

— Mas existe uma parte dessa história que nunca foi
contada para vocês.

Ela devolve os documentos.

— Se quiserem descobrir a verdade, terão que procurar
nos lugares antigos da ilha.
""")

```
atualizar_status()
botao("🏝️ Continuar investigação", fase4)
```

def fase3_desaparecimentos(event):

```
state["pistas"] += 1

mostrar("""
```

Milo olha para a floresta.

— Pessoas desapareceram ao longo dos anos.

Barbara explica que alguns moradores simplesmente
não voltaram para casa.

— Nunca encontramos uma explicação.

Milo completa:

— E todas as histórias parecem levar para a mesma região.

A floresta fica em silêncio.

Vocês percebem que a investigação pode ser muito mais
perigosa do que imaginavam.
""")

```
atualizar_status()
botao("🏝️ Continuar investigação", fase4)
```

# ============================================================

# FASE 4 — OS TRÊS LUGARES

# ============================================================

def fase4():

```
preparar(4)

mostrar("""
```

🏘️ FASE 4 — A VILA

Milo leva vocês até o centro da vila.

Barbara mostra três lugares importantes.

⛪ A igreja antiga
🏚️ A casa abandonada
🔦 O farol

Segundo Barbara, todos esses lugares possuem alguma
relação com a história da ilha.

Milo explica:

— Não sabemos exatamente o que vocês vão encontrar.

— Mas se o parente de vocês realmente esteve aqui,
é possível que tenha deixado alguma pista.

Agora vocês precisam escolher por onde começar.
""")

```
botao("⛪ Investigar a igreja", fase5)
botao("🏚️ Investigar a casa abandonada", fase6)
botao("🔦 Investigar o farol", fase7)
```

# ============================================================

# FASE 5 — IGREJA

# ============================================================

def fase5():

```
preparar(5)

mostrar("""
```

⛪ FASE 5 — A IGREJA ANTIGA

A igreja está abandonada há muitos anos.

A porta range quando vocês entram.

O interior está coberto de poeira.

Milo caminha lentamente pelo corredor.

— Minha família costumava vir aqui quando eu era criança.

Barbara observa as paredes.

Existem símbolos antigos espalhados pelo prédio.

Alguns parecem ter sido desenhados de propósito.

Milo fica preocupado.

— Eu já vi esses símbolos antes.

Talvez eles sejam uma das primeiras pistas sobre o
mistério da ilha.

O que você faz?
""")

```
botao("🔎 Examinar os símbolos", fase5_simbolos)
botao("📖 Procurar documentos", fase5_documentos)
botao("📷 Fotografar os símbolos", fase5_foto)
```

def fase5_simbolos(event):

```
state["pistas"] += 2

mostrar("""
```

Você examina os símbolos com cuidado.

Depois de comparar vários desenhos, percebe que eles
não estão espalhados aleatoriamente.

Quando vistos juntos, parecem formar um mapa.

Barbara se aproxima.

— Então os símbolos estão indicando algum lugar.

Milo aponta para uma parte do desenho.

— Essa direção leva para a floresta.
""")

```
atualizar_status()
botao("🌲 Seguir a investigação", fase8)
```

def fase5_documentos(event):

```
pegar("livro antigo")
state["pistas"] += 3

mostrar("""
```

Atrás de um banco antigo você encontra um pequeno livro.

As páginas estão amareladas e algumas estão quase
apagadas pelo tempo.

O livro fala sobre antigos moradores da ilha e menciona
um ritual relacionado aos símbolos encontrados nas paredes.

Barbara lê algumas páginas.

— Isso pode explicar por que minha família nunca falou
sobre esse lugar.

Milo guarda o livro com cuidado.

— Precisamos continuar procurando.
""")

```
atualizar_status()
botao("🌲 Seguir a investigação", fase8)
```

def fase5_foto(event):

```
pegar("fotografia dos símbolos")
state["pistas"] += 1

mostrar("""
```

Você fotografa cuidadosamente os símbolos.

Barbara percebe que alguns detalhes são difíceis de ver
a olho nu.

— Talvez possamos comparar essa fotografia com outras
pistas mais tarde.

Milo concorda.

— Guardem isso. Pode ser importante.
""")

```
atualizar_status()
botao("🌲 Seguir a investigação", fase8)
```

# ============================================================

# FASE 6 — CASA

# ============================================================

def fase6():

```
preparar(6)

mostrar("""
```

🏚️ FASE 6 — A CASA ABANDONADA

A casa fica afastada das outras construções da vila.

Milo explica que ninguém mora ali há muitos anos.

— Algumas pessoas dizem que o antigo dono sabia demais
sobre a ilha.

Barbara abre a porta.

O interior está coberto de poeira, mas alguns objetos
parecem ter sido mexidos recentemente.

Vocês começam a investigar.

Existem documentos, uma escada antiga e uma porta que
leva para o porão.

Onde procurar?
""")

```
botao("📄 Procurar documentos", fase6_documentos)
botao("⬆️ Subir as escadas", fase6_escadas)
botao("⬇️ Investigar o porão", fase6_porao)
```

def fase6_documentos(event):

```
pegar("documentos da família")
state["pistas"] += 3

mostrar("""
```

Entre vários papéis antigos, você encontra documentos
com o mesmo sobrenome da sua família.

Uma anotação chama sua atenção:

"Se alguém encontrar estes documentos, não confie
nas aparências. A ilha guarda um segredo."

Barbara fica surpresa.

— Isso confirma que sua família esteve envolvida.

Milo olha para a porta.

— Precisamos descobrir o que eles estavam tentando fazer.
""")

```
atualizar_status()
botao("🌲 Continuar", fase8)
```

def fase6_escadas(event):

```
pegar("chave enferrujada")
state["pistas"] += 2
perder_sanidade()

mostrar("""
```

No andar superior você encontra uma pequena chave enferrujada.

Ao lado dela existe uma fotografia antiga.

A fotografia mostra algumas pessoas reunidas diante
da floresta.

Uma delas parece ser o seu parente desaparecido.

Por alguns segundos, você sente a impressão de estar
sendo observado.

Barbara percebe sua preocupação.

— Vamos sair daqui por enquanto.
""")

```
botao("🌲 Continuar", fase8)
```

def fase6_porao(event):

```
pegar("fotografia antiga")
state["pistas"] += 3

mostrar("""
```

O porão está completamente escuro.

Milo ilumina as paredes enquanto vocês procuram alguma pista.

Em uma caixa antiga existe uma fotografia.

Nela aparece um grupo de moradores diante de uma entrada
subterrânea.

No verso da fotografia existe uma frase:

"Aquilo que está abaixo da ilha nunca deve ser acordado."

Barbara fica em silêncio.

Agora vocês sabem que existe alguma coisa escondida
debaixo da ilha.
""")

```
botao("🌲 Continuar", fase8)
```

# ============================================================

# FASE 7 — FAROL

# ============================================================

def fase7():

```
preparar(7)

mostrar("""
```

🔦 FASE 7 — O FAROL

O farol fica no ponto mais alto da vila.

Milo explica que ele está abandonado há anos.

— Antigamente, ele era usado para orientar os barcos.

Barbara abre a porta.

Vocês sobem lentamente os degraus.

No topo existe uma pequena caixa escondida.

Dentro dela há uma fotografia antiga.

Ao fundo da imagem existe uma figura estranha.

Ninguém sabe explicar exatamente o que aparece nela.

Milo fica pálido.

— Isso não deveria estar nessa fotografia.

Barbara observa a imagem.

— Então as histórias podem ser verdadeiras.
""")

```
pegar("fotografia da criatura")
state["pistas"] += 3
atualizar_status()

botao("🌙 Continuar investigação", fase8)
```

# ============================================================

# FASE 8 — PRIMEIRA NOITE

# ============================================================

def fase8():

```
preparar(8)

mostrar("""
```

🌙 FASE 8 — A PRIMEIRA NOITE

A investigação continua até o anoitecer.

Milo decide que vocês devem passar a noite em uma casa
segura da vila.

Barbara prepara algumas lanternas.

O vento bate nas janelas.

Durante a madrugada...

TOC.

TOC.

TOC.

Todos ficam em silêncio.

Milo sussurra:

— Não abra.

Barbara olha para a janela.

— E é exatamente isso que me preocupa.

As batidas continuam.

O que você faz?
""")

```
botao("🪟 Abrir a janela", fase8_janela)
botao("😶 Ignorar as batidas", fase8_ignorar)
botao("🚪 Sair pela porta", fase8_porta)
```

def fase8_janela(event):

```
state["pistas"] += 2
perder_sanidade()

mostrar("""
```

Você abre a janela.

Não existe ninguém do lado de fora.

Mas, no chão, existem marcas enormes.

Elas parecem pegadas.

Milo observa de longe.

— Eu conheço essas marcas.

Barbara responde:

— Então ela voltou.
""")

```
botao("🌅 Continuar", fase9)
```

def fase8_ignorar(event):

```
state["pistas"] += 1

mostrar("""
```

Vocês decidem não responder.

Depois de alguns minutos, as batidas param.

O silêncio volta.

Na manhã seguinte, porém, vocês encontram marcas
profundas do lado de fora da casa.

Alguma coisa esteve ali durante a noite.
""")

```
botao("🌅 Continuar", fase9)
```

def fase8_porta(event):

```
state["pistas"] += 3

mostrar("""
```

Vocês saem cuidadosamente pela porta.

A vila está completamente silenciosa.

No caminho encontram várias pegadas enormes.

Milo se agacha para observar.

— Isso não pertence a nenhum animal que conhecemos.

Barbara olha para a floresta.

— E elas estão indo para lá.
""")

```
botao("🌅 Continuar", fase9)
```

# ============================================================

# FASE 9 — DESAPARECIMENTO

# ============================================================

def fase9():

```
preparar(9)

mostrar("""
```

🚨 FASE 9 — O DESAPARECIMENTO

Na manhã seguinte, uma notícia assustadora se espalha
pela vila.

Um dos moradores desapareceu.

Milo reconhece imediatamente a pessoa.

— Ele estava aqui ontem.

Barbara tenta manter a calma.

— Precisamos encontrá-lo antes que seja tarde.

Vocês procuram informações pela vila.

Existem duas possibilidades:

seguir as marcas encontradas perto das casas ou
seguir diretamente para a floresta.
""")

```
botao("🏘️ Procurar pela vila", fase9_vila)
botao("🌲 Procurar na floresta", fase9_floresta)
```

def fase9_vila(event):

```
state["pistas"] += 1

mostrar("""
```

Vocês procuram pelas ruas da vila.

Perto de uma das casas encontram marcas no chão.

Elas seguem na direção da floresta.

Barbara observa o caminho.

— Então ele provavelmente foi levado para lá.
""")

```
botao("🔎 Continuar investigação", fase10)
```

def fase9_floresta(event):

```
state["pistas"] += 2

mostrar("""
```

Vocês seguem imediatamente para a floresta.

Depois de alguns minutos encontram pegadas enormes.

Milo compara as marcas com as encontradas durante a noite.

— São iguais.

Barbara percebe que existem marcas de passos humanos
misturadas às pegadas.

O desaparecido passou por ali.
""")

```
botao("🔎 Continuar investigação", fase10)
```

# ============================================================

# FASE 10

# ============================================================

def fase10():

```
preparar(10)

mostrar("""
```

🔎 FASE 10 — A INVESTIGAÇÃO

Vocês seguem as pistas pela floresta.

A vegetação fica mais fechada.

Depois de algum tempo, encontram um objeto no chão.

É algo que pertence ao morador desaparecido.

Milo pega o objeto.

— Ele esteve aqui.

Barbara observa a direção das marcas.

— E não estava sozinho.

As pistas mostram que alguém ou alguma coisa
o levou para dentro da floresta.

Vocês decidem continuar.
""")

```
pegar("objeto do desaparecido")
state["pistas"] += 2

botao("🌲 Continuar pela floresta", fase11)
```

# ============================================================

# FASE 11

# ============================================================

def fase11():

```
preparar(11)

mostrar("""
```

🌲 FASE 11 — A FLORESTA

A floresta fica cada vez mais escura.

Milo conhece alguns caminhos antigos, mas nem mesmo ele
reconhece aquela região.

Barbara encontra uma trilha quase escondida entre as árvores.

— Alguém passou por aqui recentemente.

Vocês precisam decidir como continuar.
""")

```
botao("🥾 Seguir a trilha", fase11_trilha)
botao("🪵 Marcar o caminho", fase11_marcar)
botao("⚠️ Separar o grupo", fase11_separar)
```

def fase11_trilha(event):

```
state["pistas"] += 2

mostrar("""
```

Vocês seguem a trilha juntos.

As marcas ficam mais claras conforme avançam.

Milo percebe que a trilha parece levar para uma área
que não aparece nos mapas atuais da ilha.
""")

```
botao("🔥 Continuar", fase12)
```

def fase11_marcar(event):

```
state["pistas"] += 1

mostrar("""
```

Barbara marca algumas árvores para que vocês consigam
encontrar o caminho de volta.

A estratégia deixa a investigação mais segura.

Depois de alguns minutos, vocês encontram um local
adequado para montar acampamento.
""")

```
botao("🔥 Continuar", fase12)
```

def fase11_separar(event):

```
perder_sanidade()

mostrar("""
```

Vocês consideram se separar para procurar mais pistas.

Milo imediatamente discorda.

— Não sabemos o que está nessa floresta.

Mesmo assim, você decide avançar sozinho por alguns minutos.

O silêncio ao redor começa a ficar assustador.

Você percebe que não foi uma boa ideia.

O grupo se reúne novamente antes que escureça.
""")

```
botao("🔥 Continuar", fase12)
```

# ============================================================

# FASE 12 — ACAMPAMENTO

# ============================================================

def fase12():

```
preparar(12)

mostrar("""
```

🔥 FASE 12 — O ACAMPAMENTO

A noite chega rapidamente.

Vocês montam um pequeno acampamento.

O fogo ilumina apenas uma pequena parte da floresta.

Pela primeira vez desde que chegaram à ilha, vocês têm
tempo para conversar com calma.

Milo conhece as histórias antigas.

Barbara conhece os moradores e os caminhos da ilha.

Talvez uma conversa possa revelar algo importante.
""")

```
botao("🗣️ Conversar com Milo", fase12_milo)
botao("🗣️ Conversar com Barbara", fase12_barbara)
botao("😴 Descansar", fase12_dormir)
```

def fase12_milo(event):

```
state["confianca_milo"] += 2

mostrar("""
```

Milo conta que sua família vive na ilha há gerações.

— Quando eu era pequeno, meu avô dizia para nunca
entrar nas cavernas do norte.

Ele acredita que os desaparecimentos estão ligados
a alguma coisa escondida naquela região.

— Eu nunca soube se era apenas uma história.

Agora, depois de tudo que vocês encontraram,
ele começa a acreditar que talvez fosse verdade.
""")

```
botao("🌅 Continuar", fase13)
```

def fase12_barbara(event):

```
state["confianca_barbara"] += 2

mostrar("""
```

Barbara conta que sua família sempre ajudou a cuidar
da vila.

— Minha avó conhecia histórias sobre a criatura.

Ela nunca gostava de falar sobre isso.

Barbara revela que existem registros antigos
guardados em diferentes lugares da ilha.

— Talvez sua família tenha deixado alguma coisa
para trás.
""")

```
botao("🌅 Continuar", fase13)
```

def fase12_dormir(event):

```
ganhar_sanidade()

mostrar("""
```

Você decide descansar enquanto Milo e Barbara
ficam atentos ao redor do acampamento.

A noite passa sem novos acontecimentos.

Na manhã seguinte, todos estão um pouco mais preparados
para continuar a investigação.
""")

```
botao("🌅 Continuar", fase13)
```

# ============================================================

# FASE 13

# ============================================================

def fase13():

```
preparar(13)

state["pistas"] += 3

mostrar("""
```

🐾 FASE 13 — AS PEGADAS

Na manhã seguinte, vocês encontram novas pegadas.

Dessa vez elas são muito maiores.

Barbara se aproxima cuidadosamente.

— Elas vieram da direção da caverna.

Milo observa o caminho.

— Então estamos chegando perto.

As marcas desaparecem perto de uma área cheia de árvores.

Atrás delas existe uma pequena cabana.

Vocês decidem investigar.
""")

```
atualizar_status()

botao("🏚️ Ir até a cabana", fase14)
```

# ============================================================

# FASE 14

# ============================================================

def fase14():

```
preparar(14)

mostrar("""
```

🏚️ FASE 14 — A CABANA

A cabana parece abandonada.

Dentro dela existem objetos antigos, mapas e livros.

Barbara encontra um diário.

Algumas páginas falam sobre a criatura.

Milo lê uma das anotações em voz alta:

"Ela não pode ser detida por métodos comuns."

Outra página diz que existe uma forma de enfraquecê-la.

O segredo parece estar relacionado ao símbolo original
da ilha.

Agora vocês sabem que existe uma maneira de enfrentar
o mistério.
""")

```
pegar("diário")
state["pistas"] += 3

botao("📖 Ler o diário", fase15)
```

# ============================================================

# FASE 15

# ============================================================

def fase15():

```
preparar(15)

state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
```

📖 FASE 15 — O DIÁRIO

O diário conta uma história antiga.

Muitos anos atrás, os moradores descobriram uma criatura
vivendo nas profundezas da ilha.

Ela não era como nenhum animal conhecido.

Os moradores encontraram um símbolo antigo que conseguia
enfraquecer a criatura.

Mas o símbolo acabou sendo escondido.

A última anotação diz:

"Quando a criatura despertar novamente, apenas o símbolo
original poderá revelar sua verdadeira fraqueza."

Milo fecha o diário.

— Então precisamos encontrar esse símbolo.

Barbara concorda.

— E precisamos fazer isso antes de chegar até ela.
""")

```
atualizar_status()

botao("🎒 Procurar os equipamentos", fase16)
```

# ============================================================

# FASE 16

# ============================================================

def fase16():

```
preparar(16)

mostrar("""
```

🎒 FASE 16 — PREPARAÇÃO

Agora vocês sabem que a próxima etapa será perigosa.

Antes de continuar, precisam verificar os equipamentos
encontrados durante a investigação.

Milo organiza os objetos.

Barbara verifica o diário e as pistas.

Existem três caminhos possíveis.

Você pode procurar equipamentos úteis,
buscar algo para recuperar suas forças
ou tentar encontrar diretamente o símbolo antigo.
""")

```
botao("🎒 Procurar equipamentos", fase16_arma)
botao("💊 Procurar medicamentos", fase16_medicamento)
botao("🔱 Procurar o símbolo", fase16_simbolo)
```

def fase16_arma(event):

```
pegar("equipamento")
state["batalha"] += 1

mostrar("""
```

Vocês encontram alguns equipamentos antigos que podem
ser úteis durante a exploração.

Milo verifica tudo cuidadosamente.

— Agora estamos um pouco mais preparados.

Barbara guarda os objetos importantes.

— Ainda precisamos encontrar o símbolo.
""")

```
botao("🌊 Ir para o lago", fase17)
```

def fase16_medicamento(event):

```
pegar("medicamento")

mostrar("""
```

Barbara encontra alguns medicamentos guardados
em uma caixa antiga.

Eles podem ajudar caso alguém se machuque durante
a investigação.

Milo guarda o material.

— Melhor ter isso com a gente.
""")

```
botao("🌊 Ir para o lago", fase17)
```

def fase16_simbolo(event):

```
pegar("símbolo antigo")
state["pistas"] += 3

mostrar("""
```

Depois de procurar entre os objetos antigos,
vocês encontram uma peça com o mesmo desenho
dos símbolos da igreja.

Barbara reconhece imediatamente.

— Esse é o símbolo original.

Milo segura o objeto com cuidado.

— Então finalmente encontramos uma das coisas
que estávamos procurando.
""")

```
botao("🌊 Ir para o lago", fase17)
```

# ============================================================

# FASE 17

# ============================================================

def fase17():

```
preparar(17)

mostrar("""
```

🌊 FASE 17 — O LAGO

O mapa encontrado na cabana indica que existe
outra pista perto de um lago.

Depois de caminhar por algum tempo, vocês chegam
a uma região cercada por pedras.

A água está completamente parada.

Barbara percebe um reflexo estranho no fundo.

Milo aponta para a margem.

— Talvez exista alguma coisa escondida aqui.
""")

```
botao("🌊 Procurar dentro da água", fase17_agua)
botao("🔎 Procurar ao redor", fase17_redor)
botao("➡️ Ignorar o lago", fase17_ignorar)
```

def fase17_agua(event):

```
perder_vida()
pegar("cristal")
state["pistas"] += 2

mostrar("""
```

Você procura dentro da água e encontra um pequeno cristal.

A busca é cansativa e você acaba se machucando levemente
durante a procura.

Quando o cristal é colocado perto do símbolo,
ele começa a refletir uma luz diferente.

Barbara observa surpresa.

— Isso definitivamente não é comum.
""")

```
botao("🕳️ Continuar", fase18)
```

def fase17_redor(event):

```
pegar("cristal")
state["pistas"] += 2

mostrar("""
```

Vocês procuram ao redor do lago.

Atrás de algumas pedras encontram um pequeno cristal.

Milo percebe que ele parece reagir ao símbolo antigo.

Barbara aponta para a direção da floresta.

— Acho que ele está indicando um caminho.
""")

```
botao("🕳️ Continuar", fase18)
```

def fase17_ignorar(event):

```
state["pistas"] += 1

mostrar("""
```

Vocês decidem não investigar o lago profundamente.

Mesmo assim, encontram algumas marcas nas pedras
que indicam que alguém esteve ali recentemente.

As marcas apontam para uma caverna escondida.
""")

```
botao("🕳️ Continuar", fase18)
```

# ============================================================

# FASE 18

# ============================================================

def fase18():

```
preparar(18)

mostrar("""
```

🕳️ FASE 18 — A CAVERNA

O caminho termina diante de uma entrada escondida.

A caverna é escura e parece muito antiga.

Milo olha para dentro.

— É aqui.

Barbara segura o cristal.

Ele começa a emitir um pequeno brilho.

— O símbolo está reagindo.

Agora vocês precisam decidir como entrar.
""")

```
botao("🚪 Entrar na caverna", fase18_entrar)
botao("🔎 Procurar outra entrada", fase18_outra)
```

def fase18_entrar(event):

```
state["pistas"] += 3

mostrar("""
```

Vocês entram diretamente na caverna.

As paredes possuem os mesmos símbolos encontrados
na igreja.

Quanto mais avançam, mais forte fica o brilho do cristal.

Milo percebe que alguns símbolos parecem recentes.

Alguém esteve ali antes de vocês.
""")

```
botao("👹 Continuar", fase19)
```

def fase18_outra(event):

```
state["pistas"] += 1

mostrar("""
```

Vocês procuram uma segunda entrada.

Depois de alguns minutos encontram uma passagem estreita.

Ela leva para dentro da mesma caverna.

Barbara percebe marcas antigas nas paredes.

— Parece que essa passagem era usada pelos moradores.
""")

```
botao("👹 Continuar", fase19)
```

# ============================================================

# FASE 19

# ============================================================

def fase19():

```
preparar(19)

perder_sanidade()

mostrar("""
```

👹 FASE 19 — O PRIMEIRO ENCONTRO

Um rugido ecoa pelas paredes.

Todos param imediatamente.

O brilho do cristal desaparece.

Por alguns segundos, vocês conseguem ver uma enorme
silhueta no final do corredor.

A criatura observa o grupo.

Milo sussurra:

— Não façam movimentos bruscos.

Barbara responde:

— Precisamos sair daqui.

A criatura se aproxima.

Vocês correm de volta pela caverna.

Agora sabem que as histórias eram verdadeiras.
""")

```
botao("🏃 Fugir da criatura", fase20)
```

# ============================================================

# FASE 20

# ============================================================

def fase20():

```
preparar(20)

mostrar("""
```

🏃 FASE 20 — A FUGA

Vocês correm pelos corredores da caverna.

O caminho se divide em três partes.

Atrás de vocês, a criatura continua se aproximando.

Milo grita:

— Precisamos escolher rápido!

Barbara aponta para os caminhos.

— Qualquer um deles pode levar para fora.

Você precisa decidir.
""")

```
botao("⬅️ Esquerda", fase20_esquerda)
botao("➡️ Direita", fase20_direita)
botao("🫣 Procurar um esconderijo", fase20_esconder)
```

def fase20_esquerda(event):

```
state["pistas"] += 1

mostrar("""
```

Vocês seguem pela esquerda.

O caminho parece mais longo, mas vocês encontram
algumas marcas antigas indicando uma saída.
""")

```
botao("🔎 Descobrir a fraqueza", fase21)
```

def fase20_direita(event):

```
state["pistas"] += 2

mostrar("""
```

Vocês seguem pela direita.

O corredor leva até uma sala antiga.

Na parede existe uma inscrição sobre o símbolo original.

Barbara percebe que aquela informação pode ser importante.
""")

```
botao("🔎 Descobrir a fraqueza", fase21)
```

def fase20_esconder(event):

```
ganhar_sanidade()

mostrar("""
```

Vocês encontram uma pequena passagem lateral.

Todos permanecem em silêncio até a criatura passar.

Depois que o som desaparece, vocês continuam.

O susto foi grande, mas agora sabem que precisam
entender a fraqueza da criatura antes de voltar.
""")

```
botao("🔎 Descobrir a fraqueza", fase21)
```

# ============================================================

# FASE 21

# ============================================================

def fase21():

```
preparar(21)

state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
```

🔎 FASE 21 — A FRAQUEZA

Na sala antiga existe uma inscrição enorme.

Barbara começa a traduzir os símbolos.

A mensagem explica que a criatura pode ser enfraquecida
quando o símbolo original da ilha é ativado.

Milo olha para vocês.

— Então agora sabemos como enfrentá-la.

Barbara segura o símbolo.

— Mas precisamos chegar até o esconderijo primeiro.

A inscrição mostra uma passagem escondida.
""")

```
atualizar_status()

botao("🏚️ Seguir para o esconderijo", fase22)
```

# ============================================================

# FASE 22

# ============================================================

def fase22():

```
preparar(22)

mostrar("""
```

🏚️ FASE 22 — O ESCONDERIJO

A passagem leva para uma área subterrânea enorme.

Existem marcas nas paredes e objetos deixados por
antigos moradores.

Milo reconhece alguns símbolos.

— Minha família falava sobre esse lugar.

Barbara encontra uma porta antiga.

— Então o esconderijo deve estar atrás dela.

Vocês se aproximam lentamente.

A criatura está em algum lugar daquele lugar.

Agora não há mais como ignorar o segredo da ilha.
""")

```
botao("🚪 Continuar", fase23)
```

# ============================================================

# FASE 23

# ============================================================

def fase23():

```
preparar(23)

state["pistas"] += 1

mostrar("""
```

🆘 FASE 23 — O RESGATE

Antes de chegar ao esconderijo, vocês escutam uma voz.

É o morador desaparecido.

Ele está escondido em uma pequena sala.

Milo corre até ele.

— Nós estávamos procurando você!

O homem explica que foi levado para aquele lugar
e conseguiu escapar.

Ele está assustado.

— Vocês precisam ir embora.

Barbara pergunta:

— O que aconteceu?

O homem olha para o corredor.

— Ela está acordada.

Agora vocês precisam decidir o que fazer com ele.
""")

```
botao("🚶 Levar o homem embora", fase24)
botao("🫣 Deixá-lo escondido", fase24)
```

# ============================================================

# FASE 24

# ============================================================

def fase24():

```
preparar(24)

mostrar("""
```

🚪 FASE 24 — A ENTRADA

Vocês encontram uma enorme porta de pedra.

No centro existe um símbolo idêntico ao símbolo original.

Milo se aproxima.

— Essa deve ser a entrada do esconderijo.

Barbara observa o desenho.

— Se tivermos o símbolo certo, talvez consigamos abrir
sem fazer barulho.

Você verifica seu inventário.
""")

```
if "símbolo antigo" in state["inv"]:

    state["pistas"] += 3

    mostrar("""
```

O símbolo encaixa perfeitamente.

A porta começa a se mover.

Um brilho aparece nas paredes.

Por alguns segundos, ninguém fala nada.

A passagem finalmente se abre.
""")

```
else:

    perder_vida()

    mostrar("""
```

Vocês não possuem o símbolo necessário.

Depois de algum esforço, conseguem abrir uma passagem.

O barulho ecoa pelo subterrâneo.

Milo olha preocupado.

— Agora ela sabe que estamos aqui.
""")

```
atualizar_status()

botao("🚪 Entrar no esconderijo", fase25)
```

# ============================================================

# FASE 25

# ============================================================

def fase25():

```
preparar(25)

state["pistas"] += 4

mostrar("""
```

📜 FASE 25 — O PASSADO DA FAMÍLIA

Dentro do esconderijo existem documentos muito antigos.

Vocês começam a procurar informações sobre a criatura.

Então encontram algo inesperado.

Os documentos falam sobre a família de Olivier e Amelie.

O parente desaparecido esteve naquela mesma ilha muitos
anos atrás.

Ele descobriu a existência da criatura e tentou impedir
que ela fosse libertada.

Uma das últimas anotações diz:

"Se alguém da minha família encontrar este lugar,
precisará terminar o que eu comecei."

Barbara fica emocionada.

— Então ele não desapareceu por acaso.

Milo completa:

— Ele estava tentando proteger a ilha.

Agora vocês entendem por que os documentos foram
escondidos durante tantos anos.
""")

```
atualizar_status()

botao("⚔️ Preparar para o confronto", fase26)
```

# ============================================================

# FASE 26

# ============================================================

def fase26():

```
preparar(26)

mostrar("""
```

⚔️ FASE 26 — PREPARAÇÃO

A criatura está próxima.

Vocês precisam organizar tudo o que descobriram.

O símbolo antigo pode ser a principal esperança.

O cristal também parece reagir à presença da criatura.

O diário contém informações importantes.

Milo e Barbara estão prontos para ajudar.

Como vocês querem se preparar?
""")

```
botao("🎒 Organizar equipamentos", fase26_arma)
botao("🔱 Preparar o símbolo", fase26_simbolo)
botao("📖 Revisar as informações", fase26_info)
```

def fase26_arma(event):

```
if "equipamento" in state["inv"]:

    state["batalha"] += 1

    mostrar("""
```

Vocês organizam os equipamentos encontrados durante
a investigação.

Tudo está preparado para a exploração final.

Milo verifica se nada importante foi esquecido.

— Agora podemos continuar.
""")

```
else:

    mostrar("""
```

Vocês verificam os equipamentos disponíveis.

Mesmo sem ter encontrado tudo, vocês decidem continuar.

Barbara segura o diário.

— O símbolo continua sendo nossa principal pista.
""")

```
botao("👹 Ir até a criatura", fase27)
```

def fase26_simbolo(event):

```
if "símbolo antigo" in state["inv"]:

    state["batalha"] += 2

    mostrar("""
```

O símbolo reage imediatamente quando vocês o retiram
do inventário.

As marcas nas paredes começam a brilhar.

Barbara percebe:

— Ele está funcionando.

Milo respira fundo.

— Então essa pode ser nossa melhor chance.
""")

```
else:

    mostrar("""
```

Vocês procuram pelo símbolo, mas percebem que ele
não está com vocês.

Barbara decide confiar nas informações do diário.
""")

```
botao("👹 Ir até a criatura", fase27)
```

def fase26_info(event):

```
state["monstro_fraqueza"] = True
state["batalha"] += 2

mostrar("""
```

Vocês revisam todas as pistas.

O diário, o cristal e as inscrições contam a mesma história.

A criatura fica mais fraca quando o símbolo original
é ativado.

Agora vocês entendem exatamente o que precisam fazer.

Milo olha para vocês.

— Vamos terminar isso.
""")

```
botao("👹 Ir até a criatura", fase27)
```

# ============================================================

# FASE 27

# ============================================================

def fase27():

```
preparar(27)

mostrar("""
```

👹 FASE 27 — O MONSTRO

Vocês chegam à última sala.

O espaço é enorme.

No centro existe uma grande estrutura cercada
pelos mesmos símbolos encontrados na igreja.

A criatura está ali.

Ela observa o grupo em silêncio.

Milo dá um passo à frente.

— É aqui que tudo termina.

Barbara segura o símbolo.

— Ou começa uma nova história.

A criatura se movimenta.

Todos se preparam.

É hora de decidir como agir.
""")

```
botao("⚔️ Enfrentar a criatura", fase28)
```

# ============================================================

# FASE 28

# ============================================================

def fase28():

```
preparar(28)

mostrar("""
```

⚔️ FASE 28 — O CONFRONTO

A criatura começa a avançar.

Vocês precisam trabalhar juntos.

Existem quatro maneiras de agir.

Cada escolha pode aumentar a confiança do grupo
ou ajudar a enfraquecer a criatura.

Escolha cuidadosamente.
""")

```
botao("⚔️ Tentar atacar", fase28_atacar)
botao("🔱 Ativar o símbolo", fase28_simbolo)
botao("🛡️ Ajudar Milo", fase28_milo)
botao("🛡️ Ajudar Barbara", fase28_barbara)
```

def fase28_atacar(event):

```
if "equipamento" in state["inv"] and state["monstro_fraqueza"]:

    state["batalha"] += 3

    mostrar("""
```

Vocês aproveitam o momento em que a criatura está
enfraquecida e avançam juntos.

A estratégia funciona.

A criatura recua.

Milo grita:

— Continue!

Vocês percebem que estão finalmente conseguindo
enfraquecê-la.
""")

```
else:

    perder_vida()

    mostrar("""
```

Vocês tentam avançar, mas a criatura é mais resistente
do que esperavam.

O grupo precisa recuar.

Barbara percebe que o símbolo ainda é a melhor esperança.
""")

```
botao("🔥 Fazer a última escolha", fase29)
```

def fase28_simbolo(event):

```
if "símbolo antigo" in state["inv"]:

    state["batalha"] += 4
    state["monstro_fraqueza"] = True

    mostrar("""
```

Você ergue o símbolo antigo.

Os desenhos nas paredes começam a brilhar.

A criatura recua.

O cristal também começa a emitir luz.

Barbara percebe:

— Está funcionando!

Milo olha para você.

— Agora temos uma chance.
""")

```
else:

    perder_sanidade()

    mostrar("""
```

Você tenta ativar o símbolo, mas percebe que ele
não está com você.

A criatura continua avançando.

Vocês precisam pensar em outra estratégia.
""")

```
botao("🔥 Fazer a última escolha", fase29)
```

def fase28_milo(event):

```
if state["milo_vivo"]:

    state["confianca_milo"] += 2
    state["batalha"] += 2

    mostrar("""
```

Você ajuda Milo a se posicionar.

Ele consegue se concentrar na investigação dos símbolos.

Milo olha para você.

— Obrigado por confiar em mim.

Juntos, vocês conseguem ganhar alguns segundos
para continuar a investigação.
""")

```
botao("🔥 Fazer a última escolha", fase29)
```

def fase28_barbara(event):

```
if state["barbara_viva"]:

    state["confianca_barbara"] += 2
    state["batalha"] += 2

    mostrar("""
```

Você ajuda Barbara a chegar até uma das inscrições.

Ela percebe um detalhe que ninguém havia notado.

— Existe outro símbolo aqui!

A descoberta ajuda o grupo a entender melhor
como enfraquecer a criatura.

Barbara sorri.

— Eu sabia que podíamos confiar uns nos outros.
""")

```
botao("🔥 Fazer a última escolha", fase29)
```

# ============================================================

# FASE 29 — ÚLTIMA ESCOLHA

# ============================================================

def fase29():

```
preparar(29)

mostrar("""
```

🔥 FASE 29 — A ÚLTIMA ESCOLHA

A criatura está enfraquecida.

Depois de tudo que vocês descobriram,
a verdade sobre a ilha finalmente está diante de vocês.

Milo olha para Barbara.

Barbara olha para o símbolo.

Vocês têm apenas uma última decisão.

O que fazer?
""")

```
botao("✨ Tentar derrotar a criatura", fase29_derrotar)
botao("🔒 Selar a criatura novamente", fase29_selar)
botao("🏃 Fugir da ilha", fase29_fugir)
```

def fase29_derrotar(event):

```
if state["batalha"] >= 5 and state["monstro_fraqueza"]:

    state["monstro_derrotado"] = True

    mostrar("""
```

O símbolo começa a brilhar intensamente.

A criatura perde sua força.

As inscrições nas paredes iluminam toda a sala.

Depois de anos de medo, o segredo finalmente chega
ao fim.

A ilha está livre.
""")

```
else:

    state["monstro_derrotado"] = False

    mostrar("""
```

Vocês tentam derrotar a criatura, mas percebem que
ainda não conseguiram enfraquecê-la o suficiente.

A criatura recua para as profundezas.

Vocês precisam escapar enquanto ainda podem.
""")

```
fase30()
```

def fase29_selar(event):

```
state["monstro_derrotado"] = False
state["batalha"] = max(state["batalha"], 3)

mostrar("""
```

Vocês decidem não destruir a criatura.

Em vez disso, usam os símbolos antigos para selar
novamente a passagem.

A criatura desaparece nas profundezas.

A ilha fica silenciosa.

Mas vocês sabem que o segredo ainda existe.

Talvez um dia alguém volte para descobrir o que
realmente aconteceu.
""")

```
fase30()
```

def fase29_fugir(event):

```
state["monstro_derrotado"] = False
state["vida"] = max(state["vida"], 1)

mostrar("""
```

Vocês percebem que continuar seria arriscado demais.

Milo guia o grupo de volta pelos túneis.

Barbara encontra o caminho de saída.

Quando vocês chegam ao lado de fora,
a ilha começa a ficar para trás.

Vocês sobreviveram.

Mas a criatura continua escondida.

E o segredo da ilha permanece.
""")

```
fase30()
```

# ============================================================

# FASE 30 — FINAIS

# ============================================================

def fase30():

```
limpar()

vivos = []

if state["milo_vivo"]:
    vivos.append("Milo")

if state["barbara_viva"]:
    vivos.append("Barbara")

if state["personagem"] == "Olivier":

    if state["olivier_vivo"]:
        vivos.append("Olivier")

else:

    if state["amelie_viva"]:
        vivos.append("Amelie")


# FINAL 1
if state["monstro_derrotado"] and len(vivos) >= 3:

    mudar_imagem("final_01.png")

    mostrar("""
```

🌟 FINAL PERFEITO

A criatura finalmente é derrotada.

Milo e Barbara conseguem deixar o esconderijo
junto com você.

O segredo da ilha foi descoberto.

Os documentos provam que seu parente tentou proteger
a ilha muitos anos atrás.

Agora a história dele finalmente pode ser contada.

A vila começa a mudar.

Os moradores já não precisam viver com medo.

Depois de tantos anos, a ilha finalmente pode ter paz.
""")

```
# FINAL 2
elif state["monstro_derrotado"]:

    mudar_imagem("final_02.png")

    mostrar("""
```

🌅 FINAL DA VITÓRIA

A criatura foi derrotada.

Porém, nem todos conseguiram terminar a investigação
juntos.

Os sobreviventes deixam a ilha levando os documentos
e as provas encontradas.

A verdade sobre a criatura finalmente poderá ser revelada.

Mas algumas perguntas continuam sem resposta.

Sobreviventes:
""" + ", ".join(vivos))

```
# FINAL 3
elif state["batalha"] >= 3:

    mudar_imagem("final_03.png")

    mostrar("""
```

👁️ FINAL DO SELAMENTO

Vocês conseguem selar a criatura novamente.

A ilha volta a ficar silenciosa.

Milo e Barbara sabem que o perigo não desapareceu
completamente.

O segredo continua escondido nas profundezas.

Talvez o selo dure muitos anos.

Talvez não.

Por enquanto, a ilha está segura.
""")

```
# FINAL 4
elif state["vida"] > 0:

    mudar_imagem("final_06.png")

    mostrar("""
```

🏃 FINAL DA FUGA

Vocês conseguem chegar ao barco.

A ilha fica cada vez menor no horizonte.

Milo e Barbara permanecem na ilha,
pois aquele lugar sempre foi a casa deles.

Você leva consigo as pistas e os documentos
encontrados durante a investigação.

A criatura ainda está viva.

E o segredo continua enterrado.

Talvez um dia alguém volte.
""")

```
# FINAL 5
else:

    mudar_imagem(
        "Gemini_Generated_Image_l0ib99l0ib99l0ib.png"
    )

    mostrar("""
```

💀 FINAL DA ILHA

A investigação chega ao fim.

A criatura continua escondida nas profundezas
da ilha.

O segredo permanece desconhecido.

Os documentos encontrados desaparecem junto
com a antiga história.

A ilha continua guardando seus mistérios.

E ninguém sabe o que acontecerá quando
alguém tentar descobri-los novamente.
""")

```
mostrar("""
```

============================================================

🎮 FIM DO JOGO

============================================================
""")

```
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
    ", ".join(state["inv"])
)

botao(
    "🔄 Jogar novamente",
    reiniciar
)
```

# ============================================================

# REINICIAR

# ============================================================

def reiniciar(event):

```
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

fase1()
```

# ============================================================

# COMEÇAR O JOGO

# ============================================================

fase1()
