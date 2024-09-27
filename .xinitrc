#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# twm &
# xclock -geometry 50x50-1+1 &
# xterm -geometry 80x50+494+51 &
# xterm -geometry 80x20+494-0 &
# exec xterm -geometry 80x66+0+0 -name login

# # TODO: put in other place
# xinput create-master "Touh"
# xinput reattach "Melfas LGDisplay Incell Touch" "Touch pointer"
# xinput map-to-output "Melfas LGDisplay Incell Touch" DP-0
# systemctl --user enable opentabletdriver --now

# ~/.screenlayout/main.sh

numlockx &
xsettingsd &
dunst &
picom &
pasystray &
powerkit &
blueman-applet &
blueman-tray &
yandex-disk start &
yandex-disk-indicator &
lxpolkit &
unclutter --timeout 2147483647 --hide-on-touch -b &
# start-pulseaudio-x13 &

# Make sure this is before the 'exec' command or it won't be sourced.
[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

[ -f ~/.xexec ] && . ~/.xexec

