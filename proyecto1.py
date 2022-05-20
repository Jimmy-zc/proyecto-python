
productos = []
nombre_del_producto = input('Bienvenido a la tiendita el Jimmy, ingrese el nombre del articulo: ')
productos.append(nombre_del_producto)
precio = int(input('ingrese el precio del articulo: '))
total = precio




ciclo = True
while ciclo:
    pregunta= input('''
    --> desea agregar mas productos? (si - no) 
    --> desea ver el carrito (lista)
    --> eliminar el articulo anterior (dell)''')

    if pregunta == 'si':
        nombre_del_producto= input('ingrese el nombre del articulo: ')
        productos.append(nombre_del_producto)
        precio = int(input('ingrese el precio del articulo: '))
        total += precio

    elif pregunta == 'lista':
        print('los articulos en el inventario son: ', productos, 'y el monto a pagar es de $',total)

    elif pregunta == 'dell':
        print('el articulo', productos[-1],' ha sido eliminado')
        productos.pop()
        total -= precio
        

    else:
        ciclo = False


print('los articulos comprados fueron: ', productos, 'por un total de $ ' , total)



