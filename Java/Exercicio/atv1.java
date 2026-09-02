public class atv1 {

    public void processoVendas(double valor, int pontos){
        double desconto = valor * 0.15;
        double totalValor = valor - desconto;

        if(pontos > 0){
            totalValor = totalValor - (pontos * 5);
        }

        System.out.println("Total com dedução extra de pontos: " + totalValor);
    }

    private void resumoVenda(double valor, int desconto, double totalValor){
        System.out.println("Valor original: " + valor);
        System.out.println("Desconto: " + desconto);
        System.out.println("Total: " + totalValor);
    }
}
