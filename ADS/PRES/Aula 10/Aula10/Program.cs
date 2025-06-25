using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace Aula10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n1, n2, opcao;

            do
            {
                Menu();
                opcao = int.Parse(Console.ReadLine());
                if (opcao != 5)
                {
                    Console.Clear();
                    Console.WriteLine("Informe o primeiro número");
                    n1 = int.Parse(Console.ReadLine());
                    Console.WriteLine("Informe o sgundo número");
                    n2 = int.Parse(Console.ReadLine());

                    if (opcao == 1)
                    {
                        Console.WriteLine("Soma: {0}", Soma(n1, n2));
                    }
                    else if (opcao == 2)
                    {
                        Console.WriteLine("Subtração: {0}", Subtracao(n1, n2));
                    }
                    else if (opcao == 3)
                    {
                        Console.WriteLine("Multiplicação: {0}", Multiplicacao(n1, n2));
                    }
                    else
                    {
                        if (n2 == 0)
                            Console.WriteLine("Erro - o divisor não pode ser zero!");
                        else
                            Console.WriteLine("Divisão: {0}", (double)Divisao(n1, n2));
                    }
                }
            } while (opcao != 5);



        }
        private static void Menu()
        {
            Console.WriteLine("Menu principal");
            Console.WriteLine("---------------");
            Console.WriteLine("1. Somar");
            Console.WriteLine("2. Subtrair");
            Console.WriteLine("3. Multiplicar");
            Console.WriteLine("4. Dividir");
            Console.WriteLine("5. Sair");
            Console.WriteLine("---------------");
            Console.Write("Sua opção: ");
        }

        private static int Soma(int x, int y)
        {
            return x + y;
        }

        private static int Subtracao(int x, int y)
        {
            return x - y;
        }
        private static int Multiplicacao(int x, int y)
        {
            return x * y;
        }
        private static int Divisao(int x, int y)
        {
            return x / y;
        }
    }
}
