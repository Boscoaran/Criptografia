# Criptografía

descifrador.py
Descifrador de mensajes encriptados por análisis de frencuencia y patrones 
El script analiza la frecuencia de las letras que más aparecen. A las dos que más aparecen se les asigna la E y la A respectivamente, son las letras que más aparecen en castellano.
Para el resto de letras se busca un patrón que encaje con palabras comunes. Por ejemplo "a la", se busca espacio 'a' espacio cualquier letra y 'a'. La letra en la posición que falta sera la L desencriptada.
Para cada texto hay que hacer modificiaciones. Copiar uno de los bloques de buscar... cambiar el patrón que se busca y poner en des[ ] la posición que ocupa la letra en el abecedario menos 1.
Se puede adaptar a otros idiomas si se conocen las dos letras con más frecuencia.
Cuanto más largo sea el texto más fácil sera desencriptarlo.

comprobarhash.sh
Busca un archivo con un hash concreto y obtiene el mensaje incluido en el por medio de stegosuite.
Para usarlo es necesario cambiar la ruta en la que busca el archivo y ajustar la busqueda (cambiar el tipo de archivo que se busca o poner el nombre si es solo uno).
También es necesario cambiar el hash por el que se busca. Es necesario tener instalado stegosuite. "sudo apt install stegosuite".
El programa usa MD5, no es necesario instalarlo, viene por defecto. 
