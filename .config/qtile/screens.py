# Screens or monitors

from libqtile import bar
from libqtile.config import Screen

from apps import home
from widgets import init_widgets, init_widgets_part, bar_color, bar_margin
from groups import group_names

screen_order    = [1, 0, 2]

# Init as center right left then swap left around
# should be:
# | *** | DEV | Window Name                       Upd:  45 | Mem:  53% | CPU:   3% | Doom | Up | Time | V |
screens = [
    Screen( # center
        top = bar.Bar(widgets = init_widgets(), size = 24, margin = bar_margin, background = bar_color, ),
        # wallpaper=home + '/.config/qtile/wallpapers/center.png', # girl in center
        wallpaper=home + '/.config/qtile/wallpapers/darker.png', # left.png none
        wallpaper_mode='stretch', ),
    Screen( # right
        top = bar.Bar(widgets = init_widgets_part(), size = 24, margin = bar_margin, background = bar_color, ),
        wallpaper=home + '/.config/qtile/wallpapers/darker.png', # gray_5.png girl on right
        wallpaper_mode='stretch', ),
    Screen( # left
        top = bar.Bar(widgets = init_widgets_part(), size = 24, margin = bar_margin, background = bar_color, ),
        wallpaper=home + '/.config/qtile/wallpapers/darker.png', # left.png none
        wallpaper_mode='fill', ),
]

