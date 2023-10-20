
import os
import subprocess
import datetime
import re

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, KeyChord
from libqtile.config import Screen, EzKey, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from uptime import uptime

# ---------------------------------------------------------------------------- #
#                                   APP GUESS                                  #
# ---------------------------------------------------------------------------- #
def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    # from whichcraft import which
    from shutil import which
    return which(name) is not None

terminal = guess_terminal()
terminal_exec = terminal
if (is_tool("kitty")):
    terminal = "kitty"
    terminal_exec = "kitty"
# if (is_tool("alacritty")): # Until i figure out how to add touch support to kitty
#     terminal = "alacritty"
#     terminal_exec = "alacritty -e"

home = os.path.expanduser('~')
dotfiles = home + "/.dotfiles"
mod = "mod4"
altbrowser = "vivaldi-stable"
mybrowser = "qutebrowser"
spawnshortcuts = "qutebrowser --target private-window -R " + dotfiles + "/.shortcuts.html";
filemanager = terminal_exec + " ranger"
filemanager_gui = "nemo"
editor = terminal_exec + " nvim"
editor_gui = "code"
process_explr = terminal_exec + " btop"

screen_order = [1, 0, 2]

rofi_launcher = home + "/.config/rofi/launchers/type-4/launcher.sh" # Run apps (.desktop)
rofi_powermenu = home + "/.config/rofi/powermenu/type-1/powermenu.sh" # Power menu
rofi_run = home + "/.config/rofi/launchers/type-4/launcher-run.sh" # Run bin
rofi_window =  home + "/.config/rofi/launchers/type-4/launcher-win.sh" # All screens
rofi_windowcd =  home + "/.config/rofi/launchers/type-4/launcher-wcd.sh" # Current screen
rofi_websearch = home + "/.config/rofi/applets/rofi-search.sh"
#
# rofi_launcher = "rofi -show drun" # Run apps (.desktop)
# rofi_power_menu = "rofi -show power-menu -modi \"power-menu:rofi-power-menu --no-symbols\"" # Power menu
# rofi_run = "rofi -show run" # Run bin
# rofi_window = "rofi -show window" # All screens
# rofi_windowcd = "rofi -show windowcd" # Current screen
# rofi_websearch = ""

# ---------------------------------------------------------------------------- #
#                                 SCREEN SWITCH                                #
# ---------------------------------------------------------------------------- #

def switch_screens(target_screen):
    '''Send the current group to the other screen.'''
    @lazy.function
    def _inner(qtile):
        current_group = qtile.screens[1 - target_screen].group
        qtile.screens[target_screen].setGroup(current_group)

    return _inner


def focus_or_switch(group_name):
    '''
    Focus the selected group on the current screen or switch to the other
    screen if the group is currently active there
    '''
    @lazy.function
    def _inner(qtile):
        # Check what groups are currently active
        groups = [s.group.name for s in qtile.screens]

        try:
            # Jump to that screen if we are active
            index = groups.index(group_name)
            qtile.toScreen(index)
        except ValueError:
            # We're not active so pull the group to the current screen
            qtile.currentScreen.setGroup(qtile.groupMap[group_name])

    return _inner

# ---------------------------------------------------------------------------- #
#                                LAZY FUNCTIONS                                #
# ---------------------------------------------------------------------------- #

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

# ---------------------------------------------------------------------------- #
#                                     ICONS                                    #
# ---------------------------------------------------------------------------- #

# https://pictogrammers.github.io/@mdi/font/6.9.96/
icons = {
    "group_www": "󰋙", # mdi-hexagon-outline
    "group_sys": "󰞷", # mdi-console-line
    "group_dev": "󰅪", # mdi-code-brackets
    "group_doc": "󰧮", # mdi-file-document-outline
    "group_vbx": "󰍹", # mdi-monitor
    "group_cht": "󰍪", # mdi-message-text-outline
    "group_mus": "󰲸", # mdi-playlist-music
    "group_vid": "󰯜", # mdi-video-outline
    "group_gfx": "󰌨", # mdi-layers

    "update": "󰑓", # mdi-reload
    "disk": "󰉉", # mdi-floppy
    "ram": "󰓡", # mdi-swap-horizontal
    "cpu": "󰍛", # mdi-memory
    "volume": "󰕾", # mdi-volume-high
    "uptime": "󰔛", # mdi-timer-outline
    "doomsday": "󰯈", # mdi-skull-outline
    "calendar": "󰸗", # mdi-calendar-month
    "clock": "󱑏", # mdi-clock-time-five-outline

    # "screen_focus": "󰍹", # mdi-monitor
    # "screen_nofocus": "󰶐", # mdi-monitor-off
    "screen_focus": "󰞯", # mdi-chart-donut
    "screen_nofocus": "󰞯", # mdi-chart-donut
    }

# ---------------------------------------------------------------------------- #
#                                    GROUPS                                    #
# ---------------------------------------------------------------------------- #

groups = [
    Group("WWW", label = icons["group_www"], layout="columns"),
    Group("SYS", label = icons["group_sys"], layout="columns"),
    Group("DEV", label = icons["group_dev"], layout="columns"),
    Group("DOC", label = icons["group_doc"], layout="columns"),
    Group("VBX", label = icons["group_vbx"], layout="columns"),
    Group("CHT", label = icons["group_cht"], layout="columns"),
    Group("MUS", label = icons["group_mus"], layout="columns"),
    Group("VID", label = icons["group_vid"], layout="columns"),
    Group("GFX", label = icons["group_gfx"], layout="columns"),
    ScratchPad("scratchpad", [ 
        DropDown("term", "kitty -T QuakeTerminal", 
            match=Match(title="QuakeTerminal"), width=1, x=0, height=0.45, on_focus_lost_hide=True
            ),
        ])
    ]
    

# ---------------------------------------------------------------------------- #
#                                   KEYBINDS                                   #
# ---------------------------------------------------------------------------- #

tabletscript = dotfiles + "/scripts/maptotablet.sh"
touchsscript = dotfiles + "/scripts/maptotouchs.sh"

# qtile actually has an emacs style `EzKey` helper that makes specifying
# key bindings a lot nicer than the default.
#
# Keys follow some "logic"
# meta - movement, change layout and app spawn
# meta + shift - move windows and alt versions of meta keys
# meta + alt - group movement
# meta + ctrl - change window size
# meta + ctrl + alt - qtile extremes so no accidents
#
keys = [EzKey(k[0], *k[1:]) for k in [
    # Navigation
    # Swtich focus between panes
    ("M-<Left>", lazy.layout.left()),
    ("M-<Down>", lazy.layout.down()),
    ("M-<Up>", lazy.layout.up()),
    ("M-<Right>", lazy.layout.right()),

    ("M-h", lazy.layout.left()),
    ("M-j", lazy.layout.down()),
    ("M-k", lazy.layout.up()),
    ("M-l", lazy.layout.right()),

    # Swap panes: target relative to active.
    ("M-S-<Left>", lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    ("M-S-<Down>", lazy.layout.shuffle_down(), lazy.layout.section_down()),
    ("M-S-<Up>", lazy.layout.shuffle_up(), lazy.layout.section_up()),
    ("M-S-<Right>", lazy.layout.shuffle_right(), lazy.layout.swap_right()),

    ("M-S-h", lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    ("M-S-j", lazy.layout.shuffle_down(), lazy.layout.section_down()),
    ("M-S-k", lazy.layout.shuffle_up(), lazy.layout.section_up()),
    ("M-S-l", lazy.layout.shuffle_right(), lazy.layout.swap_right()),

    # Grow/shrink the main the focused window
    ("M-C-<Left>", lazy.layout.grow_left(), lazy.layout.shrink()),
    ("M-C-<Down>", lazy.layout.grow_down()),
    ("M-C-<Up>", lazy.layout.grow_up()),
    ("M-C-<Right>", lazy.layout.grow_right(), lazy.layout.grow()),

    ("M-C-h", lazy.layout.grow_left(), lazy.layout.shrink()),
    ("M-C-j", lazy.layout.grow_down()),
    ("M-C-k", lazy.layout.grow_up()),
    ("M-C-l", lazy.layout.grow_right(), lazy.layout.grow()),

    ("M-<bracketleft>", lazy.layout.decrease_nmaster()),
    ("M-<bracketright>", lazy.layout.increase_nmaster()),

    # TODO meta alt
    ##Switch focus between two screens
    ("M-A-h", lazy.screen.prev_group()),
    ("M-A-l", lazy.screen.next_group()),
    ("M-A-S-<Left>", lazy.screen.prev_group()),
    ("M-A-S-<Right>", lazy.screen.next_group()),
    #("M-A-<Left>", lazy.to_screen(1)),
    # ("M-A-<Left>", lazy.prev_screen()),
    # ("M-A-<Right>", lazy.next_screen()),
    ("M-A-1", lazy.to_screen(screen_order[0])),
    ("M-A-2", lazy.to_screen(screen_order[1])),
    ("M-A-3", lazy.to_screen(screen_order[2])),
    ("M-A-<Left>", lazy.to_screen(screen_order[0])),
    ("M-A-<Down>", lazy.to_screen(screen_order[1])),
    ("M-A-<Up>", lazy.to_screen(screen_order[1])),
    ("M-A-<Right>", lazy.to_screen(screen_order[2])),
    ("M-A-j", lazy.prev_screen()),
    ("M-A-k", lazy.next_screen()),
    ##Move the focused group to one of the screens and follow it
    #("M-S-<bracketleft>", switch_screens(0), lazy.to_screen(0)),
    #("M-S-<bracketright>", switch_screens(1), lazy.to_screen(1)),

    # Layouts
    ("M-<backslash>", lazy.next_layout()),
    ("M-S-<backslash>", lazy.prev_layout()),
    ("M-r", lazy.layout.rotate(), lazy.layout.flip(), lazy.layout.spaw_column_left(), lazy.layout.spaw_column_right()),
    #("M-S-r", lazy.layout.flip()),
    ("M-<space>", lazy.layout.toggle_split()),
    #("M-f", lazy.prev_layout()),
    #("M-f", lazy.prev_layout()),

    # Applications
    ("M-<Return>", lazy.spawn(terminal)),
    ("M-S-<Return>", lazy.group['scratchpad'].dropdown_toggle("term")),
    ("M-e", lazy.spawn(filemanager)),
    ("M-S-e", lazy.spawn(filemanager_gui)),
    ("M-w", lazy.spawn(mybrowser)),
    ("M-S-w", lazy.spawn(altbrowser)),
    ("<Print>", lazy.spawn("flameshot gui")),
    ("S-<Print>", lazy.spawn("peek")),
    ("M-v", lazy.spawn(editor)),
    ("M-S-v", lazy.spawn(editor_gui)),
    ("M-p", lazy.spawn("gpick")),
    
    ("M-t", lazy.spawn(process_explr)),
    ("M-A-t", lazy.spawn("/bin/bash -c '" + tabletscript +"'")),
    ("M-S-t", lazy.spawn("/bin/bash -c '" + touchsscript +"'")),

    # Rofi
    ("M-<grave>", lazy.spawn(rofi_launcher)),
    ("M-S-<grave>", lazy.spawn(rofi_run)),
    ("M-C-<grave>", lazy.spawn(rofi_websearch)),
    ("M-A-<grave>", lazy.spawn(rofi_powermenu)),
    ("M-<Tab>", lazy.spawn(rofi_windowcd)),
    ("M-S-<Tab>", lazy.spawn(rofi_window)),


    # Check keys
    ("M-<slash>", getwmclass),
    ("M-S-<slash>", getwmtitle),

    # Windows
    ("M-f", lazy.window.toggle_floating()),
    ("M-q", lazy.window.kill()),
    ("M-A-r", lazy.reload_config()),
    ("M-A-C-r", lazy.restart()),
    ("M-A-C-q", lazy.shutdown()),
    ("M-<Page_Down>", lazy.spawn("Qminimize -m")),
    ("M-S-<Page_Down>", lazy.spawn("Qminimize -u")),
    ("M-<Page_Up>", lazy.window.toggle_fullscreen()),
    ("M-S-<Page_Up>", lazy.layout.maximize()),
    # Shut down qtile.
    ("M-n", lazy.layout.normalize()),
    ("M-s", lazy.spawn(spawnshortcuts)),

    # Change the volume if your keyboard has special volume keys.
    ("<XF86AudioRaiseVolume>", increase_vol),
    ("<XF86AudioLowerVolume>", decrease_vol),
    ("<XF86AudioMute>", mute_vol),
    ("<XF86AudioPlay>", lazy.spawn("playerctl play-pause")),
    ("<XF86AudioPause>", lazy.spawn("playerctl play-pause")),
]]


keys += [

    # Umlauts
    KeyChord([mod], "semicolon", [
        Key(["shift"], "a", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+adiaeresis'")),
        Key(["shift"], "o", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+odiaeresis'")),
        Key(["shift"], "u", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+udiaeresis'")),
        Key(["shift"], "s", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+ssharp'")),

        Key([], "a", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key adiaeresis'")),
        Key([], "o", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key odiaeresis'")),
        Key([], "u", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key udiaeresis'")),
        Key([], "s", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key ssharp'")),
    ]),

    # Monitors
    # KeyChord([mod, "shift"], "m", [
    #     KeyChord([], "l", [
    #         Key([], "n", lazy.spawn("/bin/bash -c '" + tabletscript + " normal'")),
    #         Key([], "l", lazy.spawn("/bin/bash -c '" + tabletscript + " left'")),
    #         Key([], "r", lazy.spawn("/bin/bash -c '" + tabletscript + " right'")),
    #         Key([], "i", lazy.spawn("/bin/bash -c '" + tabletscript + " inverted'")),
    #     ]),
    #     KeyChord([], "r", [
    #         Key([], "n", lazy.spawn("xrandr --output DP-3 --rotate normal")),
    #         Key([], "l", lazy.spawn("xrandr --output DP-3 --rotate left")),
    #         Key([], "r", lazy.spawn("xrandr --output DP-3 --rotate right")),
    #         Key([], "i", lazy.spawn("xrandr --output DP-3 --rotate inverted")),
    #     ]),
    #     KeyChord([], "m", [
    #         Key([], "n", lazy.spawn("xrandr --output DP-0 --rotate normal")),
    #         Key([], "l", lazy.spawn("xrandr --output DP-0 --rotate left")),
    #         Key([], "r", lazy.spawn("xrandr --output DP-0 --rotate right")),
    #         Key([], "i", lazy.spawn("xrandr --output DP-0 --rotate inverted")),
    #     ]),
    # ]),
]

# .: Jump between groups and also throw windows to groups :. #
for _ix, group in enumerate(groups[:9]):
    # Index from 1-0 instead of 0-9
    ix = 0 if _ix == 9 else _ix + 1

    keys.extend([EzKey(k[0], *k[1:]) for k in [
        # M-ix = switch to that group
        ("M-%d" % ix, lazy.group[group.name].toscreen()),
        #("M-%d" % ix, focus_or_switch(group.name)),
        # M-S-ix = switch to & move focused window to that group
        ("M-S-%d" % ix, lazy.window.togroup(group.name)),
    ]])

# .: Use the mouse to drag floating layouts :. #
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
    ]

# ---------------------------------------------------------------------------- #
#                                WIDGET HELPERS                                #
# ---------------------------------------------------------------------------- #

def get_uptime():
    seconds = uptime()
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02}:{:02}".format(int(h), int(m))

def get_doomsday():
    return subprocess.run([dotfiles + "/bin/doomsday-clock", "-s"], capture_output = True, text = True).stdout[:-1]

# ---------------------------------------------------------------------------- #
#                                    LAYOUTS                                   #
# ---------------------------------------------------------------------------- #

# layout_theme = {
#     "margin": 5,
#     "border_width": 2,
#     "border_focus": "#c58265",
#     "border_normal": "#2d3542",
#     "border_focus_stack": "#c89265",
#     "border_normal_stack": "#7d634c"
#     }

layout_theme = {
    "border_width": 2,
    "border_focus": "#c58265",
    "border_normal": "#2d3542",
    "border_focus_stack": "#c89265",
    "border_normal_stack": "#7d634c"
    }

layouts = [
    # layout.MonadWide(**layout_theme, align=layout.MonadTall._left, margin=12),
    layout.Columns(**layout_theme, margin=6),
    layout.Tile(**layout_theme, margin=6),
    layout.VerticalTile(**layout_theme, margin=6),
    # layout.MonadTall(**layout_theme, align=layout.MonadTall._right, margin=12),
    #layout.Floating(**layout_theme),
    # layout.Spiral(**layout_theme, margin=6),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme, margin=6),
    # layout.Matrix(**layout_theme, margin=6),
    # layout.RatioTile(),
    #layout.TreeTab(),
    # layout.Zoomy(),
]

# ---------------------------------------------------------------------------- #
#                                 WIDGET CONFIG                                #
# ---------------------------------------------------------------------------- #

bar_opacity = "bb";
# bar_color = "#202020" + bar_opacity;
bar_color = "#282828" + bar_opacity;
icon_font = "Material Design Icons"

# colors = {
#     "main": "#e27100",
#     "accent": "#d8ceb8",
#     "off": "#606060",
#     }

colors = {
    "main": "#d65d0e",
    "accent": "#ebdbb2",
    "off": "#665c54",
    }

widget_defaults = {
    "font": "Cascadia Mono PL",
    "fontsize": 13,
    "padding": 3,
    "foreground": colors["accent"]
}

sep_def = {
    "linewidth": 1,
    "padding": 6
    }

spacer_def = {
    "length": 12
    }

fa_def = {
    "foreground": colors["main"],
    "padding": 0,
    "font": icon_font,
    "fontsize": 36,
    }

widget_volume = widget.PulseVolume(
    step = 5,
    fmt = "{}",
    **widget_defaults
    )

# ---------------------------------------------------------------------------- #
#                                MAIN SCREEN BAR                               #
# ---------------------------------------------------------------------------- #

def init_widgets():
    return [
        widget.GroupBox(
            disable_drag = True,
            rounded = False,
            highlight_method = "block",
            active = colors["main"],
            inactive = colors["off"],
            # this_current_screen_border = "#404040" + bar_opacity,
            # other_current_screen_border = "#202020" + "22",
            # this_screen_border = "#404040" + bar_opacity,
            # other_screen_border = "#202020" + "22",
            this_current_screen_border = "#504945" + bar_opacity,
            other_current_screen_border = "#282828" + "22",
            this_screen_border = "#504945" + bar_opacity,
            other_screen_border = "#282828" + "22",
            **fa_def
            ),

        widget.WindowName(
            **widget_defaults,
            parse_text = lambda text: text.rsplit("— ", 1)[1]
            ),

        widget.TextBox( **fa_def, text = icons["update"] ),
        widget.CheckUpdates(
            **widget_defaults,
            # distro = "Arch",
            custom_command = "yay -Qu", # no manjaro option
            custom_command_modify = lambda x: x - 1,
            update_interval = 1800,
            display_format = "{updates}",
            no_update_string = " 0",
            # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e apt list --upgradable')}, # konsole
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -x yay -Qu')}, # xfce4-terminal
            colour_have_updates = colors["accent"],
            colour_no_updates = colors["off"],
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["disk"] ),
        widget.DF(
            **widget_defaults,
            format="{r:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
            visible_on_warn = False
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["ram"] ),
        widget.Memory(
            format="{MemPercent:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["cpu"] ),
        widget.CPU(
            **widget_defaults,
            format="{load_percent:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["volume"] ),
        widget_volume,

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["uptime"] ),
        widget.GenPollText(
            **widget_defaults,
            func = get_uptime,
            update_interval = 60
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["doomsday"] ),
        widget.GenPollText(
            **widget_defaults,
            func = get_doomsday,
            update_interval = 60 * 60 * 6
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["calendar"] ),
        widget.Clock(
            **widget_defaults,
            format="%d/%m",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e ncal -yMb')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["clock"] ),
        widget.Clock(
            **widget_defaults,
            format="%H:%M:%S",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e ncal -yMb')},
            ),

        widget.Spacer(**spacer_def),

        widget.WidgetBox(
            **fa_def,
            close_button_location='right',
            text_closed='󰘔', # mdi-application-outline
            text_open='󰶮', # mdi-application-import
            widgets = [
                # widget.KeyboardLayout(
                #     **widget_defaults,
                #     ),
                widget.Systray(
                    **fa_def,
                    ),
                widget.Spacer(**spacer_def),
                widget.CurrentLayoutIcon(
                    **fa_def,
                    ),
                widget.Spacer(**spacer_def),
            ]
        ),

        widget.Spacer(**spacer_def),
        widget.CurrentScreen(
            **fa_def,
            active_text = icons["screen_focus"],
            inactive_text = icons["screen_nofocus"],
            active_color = colors["main"],
            inactive_color = colors["off"],
            ),
        widget.Spacer(**spacer_def),
        ]


# ---------------------------------------------------------------------------- #
#                                SIDE SCREEN BAR                               #
# ---------------------------------------------------------------------------- #

def init_widgets_part():
    return [
        widget.GroupBox(
            disable_drag = True,
            rounded = False,
            highlight_method = "block",
            active = colors["main"],
            inactive = colors["off"],
            this_current_screen_border = "#504945" + bar_opacity,
            other_current_screen_border = "#282828" + "22",
            this_screen_border = "#504945" + bar_opacity,
            other_screen_border = "#282828" + "22",
            **fa_def
            ),

        widget.WindowName(
            **widget_defaults,
            parse_text = lambda text: text.rsplit("— ", 1)[1]
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["calendar"] ),
        widget.Clock(
            **widget_defaults,
            format="%d/%m",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e ncal -yMb')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["clock"] ),
        widget.Clock(
            **widget_defaults,
            format="%H:%M:%S",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e ncal -yMb')},
            ),

        widget.Spacer(**spacer_def),

        widget.WidgetBox(
            **fa_def,
            close_button_location='right',
            text_closed='󰘔', # mdi-application-outline
            text_open='󰶮', # mdi-application-import
            widgets = [
                widget.CurrentLayoutIcon(
                    **fa_def,
                ),
                widget.Spacer(**spacer_def),
            ]
        ),

        widget.Spacer(**spacer_def),
        widget.CurrentScreen(
            **fa_def,
            active_text = icons["screen_focus"],
            inactive_text = icons["screen_nofocus"],
            active_color = colors["main"],
            inactive_color = colors["off"],
            ),
        widget.Spacer(**spacer_def),
        ]

# ---------------------------------------------------------------------------- #
#                                    SCREENS                                   #
# ---------------------------------------------------------------------------- #

# Init as center right left then swap left around
# should be:
# | *** | DEV | Window Name                       Upd:  45 | Mem:  53% | CPU:   3% | Doom | Up | Time | V |
screens = [
    Screen( # center
        top = bar.Bar(widgets = init_widgets(), size = 24, background = bar_color, ), 
        wallpaper=home + '/.config/qtile/wallpapers/center.png', 
        wallpaper_mode='stretch', ),
    Screen( # right
        top = bar.Bar(widgets = init_widgets_part(), size = 24, background = bar_color, ), 
        wallpaper=home + '/.config/qtile/wallpapers/gray_5.png', 
        wallpaper_mode='fill', ),
    Screen( # left
        top = bar.Bar(widgets = init_widgets_part(), size = 24, background = bar_color, ), 
        wallpaper=home + '/.config/qtile/wallpapers/left.png', 
        wallpaper_mode='stretch', ),
]

# ---------------------------------------------------------------------------- #
#                               FLOATING WINDOWS                               #
# ---------------------------------------------------------------------------- #

floating_layout = layout.Floating(
    float_rules=[
        # xprop WM_CLASS
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # Match(title=WM_NAME, wm_class=WM_CLASS, role=WM_WINDOW_ROLE)
        *layout.Floating.default_float_rules,
        # gitk
        Match(wm_class="confirmreset"), 
        Match(wm_class="makebranch"), 
        Match(wm_class="maketag"), 
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"), 
        Match(title="pinentry"),  # GPG key password entry
        # xfce
        Match(wm_class="xfce4-appearance-settings"),
        # godot
        Match(wm_class="Godot_ProjectList"),
        Match(title="Load Errors"), 
        # steam
        Match(title=re.compile(r"Steam \- News.*")), 
        # sideapps
        Match(wm_class="gpick"),
        # qtile
        Match(title=re.compile(r"Krita \- Edit.*")), 
        # Match(title=".shortcuts.html - qutebrowser"),
        # Match(title="V .shortcuts.html - qutebrowser"),
        # web
        Match(title=re.compile(r"Vivaldi Settings:*")), 
    ]
)

# ---------------------------------------------------------------------------- #
#                               ADDITIONAL CONFIG                              #
# ---------------------------------------------------------------------------- #

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# ---------------------------------------------------------------------------- #
#                                     HOOKS                                    #
# ---------------------------------------------------------------------------- #

@hook.subscribe.client_new
def disable_floating(window):
    rules = [
        Match(wm_class="qutebrowser")
    ]

    if any(window.match(rule) for rule in rules):
        window.togroup(qtile.current_group.name)
        window.cmd_disable_floating()

# @hook.subscribe.startup_complete
def set_screen_groups():
    # WWW SYS DEV
    # left center right = 1 0 2
    screens[0].cmd_toggle_group("SYS") # center
    # screens[1].cmd_toggle_group("WWW") # left
    screens[2].cmd_toggle_group("DEV") # right

@hook.subscribe.startup_once
def autostart():
    screens[0].cmd_toggle_group("SYS") # center
    # screens[1].cmd_toggle_group("WWW") # left
    screens[2].cmd_toggle_group("DEV") # right

    # subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    # set_screen_groups()

# @hook.subscribe.client_new
# def func(c):
#     set_screen_groups()
#     if c.name == "Desktop — Plasma":
#         c.cmd_kill()
