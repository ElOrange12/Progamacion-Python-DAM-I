<?php
	// Primero cogemos la info que viene del formulario
	$titulo = $_POST['titulo'];										// Atrapo el titulo que viene del formulario
	$contenido = $_POST['contenido'];								// Atrapo el contenido que viene del formulario
	$fecha_publicacion = $_POST['fecha_publicacion'];				// Atrapo la fecha de publicación que viene del formulario
	$autor_id = $_POST['autor_id'];									// Atrapo el ID de autor que viene del formulario
  	
	// Y luego metemos esa información en la base de datos
	$host = "localhost";											// Me conecto a la base de datos
	$user = "periodico";
	$pass = "Periodico123$";
	$db   = "periodico";

	$conexion = new mysqli($host, $user, $pass, $db);				// Ejecuto la conexion

	// Metemos los datos en la base de datos
	$sql = "
		INSERT INTO noticias VALUES(
			NULL,
			'".$titulo."',
			'".$contenido."',
			'".$fecha_publicacion."',
			".$autor_id."
		);
	";
	$conexion->query($sql);											// Lanzo la petición
	
	$conexion->close();												// Cierro la conexión
	header("Location: ../../escritorio.php");						// Y me vuelvo al escritorio
?>
