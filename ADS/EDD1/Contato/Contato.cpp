#include <iostream>
#include <string>
#include <vector>
#include <ctime>

using namespace std;

class Data {
private:
    int dia;
    int mes;
    int ano;

public:
    Data() : dia(1), mes(1), ano(1900) {}
    Data(int d, int m, int a) : dia(d), mes(m), ano(a) {}

    void setDia(int d) { dia = d; }
    int getDia() { return dia; }
    
    void setMes(int m) { mes = m; }
    int getMes() { return mes; }
    
    void setAno(int a) { ano = a; }
    int getAno() { return ano; }
};

class Contato {
private:
    string email;
    string nome;
    string telefone;
    Data dtnasc;

public:
    Contato() : email(""), nome(""), telefone("") {}
    Contato(string n, string e, string t, Data d) : nome(n), email(e), telefone(t), dtnasc(d) {}

    void setNome(string n) { nome = n; }
    string getNome() { return nome; }

    void setEmail(string e) { email = e; }
    string getEmail() { return email; }

    void setTelefone(string t) { telefone = t; }
    string getTelefone() { return telefone; }

    void setDtNasc(Data d) { dtnasc = d; }
    Data getDtNasc() { return dtnasc; }

    int idade() {
        time_t t = time(0);
        tm* now = localtime(&t);
        int anoAtual = now->tm_year + 1900;
        int mesAtual = now->tm_mon + 1;
        int diaAtual = now->tm_mday;

        int anos = anoAtual - dtnasc.getAno();

        if (mesAtual < dtnasc.getMes() || (mesAtual == dtnasc.getMes() && diaAtual < dtnasc.getDia())) {
            anos--;
        }

        return anos;
    }
};

int main() {
    const int QTD = 5;
    Contato contatos[QTD];
    
    string nome, email, telefone;
    int d, m, a;

    cout << "--- Cadastro de " << QTD << " Contatos ---" << endl;

    for (int i = 0; i < QTD; i++) {
        cout << "\nContato #" << i + 1 << ":" << endl;
        cout << "Nome: ";
        getline(cin >> ws, nome);
        cout << "Email: ";
        getline(cin, email);
        cout << "Telefone: ";
        getline(cin, telefone);
        cout << "Data de Nascimento (dia mes ano): ";
        cin >> d >> m >> a;

        contatos[i] = Contato(nome, email, telefone, Data(d, m, a));
    }

    cout << "\n--- Lista de Contatos Cadastrados ---" << endl;
    cout << "--------------------------------------------------------" << endl;
    for (int i = 0; i < QTD; i++) {
        cout << "Nome: " << contatos[i].getNome() << endl;
        cout << "Email: " << contatos[i].getEmail() << endl;
        cout << "Telefone: " << contatos[i].getTelefone() << endl;
        cout << "Idade: " << contatos[i].idade() << " anos" << endl;
        cout << "--------------------------------------------------------" << endl;
    }

    return 0;
}