# Extensiones para Gnome
Gnome es un entorno de escritorio que viene por defecto con Ubuntu.
A gnome no le gusta que su escritorio sea configurable mas alla de lo que
los desarrolladores quieren.
La comunidad crea extensiones burlando esto y haciendo mas bonito y practico el
escritorio mismo.

Listado de extensiones.
- OpnenWeater
- Caffeine
- Place Status Indicator
- User Themes
- Vitals

Comando para instalar las extensiones.
~~~
gnome-extensions install extension.zip
~~~
Para que gnome reconosca las extensiones despues de instalarlas se
debe cerrar la session.

Para habilitar las extensiones instaladas, se hace atraves de su id.
El cual es muy parecido a una dirección de correo electronico.

Para listar las extensiones de gnome instaladas.
~~~
gnome-extensions list
~~~
Para habilitar la extensión.
~~~
gnome-extensions enable id
~~~
Para instalar la herramienta para administrar las extensiones.
~~~
sudo apt install gnome-shell-extensions
~~~

