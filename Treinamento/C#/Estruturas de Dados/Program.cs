/*
Codigo feito por Marcos Andrade
Codigo para fixação de conteúdo

Enunciado:

Você trabalha em uma loja de eletrônicos e precisa gerenciar produtos. Crie um programa em C# que:

Use um array para armazenar 3 categorias fixas de produtos: "Periféricos", "Hardware", "Acessórios".
Use uma List<string> para registrar nomes de produtos adicionados pelo usuário (peça 3 nomes via Console.ReadLine()).
Use um Dictionary<int, string> para associar códigos numéricos (ex.: 100, 200, 300) aos produtos da lista, onde o código é gerado como índice * 100 + 100.
Exiba:
As categorias do array.
A lista de produtos adicionados.
Cada produto com seu código do dicionário.


*/


using System;
using System.Collections.Generic;

namespace EstruturaDados
{
    public class EstruturaDados
    {
        static void Main(string[] args)
        {
            //declarar variáveis
            string[] categorias = { "Periféricos", "Hardware", "Acessórios", };
            int quantidade = 3;
            List<string> produtos = new List<string>();
            Dictionary<int, string> produtosCodigo = new Dictionary<int, string>();

            //Mostrar categorias
            Console.WriteLine("=====================================================");
            Console.WriteLine("Categorias de produtos: ");
            Console.WriteLine("");
            foreach (string categoria in categorias)
            {
                Console.WriteLine(categoria);
            }
            Console.WriteLine("");
            Console.WriteLine("=====================================================");

            //Pedir 3 nomes e adicionar a uma lista
            for (int ii = 0; ii < quantidade; ii++)
            {
                Console.WriteLine($"Digite o {ii + 1}° produto: ");
                string produto = Console.ReadLine();
                produtos.Add(produto);

                //Adicionar ao dicionário com indíces
                produtosCodigo.Add((ii + 1) * 100, produto);
            }

            Console.WriteLine("=====================================================");
            Console.WriteLine("Produtos adicionados: ");

            //foreach para cada um

            foreach (string produtoForeach in produtos)
            {
                Console.WriteLine(produtoForeach);
            }

            Console.WriteLine("=====================================================");
            Console.WriteLine("Produtos com código: ");

            foreach (KeyValuePair<int, string> par in produtosCodigo)
            {
                Console.WriteLine($"Código {par.Key}: {par.Value}");
            }




        }
    }
}
