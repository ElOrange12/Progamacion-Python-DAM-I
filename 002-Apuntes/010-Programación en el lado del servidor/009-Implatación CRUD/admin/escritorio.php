<!-- http://localhost/GitHub/Progamacion-DAM-I/002-Apuntes/001-C%C3%B3digo/010-Programaci%C3%B3n%20en%20el%20lado%20del%20servidor/900-Implataci%C3%B3n%20CRUD/admin/escritorio.php -->

<!doctype html>
<html lang="es">
	<head>
		<title>El jocarsa - Panel de control</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/estilo.css">
	</head>
	<body>
		<nav>
			<button>Noticias</button>
			<button>Autores</button>
		</nav>
		<main>
			<?php 
				//////// Esto se conoce como router (Enrutador) ////////
				if(isset($_GET['accion'])){									// Si hay "accion" en la URL
					if($_GET['accion'] == "nuevo"){							// Si la acción es "nuevo"
						include "inc/create/formulario.php";				// En ese caso mete el formulario
					}else if($_GET['accion'] == "eliminar"){				// Defino la acción eliminar
						include "inc/delete/eliminar.php";					// En ese caso incluye eliminar.php
					}else if($_GET['accion'] == "editar"){				// Defino la acción editar
						include "inc/update/formularioactualizar.php";		// En ese caso incluyo el formulario de la edición
					}
				}else{											// En caso contrario
					include "inc/read/leer.php";				// Enseñame la tabla
				}
			?>
			<a href="?accion=nuevo" id="nuevo">+</a>
		</main>
	</body>
</html>

