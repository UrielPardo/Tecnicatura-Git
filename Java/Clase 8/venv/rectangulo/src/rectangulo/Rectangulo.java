package rectangulo;

import java.util.Scanner;

public class Rectangulo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var alto = 0;
        var ancho = 0;
        System.out.println("Digite el alto del rectángulo:");
        alto = Integer.parseInt(sc.nextLine());
        System.out.println("Digite el ancho del rectángulo:");
        ancho = Integer.parseInt(sc.nextLine());
        System.out.println("Área = "+ alto*ancho +";");
        System.out.println("Perímetro = "+(alto + ancho)*2+";");
    }
    
}
