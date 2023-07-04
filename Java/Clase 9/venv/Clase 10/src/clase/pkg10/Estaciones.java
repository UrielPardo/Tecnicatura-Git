package clase.pkg10;

import java.util.Scanner;

public class Estaciones {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el numero de un mes del año");
        var mes = Integer.parseInt(sc.nextLine());
        var estacion = "Estacion desconocida";
        if (mes == 1 || mes == 2 || mes == 3){
            estacion = "Verano";
        }
        if (mes == 4 || mes == 5 || mes == 6){
            estacion = "Otoño";
        }
        if (mes == 7 || mes == 8 || mes == 9){
            estacion = "Invierno";
        }
        if (mes == 10 || mes == 11 || mes == 12){
            estacion = "Primavera";
        }
        System.out.println("La estacion es: " + estacion);
    }
    
}
