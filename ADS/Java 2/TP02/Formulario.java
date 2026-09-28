import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Formulario extends JFrame {
    
    private List<Aluno> listaAlunos;
    private JTextField txtNome;
    private JTextField txtIdade;
    private JTextField txtEndereco;

    public Formulario() {
        // Inicializa a lista em memória[cite: 1]
        listaAlunos = new ArrayList<>();

        // Configurações da Janela[cite: 1]
        setTitle("TP02-LP214");
        setSize(400, 180);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        // O Gerenciador de Layout ideal para posicionar os 2 painéis desta forma é o BorderLayout[cite: 1]
        setLayout(new BorderLayout());

        // Configuração do Painel Superior (GridLayout 3x2, hgap 10, vgap 10)[cite: 1]
        JPanel painelSuperior = new JPanel(new GridLayout(3, 2, 10, 10));
        painelSuperior.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        painelSuperior.add(new JLabel("Nome:"));
        txtNome = new JTextField();
        painelSuperior.add(txtNome);

        painelSuperior.add(new JLabel("Idade:"));
        txtIdade = new JTextField();
        painelSuperior.add(txtIdade);

        painelSuperior.add(new JLabel("Endereço:"));
        txtEndereco = new JTextField();
        painelSuperior.add(txtEndereco);

        // Configuração do Painel Inferior (GridLayout com 4 botões)[cite: 1]
        JPanel painelInferior = new JPanel(new GridLayout(1, 4, 5, 0));
        painelInferior.setBorder(BorderFactory.createEmptyBorder(0, 10, 10, 10));

        JButton btnOk = new JButton("Ok");
        JButton btnLimpar = new JButton("Limpar");
        JButton btnMostrar = new JButton("Mostrar");
        JButton btnSair = new JButton("Sair");

        painelInferior.add(btnOk);
        painelInferior.add(btnLimpar);
        painelInferior.add(btnMostrar);
        painelInferior.add(btnSair);

        // Adicionando os painéis ao formulário principal usando BorderLayout[cite: 1]
        add(painelSuperior, BorderLayout.CENTER);
        add(painelInferior, BorderLayout.SOUTH);

        // Ações dos Botões
        
        // i. Botão Ok: armazena os dados contidos em tela em memória[cite: 1]
        btnOk.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    Aluno aluno = new Aluno();
                    aluno.setNome(txtNome.getText());
                    aluno.setIdade(Integer.parseInt(txtIdade.getText()));
                    aluno.setEndereco(txtEndereco.getText());
                    aluno.setUuid(UUID.randomUUID()); 

                    listaAlunos.add(aluno);
                    JOptionPane.showMessageDialog(Formulario.this, "Aluno salvo com sucesso!");
                    limparCampos();
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(Formulario.this, "Por favor, insira uma idade válida.", "Erro de Validação", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        // ii. Botão Limpar: apaga o conteúdo dos campos[cite: 1]
        btnLimpar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                limparCampos();
            }
        });

        // iii. Botão Mostrar: exibe pop-up com todos os ids e nomes cadastrados[cite: 1]
        btnMostrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                StringBuilder mensagem = new StringBuilder("Resultado\n");
                for (Aluno a : listaAlunos) {
                    mensagem.append("Id: ").append(a.getUuid().toString())
                            .append(" Nome: ").append(a.getNome()).append("\n");
                }
                
                JOptionPane.showMessageDialog(Formulario.this, mensagem.toString(), "Mensagem", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        // iv. Botão Sair: encerra a aplicação[cite: 1]
        btnSair.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
    }

    private void limparCampos() {
        txtNome.setText("");
        txtIdade.setText("");
        txtEndereco.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Formulario().setVisible(true);
            }
        });
    }
}