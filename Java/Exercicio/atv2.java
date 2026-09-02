public class atv2 {

    public static final double horasMensais = 160;
    public static final double horasExtras = 25.50;
    public static final double horasNormais = 38.25;

    public double calculoSalario(double horas) {
        if (horas > horasMensais) {
            return (horasMensais * horasNormais) + ((horas - horasMensais) * horasExtras);
        }
        return horas * horasNormais;
    }
}