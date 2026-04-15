public class AuditoriaLog {

    private static AuditoriaLog instancia;

    private AuditoriaLog() {}

    public static AuditoriaLog getInstance() {
        if (instancia == null) {
            instancia = new AuditoriaLog();
        }
        return instancia;
    }

    public void registrar(String mensagem) {
        System.out.println("LOG: " + mensagem);
    }
}