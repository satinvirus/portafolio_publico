def descripcion ():

    desc_nom = input("Ingresa Nombre de persona fisica o institucion: ")

    print(f"Descripcion: {desc_nom}")



def precios():

    impuestos = 0.19
    total_sin = 0
    total_con_impuestos = 0

    no_productos =  int(input("Ingresa el numero de productos: "))


    for i in range (1, no_productos +1):


        pre = float(input(f"Precio de producto No. {i} : "))

        total_con = pre + (pre * impuestos)
        total_sin += pre
        total_con_impuestos += total_con

        print(f"Precio con impuestos del producto No. {i} : {total_con}")

    descripcion()
    print(f"Total sin impuestos: {total_sin}")
    print(f"Total después de impuestos: {total_con_impuestos}")



def prueba():

    objeto1  = "Hola andres"
    objeto2 = "".join(["Hola"," andres"])

    print("Son el mismo objeto? ", objeto1 is objeto2)
    print("Tienen el mismo valor? ", objeto1 == objeto2)




def main():
    precios()
    print()
    #prueba()


if __name__ == '__main__':
    main()