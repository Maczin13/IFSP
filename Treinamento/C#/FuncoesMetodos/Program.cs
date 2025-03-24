using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FuncoesMetodos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ExibirDesconto(PedirNomeProduto(), CalcularDesconto(PedirPrecoOriginal(), 0.15));


        }

        static string PedirNomeProduto()
        {
            Console.WriteLine("===================================================================");
            Console.Write("Digite o nome do produto: ");
            string nomeProduto = Console.ReadLine();

            return nomeProduto;
        }

        static double PedirPrecoOriginal()
        {
            double precoOriginal = 0;
            bool converteu = false;

            Console.Write("Digite o preço do produto: ");

            while (!converteu)
            {
                converteu = double.TryParse(Console.ReadLine(), out precoOriginal);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico para o preço");
                }
                else if (precoOriginal <= 0)
                {
                    Console.WriteLine("Digite um valor maior que zero para o preço");
                    converteu = false;
                }

            }


            return precoOriginal;
        }

        static double CalcularDesconto(double precoOriginal, double desconto)
        {
            return precoOriginal - (precoOriginal * desconto);
        }

        static void ExibirDesconto(string nomeProduto, double precoFinal)
        {
            Console.WriteLine("===================================================================");
            Console.WriteLine($"Produto: {nomeProduto}");
            Console.WriteLine($"Preço com desconto: R${precoFinal:F2}");
            Console.WriteLine("===================================================================");
            Console.ReadKey();
        }

    }
}
