//codigo criado por Marcos Andrade para fixação do tema. Exercício: 
/*Você trabalha em uma empresa que gerencia estoque. Crie um programa em C# que:

Declare variáveis para:
Quantidade de itens em estoque (int).
Preço unitário de um item (double).
Nome do produto (string).
Se o produto está disponível (bool).
Atribua valores iniciais às variáveis.
Converta o preço unitário para inteiro (ignorando a parte decimal).
Exiba no console:
Uma mensagem com o nome do produto e a quantidade.
O preço convertido como inteiro.
Dica: Use Console.WriteLine() para exibir as saídas. */

using System;

namespace VariaveisETiposDeDados
{
    public class VariaveisETiposDeDados
    {
        static void Main(string[] args)
        {
            //declarando as variáveis
            int banana_quantidadeItensEstoque = 10;
            double banana_precoUnitarioItem = 1.99;
            string banana_nomeProduto = "Banana";
            bool banana_produtoDisponivel = true;

            //convertendo o preço para o tipo inteiro
            int banana_precoInteiro = (int)banana_precoUnitarioItem;

            //se o produto estiver disponível, exibir informações
            if (banana_produtoDisponivel)
            {
                Console.WriteLine("==========================================");
                Console.WriteLine($"Produto: {banana_nomeProduto}");
                Console.WriteLine($"Quantidade: {banana_quantidadeItensEstoque}");
                Console.WriteLine($"Preço: {banana_precoInteiro}");
                Console.WriteLine("==========================================");
            }

            //caso não esteja disponível, exibir que não há mais bananas.
            else
            {
                Console.WriteLine("Não há bananas no estoque.");
            }

        }
    }
}
