using System;

namespace ProjetoMedicamentos
{
    class Program
    {
        static void Main(string[] args)
        {
            Medicamentos controleMedicamentos = new Medicamentos();
            int opcao = -1;

            while (opcao != 0)
            {
                Console.Clear();
                Console.WriteLine("=================================");
                Console.WriteLine("       PROJETO MEDICAMENTOS      ");
                Console.WriteLine("=================================");
                Console.WriteLine("0. Finalizar processo");
                Console.WriteLine("1. Cadastrar medicamento");
                Console.WriteLine("2. Consultar medicamento (sintético)");
                Console.WriteLine("3. Consultar medicamento (analítico)");
                Console.WriteLine("4. Comprar medicamento (cadastrar lote)");
                Console.WriteLine("5. Vender medicamento (abater lote)");
                Console.WriteLine("6. Listar medicamentos");
                Console.WriteLine("=================================");
                Console.Write("Escolha uma opção: ");
                
                if (!int.TryParse(Console.ReadLine(), out opcao)) continue;

                switch (opcao)
                {
                    case 0:
                        Console.WriteLine("Encerrando...");
                        break;

                    case 1:
                        Console.Write("ID do Medicamento: ");
                        int idCadastro = int.Parse(Console.ReadLine());
                        Console.Write("Nome: ");
                        string nome = Console.ReadLine();
                        Console.Write("Laboratório: ");
                        string lab = Console.ReadLine();

                        Medicamento novoMed = new Medicamento(idCadastro, nome, lab);
                        
                        if (controleMedicamentos.pesquisar(novoMed).Id == 0)
                        {
                            controleMedicamentos.adicionar(novoMed);
                            Console.WriteLine("Medicamento cadastrado com sucesso!");
                        }
                        else
                        {
                            Console.WriteLine("Erro: Medicamento com este ID já existe.");
                        }
                        break;

                    case 2:
                        Console.Write("Informe o ID do medicamento: ");
                        Medicamento medBusca = new Medicamento { Id = int.Parse(Console.ReadLine()) };
                        Medicamento medSintetico = controleMedicamentos.pesquisar(medBusca);

                        if (medSintetico.Id != 0)
                            Console.WriteLine("\n[Dados] " + medSintetico.ToString());
                        else
                            Console.WriteLine("Medicamento não encontrado.");
                        break;

                    case 3:
                        Console.Write("Informe o ID do medicamento: ");
                        Medicamento medBuscaAnalitica = new Medicamento { Id = int.Parse(Console.ReadLine()) };
                        Medicamento medAnalitico = controleMedicamentos.pesquisar(medBuscaAnalitica);

                        if (medAnalitico.Id != 0)
                        {
                            Console.WriteLine("\n[Dados] " + medAnalitico.ToString());
                            Console.WriteLine("--- Lotes ---");
                            if (medAnalitico.Lotes.Count > 0)
                            {
                                foreach (var lote in medAnalitico.Lotes)
                                {
                                    Console.WriteLine(lote.ToString());
                                }
                            }
                            else
                            {
                                Console.WriteLine("Nenhum lote disponível.");
                            }
                        }
                        else
                        {
                            Console.WriteLine("Medicamento não encontrado.");
                        }
                        break;

                    case 4:
                        Console.Write("Informe o ID do medicamento para compra: ");
                        Medicamento medCompraBusca = new Medicamento { Id = int.Parse(Console.ReadLine()) };
                        Medicamento medCompra = controleMedicamentos.pesquisar(medCompraBusca);

                        if (medCompra.Id != 0)
                        {
                            Console.Write("ID do Lote: ");
                            int idLote = int.Parse(Console.ReadLine());
                            Console.Write("Quantidade: ");
                            int qtdeLote = int.Parse(Console.ReadLine());
                            Console.Write("Data de Vencimento (DD/MM/AAAA): ");
                            DateTime vencLote = DateTime.Parse(Console.ReadLine());

                            Lote novoLote = new Lote(idLote, qtdeLote, vencLote);
                            medCompra.comprar(novoLote);
                            Console.WriteLine("Lote comprado e cadastrado com sucesso!");
                        }
                        else
                        {
                            Console.WriteLine("Medicamento não encontrado.");
                        }
                        break;

                    case 5:
                        Console.Write("Informe o ID do medicamento para venda: ");
                        Medicamento medVendaBusca = new Medicamento { Id = int.Parse(Console.ReadLine()) };
                        Medicamento medVenda = controleMedicamentos.pesquisar(medVendaBusca);

                        if (medVenda.Id != 0)
                        {
                            Console.Write("Quantidade desejada: ");
                            int qtdeVenda = int.Parse(Console.ReadLine());

                            bool sucesso = medVenda.vender(qtdeVenda);
                            if (sucesso)
                                Console.WriteLine("Venda realizada com sucesso! Os lotes foram atualizados.");
                            else
                                Console.WriteLine("Erro na venda: Quantidade insuficiente ou indisponível.");
                        }
                        else
                        {
                            Console.WriteLine("Medicamento não encontrado.");
                        }
                        break;

                    case 6:
                        Console.WriteLine("\n--- Lista de Medicamentos ---");
                        if (controleMedicamentos.ListaMedicamentos.Count > 0)
                        {
                            foreach (var med in controleMedicamentos.ListaMedicamentos)
                            {
                                Console.WriteLine(med.ToString());
                            }
                        }
                        else
                        {
                            Console.WriteLine("Nenhum medicamento cadastrado.");
                        }
                        break;

                    default:
                        Console.WriteLine("Opção inválida!");
                        break;
                }

                if (opcao != 0)
                {
                    Console.WriteLine("\nPressione qualquer tecla para continuar...");
                    Console.ReadKey();
                }
            }
        }
    }
}
