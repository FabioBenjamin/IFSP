import javax.swing.*;
import java.awt.*;

public class Exercicio02 extends JFrame {
    public Exercicio02(){

        setTitle("Login");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        setLayout(new BorderLayout());

        JPanel painelFormulario = new JPanel (new GridLayout(2, 2));

        JLabel lblUtilizador = new JLabel("Utilizador");
        JTextField txtUtilizador = new JTextField();

        JLabel lblSenha = new JLabel("Senha: ");
        JPasswordField txtSenha = new JPasswordField();

        painelFormulario.add(lblUtilizador);
        painelFormulario.add(txtUtilizador);
        painelFormulario.add(lblSenha);
        painelFormulario.add(txtSenha);

        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton butao = new JButton("Entrar");

        painelBotao.add(butao);

        add(painelFormulario, BorderLayout.CENTER);
        add(painelBotao, BorderLayout.SOUTH);
    }

    public static void main(String[] args){
        // Trade de eventos
        SwingUtilities.invokeLater(() -> // Lambda
        {
            Exercicio02 janela = new Exercicio02();

            janela.setVisible(true);
        });
    }
}
