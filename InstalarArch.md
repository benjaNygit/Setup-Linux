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
mount /dev/sdX1 /mnt

# crear ficheros para efi y home
mkdir /mnt/boot
mkdir /mnt/boot/efi
mkdir /mnt/home

# montar efi y home
mount /dev/sdXn /mnt/boot
mount /dev/sdXn /mnt/home
~~~
Instación.
~~~
pacstrap /mnt base base-devel linux linux-firmware
~~~
Generar archivos fstab.
~~~
genfstab -U >> /mnt/etc/fstab
~~~
Cambiar al sistema o moverce dentro del sistema.
~~~
arch-chroot /mnt
~~~
Instalación de paquetes.
~~~
# internet
pacman -S networknanager
systemctl enable NetworkManagero

# paquetes
pacman -S neovim
pacman -S sudo
pacman -S ifplugd
pacman -S openssh
pacman -S xf86-input-synaptics
pacman -S linux-headers
pacman -S mkinitcpio
pacman -S grub
pacman -S efibootmgr
pacman -S os-prober

systemctl enable sshd
~~~
Configuración del sistema.
~~~
# zona horaria
ln -sf /urs/share/zoneinfo/America/Santiago /etc/localtime

# generar archivo /etc/adjtime
hwclock --systohc

# idioma
nvim /etc/locale.gen
touch /etc/locale.conf
LANG=es_ES.UTF-8 >> /etc/locale.conf
touch /etc/vconsole.conf
KEYMAP=la-latin1 >> /etc/vconsole.conf

# nombre pc
touch /etc/hostname
nombre >> /etc/hostname

nvim /etc/hosts
# escribir
127.0.0.1	localhost
::1		localhost
127.0.1.1	nombre.localdomain	nombre
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
~~~
# para herramientas graficas
sudo pacman -S xorg xorg-server xorg-init mesa mesa-demos
sudp pacman -S xf86-video-vesa
sudp pacman -S xf86-video-intel intel-ucode
~~~
Paquetes para el sistema.
~~~
# para audio
sudo pacman -S pulseaudio
sudo pacman -S pavucontrol
sudo pacman -S pamixer

# para trasnparencia
sudo pacman -S picom

# para multiples monitores
sudo pacman -S arandr
~~~
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
~~~
Instalar Qtile.
~~~
sudo pacman -S qtile

# terminal de qtile
sudo pacman -S xterm
~~~

