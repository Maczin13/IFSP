using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula01_MediaAritimetica
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //declarando variáveis
            string nomeAluno, status;
            double notaUm = 0, notaDois = 0, notaTres = 0, notaQuatro = 0, media = 0;
            int quantidadeNotas = 4;
            bool resultadoUm = false, resultadoDois = false, resultadoTres = false, resultadoQuatro = false;

            //Lendo variável nome
            Console.WriteLine("Digite o nome do aluno: ");
            nomeAluno = Console.ReadLine();

            //Tentando converter entrada de usuário para nota um
            while(!resultadoUm)
            {
                Console.WriteLine("Digite a primeira nota: ");
                resultadoUm = double.TryParse(Console.ReadLine(), out notaUm);

                if(notaUm > 10 || notaUm < 0) 
                {
                    Console.WriteLine("O número precisa estar entre 0 e 10");
                    resultadoUm = false;
                }
                
                else if(!resultadoUm)
                {
                    Console.WriteLine("Você precisa digitar um número válido!");
                }
            }

            //Tentando converter entrada de usuário para nota dois
            while (!resultadoDois)
            {
                Console.WriteLine("Digite a segunda nota: ");
                resultadoDois = double.TryParse(Console.ReadLine(), out notaDois);

                if (notaDois > 10 || notaDois < 0)
                {
                    Console.WriteLine("O número precisa estar entre 0 e 10");
                    resultadoDois = false;
                }

                else if (!resultadoDois)
                {
                    Console.WriteLine("Você precisa digitar um número válido!");
                }
            }

            //Tentando converter entrada de usuário para nota três
            while (!resultadoTres)
            {
                Console.WriteLine("Digite a terceira nota: ");
                resultadoTres = double.TryParse(Console.ReadLine(), out notaTres);

                if (notaTres > 10 || notaTres < 0)
                {
                    Console.WriteLine("O número precisa estar entre 0 e 10");
                    resultadoTres = false;
                }

                else if (!resultadoTres)
                {
                    Console.WriteLine("Você precisa digitar um número válido!");
                }
            }

            //Tentando converter entrada de usuário para nota quatro
            while (!resultadoQuatro)
            {
                Console.WriteLine("Digite a quarta nota: ");
                resultadoQuatro = double.TryParse(Console.ReadLine(), out notaQuatro);

                if (notaQuatro > 10 || notaQuatro < 0)
                {
                    Console.WriteLine("O número precisa estar entre 0 e 10");
                    resultadoQuatro = false;
                }

                else if (!resultadoQuatro)
                {
                    Console.WriteLine("Você precisa digitar um número válido!");
                }
            }

            //Calculando media
            media = (notaUm + notaDois + notaTres + notaQuatro)/quantidadeNotas;

            //Verificando Status
            if(media >=6)
            {
                status = "Aprovado";
            }
            else
            {
                status = "Reprovado";
            }


            //Exibindo media
            Console.WriteLine("---------------------------");
            Console.WriteLine($"Aluno: {nomeAluno}");
            Console.WriteLine($"Media: {media.ToString("n1")}");
            Console.WriteLine($"Status: {status}");
            Console.WriteLine("---------------------------");

            Console.ReadKey();


        }
    }
}
