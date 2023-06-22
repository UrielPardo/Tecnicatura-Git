package ejercicio.pkg6;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Digite la cantidad de dolares que posee Guillermo");
        var dolar = Float.parseFloat(sc.nextLine());
        dolar = dolar+(dolar/2);
        dolar = dolar+(dolar/2);
        System.out.println("Entre Guillermo, Luis y Juan tienen USD$" + dolar );
    }
}
