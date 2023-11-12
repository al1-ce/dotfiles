#!/bin/bash

echo-blue () {
    echo -e "\e[34m\e[1m$1\e[0m"
}

echo-red () {
    echo -e "\e[31m\e[1m$1\e[0m"
}

if [ "$(id -u)" = 0 ]; then
    echo-red "## This script MUST NOT be run as root user since it makes changes ##"
    echo-red "## to the \$HOME directory of the \$USER executing this script.    ##"
    exit 1
fi

echo-blue "## Script now will begin installation of AtheOS ##"
echo " "
echo-red "## Please be nearby since script might need your input or in case of any ##"
echo-red "## errors that will come up. Also note that you will be required to      ##"
echo-red "## enter your sudo password for some operations.                         ##"

while true; do
    read -p "Do you want to continue? [y/N]" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
    esac
    exit;
done


echo-blue "## Syncing repos ##"

echo -e "[multilib]\nInclude = /etc/pacman.d/mirrorlist" | sudo tee -a /etc/pacman.conf > /dev/null
sudo pacman -Syu --noconfirm

echo-blue "## Enabling AUR and installing PKM with YAY ##"

sudo pacman -S --needed git base-devel --noconfirm
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay

echo-blue "## Configuring YAY for first use ##"

yay -Y --gendb --nodiffmenu --noeditmenu --nouseask --nocleanmenu
yay -Syu --devel --nodiffmenu --noeditmenu --nouseask --nocleanmenu
yay -Y --devel --combinedupgrade --batchinstall --save --nodiffmenu --noeditmenu --nouseask --nocleanmenu
sudo cp etcfiles/pacman.conf /etc/pacman.con

echo-blue "## Installing official repo and aur packages from pkglist ##"

sudo pacman -S --needed xorg
yay -S --needed $(awk '!/^ *#/ && NF' pkglist.conf) --nodiffmenu --noeditmenu --nouseask --nocleanmenu

echo-blue "## Installing packages from other sources ##"

python -m ensurepip
# pip install --user streamdeck_ui
# pip install psutil
# pip install ewmh
# pip install fuzzywuzzy
# pip install uptime
# pip install xcffib
# pip install --no-cache-dir cairocffi

# pip install powerline-shell

echo-blue "## Enabling systemctl services ##"

sudo systemctl enable bluetooth.service
sudo systemctl enable dbus.service
sudo systemctl enable greetd.service
sudo systemctl enable polkit.service
sudo systemctl enable touchegg.service
sudo systemctl enable pipewire
sudo systemctl enable pipewire-pulse
sudo systemctl enable wireplumber
sudo systemctl enable opentabletdriver

# echo-blue "## Copying scripts ##"
#
# mkdir -p ~/.local/bin
# cp -r ~/.dotfiles/scripts ~/.local/bin

echo-blue "## Configuring git ##"

git config --global init.defaultBranch master

echo-blue "## Copying configuration files ##"

yadm clone https://github.com/al1-ce/dotfiles.git

sudo cp -rT ~/.dotfiles/rice/etc/$1 /etc/$1

echo-blue "## Installation complete ##"

while true; do
    read -p "Do you want to reboot? [y/n]" yn
    case $yn in
        [Yy]* ) shutdown -r 0; break;;
        [Nn]* ) source ~/.bashrc; exit;;
    esac
done
