# Setup-Linux
Este repositorio contiene información y configuraciones que uso personalmente para mis entornos UNIX.

El proposito de guardar esto en la nube, es el de poder replicar mi Setup de linux para cualquier
dispositivo en el cual no necesite.

## Paquetes
Un listado de los paquetes instalas atraves del gestor de paquetes de Ubuntu apk.
+ neofetch
+ pip
+ figlet
+ htop
+ tree
+ neovim
+ default-jre
+ openjdk-8-jre-headless
+ curl
+ nodejs
+ ranger
+ npm
+ yarn
+ glow
+ tmux

Para usar la clipbord se instalan dos paquetes.
+ xclip
+ xsel

## Versiones de los paquetes
Algunos paquetes requieren de sierta versión para ser parte del setup.
+ node => 16.16.0
+ neovim => 0.7.0

### Como instalar node
Este paquete en Ubuntu esta desactualizado, por lo que para instalar una version mas nueva
se debe hacer diferente.

Primero ejecutamos este comando para instalar nvm.
~~~
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
~~~
Luego permitimos su uso para nuestro usuario.
~~~
source ~/.profile
~~~
Mostramos todas las versiones de node disponibles.
~~~
nvm ls-remote
~~~
Inslatamos la version que queramos.
~~~
nvm install 16.17.1
~~~
Para desinstalar node primero desactivalo, luego desinstala.
~~~
nvm deactivate
nvm uninstall v16.17.1
~~~
## Comandos para generar ssh en github
Los siguientes pasos son para generar el token que se conecta con github para no colocar
la contraseña cada vez que se interactue con el repositior en la nube.

Para generar el token.
~~~
ssh-keygen -t rsa -b 4096 -C "correo"
~~~
Pedira una ruta, precionar enter sin colocar nada.
Luego pedira una contraseña, se puede dejar vacio, pero debes recordar la contraseña de poner una.

Comando para verificar que todo va bien.
~~~
eval $(ssh-agent -s)
~~~
Mostrara como resultado si todo esta bien *Agent pid "y un numero"*.

Finalmente para que el token funcione, aparte de colocar la clave publica el github.
~~~
ssh-add ~/.ssh/id_rsa
~~~

## Terminal
Para Ubuntu uso la terminal kitty.

Para Windows uso la terminal de Ubuntu que se instala por la tienda.

Yo configuro mi terminal atraves del archivo .bashrc

Para los los alias creo el archivo .bash_alias que puedes encontrar en este repositorio.
Para usarlos debes editar el .bashrc, agregando el siguiente codigo:

~~~
if [ -f ~/.bash_alias ]; then
    . ~/.bash_alias
fi
~~~

Para personalizar la apariencia del bash, se modifica el .bashrc cambiando el PS1.
Esta parte del codigo se encuentra como por la linea 60.
~~~

if [ "$color_prompt" = yes ]; then
     PS1='\[\e[0;1;91m\]\u\[\e[0;1m\]@\[\e[0;3m\]\H\[\e[0;1;91m\]:\[\e[0;1m\][\[\e[0;2m\]\j\[\e[0;1m\]]\[\e[0;34m\]\w\[\e[0;1m\](\[\e[0;4;93m\]$(git branch 2>/dev/null | grep '"'"'^*'"'"' | colrm 1 2)\[\e[0;1m\])\n\[\e[0;1;91m\]$\[\e[0m \]'
    # PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
~~~

Para la terminal kitty y el paquete tmux con la configuracion anterior.
Se debe hacer un cambio un poco mas arriba.


Este codigo activa la condicion de para usar el PS1 modificado, pero lo hace atraves de una
variable de entorno. En kitty y tmux el valor de la variable cambio.

Puede verse el valor de TERM por cada terminal con el siguiente comando.
~~~
echo $TERM
~~~

Quitar xterm-kitty si no se usa esta terminal.
~~~
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color|xterm-kitty|screen) color_prompt=yes;;
esac
~~~
## Tmux
Este paquete tiene su propia configuración. En el archivo .tmux.conf y va en ~.

Para usar la configuracion de tmux es necesario instalar un repositorio para usar plugins.

~~~
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
~~~
Luego precionar control + z + I. En mi caso cambie la teca Leader de tmux.

Lista de plugins para tmux
--------------------------
+ [tmux-battery](https://github.com/tmux-plugins/tmux-battery)
+ [tmux-cpu](https://github.com/tmux-plugins/tmux-cpu)
+ [tmux-online-stattus](https://github.com/tmux-plugins/tmux-online-status)


