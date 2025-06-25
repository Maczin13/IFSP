using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula_11
{
    internal class Program
    {
        static void Main(string[] args)
        {

        }

        static double Cubo(double x)
            { return x * x; }
        static bool EPar(double x)
        {
            if (x % 2 == 0) { return true; }
            else { return false; }
        }

        static string ClassificarNum(double x)
        {
            if(x % 2 == 0) { return "Par"; }
            else { return "Impar"; }
        }
        static string EhPrimo(int numero)
        {
            if (numero <= 1) return "nao";
            if (numero <= 3) return "sim";
            if (numero % 2 == 0 || numero % 3 == 0) return "nao";

            for (int i = 5; i * i <= numero; i = i + 6)
            {
                if (numero % i == 0 || numero % (i + 2) == 0)
                {
                    return "Nao";
                }
            }
            return "sim";
        }

    }
}
