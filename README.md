# descifrador
Descifrazor de mensajes encriptados por análisis de frencuencia y patrones 
El script analiza la frecuencia de las letras que más aparecen. A las dos que más aparecen se les asigna la E y la A respectivamente, son las letras que más aparecen en castellano.
Para el resto de letras se busca un patrón que encaje con palabras comunes. Por ejemplo "a la", se busca espacio 'a' espacio cualquier letra y 'a'. La letra en la posición que falta sera la L desencriptada.
Para cada texto hay que hacer modificiaciones. Copiar uno de los bloques de buscar... cambiar el patrón que se busca y poner en des[ ] la posición que ocupa la letra en el abecedario menos 1.
Se puede adaptar a otros idiomas si se conocen las dos letras con más frecuencia.
Cuanto más largo sea el texto más fácil sera desencriptarlo.
