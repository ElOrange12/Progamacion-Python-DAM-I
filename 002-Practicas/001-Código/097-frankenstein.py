from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def raiz():
	return ''' 
	<!doctype html>
<html lang="es">
	<head>
		<title>ElOrangeBLOG</title>
		<meta charset="utf-8">
		<style>
			body{background:steelblue; color:steelblue; font-family:sans-serif;}
			header, main, footer{background:white; padding:20px; margin:auto; width:600px;}
			header, footer{text-align:center;}
			main{color:black;}
		</style>
	</head>
	<body>
		<header><h1>ElOrangeBLOG</h1></header>
		<main>
			<article>
				<h3>Titulo del artículo</h3>
				<time>16-10-2025</time>
				<p>Daniel Oliveira Vidal</p>
				<p>Este es el contenido de un artículo ficticio</p>
			</article>
		</main>
		<footer>(c)2025 Daniel Oliveira Vidal</footer>
	</body>
</html>
'''

if __name__ == '__main__':
	aplicacion.run(debug = True)
