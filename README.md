# Reto-1-
Solución
Se requiere desarrollar un sistema de login que permita identificar a los usuarios que pertenecen a un curso específico y del cual conocen el código de dicho curso.

A través del sistema se verifica un usuario y la contraseña, y finalmente se realiza la autenticación por medio de un captcha de seguridad.
Dicho captcha corresponde a una operación matemática simple que relaciona los números pertenecientes al código del curso.

Sistema de login
Para ejecutar el programa se conoce el código del curso (51687) y la contraseña es el código leído hacia atrás.

Se evidencia que hay 3 operaciones matemáticas (operacion1, operacion2 y operacion3) en las cuales se usan las cifras del código de grupo (51687), el objetivo es que todas las operaciones tengan como resultado la penúltima cifra (8)

Por medio de una serie de "if-else" se relaciona la entrada de los datos del usuario y que estos sean iguales == que los datos definidos de entrada. Si esto no se cumple se envía 'Error'

Al tener usuario y contraseña correctos se pasa a la verificación del captcha
Este corresponde a la operación 687 + 8 donde el resultado debe ser 695.

para esto, se realiza una verificación de que el resultado ingresado sea igual == a la operación de int(operaciones) y el punúltimo dígito.
