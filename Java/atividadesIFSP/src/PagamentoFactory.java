public class PagamentoFactory {

    public static PagamentoStrategy criarPagamento(String opcao) {

        Pagamento pagamento = new Pagamento(0, 0, 0);

        switch (opcao.toLowerCase()) {
            case "pix":
                return valor -> pagamento.desconto(valor); // -> funcão anonima (preguica de escrever mais ai vai esse mesmo e fé)
            case "cartao de credito":
                return valor -> valor;
            case "euro":
                return valor -> pagamento.eurao(valor);

            default:
                throw new IllegalArgumentException("Opção inválida");
        }
    }
}