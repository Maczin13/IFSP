using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ExercicioUm();
            ExercicioDois();
            ExercicioTres();
        }

        static void ExercicioUm()
        {
            //Declaração de variáveis
            double numeroUm = 0, numeroDois = 0, numeroTres = 0;
            bool converteu = false;

            Console.WriteLine("Exercício 1");

            //Ler números
            while (!converteu)
            {
                Console.WriteLine("Digite o primeiro número");
                converteu = double.TryParse(Console.ReadLine(), out numeroUm);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico");
                }

            }

            converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite o segundo número");
                converteu = double.TryParse(Console.ReadLine(), out numeroDois);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico");
                }

            }

            converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite o terceiro número");
                converteu = double.TryParse(Console.ReadLine(), out numeroTres);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico");
                }

            }

            if(numeroUm > numeroDois && numeroUm > numeroTres)
            {
                Console.WriteLine($"O maior numero digitado é: {numeroUm}");
            }
            else if (numeroDois > numeroUm && numeroDois > numeroTres)
            {
                Console.WriteLine($"O maior numero digitado é: {numeroDois}");
            }

            else if (numeroTres > numeroUm && numeroTres > numeroDois)
            {
                Console.WriteLine($"O maior numero digitado é: {numeroTres}");
            }

            else if (numeroUm == numeroDois && numeroDois > numeroTres)
            {
                Console.WriteLine($"O maior número é {numeroUm}... que foi digitado duas vezes");
            }

            else if (numeroUm == numeroTres && numeroTres > numeroDois)
            {
                Console.WriteLine($"O maior número é {numeroUm}... que foi digitado duas vezes");
            }

            else if (numeroDois == numeroTres && numeroTres > numeroUm)
            {
                Console.WriteLine($"O maior número é {numeroDois}... que foi digitado duas vezes");
            }
            else
            {
                Console.WriteLine("O palhaço digitou o mesmo número três vezes em um programa que verifica o maior.");
            }

        }

        static void ExercicioDois()
        {
            //declarando variáveis
            double aa = 0, bb = 0, cc = 0, delta = 0, x1 = 0, x2 = 0;
            bool converteu = false;

            Console.WriteLine("Ex 2");

            //Lendo valor de A e verificando se é igual a 0
            while(!converteu)
            {
                Console.WriteLine("Digite o valor de 'A': ");
                converteu = double.TryParse(Console.ReadLine(), out aa);

                if(aa == 0)
                {
                    Console.WriteLine("Não é possível calcular uma equação de segundo grau com a = 0!");
                    converteu = false;
                }
                if(!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
            }
            converteu = false;

            //Lendo o valor de B
            while (!converteu)
            {
                Console.WriteLine("Digite o valor de 'B': ");
                converteu = double.TryParse(Console.ReadLine(), out bb);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
            }
            converteu = false;

            //lendo o valor de C
            while (!converteu)
            {
                Console.WriteLine("Digite o valor de 'C': ");
                converteu = double.TryParse(Console.ReadLine(), out cc);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
            }

            //calculando valor de delta e verificando se é negativo
            delta = Math.Pow(bb, 2) - (4 * aa * cc);

            if(delta < 0)
            {
                Console.WriteLine("Delta negativo não há raiz...");
            }

            else
            {
                //Calculando valor de X
                x1 = (-bb + Math.Sqrt(delta)) / 2 * aa;
                x2 = (-bb - Math.Sqrt(delta)) / 2 * aa;

                Console.WriteLine($"Os valores de X são: {x1} e {x2}");

            }



        }

        static void ExercicioTres()
        {
            int numeroSemana = 0;
            bool converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite um número de 1 a 7: ");

                converteu = int.TryParse(Console.ReadLine(),out numeroSemana);

                if(numeroSemana < 1 || numeroSemana > 7)
                {
                    Console.WriteLine("O número precisa ser de 1 a 7");
                    converteu = false;
                }
                else if(!converteu)
                {
                    Console.WriteLine("Digite um valor inteiro!");
                }
            }

            switch(numeroSemana)
            {
                case 1:
                    Console.WriteLine("Domingo");
                    break;

                case 2:
                    Console.WriteLine("Segunda");
                    break;

                case 3:
                    Console.WriteLine("Terça");
                    break;

                case 4:
                    Console.WriteLine("Quarta");
                    break;

                case 5:
                    Console.WriteLine("Quinta");
                    break;

                case 6:
                    Console.WriteLine("Sexta");
                    break;

                case 7:
                    Console.WriteLine("Sábado");
                    break;

                default:
                    Console.WriteLine("Ta brincando");
                    break;

            }
        }
    }
}