using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula_07
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //ExemploUm();
            //ExUm();
            ExDois();
        }

        static void ExemploUm()
        {
            string[] alunos = new string[10];


            for (int ii = 0; ii < alunos.Length; ii++)
            {
                Console.WriteLine($"Digite o nome o aluno {ii + 1}: ");
                alunos[ii] = Console.ReadLine();
            }

            foreach (string aluno in alunos)
            {
                Console.WriteLine(aluno);
            }
            Console.ReadKey();
        }

        static void ExUm()
        {
            double[] numeros = new double[10];
            double maiorNumero = 0;          
            bool converteu;

            for (int ii = 0; ii < numeros.Length; ii++)
            {
                do
                {
                    Console.WriteLine($"Digite o valor do número {ii + 1}");
                    converteu = double.TryParse(Console.ReadLine(), out numeros[ii]);

                    if(!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico!");
                    }
                } while (!converteu);
                
            }

            maiorNumero = numeros[0];

            for(int ii = 1; ii < numeros.Length; ii++)
            {
                if (numeros[ii] > maiorNumero)
                {
                    maiorNumero = numeros[ii];
                }
            }

            Console.WriteLine(maiorNumero);

        }

        static void ExDois()
        {
            string[] alunos = new string[5];
            double[] p1 = new double[5];
            double[] p2 = new double[5];
            double[] media = new double[5];
            bool converteu;

            for (int ii = 0; ii < alunos.Length; ii++)
            {
                Console.WriteLine($"Digite o nome o aluno {ii + 1}: ");
                alunos[ii] = Console.ReadLine();

                do
                {
                    Console.WriteLine("Digite a nota da P1: ");

                    converteu = double.TryParse(Console.ReadLine(), out p1[ii]);

                    if(!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico para nota!");
                    }
                    else if (p1[ii] < 0 ||  p1[ii] > 10)
                    {
                        Console.WriteLine("A nota deve ser de 1 a 10!");
                        converteu = false;
                    }        

                } while (!converteu);

                do
                {
                    Console.WriteLine("Digite a nota da P2: ");

                    converteu = double.TryParse(Console.ReadLine(), out p2[ii]);

                    if (!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico para nota!");
                    }
                    else if (p2[ii] < 0 || p2[ii] > 10)
                    {
                        Console.WriteLine("A nota deve ser de 1 a 10!");
                        converteu = false;
                    }

                } while (!converteu);
            }

            Console.Clear();

            for (int ii = 0; ii < alunos.Length; ii++)
            {
                Console.WriteLine("===============================================================================");
                Console.WriteLine($"Aluno: {alunos[ii]} P1: {p1[ii]} P2: {p2[ii]} Media: {(p1[ii] + p2[ii])/2}");
                Console.WriteLine("===============================================================================");
            }

            Console.ReadKey();

        }
    }
}
