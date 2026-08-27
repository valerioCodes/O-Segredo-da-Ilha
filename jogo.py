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

def fase1(event=None):
preparar(1)

```
mostrar("""
```

🏝️ O SEGREDO NA ILHA

Olivier e Amelie estão viajando de barco em direção
a uma pequena ilha.

Os dois encontraram documentos antigos relacionados
à própria família.

Entre esses documentos havia referências a um parente
que desapareceu muitos anos atrás.

Enquanto o barco se aproxima da ilha, os dois observam
a costa pela primeira vez.

Eles ainda não sabem o que encontrarão.

Na ilha, Milo e Barbara já vivem há muitos anos.

Os dois conhecem as histórias, os caminhos e os lugares
antigos da região.

Agora Olivier e Amelie finalmente estão chegando.

A viagem está prestes a mudar completamente a vida deles.

Escolha quem será o personagem principal.
""")

```
criar_botao("🧑 Olivier", escolher_olivier)
criar_botao("👩 Amelie", escolher_amelie)
```

def escolher_olivier(event=None):
state["personagem"] = "Olivier"
fase2()

def escolher_amelie(event=None):
state["personagem"] = "Amelie"
fase2()

def fase2(event=None):
preparar(2)

```
mostrar("""
```

🚢 A CHEGADA

O barco finalmente chega ao pequeno porto da ilha.

Olivier e Amelie desembarcam.

Na praia, duas pessoas esperam por eles.

São Milo e Barbara.

Milo e Barbara já moram na ilha há anos.
Eles conhecem os caminhos, a vila e as histórias
antigas daquele lugar.

Milo se aproxima.

— Vocês devem ser os visitantes que estavam chegando.

Barbara observa os documentos que vocês carregam.

— Vieram procurar alguém da família?

Olivier e Amelie percebem que aqueles dois parecem
saber muito mais sobre a ilha do que imaginavam.

A investigação começa.
""")

```
criar_botao("🏝️ Conversar com Milo", fase3_milo)
criar_botao("🏝️ Conversar com Barbara", fase3_barbara)
```

def fase3_milo(event=None):
state["confianca_milo"] += 1
state["pistas"] += 1
preparar(3)

```
mostrar("""
```

🗣️ MILO

Milo explica que sua família vive na ilha há gerações.

Ele conhece trilhas, casas abandonadas e lugares
que não aparecem nos mapas.

— Se vocês estão procurando respostas, posso ajudar.

Milo também conta que alguns moradores desapareceram
ao longo dos anos.

Ele fala sobre uma região antiga da ilha onde ninguém
gosta de entrar.

Segundo ele, existem histórias sobre algo que vive
nas profundezas daquele lugar.

Talvez seja lá que o mistério tenha começado.

Milo olha para vocês e espera uma resposta.
""")

```
criar_botao("➡️ Continuar", fase4)
```

def fase3_barbara(event=None):
state["confianca_barbara"] += 1
state["pistas"] += 1
preparar(3)

```
mostrar("""
```

🗣️ BARBARA

Barbara conta que sua família também mora na ilha
há muitas gerações.

Ela conhece histórias sobre símbolos antigos
encontrados pela região.

Segundo sua avó, esses símbolos protegiam a ilha
de alguma coisa.

Barbara acredita que os documentos de Olivier
e Amelie podem estar relacionados a essa história.

— Talvez sua família tenha deixado alguma coisa aqui.

Ela aponta para a vila.

Existem vários lugares antigos que podem esconder
as respostas que vocês procuram.
""")

```
criar_botao("➡️ Continuar", fase4)
```

def fase4(event=None):
preparar(4)

```
mostrar("""
```

🏘️ A VILA

Milo e Barbara mostram a vila para Olivier e Amelie.

Existem três lugares importantes.

Uma igreja antiga.

Uma casa abandonada.

E um velho farol.

Cada lugar pode esconder uma pista diferente.

A decisão de vocês pode mudar o caminho da investigação.

Onde vocês vão começar?
""")

```
criar_botao("⛪ Ir para a igreja", fase5)
criar_botao("🏚️ Ir para a casa abandonada", fase6)
criar_botao("🔦 Ir para o farol", fase7)
```

def fase5(event=None):
preparar(5)

```
mostrar("""
```

⛪ A IGREJA

A igreja está abandonada há muitos anos.

Milo e Barbara conhecem o lugar, mas mesmo eles
evitam entrar ali durante a noite.

Nas paredes existem símbolos antigos.

Barbara reconhece alguns deles.

— Minha família falava sobre esses símbolos.

Vocês começam a investigar.

Talvez os símbolos sejam uma pista para descobrir
o que aconteceu com o parente desaparecido.
""")

```
criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
criar_botao("📖 Procurar documentos", fase5_documentos)
```

def fase5_simbolos(event=None):
state["pistas"] += 2
pegar("fotografia dos símbolos")

```
preparar(5)

mostrar("""
```

🔎 OS SÍMBOLOS

Os símbolos parecem formar uma espécie de caminho.

Barbara percebe que alguns desenhos apontam
para a floresta.

Você fotografa os símbolos para estudar depois.

Milo observa os desenhos em silêncio.

— Se isso estiver certo, a floresta pode ser
o próximo lugar que precisamos investigar.

Vocês guardam a fotografia.

Talvez ela seja uma das pistas mais importantes
encontradas até agora.
""")

```
criar_botao("🌲 Continuar", fase8)
```

def fase5_documentos(event=None):
state["pistas"] += 3
pegar("livro antigo")

```
preparar(5)

mostrar("""
```

📖 O LIVRO ANTIGO

Atrás de um banco antigo vocês encontram um livro.

Ele fala sobre uma criatura que estaria escondida
nas profundezas da ilha.

Uma das páginas menciona um símbolo capaz
de enfraquecê-la.

Barbara fica séria ao ler a passagem.

— Minha avó dizia que essas histórias eram apenas
lendas.

Milo responde:

— Talvez nunca tenham sido.

Vocês guardam o livro.

Agora existe uma nova pergunta:

O que realmente está escondido na ilha?
""")

```
criar_botao("🌲 Continuar", fase8)
```

def fase6(event=None):
preparar(6)

```
mostrar("""
```

🏚️ A CASA ABANDONADA

Milo leva vocês até uma casa abandonada.

O antigo morador desapareceu muitos anos atrás.

A casa está coberta de poeira.

Dentro existem documentos, fotografias e objetos
que parecem ter sido deixados às pressas.

Talvez alguma dessas coisas explique o passado
da ilha.

Milo avisa:

— Não mexam em nada sem olhar primeiro.

Vocês começam a investigar.
""")

```
criar_botao("📄 Procurar documentos", fase6_documentos)
criar_botao("⬆️ Subir as escadas", fase6_escadas)
criar_botao("⬇️ Investigar o porão", fase6_porao)
```

def fase6_documentos(event=None):
state["pistas"] += 3
pegar("documentos da família")

```
preparar(6)

mostrar("""
```

📄 OS DOCUMENTOS

Entre os documentos aparece o sobrenome da família.

Barbara fica surpresa.

— Sua família realmente esteve aqui.

Os papéis mostram que um membro da família
visitou a ilha muitos anos atrás.

Também existe uma anotação sobre uma área proibida.

Agora existe uma ligação clara entre vocês
e o passado da ilha.

Talvez o desaparecimento do parente não tenha
sido um acidente.
""")

```
criar_botao("🌲 Continuar", fase8)
```

def fase6_escadas(event=None):
state["pistas"] += 2
pegar("fotografia antiga")

```
preparar(6)

mostrar("""
```

📸 A FOTOGRAFIA

No andar de cima vocês encontram uma fotografia.

Ela mostra algumas pessoas diante da floresta.

Uma delas parece ser o parente desaparecido.

Milo reconhece o lugar.

— Eu sei onde isso foi tirado.

Barbara olha para a fotografia.

— Então talvez ainda exista alguma coisa naquele lugar.

A fotografia pode levar vocês até a próxima pista.
""")

```
criar_botao("🌲 Continuar", fase8)
```

def fase6_porao(event=None):
state["pistas"] += 3
pegar("fotografia antiga")

```
preparar(6)

mostrar("""
```

⬇️ O PORÃO

No porão existe uma caixa escondida.

Dentro dela há uma fotografia antiga.

No verso está escrito:

"Aquilo que está abaixo da ilha nunca deve ser despertado."

O silêncio toma conta do grupo.

Milo fecha a caixa.

— Acho que encontramos algo que ninguém deveria
ter encontrado.

O segredo parece estar relacionado às cavernas.
""")

```
criar_botao("🌲 Continuar", fase8)
```

def fase7(event=None):
preparar(7)

```
state["pistas"] += 3
pegar("fotografia da criatura")

mostrar("""
```

🔦 O FAROL

O farol abandonado fica no alto de uma região
rochosa.

Milo conhece o caminho e acompanha vocês.

No topo existe uma caixa antiga.

Dentro dela há uma fotografia.

Ao fundo aparece uma figura estranha.

Barbara fica assustada.

— Então as histórias podem ser verdadeiras.

A fotografia mostra algo que não parece humano.

Agora vocês sabem que existe alguma coisa
escondida na ilha.
""")

```
atualizar_status()
criar_botao("🌙 Continuar", fase8)
```

def fase8(event=None):
preparar(8)

```
mostrar("""
```

🌙 A PRIMEIRA NOITE

A investigação demora mais do que esperavam.

A noite chega.

Milo e Barbara levam vocês para uma casa segura
na vila.

Durante a madrugada, alguém bate na janela.

TOC.

TOC.

TOC.

Milo pede para ninguém abrir.

— Não façam barulho.

O que você faz?
""")

```
criar_botao("🪟 Abrir a janela", fase8_janela)
criar_botao("😶 Ignorar", fase8_ignorar)
```

def fase8_janela(event=None):
perder_sanidade()
state["pistas"] += 2

```
mostrar("""
```

🪟 A JANELA

Você abre a janela.

Não há ninguém.

Mas existem marcas profundas no chão.

Milo reconhece as marcas.

— Eu já vi isso antes.

Barbara olha para a floresta.

— Então ela voltou.

Ninguém consegue dormir depois disso.

A investigação acabou de ficar muito mais perigosa.
""")

```
criar_botao("🌅 Continuar", fase9)
```

def fase8_ignorar(event=None):
state["pistas"] += 1

```
mostrar("""
```

😶 O SILÊNCIO

Vocês decidem ignorar as batidas.

Ninguém abre a janela.

Quando amanhece, encontram marcas no chão
perto da casa.

Alguma coisa esteve ali durante a noite.

Milo observa as marcas e fica preocupado.

— Precisamos descobrir o que está acontecendo.
""")

```
criar_botao("🌅 Continuar", fase9)
```
