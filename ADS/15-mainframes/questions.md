# Perguntas e respostas de defesa

**Por que largura fixa em vez de CSV?**  
Arquivos posicionais permitem contratos estáveis de offsets e são comuns em integrações batch. O custo é menor flexibilidade e maior sensibilidade a erro de comprimento.

**O que o copybook representa?**  
Ele documenta e interpreta a estrutura do registro: campos alfanuméricos `PIC X` e numéricos `PIC 9`, suas posições e tamanhos. A classe Python é uma simulação executável desse mapeamento.

**Por que separar rejeitados?**  
O lote precisa continuar processando registros isoladamente e preservar exceções para correção. Misturar rejeitado com aceito perde rastreabilidade e pode contaminar o retorno.

**Como a reconciliação protege o batch?**  
Ela compara o total lido com a soma das saídas. Se houver descarte silencioso, duplicação ou falha de escrita, a contagem não fecha e o job deve ser investigado.

**O código local é COBOL real?**  
O `program.cob` é um programa demonstrativo; a execução validada ocorre em Python porque não há compilador z/OS. O conceito é aproximado, não uma alegação de execução no mainframe.

**Qual a diferença entre ASCII e EBCDIC?**  
São codificações diferentes. A fixture é ASCII controlada; em uma transferência real eu definiria conversão, CCSID, tratamento de caracteres nacionais e validação de bytes.
