

def precio_producto(producto: float, impuesto: float):
    impuesto_producto= (impuesto * producto) / 100
    return impuesto_producto + producto

print(precio_producto(30,15)) 