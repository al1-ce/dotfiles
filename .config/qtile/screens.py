# Screens or monitors

from libqtile import bar, hook
from libqtile.config import Screen

from apps import home
from widgets import init_widgets, init_widgets_part, bar_color, bar_margin

screen_order    = [1, 0, 2]

# Init as center right left then swap left around
# should be:
# | *** | DEV | Window Name                       Upd:  45 | Mem:  53% | CPU:   3% | Doom | Up | Time | V |
screens = [
    Screen( # center
        top = bar.Bar(widgets = init_widgets(), size = 24, margin = bar_margin, background = bar_color, ),
        # wallpaper=home + '/.config/qtile/wallpapers/center.png', # girl in center
        wallpaper=home + '/.config/qtile/wallpapers/left.png', # none
        wallpaper_mode='stretch', ),
    Screen( # right
        top = bar.Bar(widgets = init_widgets_part(), size = 24, margin = bar_margin, background = bar_color, ),
        wallpaper=home + '/.config/qtile/wallpapers/gray_5.png', # girl on right
        wallpaper_mode='stretch', ),
    Screen( # left
        top = bar.Bar(widgets = init_widgets_part(), size = 24, margin = bar_margin, background = bar_color, ),
        wallpaper=home + '/.config/qtile/wallpapers/left.png', # none
        wallpaper_mode='fill', ),
]

# @hook.subscribe.startup_complete
def set_screen_groups():
    # WWW SYS DEV
    # left center right = 1 0 2
    screens[0].cmd_toggle_group("SYS") # center
    # screens[1].cmd_toggle_group("WWW") # left
    screens[1].cmd_toggle_group("DEV") # right

@hook.subscribe.startup_once
def autostart():
    screens[0].cmd_toggle_group("SYS") # center
    # screens[1].cmd_toggle_group("WWW") # left
    screens[1].cmd_toggle_group("DEV") # right

    # subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    # set_screen_groups()

