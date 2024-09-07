lista_compras = []

while True:
    
    opcion = input("a - agregar al carrito\nb - eliminar articulo\nc - mostrar lista\nd - salir: ")
    
    if (opcion == "a"):
        agregar = input("digite el nombre del articulo: ")   
        lista_compras.append(agregar)
    elif (opcion == "b"):
        print(lista_compras)
        indice = int(input("digite indice del articulo que desea eliminar: "))
        del lista_compras[indice]
    elif (opcion =="c"):
        print(lista_compras)
    elif (opcion == "d"):
        print("Gracias por participar, chaoo")
    else:
        print("Elige una opcion correcta")