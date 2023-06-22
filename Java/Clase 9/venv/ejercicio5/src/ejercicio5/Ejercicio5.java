package ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var nota1 = 0.0;
        var nota2 = 0.0;
        var nota3 = 0.0;
        do {
            System.out.println("Digite la primer nota entre 1 y 10");
            nota1 = Float.parseFloat(sc.nextLine());
        } while (nota1 < 1 || nota1 >10);
        do {
            System.out.println("Digite la segunda nota entre 1 y 10");
            nota2 = Float.parseFloat(sc.nextLine());
        } while (nota2 < 1 || nota2 >10);
        do {
            System.out.println("Digite la tercer nota entre 1 y 10");
            nota3 = Float.parseFloat(sc.nextLine());
        } while (nota3 < 1 || nota3 >10);
        System.out.println("La suma de las calificaciones es: "+(nota1+nota2+nota3));
    }
    
}
