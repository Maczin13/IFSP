using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            exUm();
        }
        static void exUm()
        {
            double nTrabalho = 0, nAvali = 0, nProvaF = 0;
            double media = 0;
            bool converteu;

            do
            {
                Console.WriteLine("Digite a nota do trabalho: ");
                converteu = double.TryParse(Console.ReadLine(), out nTrabalho);
                if(!converteu)
                {
                    Console.WriteLine("Digite um valor numérico para nota!");
                }
                else if (nTrabalho < 0 || nTrabalho > 10)
                {
                    Console.WriteLine("Digite uma nota de 0 a 10");
                    converteu = false;
                }

            } while (!converteu);

            do
            {
                Console.WriteLine("Digite a nota da avaliação semestral: ");
                converteu = double.TryParse(Console.ReadLine(), out nAvali);
                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico para nota!");
                }
                else if (nAvali < 0 || nAvali > 10)
                {
                    Console.WriteLine("Digite uma nota de 0 a 10");
                    converteu = false;
                }

            } while (!converteu);

            do
            {
                Console.WriteLine("Digite a nota da Prova Final: ");
                converteu = double.TryParse(Console.ReadLine(), out nProvaF);
                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico para nota!");
                }
                else if (nProvaF < 0 || nProvaF > 10)
                {
                    Console.WriteLine("Digite uma nota de 0 a 10");
                    converteu = false;
                }

            } while (!converteu);

            media = ((nTrabalho * 2) + (nAvali * 3) + (nProvaF * 5)) / 10;

            if(media >= 8)
            {
                Console.WriteLine("A");
            }
            else if (media >= 7)
            {
                Console.WriteLine("B");
            }
            else if (media >= 6)
            {
                Console.WriteLine("C");
            }
            else if (media >= 5)
            {
                Console.WriteLine("D");
            }
            else
            {
                Console.WriteLine("E");
            }
        }
    }
}
