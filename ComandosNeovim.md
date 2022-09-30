# Apuntes sobre los comandos de NeoVim
Listado de comandos para usar en el modo comando.

Para desplazarce y editar ficheros.
|COMANDO|SIGNIFICADO|
|-------|-----------|
|h	|Mover cursor a la izquierda.
|l	|Mover cursor a la derecha.
|j	|Mover cursor hacia abajo.
|k	|Mover cursor hacia arriba.
|i	|Modo inserción en la posición actual.
|a	|Modo inserción en la siguiente posición.
|A	|Modo inserción al final de la linea.
|o	|Crea nueva linea debajo y en modo inserción.
|O	|Crea nueva linea arriba y en modo inserción.
|ESC	|Salir de cualquier modo al modo comando.
|x	|Borrar caracter actual.
|X	|Borrar caracter de la izquierda.
|dd	|Borrar linea actual.
|D	|Borrar desde posición actual hasta final de la linea.
|J	|Junta linea actual con la siguiente.
|u	|Deshacer acción.
|CTRL+R	|Rehacer acción.

Manipulación de ficheros.
|COMANDO|SIGNIFICADO|
|-------|-----------|
|:w	|Grabar los cambios.
|:w ...	|Grabar como ...
|:q	|Salir
|:q!	|Salir sin grabar.
|ZZ	|Salir y grabar los cambios.
|:x	|Salir y grabar los cambios.
|:wq!	|Salir y grabar los cambios.
|:e ...	|Abrir fichero.

Moverce entre ficheros abiertos.
|COMANDO|SIGNIFICADO|
|-------|-----------|
|:bn	|Siguiente fichero.
|:bp	|Anterior fichero.
|:bd	|Cerrar fichero actual.

