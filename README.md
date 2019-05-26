# NoSQL-finalProject-
Proyecto final de la clase "Bases de datos NoSQL" 

## Agregar datos a Mongo

Después de clonar el repositorio y acceder a la carpeta del proyecto se puede correr la siguiente línea desde la consola para importar los datos a la colección `rates` en la base de datos `suicides`.

~~~ Bash
mongoimport -d suicides -c rates --type csv --file "suicide_rates.csv" --headerline 
~~~


En caso de utilizar una base de datos con autenticación:

~~~ Bash
mongoimport -u Usuario -p Password --authenticationDatabase admin \
-d suicides -c rates --type csv --file "suicide_rates.csv" --headerline 
~~~

Cambiar Usuario y Password por los datos correspondientes de un usuario válido de la base de datos.
