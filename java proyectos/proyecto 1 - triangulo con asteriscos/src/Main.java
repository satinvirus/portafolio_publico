import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
    /*
        char caracter = '\u0040';
        char decimal = 64;

        System.out.println("caracter = " + caracter);
        System.out.println("decimal = " + decimal);
        System.out.println("decimal = caracter? = " + (decimal == caracter));
        System.out.println("caracter corresponde en byte a = " + Character.BYTES);
        System.out.println("caracter corresponde en bytes a = " + Character.SIZE);
        System.out.println("caracter valor minimo a = " + Character.MIN_VALUE);
        System.out.println("caracter valor maximo a = " + Character.MAX_VALUE);


        for (int i = 0 ; i<=5;i++){

            System.out.println("ciclo for esta en el numero = " + i);

        }

        Scanner teclado = new Scanner(System.in);

            System.out.println("ingresa un valor: ");
            int valor = teclado.nextInt();


        for(int i = 1; i<= valor;i++){

            System.out.println("ciclo for esta en el numero con un valor ingresado por el usuario = " + i);

        }*/
        cuadrado();
        triangulo_escaleno();
        triangulo_escalenoalrevez();
        triangulo_equilatero();

    }

    public static void cuadrado (){
        int i, j;

        for (i = 1; i <= 5; i++){ // y filas

            for (j=1; j <=5; j++ ){ //x comlumnas
                System.out.print("* ");
            }
            System.out.println();

        }

        System.out.println("------------------------------");

    }


    public static void triangulo_escaleno(){

        int i, j;
        for (i = 1; i <= 5; i++){ // y filas

            for (j=1; j <= i; j++ ){ //x comlumnas
                System.out.print("* ");


            }
            System.out.println();

        }
        System.out.println("------------------------------");

    }

    public static void triangulo_escalenoalrevez(){

        int i, j;

        for (i = 1; i < 6; i++){ //  filas

            for (j=1; j < 6; j++){ // comlumnas
                System.out.print("");


            }
            for (j=i; j < 6; j++){ // comlumnas
                System.out.print("* ");


            }
            System.out.println("");

        }
        System.out.println("------------------------------");

    }

    public static void triangulo_equilatero(){


        int i, j ;

        for (i = 1; i < 5; i++){ // y filas

            for (j=1; j < i; j++ ){ //x comlumnas
                System.out.print("* ");


            }
            System.out.println();

        }




        for (i = 1; i < 6; i++){ //  filas

            for (j=1; j < 6; j++){ // comlumnas
                System.out.print("");


            }
            for (j=i; j < 6; j++){ // comlumnas
                System.out.print("* ");


            }
            System.out.println("");

        }




        for (i = 1; i < 5; i++){ // y filas

            for (j = 1; j > i; j++ ){ //x comlumnas /////////////////
                System.out.print("* ");


            }
            System.out.println();

        }




        for (i = 1; i > 6; i++){ //  filas

            for (j=1; j > 6; j++){ // comlumnas
                System.out.print("");


            }
            for (j=i; j > 6; j++){ // comlumnas
                System.out.print("* ");


            }
            System.out.println("");

        }







        System.out.println("------------------------------");




    }














}