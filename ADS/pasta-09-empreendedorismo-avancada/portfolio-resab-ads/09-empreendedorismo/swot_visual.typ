#set page(paper: "a4", flipped: true, margin: (x: 30pt, y: 16pt), fill: rgb("F7F9FC"))
#set text(font: "Liberation Sans", size: 9pt, fill: rgb("243247"))
#set par(leading: 1em)
#let navy = rgb("17324D")
#let green = rgb("DDF5EF")
#let red = rgb("FCE4E4")
#let blue = rgb("DCEEFF")
#let amber = rgb("FFF0D8")
#let bullet(txt) = [#sym.bullet #h(4pt) #txt #linebreak()]
#let quad(label, subtitle, body, fill, accent) = box(width: 1fr, height: 150pt, fill: fill, stroke: 1.2pt + accent, radius: 9pt, inset: 10pt)[
  #text(size: 13pt, weight: "bold", fill: accent)[#label]
  #v(3pt)
  #text(size: 8pt, weight: "bold", fill: rgb("60758D"))[#subtitle]
  #v(12pt)
  #body
]

#align(center)[
  #text(size: 24pt, weight: "bold", fill: navy)[SWOT]
  #linebreak()
  #text(size: 11pt, fill: rgb("60758D"))[Agenda Adaptativa de Estudos · análise interna e externa]
]
#v(12pt)
#grid(columns: (1fr, 1fr), gutter: 12pt,
  quad([FORÇAS], [Fatores internos · capacidades], [#bullet[Priorização explicável por RICE, WSJF e ROI de tempo] #bullet[MVP pequeno, mensurável e executável] #bullet[Orçamento de horas explícito] #bullet[Registro de hipóteses e status de validação]], green, rgb("1E8066")),
  quad([FRAQUEZAS], [Fatores internos · limitações], [#bullet[Hipótese de valor ainda não validada] #bullet[Sem integração real com calendários] #bullet[Sem histórico de coortes] #bullet[Alcance e impacto ainda são estimativas subjetivas]], red, rgb("B84A4A")),
  quad([OPORTUNIDADES], [Fatores externos · possibilidades], [#bullet[Nichos de preparação e autodidatismo] #bullet[Integração com ferramentas educacionais] #bullet[Experimentos de recomendação e revisão espaçada] #bullet[Parcerias com comunidades de estudo]], blue, rgb("286AA6")),
  quad([AMEAÇAS], [Fatores externos · riscos], [#bullet[Concorrentes com calendário, comunidade e maior distribuição] #bullet[Baixa retenção após a novidade inicial] #bullet[Custo de aquisição superior ao valor percebido] #bullet[Preocupações com dados pessoais e confiança]], amber, rgb("B56C13"))
)
#v(6pt)
#grid(columns: (1fr, 1fr), gutter: 12pt,
  box(width: 1fr, fill: white, stroke: 0.8pt + rgb("C9D4E2"), radius: 8pt, inset: 13pt)[
    #text(size: 9pt, weight: "bold", fill: navy)[Mitigação objetiva]
    #v(5pt)
    Entrevistar antes de ampliar funcionalidades; medir ativação, retenção semanal, tarefas concluídas e tempo até o primeiro valor; testar canais por custo por usuário ativado; minimizar dados e comunicar o uso com transparência.
  ],
  box(width: 1fr, fill: white, stroke: 0.8pt + rgb("C9D4E2"), radius: 8pt, inset: 13pt)[
    #text(size: 9pt, weight: "bold", fill: navy)[Critérios de pivotagem]
    #v(5pt)
    Manter a direção se houver uso recorrente e melhora mensurável. Simplificar o fluxo se houver interesse sem retenção. Alterar a proposta se houver dor sem ativação. Pivotar ou interromper se não houver dor relevante e o custo de aquisição for alto.
  ]
)
#v(4pt)
#align(right)[#text(size: 7pt, fill: rgb("60758D"))[Documento de trabalho · Riscos e hipóteses devem ser reavaliados com evidência]
]
