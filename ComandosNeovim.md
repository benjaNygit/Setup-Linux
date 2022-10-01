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
|INSERT	|Desde modo insertar nos pasa a modo remplazar.
|r	|Modo remplazar para el caracter actual.
|R	|Modo remplazar desde la posición actual hasta el final de la linea.
|o	|Crea nueva linea debajo y en modo inserción.
|O	|Crea nueva linea arriba y en modo inserción.
|ESC	|Salir de cualquier modo al modo comando.
|x	|Borrar caracter actual.
|X	|Borrar caracter de la izquierda.
|dd	|Borrar linea actual.
|c	|Cambiar, borra y nos deja en modo inserción.
|c	|Cambiar linea, borra la linea y nos deja en modo inserción.
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

Para desplazarce avanzado.
|COMANDO|SIGNIFICADO|
|-------|-----------|
|w	|Nos posiciona al inicio de la proxima palabra.
|b	|Nos posiciona al inicio de la anterior palabra.
|e	|Nos posiciona al final de la proxima palabra.
|ge	|Nos posiciona al final de la anterior palabra.
|W	|Igual a w, pero más inteligente.
|B	|Igual a b, pero más inteligente.
|E	|Igual a e, pero más inteligente.
|gE	|Igual a ge, pero más inteligente.
|$	|Nos posiciona al final de la linea.
|0	|Nos posiciona al inicio de la linea.
|^	|Nos posiciona al inicio de la linea, sin tomar en cuenta espacios en blanco.
|{	|Nos posiciona en el anterior bloque de codigo o parrafo.
|}	|Nos posiciona en el siguiente bloque de codigo o parrafo.
|f..	|Busqueda hacia adelante del primer caracter ..
|F..	|Busqueda hacea atras del primer caracter ..
|t..	|Igual a f.. pero nos posiciona un caracter antes.
|T..	|Igual a F.. pero nos posiciona un caracter despues.
|%	|Nos posiciona en el par del {}, [], ().
|...G	|Nos posiciona en la linea ...
|gg	|Ir a la primera linea del documento.
|G	|Ir a la ultima linea del documento.
|...%	|Ir a al ... porciento del documento.
|CTRL+E	|Scroll de una linea hacia arriba.
|CTRL+Y	|Scroll de una linea hacia abajo.
|zz	|Scroll para posicionar cursor en la mitad de la pantalla, sin mover cursor.
|zt	|Scroll para posicionar cursor al principio de la panralla, sin mover cursor.
|zb	|Scroll para posicionar cursor al final de la pantalla, son mover cursor.
|H	|Posiciona cursor al principio de la pantalla.
|M	|Posiciona cursor al medio de la pantalla.
|L	|Posiciona cursor al final de la pantalla.

Comandos de uso comun que neovim simplifico.
|COMANDO|EQUIVALENTE|
|-------|-----------|
|x	|dl
|X	|dh
|D	|d$
|C	|c$
|s	|cl
|S	|cc

Copiar y pegar.
|COMANDO|EQUIVALENTE|
|-------|-----------|
|p	|Pegar, si es una linea entera se pega debajo de la linea actual.
|p	|Pegar, si es una porción de texto se pega a la derecha.
|P	|Igual a p, pero pega arriba.
|P	|Igual a p, pero pega a la izquierda.
|]p	|Pega con indentado.
|v	|Modo selección.
|V	|Modo selección solo para lineas.
|CTRL+v	|Modo selección en bloque.
|y	|Copiar texto seleccionado.
|yy	|Copia la linea actual.
|d,x,c	|Cortar.

Comandos para pestañas.
|COMANDO|EQUIVALENTE|
|-------|-----------|
|:tabnew|Crea una pestaña vacia.
|:tabedit ...	|Abre ... en una nueva pestaña.
|:tabclose	|Cierra la pestaña actual.
|:tabnext	|Saltar a la siguiente pestaña.
|:tabprev	|Saltar a la anterior pestaña.
|gt	|Saltar a la siguiente pestaña.
|gT	|Saltar a la anterior pestaña.
|:tabs	|Lista las pestañas abiertas.

Comandos para ventanas.
|COMANDO|EQUIVALENTE|
|-------|-----------|
|:split ...	|Partir la pantalla horizontalmente.
|:vsplit ...	|Partir la pantalla vertivalmente.
|:close	|Cerrar ventana actual.
|:only	|Hacer la ventana actual la unica.

Comandos para buffers
|COMANDO|EQUIVALENTE|
|-------|-----------|
|:buffers	|Ver listado de buffers abiertos.
|:buffer ..	|Abrir buffer numero ..
|:bn	|Ir al siguiente buffer.
|:bp	|Ir al buffer siguiente.
|:bt	|Ir al primer buffer.
|:bl	|Ir al ultimo buffer.
|:bd	|Cerrar buffer actual.

Comandos para pregado de codigo.
|COMANDO|EQUIVALENTE|
|-------|-----------|
|zf	|Plegar texto seleccionado.
|za	|Abrir plegado.
|zR	|Desplegar todos los pliegues del fichero.
|zd	|Eliminar pliegue.
|zE	|Eliminar todos los pliegues del fichero.
|zc	|Cerrar un pliegue.

