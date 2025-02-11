#!/bin/bash
copyEtc() {
    echo "Copying /etc/$1"
    cp -rT ~/.dotfiles/rice/etc/$1 /etc/$1
}

copyEtcFile() {
    echo "Copying /etc/$1"
    cp ~/.dotfiles/rice/etc/$1 /etc/$1
}

copyEtc greetd
copyEtc zsh

copyEtcFile pacman.conf

echo "Copying X config to $HOME"

cp ~/.dotfiles/rice/xconfig/.xprofile ~/.xprofile
cp ~/.dotfiles/rice/xconfig/.xexec ~/.xexec

echo "Successfully finished"

