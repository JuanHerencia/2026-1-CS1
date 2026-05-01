package controller;
import model.VehiculoElectrico;

/**
 *
 * @author PCA00
 */
public class Main {
    // Debido a este main, la clase Main se transforma en clase ejecutable
    public static void main(String[] args) {
        VehiculoElectrico ve = new VehiculoElectrico();
        ve.darPotencia(500);
    }
}
