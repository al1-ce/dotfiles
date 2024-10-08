#!/usr/bin/env sh

# More info : https://github.com/jaagr/polybar/wiki

# Install the following applications for polybar and icons in polybar if you are on ArcoLinuxD
# yaourt -S polybar awesome-terminal-fonts
# Tip : There are other interesting fonts that provide icons like nerd-fonts-complete

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done

if type "xrandr" > /dev/null; then
    for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
        if [ $m = "DP-2" ]; then
            MONITOR=$m polybar --reload main -c ~/.config/polybar/config.ini & disown
        else
            MONITOR=$m polybar --reload side -c ~/.config/polybar/config.ini & disown
        fi
    done
else
    polybar --reload mainbar-qtile  -c ~/.config/polybar/config.ini & disown
fi

