import javax.swing.*;

public class Exercicio01 extends JFrame {

    public Exercicio01(){

        // Titulo da janela
        setTitle("Primeira Janela - LBP2");
        // Tamanho da pagina
        setSize(800, 600);
        // Conseguir fechar a pagina
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }

    public static void main(String[] args){
        // Trade de eventos
        SwingUtilities.invokeLater(() -> // Lambda
        {
            Exercicio01 janela = new Exercicio01();

            janela.setVisible(true);
        });
    }

}
