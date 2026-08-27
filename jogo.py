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
"    🧠 Sanidade: " + str(state["sanidade"]) +
"    🔎 Pistas: " + str(state["pistas"]) +
"    🎒 Itens: " + str(len(state["inv"]))
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

def fase1(event=None):
preparar(1)

```
mostrar("""
```

🏝️ O SEGREDO NA ILHA

Durante muitos anos, uma pequena ilha permaneceu
afastada do restante do mundo.

Poucas pessoas conhecem a verdadeira história daquele
lugar. Existem relatos de desaparecimentos, construções
abandonadas e acontecimentos que os moradores preferem
não comentar.

Olivier e Amelie descobriram documentos antigos
relacionados à própria família.

Entre os documentos havia referências a uma ilha distante
e a um parente que desapareceu muitos anos atrás.

Depois de investigar durante algum tempo, os dois decidem
viajar até lá para descobrir o que realmente aconteceu.

O barco atravessa o mar.

A ilha começa a aparecer no horizonte.

Olivier e Amelie ainda não sabem que aquela viagem
vai mudar completamente suas vidas.

Antes de desembarcar, você precisa escolher
quem será o personagem principal da história.
""")

```
criar_botao("🧑 Olivier", escolher_olivier)
criar_botao("👩 Amelie", escolher_amelie)
```

def escolher_olivier(event):
state["personagem"] = "Olivier"
fase2()

def escolher_amelie(event):
state["personagem"] = "Amelie"
fase2()

def fase2(event=None):
preparar(2)

```
mostrar("""
```

🚢 FASE 2 — A VIAGEM

O barco continua avançando lentamente pelo mar.

Olivier e Amelie estão juntos na viagem.

Nenhum dos dois conhece pessoalmente os moradores da ilha.

O vento bate contra o barco enquanto eles observam
a costa se aproximar.

Olivier segura os documentos antigos.

Amelie observa uma fotografia encontrada entre os papéis.

A imagem mostra algumas pessoas diante de uma construção
antiga da ilha.

No verso da fotografia existe uma pequena anotação:

"Procure a verdade onde tudo começou."

Depois de algumas horas, o barco finalmente se aproxima
do pequeno porto.

É a primeira vez que Olivier e Amelie colocam os pés
na ilha.

Na praia, duas pessoas esperam pela chegada dos visitantes.

São Milo e Barbara.

Milo e Barbara já moram na ilha há muitos anos.

Milo conhece praticamente todos os caminhos da região.

Barbara conhece as histórias antigas dos moradores.

Os dois observam os visitantes chegando.

A investigação está prestes a começar.
""")

```
criar_botao("🏝️ Desembarcar na ilha", fase3)
```

def fase3(event=None):
preparar(3)

```
mostrar("""
```

🏝️ FASE 3 — OS MORADORES

Olivier e Amelie desembarcam no pequeno porto.

Milo se aproxima primeiro.

— Vocês devem ser os visitantes que estavam chegando.

Barbara observa os documentos que eles carregam.

— Vieram procurar alguém da família?

Olivier e Amelie explicam que encontraram documentos
antigos relacionados a um parente desaparecido.

Milo fica em silêncio por alguns segundos.

Barbara troca um olhar com ele.

— Então vocês vieram atrás daquela história...

Milo explica que ele e Barbara nasceram e vivem na ilha.

Eles conhecem os lugares antigos e sabem que existem
muitos rumores sobre acontecimentos estranhos.

Barbara avisa:

— A ilha parece tranquila, mas existem lugares onde
até os moradores evitam entrar.

Milo aponta para a vila.

— Se vocês querem descobrir o que aconteceu com
o parente de vocês, podemos ajudar.

Agora você pode conversar com os moradores.
""")

```
criar_botao("🗣️ Conversar com Milo", fase3_milo)
criar_botao("🗣️ Conversar com Barbara", fase3_barbara)
criar_botao("🔎 Perguntar sobre a ilha", fase3_ilha)
```

def fase3_milo(event):
state["confianca_milo"] += 1

```
mostrar("""
```

Milo explica que sua família vive na ilha há gerações.

Ele conhece trilhas, casas abandonadas e vários caminhos
que não aparecem nos mapas atuais.

— Quando eu era criança, meu avô contava histórias
sobre uma coisa que existia nas profundezas da ilha.

Milo admite que nunca soube se aquilo era verdade.

Mas alguns desaparecimentos fizeram as antigas histórias
voltarem a ser comentadas.

— Se vocês realmente querem procurar respostas,
precisam ter cuidado.
""")

```
atualizar_status()
criar_botao("➡️ Continuar investigação", fase4)
```

def fase3_barbara(event):
state["confianca_barbara"] += 1

```
mostrar("""
```

Barbara conta que sua família também mora na ilha
há muitas gerações.

Ela conhece histórias que foram passadas de avós
para netos.

— Existem símbolos antigos espalhados pela ilha.

Alguns ficam na igreja.

Outros aparecem em construções abandonadas.

Barbara diz que os moradores costumavam acreditar
que esses símbolos protegiam a ilha de alguma coisa.

— Eu nunca soube exatamente do quê.
""")

```
atualizar_status()
criar_botao("➡️ Continuar investigação", fase4)
```

def fase3_ilha(event):
state["pistas"] += 1

```
mostrar("""
```

Milo aponta para os principais lugares da ilha.

Ao centro fica a vila.

Mais adiante existe uma igreja abandonada.

No alto de uma região rochosa está o antigo farol.

E depois da floresta existem cavernas que quase
ninguém visita.

Barbara explica:

— Se sua família esteve aqui, provavelmente deixou
alguma pista em um desses lugares.

Agora vocês precisam decidir onde começar.
""")

```
atualizar_status()
criar_botao("➡️ Escolher o primeiro lugar", fase4)
```

def fase4(event=None):
preparar(4)

```
mostrar("""
```

🏘️ FASE 4 — A VILA

Milo e Barbara acompanham Olivier e Amelie pela vila.

Como moradores da ilha, os dois sabem exatamente
onde ficam os lugares mais antigos.

Milo aponta para a igreja.

— Esse é um dos lugares mais antigos daqui.

Barbara aponta para uma casa abandonada.

— Essa casa também tem uma história complicada.

Por último, Milo aponta para o farol.

— Lá em cima existem registros antigos.

Vocês precisam escolher onde começar a investigação.
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

⛪ FASE 5 — A IGREJA

Milo guia vocês até a igreja antiga.

O lugar está abandonado há muitos anos.

Barbara abre a porta cuidadosamente.

Dentro, tudo está coberto de poeira.

Nas paredes existem desenhos estranhos.

Milo se aproxima.

— Esses símbolos fazem parte das histórias antigas.

Barbara observa alguns deles.

— Minha avó dizia que eles eram importantes.

Vocês começam a investigar.

Talvez os símbolos possam revelar alguma pista.
""")

```
criar_botao("🔎 Examinar os símbolos", fase5_simbolos)
criar_botao("📖 Procurar documentos", fase5_documentos)
criar_botao("📷 Fotografar os símbolos", fase5_fotografia)
```

def fase5_simbolos(event):
state["pistas"] += 2

```
mostrar("""
```

Você observa os símbolos cuidadosamente.

Depois de comparar vários desenhos, percebe que eles
parecem formar um caminho.

Barbara se aproxima.

— Isso parece um mapa.

Milo aponta para uma região do desenho.

— Essa direção leva para a floresta.

Talvez os símbolos estejam indicando onde procurar
a próxima pista.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase5_documentos(event):
pegar("livro antigo")
state["pistas"] += 3

```
mostrar("""
```

Atrás de um banco antigo vocês encontram um livro.

As páginas estão amareladas.

Barbara começa a ler.

O livro fala sobre os primeiros moradores da ilha
e menciona uma antiga criatura.

Milo fica surpreso.

— Eu já ouvi algumas dessas histórias.

Uma das páginas fala sobre um símbolo capaz de
enfraquecer a criatura.

Essa informação pode ser muito importante.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase5_fotografia(event):
pegar("fotografia dos símbolos")
state["pistas"] += 1

```
mostrar("""
```

Você fotografa os símbolos encontrados nas paredes.

Barbara percebe que alguns detalhes são difíceis
de enxergar diretamente.

Talvez a fotografia possa ser comparada com outras
pistas encontradas durante a investigação.

Milo guarda a informação.

— Não percam essa fotografia.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase6(event=None):
preparar(6)

```
mostrar("""
```

🏚️ FASE 6 — A CASA ABANDONADA

Milo leva vocês até uma casa que está abandonada
há muitos anos.

— Ninguém mora aqui desde antes de eu nascer.

Barbara explica que o antigo dono desapareceu
em circunstâncias misteriosas.

Dentro da casa existem móveis antigos,
papéis e objetos cobertos de poeira.

Vocês começam a procurar pistas.

A casa possui três lugares interessantes.
""")

```
criar_botao("📄 Procurar documentos", fase6_documentos)
criar_botao("⬆️ Subir as escadas", fase6_escadas)
criar_botao("⬇️ Investigar o porão", fase6_porao)
```

def fase6_documentos(event):
pegar("documentos da família")
state["pistas"] += 3

```
mostrar("""
```

Entre os documentos antigos existe algo inesperado.

O sobrenome da sua família aparece várias vezes.

Barbara lê uma anotação.

— Sua família realmente esteve aqui.

Milo encontra outra página.

Nela está escrito que alguém tentou descobrir
o segredo das cavernas.

A investigação acaba de ganhar uma nova direção.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase6_escadas(event):
pegar("chave enferrujada")
pegar("fotografia antiga")
state["pistas"] += 2

```
mostrar("""
```

No andar de cima vocês encontram uma pequena chave
enferrujada e uma fotografia.

A fotografia mostra algumas pessoas diante da floresta.

Uma delas se parece muito com o parente desaparecido.

Barbara fica surpresa.

— Essa pessoa realmente pode ser ele.

Milo observa a fotografia.

— Então ele esteve aqui.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase6_porao(event):
pegar("fotografia antiga")
state["pistas"] += 3

```
mostrar("""
```

No porão existe uma caixa escondida.

Dentro dela há uma fotografia antiga.

A imagem mostra moradores diante de uma entrada
subterrânea.

No verso está escrito:

"Aquilo que está abaixo da ilha nunca deve ser despertado."

Milo fica sério.

Barbara percebe que o segredo da ilha pode estar
ligado às cavernas.
""")

```
atualizar_status()
criar_botao("🌲 Continuar", fase8)
```

def fase7(event=None):
preparar(7)

```
pegar("fotografia da criatura")
state["pistas"] += 3

mostrar("""
```

🔦 FASE 7 — O FAROL

Milo e Barbara acompanham vocês até o antigo farol.

Como moradores da ilha, eles conhecem o caminho
até o topo.

O farol está abandonado.

Vocês sobem lentamente as escadas.

No último andar encontram uma caixa antiga.

Dentro dela existe uma fotografia.

Na imagem aparece uma figura estranha ao fundo.

Barbara fica em silêncio.

Milo reconhece o local.

— Essa fotografia foi tirada muitos anos atrás.

Vocês começam a perceber que as histórias sobre
a criatura podem não ser apenas histórias.
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

🌙 FASE 8 — A PRIMEIRA NOITE

A investigação demora mais do que vocês esperavam.

A noite chega.

Milo sugere que todos voltem para a vila.

Como conhece a região, ele escolhe uma casa segura
para vocês passarem a noite.

Barbara fecha as janelas.

Durante a madrugada, todos escutam:

TOC.

TOC.

TOC.

Alguém parece estar batendo na janela.

Milo fica imóvel.

— Não abra.

Barbara olha para os outros.

— Vamos esperar.

O som continua por alguns segundos.

O que você decide fazer?
""")

```
criar_botao("🪟 Abrir a janela", fase8_janela)
criar_botao("😶 Ignorar", fase8_ignorar)
criar_botao("🚪 Verificar a porta", fase8_porta)
```

def fase8_janela(event):
state["pistas"] += 2
perder_sanidade()

```
mostrar("""
```

Você abre a janela.

Não existe ninguém do lado de fora.

Porém, existem marcas enormes no chão.

Milo se aproxima.

Ele reconhece as marcas.

— Eu já vi isso antes.

Barbara olha para a floresta.

— Então ela voltou.
""")

```
criar_botao("🌅 Continuar", fase9)
```

def fase8_ignorar(event):
state["pistas"] += 1

```
mostrar("""
```

Vocês decidem não abrir a janela.

Depois de alguns minutos, as batidas param.

Quando amanhece, todos saem para verificar
o lado de fora.

Existem marcas profundas no chão.

Alguma coisa esteve perto da casa durante a noite.
""")

```
criar_botao("🌅 Continuar", fase9)
```

def fase8_porta(event):
state["pistas"] += 2

```
mostrar("""
```

Vocês verificam cuidadosamente a porta.

Do lado de fora existem marcas no chão.

Milo observa.

— Elas vêm da direção da floresta.

Barbara percebe que existem pegadas humanas
misturadas às marcas.

Talvez alguém tenha sido levado para lá.
""")

```
criar_botao("🌅 Continuar", fase9)
```

def fase9(event=None):
preparar(9)

```
mostrar("""
```

🚨 FASE 9 — O DESAPARECIMENTO

Na manhã seguinte, uma notícia preocupa toda a vila.

Um dos moradores desapareceu.

Milo conhece a pessoa.

— Ele estava aqui ontem.

Barbara começa a procurar informações.

Como moradores da ilha, os dois conhecem os caminhos
que levam para fora da vila.

Vocês precisam decidir onde procurar primeiro.
""")

```
criar_botao("🏘️ Procurar na vila", fase9_vila)
criar_botao("🌲 Seguir para a floresta", fase9_floresta)
```

def fase9_vila(event):
state["pistas"] += 1

```
mostrar("""
```

Vocês procuram pelas ruas da vila.

Perto de uma das casas encontram marcas no chão.

Milo segue as marcas.

Elas levam para fora da vila.

Barbara aponta para a floresta.

— Ele provavelmente passou por aqui.
""")

```
criar_botao("🔎 Continuar", fase10)
```

def fase9_floresta(event):
state["pistas"] += 2

```
mostrar("""
```

Vocês seguem diretamente para a floresta.

Depois de alguns minutos encontram pegadas.

Milo compara as marcas.

— São iguais às que vimos perto da casa.

Barbara percebe outras marcas misturadas.

O desaparecido esteve ali.
""")

```
criar_botao("🔎 Continuar", fase10)
```

def fase10(event=None):
preparar(10)

```
pegar("objeto do desaparecido")
state["pistas"] += 2

mostrar("""
```

🔎 FASE 10 — A INVESTIGAÇÃO

O grupo segue as marcas pela floresta.

A vegetação fica cada vez mais fechada.

Depois de algum tempo, Barbara encontra um objeto
no chão.

Milo reconhece imediatamente.

— Isso pertence ao homem desaparecido.

Vocês continuam procurando.

As marcas seguem cada vez mais para dentro da floresta.

Não existe mais dúvida.

Ele esteve ali.

E alguma coisa o levou para algum lugar.
""")

```
atualizar_status()
criar_botao("🌲 Continuar pela floresta", fase11)
```

def fase11(event=None):
preparar(11)

```
mostrar("""
```

🌲 FASE 11 — A FLORESTA

Milo assume a liderança.

Como conhece a ilha desde criança, ele sabe quais
caminhos costumam levar para regiões mais afastadas.

Barbara observa as árvores.

— Essas marcas são recentes.

O grupo encontra uma trilha quase escondida.

Vocês precisam decidir como continuar.
""")

```
criar_botao("🥾 Seguir a trilha", fase11_trilha)
criar_botao("🪵 Marcar o caminho", fase11_marcar)
criar_botao("🔎 Procurar pistas ao redor", fase11_pistas)
```

def fase11_trilha(event):
state["pistas"] += 2

```
mostrar("""
```

Vocês seguem a trilha.

Milo reconhece alguns pontos do caminho.

— Eu nunca tinha visto essas marcas aqui.

Depois de alguns minutos, vocês encontram
uma área desconhecida.

A trilha continua até uma pequena cabana.
""")

```
criar_botao("🏚️ Continuar", fase12)
```

def fase11_marcar(event):
state["pistas"] += 1

```
mostrar("""
```

Barbara decide marcar algumas árvores.

Assim, caso precisem voltar rapidamente,
conseguirão encontrar o caminho.

Milo concorda.

— Boa ideia.

O grupo continua até encontrar um local adequado
para passar a noite.
""")

```
criar_botao("🔥 Continuar", fase12)
```

def fase11_pistas(event):
state["pistas"] += 2

```
mostrar("""
```

Vocês procuram ao redor da trilha.

Encontram marcas antigas nas árvores.

Barbara percebe que alguns símbolos são iguais
aos encontrados na igreja.

Milo fica preocupado.

— Estamos seguindo exatamente o caminho
indicado pelos símbolos.
""")

```
criar_botao("🔥 Continuar", fase12)
```

def fase12(event=None):
preparar(12)

```
mostrar("""
```

🔥 FASE 12 — O ACAMPAMENTO

A noite chega novamente.

O grupo monta um pequeno acampamento.

O fogo ilumina apenas uma pequena parte da floresta.

Como Milo e Barbara já vivem na ilha há muitos anos,
eles conhecem histórias que os visitantes nunca ouviram.

Talvez seja a hora de descobrir mais.
""")

```
criar_botao("🗣️ Conversar com Milo", fase12_milo)
criar_botao("🗣️ Conversar com Barbara", fase12_barbara)
criar_botao("😴 Descansar", fase12_descansar)
```

def fase12_milo(event):
state["confianca_milo"] += 2

```
mostrar("""
```

Milo conta que seu avô falava sobre uma criatura
que vivia em uma região subterrânea da ilha.

— Eu sempre achei que fosse apenas uma história
para assustar crianças.

Ele explica que alguns moradores desapareceram
depois de procurar as cavernas.

— Talvez as histórias fossem verdadeiras.
""")

```
criar_botao("🌅 Continuar", fase13)
```

def fase12_barbara(event):
state["confianca_barbara"] += 2

```
mostrar("""
```

Barbara conta que sua família guardava registros
sobre símbolos antigos.

— Minha avó dizia que esses símbolos protegiam
a ilha de alguma coisa.

Ela acredita que o segredo esteja relacionado
à família de Olivier e Amelie.

— Talvez vocês tenham vindo até aqui justamente
para terminar algo que começou há muito tempo.
""")

```
criar_botao("🌅 Continuar", fase13)
```

def fase12_descansar(event):
ganhar_sanidade()

```
mostrar("""
```

Vocês decidem descansar.

Milo e Barbara ficam atentos durante a noite.

A manhã chega sem novos acontecimentos.

Todos recuperam um pouco das forças.

Agora é hora de continuar a investigação.
""")

```
criar_botao("🌅 Continuar", fase13)
```

def fase13(event=None):
preparar(13)

```
state["pistas"] += 2

mostrar("""
```

🐾 FASE 13 — AS PEGADAS

Na manhã seguinte, novas pegadas aparecem.

Elas são maiores do que qualquer animal conhecido
na ilha.

Milo observa cuidadosamente.

— Essas marcas vão até aquela região.

Barbara aponta para uma pequena cabana escondida
entre as árvores.

O grupo decide investigar.

Talvez finalmente encontrem uma resposta.
""")

```
atualizar_status()
criar_botao("🏚️ Ir até a cabana", fase14)
```

def fase14(event=None):
preparar(14)

```
mostrar("""
```

🏚️ FASE 14 — A CABANA

A cabana parece abandonada.

Dentro existem livros, mapas e objetos antigos.

Barbara encontra um diário.

Milo reconhece alguns símbolos desenhados nas páginas.

O diário conta que antigos moradores descobriram
uma criatura nas profundezas da ilha.

Também fala sobre uma forma de enfraquecê-la.

A resposta parece estar relacionada a um símbolo antigo.
""")

```
pegar("diário")
state["pistas"] += 3

atualizar_status()
criar_botao("📖 Ler o diário", fase15)
```

def fase15(event=None):
preparar(15)

```
state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
```

📖 FASE 15 — O DIÁRIO

O diário revela uma parte assustadora da história.

Muitos anos atrás, moradores encontraram uma criatura
vivendo nas profundezas da ilha.

Eles descobriram que ela podia ser enfraquecida
por meio de um símbolo antigo.

O símbolo foi escondido para impedir que pessoas
tentassem libertar a criatura.

A última anotação diz:

"Quando ela despertar novamente, apenas o símbolo original
poderá revelar sua verdadeira fraqueza."

Milo fecha o diário.

Barbara olha para os visitantes.

— Então precisamos encontrar esse símbolo.
""")

```
atualizar_status()
criar_botao("🎒 Procurar os equipamentos", fase16)
```

def fase16(event=None):
preparar(16)

```
mostrar("""
```

🎒 FASE 16 — PREPARAÇÃO

Agora vocês sabem que estão chegando perto
da verdade.

Antes de continuar, o grupo organiza os equipamentos
encontrados durante a investigação.

Milo verifica os objetos.

Barbara revisa as pistas.

Vocês precisam escolher o que será mais importante
para continuar.
""")

```
criar_botao("🎒 Organizar equipamentos", fase16_equipamentos)
criar_botao("💊 Procurar medicamentos", fase16_medicamento)
criar_botao("🔱 Procurar o símbolo", fase16_simbolo)
```

def fase16_equipamentos(event):
pegar("equipamento")
state["batalha"] += 1

```
mostrar("""
```

Vocês organizam os equipamentos encontrados
durante a investigação.

Milo verifica se tudo está em ordem.

Barbara guarda as pistas mais importantes.

O grupo está mais preparado para continuar.
""")

```
atualizar_status()
criar_botao("🌊 Ir para o lago", fase17)
```

def fase16_medicamento(event):
pegar("medicamento")

```
mostrar("""
```

Barbara encontra medicamentos em uma caixa antiga.

Eles podem ser úteis caso alguém se machuque
durante a investigação.

Milo guarda o material.

— É melhor levar.
""")

```
atualizar_status()
criar_botao("🌊 Ir para o lago", fase17)
```

def fase16_simbolo(event):
pegar("símbolo antigo")
state["pistas"] += 3
state["batalha"] += 2

```
mostrar("""
```

Depois de procurar entre os objetos antigos,
vocês encontram uma peça com o mesmo desenho
dos símbolos encontrados na igreja.

Barbara reconhece imediatamente.

— Esse é o símbolo original.

Milo observa o objeto.

— Então finalmente encontramos uma das coisas
que procurávamos.
""")

```
atualizar_status()
criar_botao("🌊 Ir para o lago", fase17)
```

def fase17(event=None):
preparar(17)

```
mostrar("""
```

🌊 FASE 17 — O LAGO

O mapa encontrado na cabana indica que existe
uma pista próxima a um lago.

Depois de caminhar por algum tempo,
vocês chegam ao local.

A água está completamente parada.

Barbara observa as pedras ao redor.

Milo percebe uma marca antiga.

— Parece que alguém esteve aqui.

Talvez exista alguma coisa escondida.
""")

```
criar_botao("🔎 Procurar ao redor", fase17_redor)
criar_botao("🌊 Investigar a margem", fase17_margem)
criar_botao("➡️ Seguir sem investigar", fase17_seguir)
```

def fase17_redor(event):
pegar("cristal")
state["pistas"] += 2

```
mostrar("""
```

Vocês procuram ao redor do lago.

Atrás de algumas pedras encontram um pequeno cristal.

Quando Barbara aproxima o símbolo do cristal,
ele reage com um brilho fraco.

Milo observa.

— Eles estão relacionados.
""")

```
atualizar_status()
criar_botao("🕳️ Continuar", fase18)
```

def fase17_margem(event):
pegar("cristal")
state["pistas"] += 2

```
mostrar("""
```

Vocês procuram cuidadosamente pela margem.

Depois de alguns minutos encontram um pequeno cristal.

Barbara percebe que ele parece reagir às marcas
encontradas durante a investigação.

Talvez seja mais uma peça do mistério.
""")

```
atualizar_status()
criar_botao("🕳️ Continuar", fase18)
```

def fase17_seguir(event):
state["pistas"] += 1

```
mostrar("""
```

Vocês decidem não perder tempo.

Milo aponta para uma passagem entre as pedras.

— Existe uma trilha ali.

O grupo segue o caminho.

A passagem leva para uma caverna escondida.
""")

```
atualizar_status()
criar_botao("🕳️ Continuar", fase18)
```

def fase18(event=None):
preparar(18)

```
mostrar("""
```

🕳️ FASE 18 — A CAVERNA

O caminho termina diante de uma grande entrada
na pedra.

Milo reconhece o lugar.

— Meu avô falava dessa caverna.

Barbara observa os símbolos nas paredes.

Eles são iguais aos encontrados na igreja.

Quanto mais vocês avançam, mais forte fica
a sensação de que alguém esteve ali recentemente.

A entrada se divide em diferentes caminhos.
""")

```
criar_botao("🚪 Entrar diretamente", fase18_entrar)
criar_botao("🔎 Procurar outra passagem", fase18_passagem)
```

def fase18_entrar(event):
state["pistas"] += 3

```
mostrar("""
```

Vocês entram diretamente na caverna.

As paredes estão cobertas de símbolos.

Barbara percebe que alguns parecem recentes.

Milo olha para o chão.

Existem pegadas.

Alguém esteve ali antes de vocês.

Talvez o desaparecido esteja em algum lugar
dentro daquela caverna.
""")

```
criar_botao("👹 Continuar", fase19)
```

def fase18_passagem(event):
state["pistas"] += 2

```
mostrar("""
```

Vocês procuram uma passagem alternativa.

Depois de algum tempo encontram um corredor estreito.

Milo reconhece alguns símbolos nas paredes.

— Esse caminho provavelmente era usado pelos
antigos moradores.

A passagem leva para uma região mais profunda.
""")

```
criar_botao("👹 Continuar", fase19)
```

def fase19(event=None):
preparar(19)

```
perder_sanidade()

mostrar("""
```

👹 FASE 19 — O PRIMEIRO ENCONTRO

Um som estranho ecoa pela caverna.

Todos param.

No final do corredor aparece uma enorme silhueta.

Por alguns segundos, ninguém consegue se mover.

Milo reconhece a criatura pelas histórias
que ouviu durante toda a infância.

Barbara sussurra:

— Então era verdade.

A criatura se aproxima.

Milo pede para todos recuarem.

Vocês percebem que ainda não estão preparados
para enfrentá-la.

A única opção é fugir e descobrir mais sobre
a sua fraqueza.
""")

```
criar_botao("🏃 Fugir", fase20)
```

def fase20(event=None):
preparar(20)

```
mostrar("""
```

🏃 FASE 20 — A FUGA

O grupo corre pelos corredores da caverna.

Milo conhece parte daquele caminho e consegue
guiar todos de volta.

A criatura continua atrás de vocês.

O corredor se divide.

Agora precisam escolher rapidamente.
""")

```
criar_botao("⬅️ Seguir pela esquerda", fase20_esquerda)
criar_botao("➡️ Seguir pela direita", fase20_direita)
criar_botao("🫣 Procurar um esconderijo", fase20_esconder)
```

def fase20_esquerda(event):
state["pistas"] += 1

```
mostrar("""
```

O caminho da esquerda parece longo.

Milo encontra marcas antigas nas paredes.

Elas indicam uma saída.

O grupo continua até conseguir escapar.
""")

```
criar_botao("🔎 Descobrir a fraqueza", fase21)
```

def fase20_direita(event):
state["pistas"] += 2

```
mostrar("""
```

O caminho da direita leva a uma pequena sala.

Barbara encontra uma inscrição antiga.

Ela fala novamente sobre o símbolo original.

Agora vocês têm uma pista importante.
""")

```
criar_botao("🔎 Descobrir a fraqueza", fase21)
```

def fase20_esconder(event):
ganhar_sanidade()

```
mostrar("""
```

O grupo encontra uma passagem lateral.

Todos permanecem escondidos até a criatura
passar pelo corredor.

Depois de algum tempo, o caminho fica silencioso.

Vocês conseguem sair.

Agora precisam descobrir como enfrentar
a criatura.
""")

```
criar_botao("🔎 Descobrir a fraqueza", fase21)
```

def fase21(event=None):
preparar(21)

```
state["monstro_fraqueza"] = True
state["pistas"] += 3

mostrar("""
```

🔎 FASE 21 — A FRAQUEZA

Depois de comparar o diário, os símbolos e as pistas,
Barbara consegue entender a mensagem.

A criatura não é invencível.

O símbolo original pode enfraquecê-la.

O cristal encontrado perto do lago também parece
estar relacionado ao símbolo.

Milo olha para os visitantes.

— Então temos uma chance.

Barbara completa:

— Mas precisamos chegar até ela novamente.

Agora vocês sabem o que precisam fazer.
""")

```
atualizar_status()
criar_botao("🏚️ Voltar ao esconderijo", fase22)
```

def fase22(event=None):
preparar(22)

```
mostrar("""
```

🏚️ FASE 22 — O ESCONDERIJO

As pistas levam vocês para uma região subterrânea.

Milo reconhece algumas marcas.

— Essa deve ser a parte mais antiga das cavernas.

Barbara encontra objetos deixados por antigos moradores.

Tudo indica que aquele lugar foi usado para esconder
informações sobre a criatura.

Uma grande porta aparece no final do corredor.

O segredo está atrás dela.
""")

```
criar_botao("🚪 Abrir a porta", fase23)
```

def fase23(event=None):
preparar(23)

```
state["pistas"] += 2

mostrar("""
```

🆘 FASE 23 — O RESGATE

Antes de chegar à sala principal, vocês escutam
uma voz.

É o morador desaparecido.

Ele está escondido em uma pequena sala.

Milo corre até ele.

— Nós estávamos procurando você!

O homem explica que foi levado para a caverna
e conseguiu escapar.

Ele está muito assustado.

— Vocês precisam sair daqui.

Barbara pergunta:

— O que aconteceu?

O homem responde:

— Ela está acordada.

Agora vocês precisam decidir o que fazer.
""")

```
criar_botao("🚶 Levar o homem embora", fase24_resgate)
criar_botao("🫣 Deixá-lo escondido", fase24_resgate)
```

def fase24_resgate(event):
state["pistas"] += 1

```
mostrar("""
```

Milo ajuda o homem a se levantar.

Barbara encontra um caminho seguro de volta.

O homem consegue acompanhar o grupo.

Agora vocês sabem que precisam terminar
a investigação antes que a criatura apareça novamente.

Todos seguem para a entrada principal do esconderijo.
""")

```
criar_botao("🚪 Continuar", fase24)
```

def fase24(event=None):
preparar(24)

```
mostrar("""
```

🚪 FASE 24 — A ENTRADA DO ESCONDERIJO

Vocês chegam diante de uma enorme porta de pedra.

No centro existe um símbolo.

Barbara observa atentamente.

— Esse desenho é igual ao símbolo original.

Milo aponta para uma pequena abertura.

Talvez o símbolo encontrado durante a investigação
possa abrir a passagem.

Você verifica seus itens.
""")

```
if "símbolo antigo" in state["inv"]:

    state["pistas"] += 3

    mostrar("""
```

O símbolo se encaixa perfeitamente.

A porta começa a se mover.

As paredes brilham por alguns segundos.

A passagem finalmente se abre.

Vocês estão cada vez mais perto da verdade.
""")

```
else:

    perder_vida()

    mostrar("""
```

Vocês não possuem o símbolo original.

Depois de algum esforço conseguem abrir uma pequena
passagem lateral.

O barulho ecoa pela caverna.

Milo olha para todos.

— Agora ela sabe que estamos aqui.
""")

```
atualizar_status()
criar_botao("🚪 Entrar", fase25)
```

def fase25(event=None):
preparar(25)

```
state["pistas"] += 3

mostrar("""
```

📜 FASE 25 — O PASSADO

Dentro do esconderijo existem documentos muito antigos.

Olivier ou Amelie começa a procurar informações
sobre o parente desaparecido.

Depois de algum tempo, encontra uma anotação.

O documento confirma que o parente esteve naquela ilha.

Ele descobriu a existência da criatura.

Também tentou impedir que ela fosse libertada.

Uma das últimas páginas diz:

"Se alguém da minha família encontrar este lugar,
precisará terminar o que comecei."

Barbara fica surpresa.

Milo olha para os documentos.

— Então ele estava tentando proteger a ilha.

Agora vocês entendem por que tantos registros
foram escondidos.
""")

```
atualizar_status()
criar_botao("➡️ Continuar", fase26)
```

def fase26(event=None):
preparar(26)

```
mostrar("""
```

⚔️ FASE 26 — A PREPARAÇÃO

A criatura está próxima.

Vocês precisam organizar tudo o que descobriram.

O símbolo antigo pode ser a principal esperança.

O cristal também parece reagir à presença dela.

Milo e Barbara estão prontos para ajudar.

Antes do confronto, vocês precisam decidir
como se preparar.
""")

```
criar_botao("🎒 Organizar equipamentos", fase26_equipamentos)
criar_botao("🔱 Preparar o símbolo", fase26_simbolo)
criar_botao("📖 Revisar as pistas", fase26_pistas)
```

def fase26_equipamentos(event):
if "equipamento" in state["inv"]:
state["batalha"] += 2

```
mostrar("""
```

Vocês organizam os equipamentos encontrados
durante a investigação.

Milo verifica tudo.

Barbara guarda as pistas.

O grupo está preparado para continuar.
""")

```
atualizar_status()
criar_botao("👹 Ir até a criatura", fase27)
```

def fase26_simbolo(event):
if "símbolo antigo" in state["inv"]:
state["batalha"] += 3
state["monstro_fraqueza"] = True

```
    mostrar("""
```

O símbolo reage quando é colocado perto do cristal.

Uma luz aparece nas paredes.

Barbara percebe que a descoberta pode ser importante.

Milo respira fundo.

— Essa pode ser nossa melhor chance.
""")

```
else:

    mostrar("""
```

Vocês procuram pelo símbolo, mas percebem
que ainda não conseguiram encontrá-lo.

Barbara decide confiar nas informações do diário.
""")

```
atualizar_status()
criar_botao("👹 Ir até a criatura", fase27)
```

def fase26_pistas(event):
state["batalha"] += 2
state["monstro_fraqueza"] = True

```
mostrar("""
```

Vocês revisam todas as pistas.

O diário, o cristal e os símbolos contam
a mesma história.

A criatura pode ser enfraquecida pelo símbolo.

Agora todos sabem o que precisam fazer.
""")

```
atualizar_status()
criar_botao("👹 Ir até a criatura", fase27)
```

def fase27(event=None):
preparar(27)

```
mostrar("""
```

👹 FASE 27 — O MONSTRO

O grupo chega à última sala.

O lugar é enorme.

No centro existe uma estrutura cercada pelos
mesmos símbolos encontrados na igreja.

A criatura está ali.

Milo reconhece o local.

— É aqui que tudo começou.

Barbara segura as pistas.

Olivier ou Amelie observa a criatura.

Depois de tudo que vocês descobriram,
não existe mais como voltar atrás.

O segredo da ilha está diante de vocês.
""")

```
criar_botao("⚔️ Preparar o confronto", fase28)
```

def fase28(event=None):
preparar(28)

```
mostrar("""
```

⚔️ FASE 28 — O CONFRONTO

A criatura se movimenta.

Milo e Barbara ajudam a manter o grupo unido.

O símbolo pode ser usado para enfraquecê-la.

O cristal começa a brilhar.

Vocês precisam trabalhar juntos.

Escolha uma estratégia.
""")

```
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
```

Você ativa o símbolo antigo.

As paredes começam a brilhar.

A criatura recua.

Barbara percebe que a estratégia está funcionando.

Milo grita:

— Continue!

Pela primeira vez, parece possível derrotar
a criatura.
""")

```
else:
    perder_sanidade()

    mostrar("""
```

Você tenta ativar o símbolo, mas percebe que
não o possui.

A criatura continua avançando.

O grupo precisa procurar outra forma de continuar.
""")

```
atualizar_status()
criar_botao("🔥 Última decisão", fase29)
```

def fase28_milo(event):
state["confianca_milo"] += 2
state["batalha"] += 2

```
mostrar("""
```

Você ajuda Milo a chegar até uma das inscrições.

Ele reconhece um símbolo importante.

— Eu conheço esse desenho!

Milo explica como os antigos moradores utilizavam
os símbolos para proteger a ilha.

A descoberta ajuda o grupo.
""")

```
atualizar_status()
criar_botao("🔥 Última decisão", fase29)
```

def fase28_barbara(event):
state["confianca_barbara"] += 2
state["batalha"] += 2

```
mostrar("""
```

Você ajuda Barbara a examinar as inscrições.

Ela encontra um detalhe escondido.

— Existe outro símbolo aqui!

A descoberta confirma as informações do diário.

Agora vocês sabem que a criatura pode ser enfraquecida.
""")

```
atualizar_status()
criar_botao("🔥 Última decisão", fase29)
```

def fase28_recuar(event):
perder_vida()

```
mostrar("""
```

Vocês recuam por alguns segundos.

A criatura avança, mas o grupo consegue reorganizar
a estratégia.

Milo aponta para o símbolo.

— Precisamos decidir agora.

Não existe mais tempo para fugir da decisão.
""")

```
atualizar_status()
criar_botao("🔥 Última decisão", fase29)
```

def fase29(event=None):
preparar(29)

```
mostrar("""
```

🔥 FASE 29 — A ÚLTIMA ESCOLHA

A criatura está diante de vocês.

Depois de tudo que aconteceu,
a verdade sobre a ilha finalmente foi descoberta.

Milo e Barbara sabem que aquele momento pode
decidir o futuro da ilha.

Olivier ou Amelie precisa tomar a decisão final.

O que você fará?
""")

```
criar_botao("✨ Tentar derrotar a criatura", final_derrotar)
criar_botao("🔒 Selar a criatura novamente", final_selar)
criar_botao("🏃 Fugir da ilha", final_fugir)
```

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

def fase30(event=None):
limpar()
atualizar_status()

```
if state["escolheu_derrotar"] and state["monstro_derrotado"]:

    mostrar_imagem_final("final_01.png")

    mostrar("""
```

🌟 FINAL 1 — O SEGREDO REVELADO

O símbolo antigo começa a brilhar.

As inscrições espalhadas pela sala se iluminam
uma após outra.

A criatura perde sua força.

Milo e Barbara permanecem ao lado de vocês.

Depois de tantos anos, o segredo da ilha finalmente
chega ao fim.

Os documentos encontrados provam que o parente
de Olivier ou Amelie esteve ali muitos anos atrás.

Ele tentou proteger a ilha e impedir que a criatura
voltasse a ameaçar os moradores.

Agora a verdade pode finalmente ser contada.

Milo olha para a vila ao longe.

Barbara respira aliviada.

A ilha finalmente pode ter paz.

🏝️ O SEGREDO DA ILHA FOI REVELADO.
""")

```
elif state["escolheu_derrotar"]:

    mostrar_imagem_final("final_02.png")

    mostrar("""
```

🌅 FINAL 2 — A VITÓRIA INCOMPLETA

Vocês tentam enfrentar a criatura.

Durante alguns momentos parece que a estratégia
vai funcionar.

Mas o símbolo não é suficiente.

A criatura recua para as profundezas da ilha.

Milo consegue guiar todos de volta.

Barbara leva os documentos encontrados.

Vocês sobreviveram, mas o segredo ainda existe.

A criatura continua escondida.

Talvez um dia alguém consiga terminar o que vocês
começaram.

Por enquanto, a ilha permanece em silêncio.
""")

```
elif state["escolheu_selar"]:

    mostrar_imagem_final("final_03.png")

    mostrar("""
```

🔒 FINAL 3 — O SEGREDO PERMANECE

Vocês decidem não destruir a criatura.

Barbara ajuda a ativar os símbolos antigos.

Milo acompanha o processo.

A passagem começa a se fechar.

A criatura desaparece novamente nas profundezas.

O segredo da ilha continua escondido.

Milo sabe que o perigo pode voltar um dia.

Barbara guarda os documentos encontrados.

Agora os moradores sabem que precisam proteger
aquele lugar novamente.

A ilha está segura...

por enquanto.
""")

```
elif state["escolheu_fugir"]:

    mostrar_imagem_final("final_06.png")

    mostrar("""
```

🏃 FINAL 4 — A FUGA DA ILHA

Vocês decidem que continuar seria perigoso demais.

Milo conhece o caminho de volta.

Barbara ajuda o grupo a encontrar a saída.

Olivier ou Amelie consegue chegar ao barco
com as pistas encontradas.

A ilha começa a ficar para trás.

Milo e Barbara permanecem na ilha.

Aquele lugar é a casa deles.

Vocês levam os documentos e algumas respostas,
mas não conseguiram descobrir tudo.

A criatura continua escondida.

O segredo da ilha permanece.

Talvez um dia alguém volte.
""")

```
else:

    mostrar_imagem_final("final_03.png")

    mostrar("""
```

👁️ FINAL — O MISTÉRIO CONTINUA

A investigação chegou ao fim sem respostas suficientes.

Vocês conseguiram escapar, mas muitas perguntas
continuam sem resposta.

Milo e Barbara continuam vivendo na ilha.

Eles sabem que existem lugares que ainda precisam
ser investigados.

Olivier ou Amelie leva consigo os poucos documentos
encontrados.

Talvez a verdade ainda esteja escondida em algum
lugar da ilha.

O segredo continua...
""")

```
mostrar("""
```

============================================================

🎮 FIM DO JOGO

============================================================
""")

```
mostrar("👤 Personagem: " + state["personagem"])
mostrar("❤️ Vida: " + str(state["vida"]))
mostrar("🧠 Sanidade: " + str(state["sanidade"]))
mostrar("🔎 Pistas: " + str(state["pistas"]))

if len(state["inv"]) > 0:
    mostrar("🎒 Inventário: " + ", ".join(state["inv"]))
else:
    mostrar("🎒 Inventário: vazio")

criar_botao("🔄 Jogar novamente", reiniciar)
```

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

fase1()
