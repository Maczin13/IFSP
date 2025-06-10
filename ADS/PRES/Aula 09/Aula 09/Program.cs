using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula_09
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ExUm();
            ExDois();
            ExTres();
            ExQuatro();

        }

        static void ExUm()
        {
            int quantidade = 0, quant15 = 0, quant30 = 0, quant45 = 0, quant60 = 0, quant61 = 0;
            int idade = 0;
            bool converteu;

            do
            {
                Console.Clear();
                Console.WriteLine("Digite a quantidade de pessoas que deseja ler a idade: ");
                converteu = int.TryParse(Console.ReadLine(), out quantidade);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico e inteiro!");
                    Console.ReadKey();
                }
                else if (quantidade < 0)
                {
                    Console.WriteLine("Digite um valor positivo");
                    converteu = false;
                    Console.ReadKey();
                }
                
            } while (!converteu);

            for (int ii = 0; ii < quantidade; ii++)
            {
                converteu = false;

                do
                {
                    Console.WriteLine($"Digite a idade da pessoa {ii+ 1}: ");
                    converteu = int.TryParse(Console.ReadLine(),out idade);
                    if(!converteu || idade < 0)
                    {
                        Console.WriteLine("Digite um valor numérico, inteiro e maior do que zero para idade");
                        converteu = false;
                        Console.ReadKey();
                    }
                }while (!converteu);

                if(idade <= 15)
                {
                    quant15++;
                }
                else if(idade <= 30)
                {
                    quant30++;
                }
                else if(idade <= 45)
                {
                    quant45++;
                }
                else if(idade <= 60)
                {
                    quant60++;
                }
                else
                {
                    quant61++;
                }
            }

            Console.WriteLine("Seguem as porcentagens por faixa etária: ");
            Console.WriteLine($"De 1 a 15 anos: {(quant15 * 100) / quantidade}%");
            Console.WriteLine($"De 16 a 30 anos: {(quant30 * 100) / quantidade}%");
            Console.WriteLine($"De 31 a 45 anos: {(quant45 * 100) / quantidade}%");
            Console.WriteLine($"De 46 a 60 anos: {(quant60 * 100) / quantidade}%");
            Console.WriteLine($"Acima de 61 anos: {(quant15 * 100) / quantidade}%");
        }

        static void ExDois()
        {
            string codigo = "";
            double valorVista = 0, valorPrazo = 0, valor = 0;
            int totalCompras = 0;
            bool converteu;

            do
            {
                Console.WriteLine("Digite o código da compra. (v: compras a vista p: compras a prazp f: Encerrar operação)");
                codigo = Console.ReadLine();

                switch(codigo.ToLower())
                {
                    case "v":
                        do
                        {
                            Console.WriteLine("Digite o valor da compra: ");
                            converteu = double.TryParse(Console.ReadLine(), out valor);
                            if(!converteu || valor <= 0)
                            {
                                converteu = false;
                                Console.WriteLine("Digite um valor numérico e maior que zero");
                                Console.ReadKey();
                            }
                        } while(!converteu);
                        valorVista += valor;
                        totalCompras++;

                        break;
                    case "p":
                        do
                        {
                            Console.WriteLine("Digite o valor da compra: ");
                            converteu = double.TryParse(Console.ReadLine(), out valor);
                            if (!converteu || valor <= 0)
                            {
                                converteu = false;
                                Console.WriteLine("Digite um valor numérico e maior que zero");
                                Console.ReadKey();
                            }
                        } while (!converteu);
                        valorPrazo += valor;
                        totalCompras++;
                        break;
                    case "f":
                        Console.WriteLine("Operação encerrada. Aperte qualquer tecla para prosseguir.");
                        Console.ReadKey();
                        break;
                    default:
                        Console.WriteLine("Código inválido");
                        break;
                }


            } while (codigo != "f");

            Console.WriteLine($"O valor total de compras a vista é de R${valorVista}");
            Console.WriteLine($"O valor total de compras a prazo é de R${valorPrazo}");
            Console.WriteLine($"Houve um total de {totalCompras} compras.");
            Console.WriteLine($"Será recebido hoje R${valorPrazo / 3} de compras a prazo (entradas)");
        }

        static void ExTres()
        {
            double[] numeros = new double[15];
            bool converteu;

            for ( int ii = 0; ii < numeros.Length; ii++ )
            {
                Console.WriteLine($"Digite o valor do {ii + 1}° termo");

                do
                {
                    converteu = double.TryParse(Console.ReadLine(), out numeros[ii]);
                    if(!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico");
                    }
                } while (!converteu);
            }

            foreach( double numero in numeros )
            {
                if(numero % 2 == 0)
                {
                    Console.WriteLine($"Par: {numero}");
                }
            }
            foreach (double numero in numeros)
            {
                if (numero % 2 != 0)
                {
                    Console.WriteLine($"Impar: {numero}");
                }
            }
        }

        static void ExQuatro()
        {
            const int quantidadeAlunos = 10;
            double[] notasP1 = new double[quantidadeAlunos];
            double[] notasP2 = new double[quantidadeAlunos];
            double somaMedias = 0;
            int aprovados = 0, reprovados = 0;

            for (int i = 0; i < quantidadeAlunos; i++)
            {
                notasP1[i] = LerNota($"Digite a nota da P1 do Aluno {i + 1}: ");
            }

            for (int i = 0; i < quantidadeAlunos; i++)
            {
                notasP2[i] = LerNota($"Digite a nota da P2 do Aluno {i + 1}: ");
            }

            Console.WriteLine("\nResultados:");

            for (int i = 0; i < quantidadeAlunos; i++)
            {
                double media = (notasP1[i] + notasP2[i]) / 2;
                somaMedias += media;

                if (media >= 6.0)
                    aprovados++;
                else
                    reprovados++;

                Console.WriteLine($"Aluno {i + 1} – P1: {notasP1[i]:0.0} – P2: {notasP2[i]:0.0} – Média: {media:0.0}");
            }

            double mediaClasse = somaMedias / quantidadeAlunos;
            Console.WriteLine($"\nMédia da Classe: {mediaClasse:0.0}");
            Console.WriteLine($"Quantidade de Alunos Aprovados: {aprovados}");
            Console.WriteLine($"Quantidade de Alunos Reprovados: {reprovados}");
        }
        static double LerNota(string mensagem)
        {
            double nota;
            while (true)
            {
                Console.Write(mensagem);
                if (double.TryParse(Console.ReadLine(), out nota) && nota >= 0.0 && nota <= 10.0)
                {
                    return nota;
                }
                else
                {
                    Console.WriteLine("Nota inválida! Digite um valor entre 0 e 10.");
                }
            }
        }
    }
}
