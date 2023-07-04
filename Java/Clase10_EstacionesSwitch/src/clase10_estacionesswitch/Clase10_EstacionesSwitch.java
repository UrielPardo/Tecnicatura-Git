package clase10_estacionesswitch;

import java.util.Scanner;

public class Clase10_EstacionesSwitch {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el numero de un mes del año");
        var mes = Integer.parseInt(sc.nextLine());
        var estacion = "";
        switch (mes) {
            case 1: case 2: case 3:
                estacion = "Verano";
                break;
            case 4: case 5: case 6:
                estacion = "Otoño";
                break;
            case 7: case 8: case 9:
                estacion = "Invierno";
                break;
            case 10: case 11: case 12:
                estacion = "Primavera";
                break;
            default:
                estacion = "Estacion desconocida";
        }
        System.out.println("La estacion es: " + estacion);
    }
    
}
