#!/bin/bash

copyEtc() {
    echo "Copying /etc/$1"
    sudo cp -rT $HOME/.dotfiles/rice/etc/$1 /etc/$1
}

copyEtcFile() {
    echo "Copying /etc/$1"
    sudo cp $HOME/.dotfiles/rice/etc/$1 /etc/$1
}

copyEtc greetd
copyEtc zsh

copyEtcFile pacman.conf

echo "Copying X config to $HOME"

cp $HOME/.dotfiles/rice/xconfig/.xprofile $HOME/.xprofile
cp $HOME/.dotfiles/rice/xconfig/.xexec $HOME/.xexec

echo "Successfully finished"

