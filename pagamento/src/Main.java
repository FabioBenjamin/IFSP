import java.util.Scanner;

public class Main implements PagamentoStrategy {

    private double AutoriaLog;

    // Construtor
    public Main(double AutoriaLog) {
            this.AutoriaLog = AutoriaLog;
    }

    public double getAutoriaLog() {
        return AutoriaLog;
    }

    public static void main(String[] args) {
        Scanner pergunta = new Scanner(System.in);

        System.out.println("Qual forma de pagamento (pix/Credito): ");
        String questao = pergunta.next();

        
    }
}