using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace COLETTO
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===============================================================");
            Console.WriteLine("Ex 1");
            CalcularAreaRetangulo();
            Console.WriteLine("===============================================================");
            Console.WriteLine("Ex 2");
            AreaCircuferenciaCirculo();
            Console.WriteLine("===============================================================");
            Console.WriteLine("Ex 3");
            RaquelCaixaDeSupermercado();
            Console.WriteLine("===============================================================");
            Console.WriteLine("Ex 4");
            DoisNumerosVerMaior();
            Console.WriteLine("===============================================================");
            Console.WriteLine("Exs 5 e 6 (desafio)");
            VerificarTriangulo();
            Console.WriteLine("===============================================================");
        }

        static void CalcularAreaRetangulo()
        {
            double baseRetangulo = 0, alturaRetangulo = 0;
            bool converteu = false;

            while (!converteu)
            {
                Console.Write("Digite a Base do retangulo: ");
                converteu = double.TryParse(Console.ReadLine(), out baseRetangulo);
                Console.WriteLine("");

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (baseRetangulo <= 0)
                {
                    Console.WriteLine("Digite um valor que seja maior do que zero");
                }
            }

            converteu = false;

            while (!converteu)
            {
                Console.Write("Digite a altura do retangulo: ");
                converteu = double.TryParse(Console.ReadLine(), out alturaRetangulo);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (alturaRetangulo <= 0)
                {
                    Console.WriteLine("Digite um valor que seja maior do que zero");
                }
                Console.WriteLine("");
            }

            Console.WriteLine($"A área do Retangulo é {baseRetangulo * alturaRetangulo}");
            Console.ReadKey();

        }

        static void AreaCircuferenciaCirculo()
        {
            double diametro = 0;
            double PI = Math.PI;
            bool converteu = false;

            while (!converteu)
            {
                Console.Write("Digite o valor do diâmetro do círculo: ");
                converteu = double.TryParse(Console.ReadLine(), out diametro);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (diametro <= 0)
                {
                    Console.WriteLine("Digite um valor que seja maior do que zero");
                }
                Console.WriteLine("");
            }

            Console.WriteLine($"A área do círculo é {(2 * PI * Math.Sqrt(diametro / 2)):F2}");
            Console.WriteLine($"A circuferência é {(diametro * PI):F2}");
            Console.ReadKey();
        }

        static void RaquelCaixaDeSupermercado()
        {

            double valorTotal = 0;
            double valorPago = 0;
            bool converteu = false;

            for (int ii = 0; ii < 5; ii++)
            {
                double valor = 0;
                int quantidade = 0;

                while (!converteu)
                {

                    Console.Write($"Digite o valor do produto {ii + 1}: ");

                    converteu = double.TryParse(Console.ReadLine(), out valor);

                    if (!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico!");
                    }

                    else if (valor < 0)
                    {
                        Console.WriteLine("Digite um valor que seja maior ou igual a zero");
                    }

                }

                converteu = false;

                while (!converteu)
                {


                    Console.Write($"Digite a quantidade do produto {ii + 1}: ");

                    converteu = int.TryParse(Console.ReadLine(), out quantidade);

                    if (!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico!");
                    }

                    else if (quantidade < 0)
                    {
                        Console.WriteLine("Digite um valor que seja maior ou igual a zero");
                    }


                }




                valorTotal = valorTotal + valor * quantidade;
                converteu = false;

            }

            while (!converteu)
            {
                Console.WriteLine("Digite o valor pago: ");

                converteu = double.TryParse(Console.ReadLine(), out valorPago);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }

                else if (valorPago < 0)
                {
                    Console.WriteLine("Digite um valor que seja maior ou igual a zero");
                }

            }

            if (valorPago >= valorTotal)
            {
                Console.WriteLine($"Troco: R${(valorPago - valorTotal):F2}");
            }
            else
            {
                Console.WriteLine("Já coloca no Serasa");
            }

            Console.ReadKey();


        }

        static void DoisNumerosVerMaior()
        {
            bool converteu = false;
            double numeroUm = 0, numeroDois = 0;

            while (!converteu)
            {
                Console.WriteLine("Digite um valor: ");

                converteu = double.TryParse(Console.ReadLine(), out numeroUm);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
            }

            converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite um valor diferente do primeiro: ");

                converteu = double.TryParse(Console.ReadLine(), out numeroDois);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (numeroDois == numeroUm)
                {
                    Console.WriteLine("Você sabe o que é DIFERENTE, animal?");
                    converteu = false;
                }
            }

            if (numeroUm > numeroDois)
            {
                Console.WriteLine($"O maior é: {numeroUm}");
            }
            else
            {
                Console.WriteLine($"O maior é: {numeroDois}");
            }
            Console.ReadKey();
        }

        static void VerificarTriangulo()
        {
            double ladoUm = 0, ladoDois = 0, ladoTres = 0;
            bool converteu = false;
            bool triangulo = false;

            while (!converteu)
            {
                Console.WriteLine("Digite o valor do primeiro lado: ");

                converteu = double.TryParse(Console.ReadLine(), out ladoUm);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (ladoUm <= 0)
                {
                    Console.WriteLine("Digite um valor maior do que zero");
                }
            }
            converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite o valor do segundo lado: ");

                converteu = double.TryParse(Console.ReadLine(), out ladoDois);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (ladoDois <= 0)
                {
                    Console.WriteLine("Digite um valor maior do que zero");
                }
            }
            converteu = false;

            while (!converteu)
            {
                Console.WriteLine("Digite o valor do terceiro lado: ");

                converteu = double.TryParse(Console.ReadLine(), out ladoTres);

                if (!converteu)
                {
                    Console.WriteLine("Digite um valor numérico!");
                }
                else if (ladoTres <= 0)
                {
                    Console.WriteLine("Digite um valor maior do que zero");
                }
            }

            if ((ladoUm + ladoDois > ladoTres) &&
               (ladoDois + ladoTres > ladoUm) &&
               (ladoTres + ladoUm > ladoDois))
            {
                Console.WriteLine("É um triângulo!");
                triangulo = true;
            }
            else
            {
                Console.WriteLine("Não é um triângulo");
                triangulo = false;

            }

            Console.ReadKey();

            if(triangulo)
            {
                if (ladoUm == ladoDois && ladoDois != ladoTres)
                {
                    Console.WriteLine("O triangulo é isósceles");
                }
                else if (ladoDois == ladoTres && ladoTres != ladoUm)
                {
                    Console.WriteLine("O triangulo é isósceles");
                }
                else if (ladoUm == ladoDois && ladoDois == ladoTres)
                {
                    Console.WriteLine("O triangulo é equilatero");
                }
                else
                {
                    Console.WriteLine("Triangulo escaleno");
                }
                Console.ReadKey();
            }
            
        }

        


    }
}
