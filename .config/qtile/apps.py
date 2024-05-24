# Apps for use with keymap.py

import os
from libqtile.utils import guess_terminal

def is_tool(name):
    # Check whether `name` is on PATH and marked as executable
    # from whichcraft import which
    from shutil import which
    return which(name) is not None

terminal        = guess_terminal()
terminal_exec   = terminal
term_exec       = terminal + " -x bash -c \""
term_wait       = " && read -p '' -n1 -s\""
term_end        = "\""
# if (is_tool("kitty")):
#     terminal      = "kitty"
#     terminal_exec = "kitty"
#     term_exec     = terminal_exec + " bash -c \""
if (is_tool("wezterm")):
    terminal      = "wezterm"
    terminal_exec = "wezterm -e"
    term_exec     = terminal_exec + " bash -c \""

# Makes qtile win the resizing race
def unrace_exec(cmd):
    # 0.2 seems to be smallest value to allow stuff to resize correctly
    return terminal_exec + " -- sh -c 'sleep 0.2 && " + cmd + "'"

home            = os.path.expanduser('~')
dotfiles        = home + "/.dotfiles"
altbrowser      = "vivaldi-stable"
mybrowser       = "qutebrowser"
spawnshortcuts  = "qutebrowser --target private-window -R " + dotfiles + "/.shortcuts.html"
filemanager     = unrace_exec("ranger")
filemanager_gui = "nemo"
editor          = unrace_exec("nvim")
editor_gui      = "code"
process_explr   = unrace_exec("btop")
osc_draw        = "gromit-mpx"
music_player    = unrace_exec("musikcube")

rofi_launcher   = "rofi -show drun"     # Run apps (.desktop)
rofi_run        = "rofi -show run" # Run bin
rofi_window     = "rofi -show window" # All screens
rofi_windowcd   = "rofi -show windowcd" # Current screen
# rofi_launcher   = home + "/.config/rofi/launchers/type-4/launcher.sh"     # Run apps (.desktop)
rofi_powermenu  = home + "/.config/rofi/powermenu/type-1/powermenu.sh"    # Power menu
# rofi_run        = home + "/.config/rofi/launchers/type-4/launcher-run.sh" # Run bin
# rofi_window     = home + "/.config/rofi/launchers/type-4/launcher-win.sh" # All screens
# rofi_windowcd   = home + "/.config/rofi/launchers/type-4/launcher-wcd.sh" # Current screen
rofi_websearch  = home + "/.config/rofi/applets/rofi-search.sh"
rofi_pass       = home + "/.dotfiles/bin/pass-rofi-gui"

# rofi_launcher = "rofi -show drun" # Run apps (.desktop)
# rofi_power_menu = "rofi -show power-menu -modi \"power-menu:rofi-power-menu --no-symbols\"" # Power menu
# rofi_run = "rofi -show run" # Run bin
# rofi_window = "rofi -show window" # All screens
# rofi_windowcd = "rofi -show windowcd" # Current screen
# rofi_websearch = ""

tabletscript = dotfiles + "/scripts/maptotablet.sh"
touchsscript = dotfiles + "/scripts/maptotouchs.sh"

