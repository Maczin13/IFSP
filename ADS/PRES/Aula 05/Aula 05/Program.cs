using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula_05
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //ExUm();
        }

        static void ExUm()
        {
            double number;
            bool converteu;
            int quantidadeTabuada = 10;

            do
            {
                Console.Clear();

                Console.WriteLine("Digite um número de 1 a 10: ");

                converteu = double.TryParse(Console.ReadLine(), out number);

                if (!converteu)
                {
                    Console.WriteLine("Digite um número, animal");
                    Console.ReadKey();
                }
                else if (number < 1 || number > 10)
                {
                    Console.WriteLine("Você não entendeu que tem que ser de 1 a 10?");
                    Console.ReadKey();
                }


            } while (!converteu || number < 1 || number > 10);

            Console.Clear();

            Console.WriteLine("-----------------------------------------------------");

            for (int ii = 0; ii < quantidadeTabuada; ii++)
            {
                Console.WriteLine($"{number} X {ii + 1} = {number * (ii + 1)}");
            }

            Console.WriteLine("-----------------------------------------------------");

            Console.ReadKey();
        }
    }
}
