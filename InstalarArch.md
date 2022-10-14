# Documentación para instalar Arch Linux

Cambiar distribución de teclado.
~~~
loadkeys la-latin1
~~~
Conectarse a internet.
~~~
iwctl

device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect red
station wlan0 show
exit
~~~
Verificar si el sistema es UEFI o BIOS
~~~
# si lista es uefi, si no es bios
ls /sys/firmware/efi/efivars
~~~
Relog del sistema.
~~~
timedatectl status
timedatectl set-ntp true
~~~
Comandos para particiones.
~~~
# listar particiones
lsblk

# para formatear la particiones
mkfs.ext4 /dev/sdX1

# para swap
mkswap /dev/sdX2
swapon /dev/sdX2
~~~
Para montar las particiones.
~~~
# para la partición raiz /
mount /dev/sdXn /mnt

# crear ficheros para efi y home
mkdir /mnt/boot
mkdir /mnt/boot/efi
mkdir /mnt/home

# montar efi y home
mount /dev/sdXn /mnt/boot
mount /dev/sdXn /mnt/home
~~~
Instación. Esto instalara lo basico para el funcionamiento del sistema. Incluido el kernel.
~~~
pacstrap -K /mnt base base-devel linux linux-firmware linux-headers
~~~
Generar archivos fstab. Si este da error, las particiones estan mal montadas.
Para comprobar que este bien, listar /mnt/etc/fstab y compribar si lo que dice esta bien.
~~~
genfstab -U /mnt >> /mnt/etc/fstab
~~~
Cambiar al sistema o moverce dentro del sistema.
~~~
arch-chroot /mnt
~~~
## Instalación de paquetes.
~~~
# Como se instala.
pacman -S <paquete>
~~~
|Paquete|Función|
|-------|-------|
|networkmanager|Conección a internet, por consola.|
|neovim        |Editor de texto|
|ifplugd       |Conecta y desconecta de forma automatica internet en ethernet|
|openssh       |Conección entre computadoras de forma encriptada|
|xf86-input-synaptics|Habilita el touchpad de los notebooks|
|mkinitcpio    |Dependencia del paquete linux|
|sudo          |Paquete que permite ejecutar comandos en modo administrador|

Habilitar paquetes.
~~~
systemctl enable NetworkManager
systemctl enable sshd
~~~
Instalar estos paquetes para el arranque del sistema, ademas del dualbot.
~~~
pacman -S grub
pacman -S efibootmgr
pacman -S os-prober
~~~
Configuración del sistema.
~~~
# zona horaria
ln -sf /urs/share/zoneinfo/America/Santiago /etc/localtime

# generar archivo /etc/adjtime
hwclock --systohc

# idioma
# descomentar idiomas deceados.
nvim /etc/locale.gen
locale-gen
echo "LANG=es_ES.UTF-8" > /etc/locale.conf
echo "KEYMAP=la-latin1" > /etc/vconsole.conf

# nombre pc
echo "<nombrePC>" > /etc/hostname

nvim /etc/hosts
# escribir
127.0.0.1	localhost
::1		localhost
127.0.1.1	nombrePC.localdomain	nombrePC
~~~
Crear usuario.
~~~
# contraseña para root
passwd root

# crear user
useradd -m user
passwd user

# agregar a grupo sudo
usermod -aG sudo nombre

# O agregarlo manualmente en /etc/sudoers
# debajo de root
user ALL=(ALL) ALL
~~~
Grub Install.
~~~
grub-install --target=x86_64-efi --efi-directory=/boot/efi
grub-mkconfig -o /boot/grub/grub.cfg
~~~
Salir del area de montado
~~~
exit
~~~
Desmontar
~~~
umount -R /mnt
~~~
Reiniciar
~~~
reboot
~~~
Despues de reiniciar.
## Paquetes para herramientas graficas
|Paquete|Función|
|-------|-------|
|xorg            |Graficos|
|xorg-server     |Graficos|
|xorg-xinit       |Permite ejecutar comandos antes de iniciar el entorno grafico (~/.xprofile)|
|mesa            |Graficos|
|mesa-demos      |Graficos|
|xf86-video-vesa |
|xf86-video-intel|
|intel-ucode     |

Paquetes para el sistema.
|Paquete|Función|
|-------|-------|
|pulseaudio |Para tener audio|
|pavucontrol|Para controlar el volumen|
|pamixer    |
|picom      |Para transparencia|
|arandr     |Configurar multiples monitores|
## Instalación de Qtile
Dependencias.
~~~
# gestor de sesiones
sudo pacman -S lightdm lightdm-gtg-greeter

# configurar archivo /etc/lightdm/lightdm.conf
nvim /etc/lightdm/lightdm.conf

# editar linea greeter-session=
# y poner lightdm-gtk-greeter

# habilitar lightdm
sudo systemctl enable lightdm.service

# O usar gdm, el gestor de sesiones de gnome
sudo pacman -S gdm
systemctl enable gdm.service

# para configurar el entorno de gnome
sudo pacman -S gnome-control-center
sudo pacman -S gnome-tweak-tools
~~~
Instalar Qtile.
~~~
sudo pacman -S qtile

# terminal de qtile, aunque puedes instalar cualquiera en vez de esta.
sudo pacman -S xterm
sudo pacman -S alacritty
~~~

