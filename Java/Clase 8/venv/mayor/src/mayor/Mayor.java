package mayor;

import java.util.Scanner;

public class Mayor {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var num1 = 0;
        var num2 = 0;
        System.out.println("Digite el primer numero");
        num1 = Integer.parseInt(sc.nextLine());
        System.out.println("Digite el segundo numero");
        num2 = Integer.parseInt(sc.nextLine());
        var mayor = ( num1 > num2) ? "El primer numero es mayor" : "El segundo numero es mayor";
        System.out.println("mayor = " + mayor);
    }
    
}
