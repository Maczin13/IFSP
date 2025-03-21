// Exercício feito para fixação por Marcos Andrade
/* 
Enunciado:

Você é um técnico gerenciando um sistema de vendas. Crie um programa em C# que:

Pergunte ao usuário o código do produto (1 a 4) e use switch-case para definir o nome do produto:
1: "Mouse"
2: "Teclado"
3: "Monitor"
Use do-while para pedir a quantidade em estoque até que o usuário digite um valor >= 0.
Use if-else para verificar:
Se estoque < 5, exiba "Estoque crítico".
Se estoque >= 5 e < 10, exiba "Estoque moderado".
Se estoque >= 10, exiba "Estoque ok".
Use for para simular 3 dias de vendas, subtraindo 2 itens por dia e exibindo o estoque restante. Pare se o estoque zerar (use break).
Use foreach para listar uma array de promoções: ["10% off", "Frete grátis", "Compre 2, leve 3"].

*/

using System;

namespace EstruturasControleFluxo
{
    public class EstruturasControleFluxo
    {
        static void Main(string[] args)
        {
            //declaração de variáveis
            int codigoProduto = 0, quantidadeProduto = 0, quantidadeVendaDia = 2;
            string nomeProduto = "";
            bool deuCerto = false;
            string[] promocoes = { "10% off", "Frete Grátis", "Compre 2 leve 3"};


            //Pedir para usuário escolher o codigo do produto utilizando switch case
            Console.WriteLine("=====================================================");
            Console.WriteLine("Digite o código do produto a ser consultado estoque:");
            Console.WriteLine("1: Monitor");
            Console.WriteLine("2: Mouse");
            Console.WriteLine("3: Teclado");
            Console.WriteLine("=====================================================");

            while (!deuCerto)
            {
                deuCerto = int.TryParse(Console.ReadLine(), out codigoProduto);

                if (codigoProduto < 0)
                {
                    Console.WriteLine("Digite um valor maior que zero para o código!");
                    deuCerto = false;
                }
                else if (codigoProduto > 3)
                {
                    Console.WriteLine("Digite um código existente na lista!");
                    deuCerto = false;
                }
                else if (!deuCerto)
                {
                    Console.WriteLine("Digite um valor numérico para o código!");
                }

            }

            switch (codigoProduto)
            {
                case 1:
                    nomeProduto = "monitor";
                    break;

                case 2:
                    nomeProduto = "mouse";
                    break;
                case 3:
                    nomeProduto = "teclado";
                    break;
            }

            //do while para pedir para o usuario a quantidade até digitar valor maior ou igual a zero
            deuCerto = false;

            do
            {
                Console.WriteLine("=====================================================");
                Console.WriteLine($"Digite a quantidade que há no estoque do produto {nomeProduto}");
                deuCerto = int.TryParse(Console.ReadLine(), out quantidadeProduto);

                if (quantidadeProduto < 0)
                {
                    Console.WriteLine("Digite um valor maior ou igual a zero");
                    deuCerto = false;
                }

                else if (!deuCerto)
                {
                    Console.WriteLine("Digite um valor numérico para inserir a quantidade.");
                }

            } while (!deuCerto);

            Console.WriteLine("=====================================================");

            // verificar estoque critico < 5, entre 5 e 10 moderado, acima de 10 ok
            if (quantidadeProduto < 5)
            {
                Console.WriteLine($"O status do estoque do produto {nomeProduto} é *crítico*");
            }
            else if (quantidadeProduto >= 10)
            {
                Console.WriteLine($"O status do estoque do produto {nomeProduto} é *OK*");
            }
            else
            {
                Console.WriteLine($"O status do estoque do produto {nomeProduto} é *moderado*");
            }

            Console.WriteLine("=====================================================");
            Console.WriteLine($"Simulação de venda em três dias ({quantidadeVendaDia} produtos vendidos ao dia)");

            //for para simular três dias de vendas. Cada dia 2 vendas do produto
            for (int ii = 0; ii < 3; ii++)
            {
                quantidadeProduto = quantidadeProduto - quantidadeVendaDia;

                if (quantidadeProduto <= 0)
                {
                    Console.WriteLine($"Dia {ii + 1}: O estoque acabou.");
                    break;
                }
                else
                {
                    Console.WriteLine($"Dia {ii + 1}: {quantidadeProduto}");
                }

            }

            Console.WriteLine("=====================================================");


            // foreach para exibir as promoções
            foreach (string promocao in promocoes)
            {
                Console.WriteLine(promocao);

            }

        }
    }
}
