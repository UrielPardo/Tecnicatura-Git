package ejercicio.pkg7;
import java.util.Scanner;
public class Ejercicio7 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int salario = 1000;
        var precio = 0.0;
        var porcentaje = 0.0;
        System.out.println("Digite la cantidad de carros vendidos");
        var carros = Integer.parseInt(sc.nextLine());
        if (carros > 0){
            for (int i = 1; i <= carros; i++) {
                System.out.println("Digite el valor del "+i+"° carro vendido");
                precio = Float.parseFloat(sc.nextLine());
                porcentaje = porcentaje + precio;
            }
            porcentaje = porcentaje*0.05;
        }
        System.out.println("El salario del empleado es: "+(salario+porcentaje+(carros*150)));
    }
}
