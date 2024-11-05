#!/bin/bash

# (cd "$HOME/.config/polybar/" && "$HOME/.dotfiles/scripts/rerun" "$HOME/.config/polybar/launch.sh") &

rem-accel () {
    xinput set-prop "$1" "libinput Accel Speed" -0.8
    xinput set-prop "$1" "libinput Accel Profile Enabled" 1 0 0
}

rem-accel "pointer:Logitech G304"
# rem-accel "pointer:Logitech ERGO M575"

