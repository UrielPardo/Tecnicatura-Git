package ejerciciolibro;

import java.util.Scanner;

public class EjercicioLibro {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nombre, aux;
        int id;
        float precio;
        boolean respuesta, envio;
        respuesta = true;
        envio = true;
        while (respuesta == true) {
            //Mostramos los datos a solicitar y los almacenamos en las distintas variables
            System.out.println("Ingrese los siguientes datos de un libro:");
            System.out.println("Digite el nombre del libro:");
            nombre = sc.nextLine();
            System.out.println("Digite el ID del libro:");
            id = Integer.parseInt(sc.nextLine());
            System.out.println("Digite el precio del libro:");
            precio = Float.parseFloat(sc.nextLine());
            System.out.println("Indicar si el envio es gratis (si/no)");
            aux = sc.nextLine();
            //Verificamos la respuesta del usuario comparando la cadena de caracteres, e ignorando mayusculas o minusculas
            if (aux.equalsIgnoreCase("si")) {
                envio = true;
            } 
            else if (aux.equalsIgnoreCase("no")) {
                envio = false;
            }
            
            if (envio == true){
                System.out.println("\nLos datos del libro en cuestion son:");
                System.out.println("Nombre: " + nombre);
                System.out.println("ID: " + id);
                System.out.println("Precio: " + precio);
                System.out.println("Envio gratuito?: Si");
            }
            else {
                System.out.println("\nLos datos del libro en cuestion son:");
                System.out.println("Nombre: " + nombre);
                System.out.println("ID: " + id);
                System.out.println("Precio: " + precio);
                System.out.println("Envio gratuito?: No");
            }
            System.out.println("¿Desea ingresar otro libro? (si/no)");
            aux = sc.nextLine();
            //Verificamos la respuesta del usuario comparando la cadena de caracteres, e ignorando mayusculas o minusculas
            if (aux.equalsIgnoreCase("si")) {
                //true = ingresa otro libro
                respuesta = true;
            } else if (aux.equalsIgnoreCase("no")) {
                //false = no ingresa mas libros
                respuesta = false;
            }
        } 
    }
}
