-- Crea usuario nuevo con contraseña
CREATE USER 
'empresadam'@'localhost' 
IDENTIFIED  BY 'Empresadam123$';

-- Permite acceso a ese usuario
GRANT USAGE ON *.* TO 'empresadam'@'localhost';

-- Quitale todos los limites que tenga
ALTER USER 'empresadam'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- Dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'empresadam'@'localhost';

-- Recarga la tabla de privilegios
FLUSH PRIVILEGES;
