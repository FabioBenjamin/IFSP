import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);

        double valor = 100;

        System.out.println("Digite a forma de pagamento \n(pix, cartao de credito ou euro) \nDigite sua opção: ");
        String opcao = user.nextLine();

        PagamentoStrategy pagamento = PagamentoFactory.criarPagamento(opcao);

        double valorFinal = pagamento.pagar(valor);

        System.out.println("Valor final: R$ " + valorFinal);

        AuditoriaLog log = AuditoriaLog.getInstance();
        log.registrar("Pagamento de R$ " + valorFinal + " realizado via " + opcao);

        user.close();
    }
}
