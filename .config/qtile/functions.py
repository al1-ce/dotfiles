# Functions for keybinds
import subprocess

from libqtile.lazy import lazy

from widgets import widget_volume

@lazy.function
def increase_vol(qtile):
    widget_volume.cmd_increase_vol()

@lazy.function
def decrease_vol(qtile):
    widget_volume.cmd_decrease_vol()

@lazy.function
def mute_vol(qtile):
    widget_volume.cmd_mute()

@lazy.function
def getwmclass(qtile):
    subprocess.run("notify-send \"$(xprop WM_CLASS)\"", shell=True)

@lazy.function
def getwmtitle(qtile):
    subprocess.run("notify-send \"$(xprop WM_NAME)\"", shell=True)
