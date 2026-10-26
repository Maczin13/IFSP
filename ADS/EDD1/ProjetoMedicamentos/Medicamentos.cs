using System.Collections.Generic;

namespace ProjetoMedicamentos
{
    public class Medicamentos
    {
        private List<Medicamento> listaMedicamentos;

        public List<Medicamento> ListaMedicamentos { get => listaMedicamentos; }

        public Medicamentos()
        {
            listaMedicamentos = new List<Medicamento>();
        }

        public void adicionar(Medicamento medicamento)
        {
            listaMedicamentos.Add(medicamento);
        }

        public bool deletar(Medicamento medicamento)
        {
            Medicamento medEncontrado = pesquisar(medicamento);
            
            if (medEncontrado.Id != 0 && medEncontrado.qtdeDisponivel() == 0)
            {
                listaMedicamentos.Remove(medEncontrado);
                return true;
            }
            return false;
        }

        public Medicamento pesquisar(Medicamento medicamento)
        {
            foreach (var med in listaMedicamentos)
            {
                if (med.Equals(medicamento))
                {
                    return med;
                }
            }
            return new Medicamento();
        }
    }
}
