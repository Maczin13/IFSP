using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace Aula04
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ExDois();
            ExUm();
        }

        static void ExDois()
        {
            string nomeProf = "";

            Console.WriteLine("Digite o nome do professor");
            nomeProf = Console.ReadLine();

            switch (nomeProf.ToLower())
            {
                case "coletto":
                    Console.WriteLine("Press");
                    Console.WriteLine("BDD");
                    break;
                case "Marco":
                    Console.WriteLine("EDD1");
                    break;
                case "Tuler":
                    Console.WriteLine("Auds");
                    Console.WriteLine("SWE");
                    break;
                default:
                    Console.WriteLine("palhaço");
                    break;
            }

        }

        static void ExUm()
        {
            double numero = 0;
            bool converteu = false, impar = false, continuar = true;

            while (continuar)
            {
                while (!converteu)
                {
                    Console.WriteLine("digite um número: ");

                    converteu = double.TryParse(Console.ReadLine(), out numero);

                    if (!converteu)
                    {
                        Console.WriteLine("Digite um número válido");
                    }
                }

                if ((numero % 2) == 0)
                {
                    impar = false;
                }
                else
                {
                    impar = true;
                }

                switch (impar)
                {
                    case true:
                        Console.WriteLine($"{numero} é ímpar");
                        break;
                    case false:
                        Console.WriteLine($"{numero} é par");
                        break;
                    default:
                        Console.WriteLine("Não sei como você chegou aqui");
                        break;
                }

                Console.WriteLine("Digite 1 para repetir e qualquer outra coisa para sair:");

                string escolha = Console.ReadLine();

                switch (escolha)
                {
                    case "1":
                        continuar = true;
                        converteu = false;
                        break;
                    default:
                        continuar = false;
                        break;

                }

            }



            Console.ReadKey();
        }
    }
}
