using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula01_PRES
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Declarando as variáveis
            int numeroUm = 0, numeroDois = 0, soma;
            bool resultadoUm = false;
            bool resultadoDois = false;
        
            //Lendo os valores
            while (!resultadoUm)
            {
                Console.WriteLine("Digite o primeiro número a ser somado: ");
                resultadoUm = int.TryParse(Console.ReadLine(), out numeroUm);
                if (!resultadoUm)
                {
                    Console.WriteLine("Digite um número inteiro, seu animal!");
                    
                }

            }

            while (!resultadoDois)
            {
                Console.WriteLine("Digite o segundo número a ser somado: ");
                resultadoDois = int.TryParse(Console.ReadLine(), out numeroDois);
                if (!resultadoDois)
                {
                    Console.WriteLine("Digite um número inteiro, seu animal!");
                }
            }

            //somando os valores
            soma = numeroUm + numeroDois;

            //exibindo o resultado
            Console.WriteLine($"A soma dos valores é: {soma}"); 

            Console.ReadKey();
        }
    }
}
