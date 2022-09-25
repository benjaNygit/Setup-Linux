# Como instalar Qtile
Especificare como instalar qtile en Ubuntu.

Instalar dependencias:

El siguiente comando instalara las dependencias para ejecutar qtile.
Aunque los paquetes lightdm son un gestos de sesiones, debido a que gnome que viene con Ubuntu
da errores al ejecutar qtile.
~~~
sudo apt install xorg python3-xcffib python3-pip python3-cairocffi libcairo2 lightdm python3-psutil
~~~

Para cambiar de gestor de sesiones, por ejemplo usar lightdm.
~~~
dpkg-reconfigure lightdm
~~~
Para instalar qile, se usa pip. Ya que no esta en los repositorios de apt.
~~~
sudo pip3 install qtile
~~~
Ahora creamos la sesión de Qtile.
~~~
sudo bash -c 'cat > /usr/share/xsessions/qtile-venv.desktop <<EOF
[Desktop Entry]
Name=Qtile(venv)
Comment=Qtile Session Within Venv
Exec=/usr/local/bin/qtile start
Type=Application
Keywords=wm;tiling
EOF'
~~~
Finalmente, y solo si no funciona. Desisntalar gnome.
En mi caso gnome no se desistalo aunque ejecute este comando, dentro del entorno de gnome.
Pero fue la unica diferencia que me permitio hacer que funcione. Incluso uso el gestor de sesiones de gnome.
~~~
sudo apt purge ubuntu-desktop -y && sudo apt autoremove -y && sudo apt autoclean
~~~
---
## Distribución de teclado
Qtile no respetara la distribución de teclado del sistema.
Para solucionar esto ejecutar en terminal el iguiente comnado.
~~~
setxkbmap latam
~~~
Este comnado debe ser ejecutado cada vez que Qtile se inicie.
Lo bueno es que mi configuración trae un fragmento de codigo que ejecuta comandos
de una lista cada que Qtile se inicia.
