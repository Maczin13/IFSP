#set page(paper: "a4", flipped: true, margin: (x: 28pt, y: 24pt), fill: rgb("F7F9FC"))
#set text(font: "Liberation Sans", size: 9pt, fill: rgb("243247"))
#set par(leading: 0.95em)
#let navy = rgb("17324D")
#let blue = rgb("DCEEFF")
#let teal = rgb("DDF5EF")
#let orange = rgb("FFF0D8")
#let purple = rgb("EEE8FF")
#let card(title, body, fill: white) = box(width: 1fr, height: 106pt, fill: fill, stroke: 0.8pt + rgb("C9D4E2"), radius: 7pt, inset: 10pt)[
  #text(size: 10pt, weight: "bold", fill: navy)[#title]
  #v(6pt)
  #body
]
#let bullet(txt) = [#sym.bullet #h(3pt) #txt #linebreak()]

#align(center)[
  #text(size: 21pt, weight: "bold", fill: navy)[Business Model Canvas]
  #linebreak()
  #text(size: 10pt, fill: rgb("60758D"))[Agenda Adaptativa de Estudos · MVP de priorização e validação]
]
#v(12pt)
#grid(columns: (1fr, 1fr, 1fr, 1fr), gutter: 8pt,
  card[Parceiros-chave][#bullet[Comunidades de estudo] #bullet[Provedores de calendário] #bullet[Criadores de conteúdo], fill: blue],
  card[Atividades-chave][#bullet[Entrevistar estudantes] #bullet[Testar a fatia vertical] #bullet[Medir ativação, retenção e conclusão], fill: teal],
  card[Proposta de valor][#bullet[Transformar objetivos em plano executável] #bullet[Recomendar revisão sem excesso de planejamento] #bullet[Foco em conclusão semanal], fill: orange],
  card[Relacionamento][#bullet[Onboarding guiado] #bullet[Feedback de progresso] #bullet[Revisão semanal e suporte], fill: purple],
  card[Recursos-chave][#bullet[Aplicação web] #bullet[Motor de agenda] #bullet[Dados minimizados, código e telemetria], fill: white],
  box(width: 1fr, height: 106pt, fill: rgb("EAF0F7"), stroke: 0.8pt + rgb("C9D4E2"), radius: 7pt, inset: 10pt)[
    #text(size: 10pt, weight: "bold", fill: navy)[Segmentos de clientes]
    #v(6pt)
    #bullet[Estudantes autodidatas]
    #bullet[Pessoas que perdem consistência]
    #bullet[Preparação para provas e metas]
  ],
  card[Canais][#bullet[Landing page] #bullet[Conteúdo educativo] #bullet[Indicação e comunidades], fill: blue],
  card[Estrutura de custos][#bullet[Desenvolvimento] #bullet[Hospedagem e suporte] #bullet[Aquisição de usuários], fill: orange],
  card[Fluxos de receita][#bullet[Plano gratuito] #bullet[Recurso premium de planejamento] #bullet[Possível plano educacional], fill: teal]
)
#v(11pt)
#box(width: 100%, fill: rgb("17324D"), radius: 7pt, inset: 10pt)[
  #text(size: 9pt, weight: "bold", fill: white)[Hipóteses centrais de validação]
  #h(10pt)
  #text(fill: white)[
    *H1 Problema:* estudantes autodidatas perdem consistência porque planejar e revisar consome esforço. \
    *H2 Valor:* a agenda adaptativa aumenta a conclusão semanal em relação ao planejamento manual. \
    *H3 Negócio:* usuários recorrentes consideram pagar por um recurso premium. \
    *Métrica:* ativação, tarefas concluídas, retenção por coorte, tempo até primeiro valor e disposição a pagar.
  ]
]
#v(5pt)
#align(right)[#text(size: 7pt, fill: rgb("60758D"))[Documento de trabalho · Hipóteses sujeitas a validação]
]
