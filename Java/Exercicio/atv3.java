public class atv3 {

    public class Pedido {
        private String nomeCliente;
        private double valorTotal;

        public void calcularValorTotal(){
            // Calculo dos descontos e total
        }
    }

    public class PedidoRepository {

        public void SalvarNoBancoDeDados(Pedido pedido) {
            // Abre conexão com DB e fazer o INSERT
        }
    }

    public class PedidoEmailService{

        public void EmailConfirmando(Pedido pedido) {
            // Conecta via SMTP e envia email
        }
    }
}
