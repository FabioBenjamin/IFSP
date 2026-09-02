public class Pagamento {
    public double pix;
    public double cartaoCredito;
    public double euros;

    public Pagamento(double pix, double cartaoCredito, double euros) {
        this.pix = pix;
        this.cartaoCredito = cartaoCredito;
        this.euros = euros;
    }

    public double desconto(double pix) {
        return pix - (pix * 0.10);
    }

    public double eurao(double euros){
        return euros * 5.88; // Valor do euro está 5,88
    }
}
