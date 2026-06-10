#funciones
def ficha_producto(nombre, precio, stock):
    print("-------------")
    print(f"||Nombre del producto: {nombre} ||")
    print(f"||Stock del producto: {stock} ||")
    print(f"||Precio del producto: {precio} ||")
    print("-------------")

nombre1 = input("Ingrese el nombre del producto: ")

while True:
    try:
        stock1 = int(input("Ingrese el stock del producto"))
        if stock1 < 0:
            print("debe ser mayor o igual a cero")
        else:
            break
    except ValueError:
        print("Debe de ingresar numeros")
while True:
    try:
        precio1 = int(input("Ingrese el precio"))
        if precio1 <= 0:
            print("debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Debe de ingresar numeros")
ficha_producto(nombre1, precio1, stock1)


