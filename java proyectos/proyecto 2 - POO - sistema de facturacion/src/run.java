import java.util.Scanner;

public class run {


    protected static void factura() {

        verificacion v = new verificacion();

        Scanner teclado = new Scanner(System.in);

        double impuesto = 0.19;

        double precio = 0;
        double precio_iva;

        double temp = 0;
        double temp2 = 0;


        int cont_producto = 0;

        try {
            System.out.println("Ingresa el numero de productos a facturar: ");
            cont_producto = teclado.nextInt();

        } catch (Exception e) {
            System.out.println("El valor ingresado es incorrecto, intentar de nuevo.");
        }


        for (int i = 1; i <= cont_producto; i++) {

            System.out.println("Precio de producto " + i + ": ");

            v.setprecio(precio = teclado.nextDouble());

           //precio = teclado.nextDouble();

            precio_iva =  v.getprcio() + (v.getprcio() * impuesto);

            System.out.println("Precio con iva: " + precio_iva);

            temp += precio_iva;
            temp2 += v.getprcio();


        }
        datos();
        System.out.println("Sin iva: " + temp2);
        System.out.println("iva: " + impuesto + "%");
        System.out.println("Total: " + temp);


    }

    private static void datos(){

        String descripcion;


        Scanner teclado = new Scanner(System.in);


        System.out.println("Ingresa la descripcion: ");
        descripcion = teclado.nextLine();

        System.out.println("Descripcion: " + descripcion);


    }


}
