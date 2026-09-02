public class atv4 {

    public class Endereco{
        private String Estado;
        private boolean Capital;

        public double calcularFrete() {
            if (Estado.equals("SP") && Capital) {
                return 15.00;
            } else if (Estado.equals("SP")) {
                return 25.00;
            }
            return 50.00;
        }
    }
}
