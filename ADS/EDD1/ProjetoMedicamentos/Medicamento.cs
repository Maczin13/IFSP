using System;
using System.Collections.Generic;

namespace ProjetoMedicamentos
{
    public class Medicamento
    {
        private int id;
        private string nome;
        private string laboratorio;
        private Queue<Lote> lotes;

        public int Id { get => id; set => id = value; }
        public string Nome { get => nome; set => nome = value; }
        public string Laboratorio { get => laboratorio; set => laboratorio = value; }
        public Queue<Lote> Lotes { get => lotes; }

        public Medicamento()
        {
            this.lotes = new Queue<Lote>();
        }

        public Medicamento(int id, string nome, string laboratorio)
        {
            this.id = id;
            this.nome = nome;
            this.laboratorio = laboratorio;
            this.lotes = new Queue<Lote>();
        }

        public int qtdeDisponivel()
        {
            int total = 0;
            foreach (var lote in lotes)
            {
                total += lote.Qtde;
            }
            return total;
        }

        public void comprar(Lote lote)
        {
            lotes.Enqueue(lote);
        }

        public bool vender(int qtdeDesejada)
        {
            if (qtdeDesejada <= 0 || qtdeDesejada > qtdeDisponivel())
            {
                return false;
            }

            while (qtdeDesejada > 0 && lotes.Count > 0)
            {
                Lote loteMaisAntigo = lotes.Peek();

                if (loteMaisAntigo.Qtde > qtdeDesejada)
                {
                    loteMaisAntigo.Qtde -= qtdeDesejada;
                    qtdeDesejada = 0;
                }
                else
                {
                    qtdeDesejada -= loteMaisAntigo.Qtde;
                    lotes.Dequeue();
                }
            }

            return true;
        }

        public override string ToString()
        {
            return $"{id}-{nome}-{laboratorio}-{qtdeDisponivel()}";
        }

        public override bool Equals(object obj)
        {
            if (obj is Medicamento outroMed)
            {
                return this.id == outroMed.Id;
            }
            return false;
        }

        public override int GetHashCode()
        {
            return id.GetHashCode();
        }
    }
}
