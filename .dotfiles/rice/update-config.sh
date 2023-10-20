#!/bin/bash
copyEtc() {
    echo "Copying /etc/$1"
    rm -rf ~/.dotfiles/rice/etc/$1
    cp -rT /etc/$1 ~/.dotfiles/rice/etc/$1
}

copyEtcFile() {
    echo "Copying /etc/$1"
    rm -f ~/.dotfiles/rice/etc/$1
    cp /etc/$1 ~/.dotfiles/rice/etc/$1
}

copyEtc greetd

copyEtcFile pacman.conf


