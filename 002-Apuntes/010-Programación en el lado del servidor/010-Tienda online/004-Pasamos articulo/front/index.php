<?php include "inc/cabecera.php"; ?>
<section id="heroe">
	<h3>Motivo por el cual debería comprar</h3>
	<p>Frasse sugerente al respecto</p>
	<a href="catalogo.php">Vamos a ver esa maravilla de catálogo</a>
</section>
<style>
	#heroe{
		background:orange;
		height:400px;
		display:flex;
		flex-direction:column;
		color:black;
		justify-content:center;
		align-items:center;
		border-radius:5px;
		margin-bottom:20px;
	}
	#heroe a{
		color:orange;
		background:black;
		text-decoration:none;
		padding:10px;
		border-radius:5px;
	}
</style>
<section id="razones">
	<article>
		<h4>Razón 1 por la cual debes comprar</h4>
		<p>Descripción de esa razón</p>
	</article>
	<article>
		<h4>Razón 2 por la cual debes comprar</h4>
		<p>Descripción de esa razón</p>
	</article>
	<article>
		<h4>Razón 3 por la cual debes comprar</h4>
		<p>Descripción de esa razón</p>
	</article>
	<article>
		<h4>Razón 4 por la cual debes comprar</h4>
		<p>Descripción de esa razón</p>
	</article>
<section>
<style>
	#razones{
		display:grid;
		grid-template-columns:repeat(2, 1fr);
		gap:20px;
	}
	#razones article{
		text-align:center;
		background:orange;
		padding:20px;
		border-radius:5px;	
		display:flex;
		flex-direction:column;
		color:black;
		justify-content:center;
		align-items:center;
	}

<?php include "inc/piedepagina.php"; ?>
