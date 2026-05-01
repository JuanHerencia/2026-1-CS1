/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author PCA00
 */
public class VehiculoElectrico implements IGeneradorElectrico {

    @Override
    public int obtenerEnergiaSol() {
        return 5000; // KW
    }

    @Override
    public void darPotencia(int valorPotencia) {
        System.out.println(valorPotencia + "KW");
    }
    
}
