#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

struct Funcionario {
    int prontuario;
    string nome;
    double salario;
};

void incluir(vector<Funcionario>& lista) {
    Funcionario novo;
    cout << "\nProntuario: ";
    cin >> novo.prontuario;

    for (const auto& f : lista) {
        if (f.prontuario == novo.prontuario) {
            cout << "Erro: Prontuario ja cadastrado!" << endl;
            return;
        }
    }

    cout << "Nome: ";
    cin.ignore();
    getline(cin, novo.nome);
    cout << "Salario: ";
    cin >> novo.salario;

    lista.push_back(novo);
}

void excluir(vector<Funcionario>& lista) {
    int p;
    cout << "\nProntuario para excluir: ";
    cin >> p;

    for (auto it = lista.begin(); it != lista.end(); ++it) {
        if (it->prontuario == p) {
            lista.erase(it);
            cout << "Removido." << endl;
            return;
        }
    }
    cout << "Nao encontrado." << endl;
}

void pesquisar(const vector<Funcionario>& lista) {
    int p;
    cout << "\nProntuario para pesquisa: ";
    cin >> p;

    for (const auto& f : lista) {
        if (f.prontuario == p) {
            cout << "\nNome: " << f.nome << endl;
            cout << "Salario: " << f.salario << endl;
            return;
        }
    }
    cout << "Nao encontrado." << endl;
}

void listar(const vector<Funcionario>& lista) {
    double total = 0;
    cout << fixed << setprecision(2);
    cout << "\n--- LISTA ---" << endl;
    for (const auto& f : lista) {
        cout << f.prontuario << " - " << f.nome << " - R$ " << f.salario << endl;
        total += f.salario;
    }
    cout << "Total Salarios: R$ " << total << endl;
}

int main() {
    vector<Funcionario> lista;
    int opcao;

    do {
        cout << "\n0.Sair\n1.Incluir\n2.Excluir\n3.Pesquisar\n4.Listar\nOpcao: ";
        cin >> opcao;

        if (opcao == 1) incluir(lista);
        else if (opcao == 2) excluir(lista);
        else if (opcao == 3) pesquisar(lista);
        else if (opcao == 4) listar(lista);

    } while (opcao != 0);

    return 0;
}