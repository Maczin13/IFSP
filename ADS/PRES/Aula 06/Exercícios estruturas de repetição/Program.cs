using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Exercícios_estruturas_de_repetição
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //ExUm();
            ExDois();
            //ExTres();
            //ExQuatro();
            //ExCinco();
            //ExSeis();
            //ExSete();
            //ExOito();

        }

        static void ExUm()
        {
            double notaUm = 0, notaDois = 0, somaNotas = 0;
            bool converteu;

            for (int ii = 0; ii < 5; ii++)
            {
                Console.Clear();

                do
                {
                    Console.WriteLine($"Digite a nota da P1 do aluno {ii + 1}: ");
                    converteu = double.TryParse(Console.ReadLine(), out notaUm);
                    if (!converteu)
                    {
                        Console.WriteLine("A nota deve ser um valor numérico!");
                    }
                    else if (notaUm < 0 || notaUm > 10)
                    {
                        Console.WriteLine("A nota deve ser de 0 a 10!");
                        converteu = false;
                    }
                } while (!converteu);



                do
                {
                    Console.WriteLine($"Digite a nota da P2 do aluno {ii + 1}: ");
                    converteu = double.TryParse(Console.ReadLine(), out notaDois);
                    if (!converteu)
                    {
                        Console.WriteLine("A nota deve ser um valor numérico!");
                    }
                    else if (notaDois < 0 || notaDois > 10)
                    {
                        Console.WriteLine("A nota deve ser de 0 a 10!");
                        converteu = false;
                    }
                } while (!converteu);

                Console.WriteLine($"A média do aluno {ii + 1} é {(notaUm + notaDois) / 2}");

                somaNotas += notaUm + notaDois;

            }

            Console.WriteLine($"A média geral é: {somaNotas / 10}");

        }

        static void ExDois()
        {
            double notaUm = 0, notaDois = 0, somaNotas = 0;
            int quantidadeAlunos = 1;
            bool converteu;
            string verificador = "";

            for (int ii = 0; ii < quantidadeAlunos; ii++)
            {
                Console.Clear();
                do
                {
                    Console.WriteLine($"Digite a nota da P1 do aluno {ii + 1}: ");
                    converteu = double.TryParse(Console.ReadLine(), out notaUm);
                    if (!converteu)
                    {
                        Console.WriteLine("A nota deve ser um valor numérico!");
                    }
                    else if (notaUm < 0 || notaUm > 10)
                    {
                        Console.WriteLine("A nota deve ser de 0 a 10!");
                        converteu = false;
                    }
                } while (!converteu);



                do
                {
                    Console.WriteLine($"Digite a nota da P2 do aluno {ii + 1}: ");
                    converteu = double.TryParse(Console.ReadLine(), out notaDois);
                    if (!converteu)
                    {
                        Console.WriteLine("A nota deve ser um valor numérico!");
                    }
                    else if (notaDois < 0 || notaDois > 10)
                    {
                        Console.WriteLine("A nota deve ser de 0 a 10!");
                        converteu = false;
                    }
                } while (!converteu);

                Console.WriteLine($"A média do aluno {ii + 1} é {(notaUm + notaDois) / 2}");

                somaNotas += notaUm + notaDois;

                Console.WriteLine("Digite '1' se deseja ler as notas de outro aluno. Digite qualquer outro dígito para exibir a média final");
                verificador = Console.ReadLine();

                if (verificador == "1")
                {
                    quantidadeAlunos++;
                }
            }

            Console.WriteLine($"A média geral é: {somaNotas / (quantidadeAlunos * 2)}");

        }

        static void ExTres()
        {
            int idade = 0, quantidadeMaiores = 0;
            bool converteu;

            for (int ii = 0; ii < 10; ii++)
            {
                Console.Clear();
                do
                {
                    Console.WriteLine($"Digite a idade da pessoa {ii + 1}");
                    converteu = int.TryParse(Console.ReadLine(), out idade);

                    if (!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico!");
                    }
                    else if (idade < 0)
                    {
                        Console.WriteLine("A idade deve ser maior que zero!");
                    }
                } while (!converteu);

                if (idade >= 18)
                {
                    quantidadeMaiores++;
                }
            }

            Console.WriteLine($"Existem {quantidadeMaiores} maiores de idade");
        }

        static void ExQuatro()
        {
            for (int ii = 0; ii <= 100; ii++)
            {
                if ((ii % 2) == 0)
                {
                    Console.WriteLine(ii);
                }
            }
        }

        static void ExCinco()
        {
            int qtd1a15 = 0, qtd16a30 = 0, qtd31a45 = 0, qtd46a60 = 0, qtdAcima60 = 0, qtdTotal = 15;
            int idade = 0;
            bool converteu;

            for (int ii = 0; ii < qtdTotal; ii++)
            {
                do
                {
                    Console.WriteLine($"Digite a idade da pessoa {ii + 1}");
                    converteu = int.TryParse(Console.ReadLine(), out idade);
                    if (!converteu)
                    {
                        Console.WriteLine("Digite um valor numérico para idade");
                    }
                    else if (idade <= 0)
                    {
                        Console.WriteLine("Digite um valor positivo e diferente de 0 para idade");
                        converteu = false;
                    }
                } while (!converteu);

                if (idade <= 15)
                {
                    qtd1a15++;
                }
                else if (idade <= 30)
                {
                    qtd16a30++;
                }
                else if (idade <= 45)
                {
                    qtd31a45++;
                }
                else if (idade <= 60)
                {
                    qtd46a60++;
                }
                else
                {
                    qtdAcima60++;
                }

            }

            Console.Clear();

            Console.WriteLine("Quantidades: ");
            Console.WriteLine($"Idade de 1 a 15: {qtd1a15} {(qtd1a15 * 100) / qtdTotal}%");
            Console.WriteLine($"Idade de 1 a 15: {qtd16a30} {(qtd16a30 * 100) / qtdTotal}%");
            Console.WriteLine($"Idade de 1 a 15: {qtd31a45} {(qtd31a45 * 100) / qtdTotal}%");
            Console.WriteLine($"Idade de 1 a 15: {qtd46a60} {(qtd46a60 * 100) / qtdTotal}%");
            Console.WriteLine($"Idade de 1 a 15: {qtdAcima60} {(qtdAcima60 * 100) / qtdTotal}%");


        }

        static void ExSeis()
        {
            string sexo = "";
            double peso = 0, altura = 0;
            int qtdHomens = 0, qtdMulheres = 0, qtdTotal = 20;
            double pesoTotalM = 0, pesoTotalF = 0;
            double alturaTotalM = 0, alturaTotalF = 0;
            bool converteu;

            for (int ii = 0; ii < qtdTotal; ii++)
            {
                do
                {
                    Console.Clear();
                    Console.WriteLine($"Digite o sexo da pessoa {ii + 1} ('M' para masculino ou 'F' para feminino: ");
                    sexo = Console.ReadLine();

                    if (sexo.ToUpper() == "M")
                    {
                        qtdHomens++;

                        do
                        {
                            Console.Clear();
                            Console.WriteLine($"Digite a altura da pessoa {ii + 1}: ");
                            converteu = double.TryParse(Console.ReadLine(), out altura);

                            if (!converteu)
                            {
                                Console.WriteLine("Digite um valor numérico!");
                            }
                            else if (altura < 0)
                            {
                                Console.WriteLine("Digite um valor positivo!");
                                converteu = false;
                            }
                        } while (!converteu);

                        alturaTotalM += altura;

                        do
                        {
                            Console.Clear();
                            Console.WriteLine($"Digite o peso da pessoa {ii + 1}: ");
                            converteu = double.TryParse(Console.ReadLine(), out peso);

                            if (!converteu)
                            {
                                Console.WriteLine("Digite um valor numérico!");
                            }
                            else if (altura < 0)
                            {
                                Console.WriteLine("Digite um valor positivo!");
                                converteu = false;
                            }
                        } while (!converteu);

                        pesoTotalM += peso;

                        converteu = true;
                    }
                    else if (sexo.ToUpper() == "F")
                    {
                        qtdMulheres++;

                        do
                        {
                            Console.Clear();
                            Console.WriteLine($"Digite a altura da pessoa {ii + 1}: ");
                            converteu = double.TryParse(Console.ReadLine(), out altura);

                            if (!converteu)
                            {
                                Console.WriteLine("Digite um valor numérico!");
                            }
                            else if (altura < 0)
                            {
                                Console.WriteLine("Digite um valor positivo!");
                                converteu = false;
                            }
                        } while (!converteu);

                        alturaTotalF += altura;

                        do
                        {
                            Console.Clear();
                            Console.WriteLine($"Digite o peso da pessoa {ii + 1}: ");
                            converteu = double.TryParse(Console.ReadLine(), out peso);

                            if (!converteu)
                            {
                                Console.WriteLine("Digite um valor numérico!");
                            }
                            else if (altura < 0)
                            {
                                Console.WriteLine("Digite um valor positivo!");
                                converteu = false;
                            }
                        } while (!converteu);

                        pesoTotalF += peso;
                        converteu = true;
                    }
                    else
                    {
                        Console.WriteLine("Digite exatamente o que se pede!");
                        converteu = false;
                    }

                } while (!converteu);

                Console.WriteLine($"Quantidade de homens: {qtdHomens} ({(qtdHomens * 100) / qtdTotal})");
                Console.WriteLine($"Quantidade de mulheres: {qtdMulheres} ({(qtdMulheres * 100) / qtdTotal})");

                Console.WriteLine($"A média do peso dos homens é: {pesoTotalM / qtdTotal}");
                Console.WriteLine($"A média de altura dos homens é: {alturaTotalM / qtdTotal}");

                Console.WriteLine($"A média do peso das mulheres é: {pesoTotalF / qtdTotal}");
                Console.WriteLine($"A média de altura das mulheres é: {alturaTotalF / qtdTotal}");





            }


        }

        static void ExSete()
        {
            int totalVotos1 = 0, totalVotos2 = 0, totalVotos3 = 0, totalVotos4 = 0, totalVotosNulos = 0, totalVotosBrancos = 0;
            bool continuar = true;
            int totalVotos = 0;
            string voto = "";

            do
            {

                Console.Clear();
                Console.WriteLine("Digite o seu voto (candidatos: 1, 2, 3, 4. 5: nulo. 6: branco. Digite '0' para sair. ");

                voto = Console.ReadLine();

                switch (voto) 
                {
                    case "1":
                        totalVotos1++;
                        break;
                    case "2":
                        totalVotos2++;
                        break;
                    case "3":
                        totalVotos3++;
                        break;
                    case "4":
                        totalVotos4++;
                        break;
                    case "5":
                        totalVotosNulos++;
                        break;
                    case "6":
                        totalVotosBrancos++;
                        break;
                    case "0":
                        continuar = false;
                        break;
                }

            } while (continuar);

            Console.WriteLine($"O total de votos para o candidato 1 é: {totalVotos1}");
            Console.WriteLine($"O total de votos para o candidato 2 é: {totalVotos2}");
            Console.WriteLine($"O total de votos para o candidato 3 é: {totalVotos3}");
            Console.WriteLine($"O total de votos para o candidato 4 é: {totalVotos4}");
            Console.WriteLine($"O total de votos nulos é: {totalVotosNulos} ({(totalVotosNulos * 100) / totalVotos})");
            Console.WriteLine($"O total de votos brancos é: {totalVotosBrancos} ({(totalVotosBrancos * 100) / totalVotos})");

        }

        static void ExOito()
        {
            int anterior1 = 0, anterior2 =1, temp;

            Console.WriteLine(anterior1);
            Console.WriteLine(anterior2);

            for(int ii = 0; ii < 30;ii++)
            {

                temp = anterior1 + anterior2;
                Console.WriteLine(temp);

                anterior1 = anterior2;
                anterior2 = temp;
            }

        }
    }
}
