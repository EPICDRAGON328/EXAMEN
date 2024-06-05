def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        
        return False, "La contraseña necesita 8 o más caracteres" 
        
    tiene_mayuscula = False
    tiene_numero = False

    for char in contraseña:
        
         if char.isupper():
            tiene_mayuscula = True
        
         if char.isdigit():
            tiene_numero = True
        
    if not tiene_mayuscula:
           return False, "La contraseña debe contener al menos 1 letra mayúscula."

    if not tiene_numero:
           return False, "La contraseña debe contener al menos 1 número."

    return True, "Contraseña válida."

def solicitar_contraseña():
    while True:
        contraseña = input("Ingrese su contraseña:")
        es_valida, mensaje = validar_contraseña(contraseña)
        if es_valida:
            print(mensaje)
            break
        else:
            print(mensaje)


solicitar_contraseña()