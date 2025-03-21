using System;

namespace TreinoUm
{
    public class TreinoUm
    {
        static void Main(string[] args)
        {
            // Declaração de variáveis
            double primeiroTermo = 0, razao = 0;
            int numeroTermos = 0;
            bool converteuUm = false, converteuDois = false, converteuTres = false;
            double[] termos;

            // Leitura dos valores pedidos
            Console.WriteLine("=======================================================");
            do
            {
                Console.WriteLine("Digite o primeiro termo da progressão aritmética: ");
                if (double.TryParse(Console.ReadLine(), out primeiroTermo))
                {
                    converteuUm = true;
                }
                else
                {
                    Console.WriteLine("Digite um valor numérico!");
                    converteuUm = false;
                }
            } while (!converteuUm);

            do
            {
                Console.WriteLine("Digite o número de termos da progressão aritmética: ");
                if (int.TryParse(Console.ReadLine(), out numeroTermos))
                {
                    if (numeroTermos <= 0) // Ajustei para <= para maior clareza
                    {
                        Console.WriteLine("A quantidade de termos deve ser maior que zero");
                        converteuDois = false;
                    }
                    else
                    {
                        converteuDois = true;
                    }
                }
                else
                {
                    Console.WriteLine("Digite um valor numérico e inteiro!");
                    converteuDois = false;
                }
            } while (!converteuDois);

            termos = new double[numeroTermos];

            do
            {
                Console.WriteLine("Digite a razão da progressão aritmética: ");
                if (double.TryParse(Console.ReadLine(), out razao))
                {
                    converteuTres = true;
                }
                else
                {
                    Console.WriteLine("Digite um valor numérico!");
                    converteuTres = false;
                }
            } while (!converteuTres);

            Console.WriteLine("=======================================================");

            // Cálculo da PA
            for (int ii = 0; ii < numeroTermos; ii++) // Corrigido o limite
            {
                termos[ii] = primeiroTermo + ii * razao;
                Console.WriteLine(termos[ii]);
            }

            // Exibir PA com foreach (adicionado)
            Console.WriteLine("Exibindo com foreach:");
            foreach (double termo in termos)
            {
                Console.WriteLine(termo);
            }
        }
    }
}