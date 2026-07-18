Bot hecho con python y google teachnable machine cuyo proposito es analizar jugadas de futbol para distinguir cuales fueron faltas y cuales no.
advertecia: el Bot no funciona a la perfección y en determinadas jugadas existe la posibilidad de que el bot las interprete a la inversa, es decir que detecte como falta una jugada que no lo fue y vicebersa.

funcionamiento: 
1) el bot tiene una estructura utilizando las bibliotecas de discord para conectarse con sus servidores.
2) el Bot tiene tanto eventos como comandos cuyo prefijo es "/".
3) cuando un usuario se comunique con el Bot utilizando el prefijo este le pedira imagenes las cuales deben ser enviadas en un plazo de 60s posteriores al primer mensaje.
4) luego de resivirla, la imagen es almacenada en una carpeta llamada "image" donde queda guardada para su posterior analisis.
5) una vez con la imagen almacenada se la analiza en el archivo de "model.py" en el cual se encuentra el código proveniente de google teachnable machine.
6) para finalizar se retorna el resultado del analisis hecho por google teachnable machine hacia el archivo "bot.py".
7) finalmente "bot.py" envía el resultado del analisis de "model.py" al usuaria de discord. 
