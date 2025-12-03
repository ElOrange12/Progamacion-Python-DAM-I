<?php
	$archivo = fopen("archivo.txt", "r"); // "r" = leer/read
	$contenido = fread($archivo);
	echo $contenido;
	fclose($archivo);
?>
