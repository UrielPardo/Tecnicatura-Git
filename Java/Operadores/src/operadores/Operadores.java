package operadores;

public class Operadores {

    public static void main(String[] args) {
        /*
        int num1 = 5, num2= 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma= " + solucion);
        solucion = num1 - num2;
        System.out.println("solucion de la resta= " + solucion);
        solucion = num1*num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        solucion = num1/num2;
        System.out.println("solucion de la division= " + solucion);
        var solucion2 = 3.4/num2;
        System.out.println("solucion2 resultado de la division= " + solucion2);
        solucion2 = num1 % num2;
        System.out.println("solucion2 residuo de la division= " + solucion2);
        if(num2 % 2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero impar");
        */
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
        //Ejercicio a precticar con el resto de operandos
        varNum2 -= 2;
        System.out.println("-=");
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("*=");
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("/=");
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("%=");
        System.out.println("varNum1 = " + varNum1);
    } 
}
