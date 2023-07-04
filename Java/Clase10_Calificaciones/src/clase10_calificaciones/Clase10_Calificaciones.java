package clase10_calificaciones;

import java.util.Scanner;

public class Clase10_Calificaciones {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite un numero entre 0 y 10");
        var calificacion = Integer.parseInt(sc.nextLine());
        if (9<=calificacion && calificacion<= 10){
            System.out.println("A");
        }
        else if (8<=calificacion && calificacion< 9){
            System.out.println("B");
        }
        else if (7<=calificacion && calificacion< 8){
            System.out.println("C");
        }
        else if (6<=calificacion && calificacion< 7){
            System.out.println("D");
        }
        if (0<=calificacion && calificacion< 6){
            System.out.println("F");
        }
        if (calificacion < 0 || calificacion > 10) {
            System.out.println("Fuera de rango");
        }
    }
    
}
