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

numlockx &
xfsettingsd &
dunst &
picom &
polkit-dumb-agent &
pasystray &
powerkit &
blueman-applet &
blueman-tray &
yandex-disk start &
yandex-disk-indicator &
# streamdeck --no-ui &
unclutter --timeout 2147483647 --hide-on-touch -b &
start-pulseaudio-x11 &
companion &
gromit-mpx &
# xinput create-master "Touh"
# xinput reattach "Melfas LGDisplay Incell Touch" "Touch pointer"
xinput map-to-output "Melfas LGDisplay Incell Touch" DP-0
systemctl --user enable opentabletdriver --now

exec qtile start
