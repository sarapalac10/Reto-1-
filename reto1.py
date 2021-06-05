print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user= 51687
password= 78615

cod1 = str(user)
cod2 = cod1[3]
#print(cod2)

a= 5
b= 1
c = 6
d = 8
e = 7

operacion1 = ((((a+b)*e)+c)/c)
#print(round(operacion1))

operacion2= ((((c**a)/(d*(e+d-c)))-(a+e)))/(a+b+c)
#print(round(operacion2))

operacion3= (d-a+e-c+b+a-b-b)
#print(round(operacion3))

cap= str(c) + str(d) + str(e)
# print(cap)
captcha1= int(cap)
#print(type(captcha1))

cod_final= operacion1 = operacion2 = operacion3
#print(cod_final)

captcha_final= captcha1 + cod_final
#print(captcha_final)

x= int (input("Ingresa tu usuario: "))
print(x)
if x == user :
    y = int (input("Ingresa tu contraseña: "))
    if y == password :
        print("Contraseña correcta")
        z = int(input("Ahora, realiza la siguiente operación: \n" +cap + " + " + cod2 + " ="))
        if z == captcha_final :
            print("Sesión iniciada")
        else: print("Error")
    else: print("Error")
else: print("Error")







