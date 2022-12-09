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
  
  Un tema no menor es la ruta usada para la importación de las librerias, dado un problema que comento más adelante con el VSC no he logrado usar la ruta generica para importar los datos, esto es Datasets/x.csv, ya que no me la detecta el sistema, es por eso que he debido usar la ruta completa de la ubicación en disco, y esto (a diferencia de lo creado en pycharm más adelante) no puede ser replicado en pycharm ya que en este IDE para poder editar y visualizar archivos ipynb se requiere una versión paga.
  
3. Consultas

 Las consultas fueron ejecutadas primero en MySQL, se encuentra en la carpeta ETL llamado consulta.sql, se pueden ejecutar y devolveran los valores solicitados. Esto se realizó a los fines de tener mayor facilidad de trasladar la consulta al entorno de fastAPI.
 
4. FastAPI 

Para el funcionamiento de fastAPI creé toda la estructura y los archivos necesarios para su funcionamiento. Config = Conexión con la database, Model = Creación de los modelos de tabla, Routers = Creación de las consultas, main = Todo lo necesario para que fastAPI funcione.

Se realizaron pruebas con las consultas. Durante el trabajo se ha usado tanto pymysql como sqlalchemy para la creación de las consultas, pero dado a que sqlalchemy posee una herramienta particular para el uso del localhost en docker, decanté por usar sqlalchemy a pesar de que la creación de consultas es disntinta y más tediosa que la de pymysql.

Tambien atravesé por problemas con el uso de Visual Studio Code, ya que el mismo no me generaba correctamente el entorno virtual, por lo que al hacer import de archivos .py no los reconocía y me devolvía el error "modulo name X not found", para solucionar esto directamente usé PyCharm que me genera el entorno virtual apenas inicio un proyecto, allí no tuve ningún problema de este tipo y pude gestionar los archivos de forma correcta.

5. Docker

 A pesar de ser dos simples pasos generan diferentes complicaciones a la hora de generar una imagen, la estructura del directorio es fundamental para que el container funcione correctamente; para que se gestione la conexión con la base de datos correctamente es necesario modificar parametros que luego no permite su uso a nivel local (localhost). 
 
  En este sentido, quien vaya a utilizar este docker deberá indefectiblemente crear una base de datos en su mysql que debe llamarse proyectoind y levantar los archivos pelicula, genero y actor que se encuentra en el directorio de Datasets. Hecho eso el cointeiner creará la conexión con la base y devolverá el resultado de las querys.
 
6. Presentación Final

 Puedes observar todo el proceso que realicé en el siguiente video:
 
  <p align="center">Haz clic en la siguiente imagen para ser redireccionado al video!!</p>
 <p align="center">
  
 <p align="center">
 <a href="http://www.youtube.com/watch?feature=player_embedded&v=oENQ5kqMzqo
" target="_blank"><img src="http://img.youtube.com/vi/oENQ5kqMzqo/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

</p>
 
 <p align="center">Gracias por tu atención.</p>
 <p align="center">
 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 TECNOLOGIAS USADAS
 - Pandas
 - Numpy
 - SQLAlchemy
 - MySQL
 - FastAPI
 - Docker
 
 Puedes ver más información sobre mí en el siguiente link: https://www.linkedin.com/in/rodriguezdatascience/
 
 <p align="center">
<img src="https://gifimage.net/wp-content/uploads/2018/04/programacion-informatica-gif-2.gif"  height=400>
</p>
