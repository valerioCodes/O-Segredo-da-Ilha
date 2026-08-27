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

# =========================

# FASE 1

# =========================

def fase1(event=None):
preparar(1)

```
mostrar("""
🏝️ O SEGREDO NA ILHA

Depois de muitos anos sem notícias de um antigo
parente, Olivier e Amelie encontram documentos
antigos relacionados à própria família.

Os documentos mencionam uma pequena ilha afastada
do continente.

Algumas páginas falam sobre desaparecimentos,
símbolos misteriosos e uma antiga construção
escondida nas profundezas da ilha.

Curiosos para descobrir o que realmente aconteceu,
Olivier e Amelie embarcam em uma pequena viagem.

Enquanto o barco se aproxima da ilha, os dois
observam a costa pela primeira vez.

Eles ainda não sabem que aquele lugar guarda
um segredo que envolve sua própria família.

Na ilha, Milo e Barbara já vivem há muitos anos.

Eles conhecem a vila, as trilhas, as histórias
antigas e os lugares que os visitantes normalmente
não encontram.

Agora Olivier e Amelie finalmente estão chegando.

Escolha quem será o personagem principal.
""")

criar_botao("🧑 Olivier", escolher_olivier)
criar_botao("👩 Amelie", escolher_amelie)
```

def escolher_olivier(event):
state["personagem"] = "Olivier"
fase2()

def escolher_amelie(event):
state["personagem"] = "Amelie"
fase2()

# =========================

# FASE 2

# =========================

def fase2(event=None):
preparar(2)

```
mostrar("""
🚢 A CHEGADA

Depois de algumas horas de viagem, o barco finalmente
chega ao pequeno porto da ilha.

Olivier e Amelie desembarcam carregando seus poucos
pertences e os documentos encontrados antes da viagem.

Na praia, duas pessoas esperam por eles.

São Milo e Barbara.

Os dois já moram na ilha há muitos anos e conhecem
praticamente todos os seus caminhos.

Milo se aproxima primeiro.

— Vocês devem ser os visitantes que estavam chegando.

Barbara observa os documentos que Olivier e Amelie
trouxeram.

— Vocês vieram procurar alguém da família?

Olivier e Amelie percebem que talvez tenham chegado
ao lugar certo.

A investigação está apenas começando.
""")

criar_botao("🗣️ Conversar com Milo", fase3_milo)
criar_botao("🗣️ Conversar com Barbara", fase3_barbara)
```

# =========================

# FASE 3

# =========================

def fase3_milo(event):
state["confianca_milo"] += 1
state["pistas"] += 1

```
preparar(3)

mostrar("""
🗣️ MILO

Milo conta que sua família vive na ilha há gerações.

Por conhecer a região desde criança, ele sabe onde
ficam as antigas trilhas, casas abandonadas e lugares
que quase ninguém visita.

— Se vocês estão procurando respostas, talvez eu possa
ajudar.

Milo explica que algumas pessoas desapareceram ao
longo dos anos.

Segundo as histórias que ouviu de sua família,
alguns desses desaparecimentos aconteceram perto
de uma região antiga da ilha.

— Ninguém gosta de chegar perto daquele lugar.

Olivier pergunta se ele sabe o motivo.

Milo fica em silêncio por alguns segundos.

— Porque dizem que alguma coisa vive lá.

A primeira grande pista aparece.
""")

criar_botao("➡️ Continuar", fase4)
```

def fase3_barbara(event):
state["confianca_barbara"] += 1
state["pistas"] += 1

```
preparar(3)

mostrar("""
🗣️ BARBARA

Barbara conta que sua família também vive na ilha
há várias gerações.

Desde criança, ela ouve histórias sobre símbolos
antigos encontrados em diferentes lugares.

Segundo sua avó, esses símbolos serviam para
proteger a ilha de alguma coisa.

Barbara olha novamente para os documentos.

— Talvez sua família tenha deixado alguma coisa aqui.

Ela explica que algumas histórias antigas foram
escondidas pelos moradores porque ninguém queria
falar sobre elas.

Entre essas histórias existe uma sobre uma criatura
que estaria escondida nas profundezas da ilha.

Talvez os documentos de Olivier e Amelie estejam
relacionados a tudo isso.
""")

criar_botao("➡️ Continuar", fase4)
```

# =========================

# FASE 4

# =========================

def fase4(event=None):
preparar(4)

```
mostrar("""
🏘️ A VILA

Milo e Barbara mostram a vila para Olivier e Amelie.

Apesar de pequena, a ilha possui alguns lugares
muito antigos.

Milo aponta para três construções.

A primeira é uma igreja abandonada.

A segunda é uma casa que está vazia há muitos anos.

A terceira é um velho farol construído perto das
pedras da costa.

Barbara explica que cada um desses lugares pode
esconder uma pista.

Vocês precisam decidir por onde começar.
""")

criar_botao("⛪ Ir para a igreja", fase5)
criar_botao("🏚️ Ir para a casa abandonada", fase6)
criar_botao("🔦 Ir para o farol", fase7)
```

# =========================

# FASE 5

# =========================

def fase5(event=None):
preparar(5)

```
mostrar("""
⛪ A IGREJA

A igreja está abandonada há muitos anos.

O lugar é silencioso e algumas partes do teto
já estão danificadas.

Nas paredes existem vários símbolos antigos.

Barbara reconhece alguns deles.

— Minha família falava sobre esses símbolos.

Milo observa as paredes com atenção.

— Eu nunca tinha reparado que havia tantos.

Talvez a igreja esconda uma pista importante.
""")

criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
criar_botao("📖 Procurar documentos", fase5_documentos)
```

def fase5_simbolos(event):
state["pistas"] += 2
pegar("fotografia dos símbolos")

```
mostrar("""
🔎 OS SÍMBOLOS

Os símbolos parecem formar uma espécie de caminho.

Barbara percebe que alguns desenhos apontam para
a direção da floresta.

Olivier registra os símbolos para estudar depois.

Um dos desenhos parece representar uma criatura
cercada por marcas antigas.

Milo fica preocupado.

— Acho melhor não ignorarmos isso.

A fotografia dos símbolos pode ajudar vocês
mais tarde.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase5_documentos(event):
state["pistas"] += 3
pegar("livro antigo")

```
mostrar("""
📖 O LIVRO ANTIGO

Atrás de um banco antigo vocês encontram um livro.

As páginas estão amareladas e algumas palavras
quase desapareceram com o tempo.

O livro fala sobre uma criatura que estaria escondida
nas profundezas da ilha.

Uma das páginas menciona um símbolo capaz de
enfraquecê-la.

Barbara percebe que o símbolo é parecido com os
desenhos encontrados nas paredes.

Essa informação pode ser muito importante.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

# =========================

# FASE 6

# =========================

def fase6(event=None):
preparar(6)

```
mostrar("""
🏚️ A CASA ABANDONADA

Milo leva vocês até uma casa abandonada.

O antigo morador desapareceu muitos anos atrás.

O lugar está cheio de poeira, móveis antigos
e objetos esquecidos.

Dentro da casa existem documentos, fotografias
e caixas fechadas.

Talvez alguma dessas coisas explique o passado
da ilha.
""")

criar_botao("📄 Procurar documentos", fase6_documentos)
criar_botao("⬆️ Subir as escadas", fase6_escadas)
criar_botao("⬇️ Investigar o porão", fase6_porao)
```

def fase6_documentos(event):
state["pistas"] += 3
pegar("documentos da família")

```
mostrar("""
📄 OS DOCUMENTOS

Entre os documentos aparece o sobrenome da família
de Olivier e Amelie.

Barbara fica surpresa.

— Então sua família realmente esteve aqui.

Os documentos mostram que um antigo integrante da
família pesquisava os símbolos e os desaparecimentos
da ilha.

Uma anotação diz que ele estava procurando uma
passagem escondida.

Agora existe uma ligação clara entre vocês
e o passado da ilha.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase6_escadas(event):
state["pistas"] += 2
pegar("fotografia antiga")

```
mostrar("""
🖼️ A FOTOGRAFIA

No andar de cima vocês encontram uma fotografia.

Ela mostra algumas pessoas diante da floresta.

Uma delas parece ser o parente desaparecido.

Milo reconhece o lugar.

— Eu sei onde isso foi tirado.

A fotografia pode ajudar a descobrir
para onde o grupo deve ir.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase6_porao(event):
state["pistas"] += 3
pegar("fotografia antiga")

```
mostrar("""
📦 O PORÃO

No porão existe uma caixa escondida.

Dentro dela há uma fotografia antiga.

No verso está escrito:

"Aquilo que está abaixo da ilha nunca deve ser despertado."

Barbara percebe que a mensagem combina com
as histórias que sua família contava.

O segredo parece estar relacionado às cavernas
existentes abaixo da ilha.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

# =========================

# FASE 7

# =========================

def fase7(event=None):
preparar(7)

```
state["pistas"] += 3
pegar("fotografia da criatura")

mostrar("""
🔦 O FAROL

O farol abandonado fica no alto de uma região
rochosa.

Milo conhece o caminho e acompanha vocês.

Depois de subir os degraus antigos, vocês encontram
uma pequena caixa.

Dentro dela há uma fotografia.

Ao fundo aparece uma figura estranha.

Barbara fica em silêncio por alguns segundos.

— Então as histórias podem ser verdadeiras.

Pela primeira vez, todos percebem que talvez
estejam procurando algo que realmente existe.
""")

atualizar_status()
criar_botao("🌙 Continuar", fase8)
```

# =========================

# FASE 8

# =========================

def fase8(event=None):
preparar(8)

```
mostrar("""
🌙 A PRIMEIRA NOITE

A investigação demora mais do que esperavam.

A noite chega e Milo e Barbara levam Olivier
e Amelie para uma casa segura na vila.

Durante a madrugada, alguém bate na janela.

TOC.

TOC.

TOC.

Milo pede para ninguém abrir.

Barbara olha pela janela sem se aproximar demais.

— Talvez seja melhor esperar até amanhecer.

O que vocês fazem?
""")

criar_botao("🪟 Abrir a janela", fase8_janela)
criar_botao("😶 Ignorar", fase8_ignorar)
```

def fase8_janela(event):
perder_sanidade()
state["pistas"] += 2

```
mostrar("""
🪟 A JANELA

Você abre a janela.

Não há ninguém do lado de fora.

Porém, algumas marcas podem ser vistas no chão.

Milo se aproxima para observar.

— Eu já vi essas marcas antes.

Barbara olha para a direção da floresta.

— Então ela voltou.

A descoberta deixa todos ainda mais preocupados.
""")

criar_botao("🌅 Continuar", fase9)
```

def fase8_ignorar(event):
state["pistas"] += 1

```
mostrar("""
🌙 O SILÊNCIO

Vocês decidem ignorar as batidas.

Ninguém consegue dormir direito.

Quando amanhece, novas marcas aparecem no chão
perto da casa.

Alguma coisa esteve ali durante a noite.

Milo olha para a floresta.

— Precisamos descobrir o que está acontecendo.
""")

atualizar_status()
criar_botao("🌅 Continuar", fase9)
```

# =========================

# FASE 9

# =========================

def fase9(event=None):
preparar(9)

```
mostrar("""
🚨 O DESAPARECIMENTO

Na manhã seguinte, um morador desaparece.

Milo conhece o homem e fica preocupado.

Barbara começa a procurar informações pela vila.

As marcas encontradas durante a noite podem estar
relacionadas ao desaparecimento.

Vocês precisam decidir por onde procurar.
""")

criar_botao("🏘️ Procurar na vila", fase9_vila)
criar_botao("🌲 Procurar na floresta", fase9_floresta)
```

def fase9_vila(event):
state["pistas"] += 1

```
mostrar("""
🏘️ A VILA

Vocês procuram pela vila.

Algumas marcas aparecem perto da saída.

Elas seguem para fora da região habitada.

Milo aponta para a floresta.

— Ele provavelmente foi naquela direção.

A investigação continua.
""")

atualizar_status()
criar_botao("🔎 Continuar", fase10)
```

def fase9_floresta(event):
state["pistas"] += 2

```
mostrar("""
🌲 A FLORESTA

Vocês seguem as marcas diretamente para a floresta.

As pegadas parecem recentes.

Barbara encontra um pequeno objeto no caminho.

Milo reconhece o objeto.

— Isso pertence ao homem desaparecido.

Agora vocês têm uma pista concreta.
""")

atualizar_status()
criar_botao("🔎 Continuar", fase10)
```

# =========================

# FASE 10

# =========================

def fase10(event=None):
preparar(10)

```
pegar("objeto do desaparecido")
state["pistas"] += 2

mostrar("""
🔎 A INVESTIGAÇÃO

As marcas continuam pela floresta.

Depois de algum tempo vocês encontram outro objeto
pertencente ao desaparecido.

Milo reconhece imediatamente.

— Isso é dele.

A trilha continua em direção a uma região mais
afastada da ilha.

O grupo decide continuar.
""")

atualizar_status()
criar_botao("🌲 Continuar", fase11)
```

# =========================

# FASE 11

# =========================

def fase11(event=None):
preparar(11)

```
mostrar("""
🌲 A FLORESTA

Milo lidera o grupo.

Como mora na ilha desde criança, ele conhece
muitos dos caminhos escondidos.

Uma trilha estreita aparece entre as árvores.

No final dela existe uma pequena cabana.

Barbara percebe que o lugar aparece em uma
das fotografias encontradas anteriormente.

Vocês decidem investigar.
""")

criar_botao("🥾 Seguir a trilha", fase12)
```

# =========================

# FASE 12

# =========================

def fase12(event=None):
preparar(12)

```
mostrar("""
🔥 O ACAMPAMENTO

A noite chega antes que vocês consigam voltar.

O grupo monta um pequeno acampamento.

Milo conta histórias que ouviu do avô.

Barbara explica que os símbolos antigos podem
estar relacionados à criatura.

Olivier e Amelie percebem que cada pista encontrada
parece fazer parte de uma mesma história.

Todos entendem que estão cada vez mais perto
da verdade.
""")

criar_botao("🌅 Continuar", fase13)
```

# =========================

# FASE 13

# =========================

def fase13(event=None):
preparar(13)

```
state["pistas"] += 2

mostrar("""
🐾 AS PEGADAS

Na manhã seguinte, novas pegadas aparecem.

Elas são muito maiores do que pegadas humanas.

Milo observa o chão com atenção.

— Elas vão naquela direção.

Entre as árvores aparece uma pequena cabana.

A construção parece abandonada.

Vocês seguem até lá para descobrir o que existe
dentro dela.
""")

atualizar_status()
criar_botao("🏚️ Ir para a cabana", fase14)
```

# =========================

# FASE 14

# =========================

def fase14(event=None):
preparar(14)

```
pegar("diário")
state["pistas"] += 3

mostrar("""
📖 A CABANA

Dentro da cabana existem mapas, livros e objetos
antigos.

Barbara encontra um diário escondido.

O diário fala sobre uma criatura escondida
nas profundezas da ilha.

Também menciona um símbolo capaz de enfraquecê-la.

Milo olha para Barbara.

— Então alguém já tentou enfrentar isso antes.

Agora vocês possuem uma pista muito importante.
""")

atualizar_status()
criar_botao("📖 Ler o diário", fase15)
```

# =========================

# FASE 15

# =========================

def fase15(event=None):
preparar(15)

```
state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
📖 O DIÁRIO

O diário revela que antigos moradores descobriram
uma criatura nas profundezas da ilha.

Eles descobriram que um símbolo antigo poderia
enfraquecê-la.

O símbolo foi escondido para que ninguém pudesse
usá-lo de maneira errada.

A última anotação diz:

"Se alguém da minha família encontrar este lugar,
deverá terminar o que comecei."

Olivier e Amelie percebem que talvez a mensagem
tenha sido deixada justamente para alguém como eles.

Talvez o passado de sua família seja a chave
para resolver o mistério.
""")

atualizar_status()
criar_botao("🎒 Preparar equipamentos", fase16)
```

# =========================

# FASE 16

# =========================

def fase16(event=None):
preparar(16)

```
mostrar("""
🎒 PREPARAÇÃO

Agora vocês sabem que a criatura existe.

Antes de continuar, o grupo organiza tudo o que
encontrou durante a investigação.

Milo verifica os equipamentos.

Barbara revisa as pistas.

Olivier e Amelie conferem os documentos.

Vocês precisam decidir como se preparar.
""")

criar_botao("🎒 Organizar equipamentos", fase16_equipamentos)
criar_botao("🔱 Preparar o símbolo", fase16_simbolo)
```

def fase16_equipamentos(event):
pegar("equipamento")
state["batalha"] += 2

```
mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam os equipamentos.

Milo verifica tudo cuidadosamente.

Barbara guarda as pistas mais importantes.

O grupo está mais preparado para continuar
a investigação.

Mesmo assim, ninguém sabe exatamente o que
encontrará no final.
""")

atualizar_status()
criar_botao("🌊 Continuar", fase17)
```

def fase16_simbolo(event):
pegar("símbolo antigo")
state["monstro_fraqueza"] = True
state["batalha"] += 3

```
mostrar("""
🔱 O SÍMBOLO

Entre os objetos antigos vocês encontram
o símbolo original.

Barbara reconhece imediatamente o desenho.

— É exatamente o símbolo descrito no diário.

Milo percebe que ele pode ser a chave para
enfrentar a criatura.

Agora vocês possuem algo que pode fazer
diferença no confronto.
""")

atualizar_status()
criar_botao("🌊 Continuar", fase17)
```

# =========================

# FASE 17

# =========================

def fase17(event=None):
preparar(17)

```
mostrar("""
🌊 O LAGO

As pistas levam vocês até um lago escondido.

Perto da margem existe um pequeno cristal.

Barbara percebe que ele reage ao símbolo antigo.

O cristal pode ter alguma ligação com a criatura.

Vocês precisam decidir o que fazer.
""")

criar_botao("🔎 Pegar o cristal", fase17_cristal)
criar_botao("➡️ Continuar", fase18)
```

def fase17_cristal(event):
pegar("cristal")
state["pistas"] += 2
state["batalha"] += 1

```
mostrar("""
💎 O CRISTAL

Você pega o cristal.

Ele reage imediatamente ao símbolo antigo.

Uma luz percorre as pedras próximas.

Barbara percebe que o cristal parece fazer parte
do mesmo sistema de proteção descrito no diário.

A conexão entre o cristal, o símbolo e a criatura
parece cada vez mais clara.
""")

atualizar_status()
criar_botao("🕳️ Continuar", fase18)
```

# =========================

# FASE 18

# =========================

def fase18(event=None):
preparar(18)

```
mostrar("""
🕳️ A CAVERNA

O caminho termina diante de uma enorme caverna.

Milo reconhece o lugar.

— Meu avô falava dessa caverna.

Nas paredes existem os mesmos símbolos encontrados
na igreja.

Barbara compara os desenhos com as fotografias.

Eles parecem formar um caminho.

O grupo entra na caverna.
""")

criar_botao("🚪 Entrar na caverna", fase19)
```

# =========================

# FASE 19

# =========================

def fase19(event=None):
preparar(19)

```
perder_sanidade()

mostrar("""
👹 O PRIMEIRO ENCONTRO

Um som estranho ecoa pela caverna.

O grupo para imediatamente.

Uma enorme silhueta aparece no fim do corredor.

Barbara reconhece os símbolos nas paredes.

Milo finalmente entende o que está acontecendo.

— A criatura existe.

Todos percebem que ainda não estão preparados
para enfrentá-la.

A única opção é voltar e descobrir uma maneira
de enfrentá-la.
""")

criar_botao("🏃 Fugir", fase20)
```

# =========================

# FASE 20

# =========================

def fase20(event=None):
preparar(20)

```
mostrar("""
🏃 A FUGA

O grupo corre pelos corredores da caverna.

Milo usa seu conhecimento da ilha para encontrar
uma saída.

Depois de algum tempo, vocês conseguem escapar.

Ninguém está disposto a voltar para aquela sala
sem entender como derrotar a criatura.

Agora vocês precisam descobrir a verdadeira
fraqueza dela.
""")

criar_botao("🔎 Descobrir a fraqueza", fase21)
```

# =========================

# FASE 21

# =========================

def fase21(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
🔎 A FRAQUEZA

Depois de comparar o diário, os símbolos e o cristal,
Barbara finalmente entende a mensagem.

A criatura pode ser enfraquecida.

O símbolo original é a chave.

Milo respira fundo.

— Então podemos tentar.

Olivier e Amelie percebem que a investigação
finalmente chegou ao ponto mais importante.

Vocês voltam para a região do esconderijo.
""")

criar_botao("🏚️ Ir para o esconderijo", fase22)
```

# =========================

# FASE 22

# =========================

def fase22(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
🏚️ O ESCONDERIJO

As pistas levam vocês para uma região subterrânea.

Ali existem documentos antigos e inscrições
cobrindo as paredes.

Tudo indica que aquele lugar foi usado para
esconder informações sobre a criatura.

No final do corredor existe uma grande porta.

O segredo está atrás dela.
""")

criar_botao("🚪 Abrir a porta", fase23)
```

# =========================

# FASE 23

# =========================

def fase23(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
🆘 O RESGATE

Antes de chegar à sala principal, vocês encontram
o morador desaparecido.

Milo corre para ajudá-lo.

O homem explica que foi levado para a caverna.

Ele conseguiu escapar e encontrou aquele esconderijo.

— Ela está acordada — ele avisa.

Barbara pergunta se ele sabe onde fica a criatura.

O homem aponta para uma passagem.

— Está além daquela porta.

Vocês precisam continuar.
""")

criar_botao("🚶 Levar o homem embora", fase24)
```

# =========================

# FASE 24

# =========================

def fase24(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
state["pistas"] += 1

mostrar("""
🚪 A ENTRADA

Milo ajuda o homem a sair.

Barbara encontra uma passagem segura para levá-lo
de volta à vila.

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

    A porta começa a se mover lentamente.

    Uma passagem escura aparece.

    Vocês estão muito perto do segredo.
    """)
else:
    mostrar("""
    ⚠️ A PASSAGEM

    Vocês não possuem o símbolo original.

    Mesmo assim, encontram uma passagem lateral
    escondida nas paredes.

    O caminho parece perigoso, mas é a única
    maneira de continuar.
    """)

criar_botao("🚪 Entrar", fase25)
```

# =========================

# FASE 25

# =========================

def fase25(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
state["pistas"] += 3

mostrar("""
📜 O PASSADO

Dentro do esconderijo vocês encontram documentos.

Eles confirmam que o parente de Olivier e Amelie
esteve na ilha.

Ele descobriu a criatura e tentou impedir que ela
voltasse a ameaçar os moradores.

Entre os documentos existe uma anotação:

"Se alguém da minha família encontrar este lugar,
precisará terminar o que comecei."

Agora vocês entendem por que os documentos
foram escondidos.

O mistério da família e o segredo da ilha
estão completamente ligados.
""")

criar_botao("⚔️ Continuar", fase26)
```

# =========================

# FASE 26

# =========================

def fase26(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
⚔️ A PREPARAÇÃO FINAL

A criatura está próxima.

Milo e Barbara estão prontos para ajudar.

O símbolo antigo pode ser usado para enfraquecê-la.

O cristal também pode ajudar.

O grupo se prepara para o confronto final.

Antes de seguir, vocês precisam escolher
como se preparar.
""")

criar_botao("🔱 Preparar o símbolo", fase26_simbolo)
criar_botao("🎒 Organizar equipamentos", fase26_equipamentos)
```

def fase26_simbolo(event):
if "símbolo antigo" in state["inv"]:
state["batalha"] += 3
state["monstro_fraqueza"] = True

```
    mostrar("""
    🔱 O SÍMBOLO

    O símbolo começa a reagir.

    Se vocês também encontraram o cristal,
    a reação fica ainda mais forte.

    Barbara percebe que a criatura está sendo
    afetada mesmo antes do confronto.

    Milo olha para a passagem.

    — Agora estamos preparados.
    """)
else:
    mostrar("""
    ⚠️ SEM O SÍMBOLO

    Vocês tentam preparar o ritual, mas percebem
    que não possuem o símbolo original.

    Mesmo assim, precisam continuar.
    """)

atualizar_status()
criar_botao("👹 Continuar", fase27)
```

def fase26_equipamentos(event):
pegar("equipamento")
state["batalha"] += 2

```
mostrar("""
🎒 EQUIPAMENTOS

Vocês organizam os equipamentos.

Milo verifica tudo.

Barbara guarda as pistas.

Olivier e Amelie conferem os documentos.

Agora o grupo está mais preparado para o
confronto que está prestes a acontecer.
""")

atualizar_status()
criar_botao("👹 Continuar", fase27)
```

# =========================

# FASE 27

# =========================

def fase27(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
👹 O MONSTRO

O grupo chega à última sala.

A criatura está diante de vocês.

Os símbolos cobrem as paredes.

Milo reconhece o local.

— É aqui que tudo começou.

Barbara segura o símbolo.

Olivier e Amelie percebem que o momento
pelo qual passaram por toda aquela investigação
finalmente chegou.

Agora é hora de decidir como enfrentar a criatura.
""")

criar_botao("⚔️ Preparar o confronto", fase28)
```

# =========================

# FASE 28

# =========================

def fase28(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
⚔️ O CONFRONTO

A criatura avança.

O símbolo pode ser usado para enfraquecê-la.

Milo e Barbara ajudam vocês.

Cada decisão pode mudar o resultado final.

Escolha uma estratégia.
""")

criar_botao("🔱 Ativar o símbolo", fase28_simbolo)
criar_botao("🛡️ Ajudar Milo", fase28_milo)
criar_botao("🛡️ Ajudar Barbara", fase28_barbara)
criar_botao("🏃 Recuar", fase28_recuar)
```

def fase28_simbolo(event):
if "símbolo antigo" in state["inv"]:
state["batalha"] += 4
state["monstro_fraqueza"] = True

```
    mostrar("""
    🔱 O SÍMBOLO É ATIVADO

    Você ativa o símbolo antigo.

    As paredes começam a brilhar.

    O cristal reage.

    A criatura perde força.

    Milo grita:

    — Continue!

    A estratégia está funcionando.
    """)
else:
    perder_sanidade()

    mostrar("""
    ⚠️ O SÍMBOLO NÃO ESTÁ COM VOCÊ

    Você tenta ativar o símbolo, mas percebe
    que não o possui.

    A criatura continua avançando.

    Mesmo assim, vocês precisam continuar.
    """)

atualizar_status()
criar_botao("🔥 Decisão final", fase29)
```

def fase28_milo(event):
state["confianca_milo"] += 2
state["batalha"] += 2

```
mostrar("""
🛡️ MILO AJUDA

Você ajuda Milo a procurar uma forma de usar
as inscrições da parede.

Como conhece a ilha e suas histórias desde criança,
Milo reconhece uma inscrição antiga.

A descoberta ajuda o grupo a entender como
utilizar os símbolos.

A criatura perde parte da vantagem.
""")

atualizar_status()
criar_botao("🔥 Decisão final", fase29)
```

def fase28_barbara(event):
state["confianca_barbara"] += 2
state["batalha"] += 2
state["monstro_fraqueza"] = True

```
mostrar("""
🛡️ BARBARA AJUDA

Você ajuda Barbara a procurar informações
nas inscrições.

Ela encontra uma mensagem escondida.

A informação confirma a fraqueza da criatura.

Agora vocês sabem exatamente o que precisam fazer.

Barbara respira fundo.

— Ainda podemos conseguir.
""")

atualizar_status()
criar_botao("🔥 Decisão final", fase29)
```

def fase28_recuar(event):
perder_vida()

```
mostrar("""
🏃 RECUAR

Vocês recuam.

A criatura avança.

Milo e Barbara ajudam o grupo a se reorganizar.

A situação ficou mais difícil.

Agora não existe mais tempo para fugir
da decisão final.
""")

atualizar_status()
criar_botao("🔥 Decisão final", fase29)
```

# =========================

# FASE 29

# =========================

def fase29(event=None):
limpar()
atualizar_status()
imagem.style.display = "none"

```
mostrar("""
🔥 A ÚLTIMA ESCOLHA

A criatura está diante de vocês.

Depois de toda a investigação, o segredo da ilha
finalmente foi descoberto.

Vocês sabem a verdade sobre o passado da família.

Milo e Barbara estão ao lado de vocês.

Agora só resta uma decisão.

O que vocês vão fazer?
""")

criar_botao("⚔️ Derrotar o monstro", final_derrotar)
criar_botao("🔒 Selar o monstro novamente", final_selar)
criar_botao("🏃 Fugir da ilha", final_fugir)
```

# =========================

# ESCOLHAS DOS FINAIS

# =========================

def final_derrotar(event):
state["escolheu_derrotar"] = True
state["escolheu_selar"] = False
state["escolheu_fugir"] = False

```
if state["monstro_fraqueza"] and state["batalha"] >= 5:
    state["monstro_derrotado"] = True
else:
    state["monstro_derrotado"] = False

fase30()
```

def final_selar(event):
state["escolheu_derrotar"] = False
state["escolheu_selar"] = True
state["escolheu_fugir"] = False
state["monstro_derrotado"] = False

```
fase30()
```

def final_fugir(event):
state["escolheu_derrotar"] = False
state["escolheu_selar"] = False
state["escolheu_fugir"] = True
state["monstro_derrotado"] = False

```
fase30()
```

# =========================

# FASE 30 / FINAIS

# =========================

def fase30(event=None):
limpar()
atualizar_status()

```
# FINAL 1 - DERROTA REAL DO MONSTRO
if state["escolheu_derrotar"] and state["monstro_derrotado"]:

    mostrar_imagem_final("final_01.png")

    mostrar("""
    🌟 FINAL 1 — O MONSTRO FOI DERROTADO

    O símbolo antigo começa a brilhar.

    As inscrições da sala se iluminam.

    O cristal reage ao símbolo e a criatura
    perde completamente sua força.

    Milo e Barbara permanecem ao lado de vocês.

    Depois de tantos anos, o segredo da ilha
    finalmente chega ao fim.

    Os documentos provam que o parente de Olivier
    ou Amelie tentou proteger a ilha no passado.

    Agora a verdade pode finalmente ser revelada.

    Milo e Barbara continuam na ilha, onde sempre
    viveram, mas agora podem viver sem o medo
    da criatura.

    Olivier e Amelie finalmente descobrem
    o que aconteceu com sua família.

    🏝️ A ilha está livre da criatura.

    🎉 VOCÊ CONSEGUIU O MELHOR FINAL!
    """)

# FINAL 2 - TENTOU DERROTAR, MAS NÃO CONSEGUIU
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

    Porém, o segredo ainda não terminou.

    A criatura continua escondida.

    Barbara olha para a entrada da caverna.

    — Talvez um dia alguém consiga terminar
    o que começamos.

    A ilha continua guardando seu maior segredo.
    """)

# FINAL 3 - SELAR
elif state["escolheu_selar"]:

    mostrar_imagem_final("final_03.png")

    mostrar("""
    🔒 FINAL 3 — O SELAMENTO

    Vocês decidem não destruir a criatura.

    Barbara ativa os símbolos antigos.

    Milo ajuda a manter o grupo seguro.

    O cristal reage.

    A passagem começa a se fechar.

    A criatura desaparece novamente nas profundezas.

    O segredo continua escondido.

    Olivier e Amelie percebem que talvez
    nem todo mistério precise ser destruído.

    Milo e Barbara permanecem na ilha para
    continuar protegendo aquele lugar.

    A ilha está segura...

    por enquanto.
    """)

# FINAL 4 - FUGA
elif state["escolheu_fugir"]:

    mostrar_imagem_final("final_06.png")

    mostrar("""
    🏃 FINAL 4 — A FUGA

    Vocês decidem abandonar a ilha.

    Milo conhece o caminho de volta.

    Barbara ajuda o grupo a chegar ao barco.

    Olivier ou Amelie leva os documentos
    encontrados durante a investigação.

    A ilha fica para trás.

    Milo e Barbara permanecem lá porque aquela
    é a casa deles.

    Vocês sobreviveram.

    Mas nunca descobriram toda a verdade.

    Talvez a criatura continue escondida.

    Talvez alguém precise voltar um dia.

    O segredo da ilha continua.
    """)

mostrar("""
🎮 FIM DO JOGO

Obrigado por jogar
O Segredo na Ilha!

Cada escolha pode levar a um resultado diferente.
""")

criar_botao("🔄 Jogar novamente", reiniciar)
```

# =========================

# REINICIAR

# =========================

def reiniciar(event):
state["personagem"] = ""
state["vida"] = 5
state["sanidade"] = 5
state["pistas"] = 0
state["inv"] = []

```
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
```

# =========================

# INICIAR O JOGO

# =========================

fase1()
