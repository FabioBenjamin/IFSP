import javax.swing.*;
import java.awt.*;

public class Exercicio03 extends JFrame {
    public Exercicio03() {

        setTitle("Exercicio 3 - LBP 2");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        setLayout(new BorderLayout());

        JPanel painel = new JPanel(new GridLayout(2, 2));

        JLabel lblUtilizador = new JLabel("Utilizador");
        JTextField txtUtilizador = new JTextField();

        JLabel lblSenha = new JLabel("Senha: ");
        JPasswordField txtSenha = new JPasswordField();

        painel.add(lblUtilizador);
        painel.add(txtUtilizador);
        painel.add(lblSenha);
        painel.add(txtSenha);

        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton botao = new JButton("Entrar");

        painelBotao.add(botao);

        add(painel, BorderLayout.CENTER);
        add(painelBotao, BorderLayout.SOUTH);

        botao.addActionListener(e -> {
            String nome = txtUtilizador.getText();
            String senha = new String(txtSenha.getPassword());

            if (nome.equals("admin") && senha.equals("1234")) {
                JOptionPane.showMessageDialog(null, "Login efetuado com sucesso!");
                txtUtilizador.setText("");
                txtSenha.setText("");
            } else {
                JOptionPane.showMessageDialog(null, "Falha no login!");
                txtUtilizador.setText("");
                txtSenha.setText("");
            }
        });
    }

    public static void main(String[] args) {
        // Trade de eventos
        SwingUtilities.invokeLater(() -> // Lambda
        {
            Exercicio03 janela = new Exercicio03();

            janela.setVisible(true);
        });
    }
}



