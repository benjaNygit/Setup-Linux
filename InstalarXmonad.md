# Instalar xmonad

sudo pacman -S xmonad xmonad-contrib xmobar trayer xdotool
sudo pacman -S pacman-contrib brightnessctl pamixer upower

Poner esto en .xprofile
export PATH=$HOME/.local/bin:$PATH

colocar los archivos que estan en .local/bin en el sistema.

para compilar xmonad escribir
xmonad --recompile
