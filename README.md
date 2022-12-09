<p align="center">
<img src="https://i.imgur.com/OAG522g.jpg"  height=400>
</p>



# Proyecto_Individual01
 Autor: Rodríguez Jorge Leonardo
 Tema: Proyecto - Data Engineer
 
 El presente proyecto tiene como objetivo realizar la subida de datos a partir de archivos, su tratamiento y limpieza y la puesta de ellos para la generación de ciertas consultas específicas, luego dichas consultas deben poder realizarse desde un entorno externo usando fastAPI y finalizado esto, debe poder conteneizarse con Docker listo para su exportación.
 
  Los Pasos a seguir entonces serán:
  1. Suba de archivos
  2. Limpieza
  3. Consultas
  4. FastApi
  5. Docker
  6. Presentación Final
 
 
 ###
 
1. Suba de archivos

 La suba de archivos se realiza en el archivo Suba.ipynb que se encuentra en la carpeta ETL, allí se explica con detalle la suba de los datos. En lineas generales, se creó un indice para cada tabla etiquetando el tipo de plataforma que usa. Luego se concatena todas las columnas y se crea un indice nuevo. A partir de allí se exporta la tabla creada a MySQL para mayor tratamiento.
 
2. Limpieza

 La limpieza se realiza principalmente en MySQL, en el archivo limpieza.sql, allí se explica con detalle los pasos realizados para la limpieza, los que incluye normalizar datos, eliminación de columnas, creación de un backup, modificación de los tipos de datos, tratamiento de NA, entre otros. 
 
  Cabe aclarar que la limpieza se realizó con el objetivo de realizar las consultas solicitadas para el proyecto, es posible realizar un tratamiento aún más profundo pero que por cuestiones de tiempo debieron ser omitidas, pues debemos aprender a usar FastAPI y Docker para este trabajo.
  
3. Consultas

 Las consultas fueron ejecutadas primero en MySQL, se encuentra en la carpeta ETL llamado consulta.sql, se pueden ejecutar y devolveran los valores solicitados. Esto se realizó a los fines de tener mayor facilidad de trasladar la consulta al entorno de fastAPI.
 
4. FastAPI 

Para el funcionamiento de fastAPI creé toda la estructura y los archivos necesarios para su funcionamiento. Config = Conexión con la database, Model = Creación de los modelos de tabla, Routers = Creación de las consultas, main = Todo lo necesario para que fastAPI funcione.

Se realizaron pruebas con las consultas. Durante el trabajo se ha usado tanto pymysql como sqlalchemy para la creación de las consultas, pero dado a que sqlalchemy posee una herramienta particular para el uso del localhost en docker, decanté por usar sqlalchemy a pesar de que la creación de consultas es disntinta y más tediosa que la de pymysql.

5. Docker

 A pesar de ser dos simples pasos generan diferentes complicaciones a la hora de generar una imagen, la estructura del directorio es fundamental para que el container funcione correctamente; para que se gestione la conexión con la base de datos correctamente es necesario modificar parametros que luego no permite su uso a nivel local (localhost). 
 
  En este sentido, quien vaya a utilizar este docker deberá indefectiblemente crear una base de datos en su mysql que debe llamarse proyectoind y levantar los archivos pelicula, genero y actor que se encuentra en el directorio de Datasets. Hecho eso el cointeiner creará la conexión con la base y devolverá el resultado de las querys.
 
6. Presentación Final

 Puedes observar todo el proceso que realicé en el siguiente video:
 
 
[[youtube-{16by9}-{oENQ5kqMzqo}]] 

 
 
 <p align="center">
<img src="https://gifimage.net/wp-content/uploads/2018/04/programacion-informatica-gif-2.gif"  height=400>
</p>
