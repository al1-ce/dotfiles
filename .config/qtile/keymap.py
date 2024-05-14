# Key mappings

from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.config import EzKey
from libqtile.lazy import lazy

import apps as apps
import functions as funcs
from groups import groups, scratch_name
from screens import screen_order

mod = "mod4"

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
    ("M-<Left>",  lazy.layout.left()),
    ("M-<Down>",  lazy.layout.down()),
    ("M-<Up>",    lazy.layout.up()),
    ("M-<Right>", lazy.layout.right()),

    ("M-h", lazy.layout.left()),
    ("M-j", lazy.layout.down()),
    ("M-k", lazy.layout.up()),
    ("M-l", lazy.layout.right()),

    # Swap panes: target relative to active.
    ("M-S-<Left>",  lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    ("M-S-<Down>",  lazy.layout.shuffle_down(), lazy.layout.section_down()),
    ("M-S-<Up>",    lazy.layout.shuffle_up(), lazy.layout.section_up()),
    ("M-S-<Right>", lazy.layout.shuffle_right(), lazy.layout.swap_right()),

    ("M-S-h", lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    ("M-S-j", lazy.layout.shuffle_down(), lazy.layout.section_down()),
    ("M-S-k", lazy.layout.shuffle_up(), lazy.layout.section_up()),
    ("M-S-l", lazy.layout.shuffle_right(), lazy.layout.swap_right()),

    # Grow/shrink the main the focused window
    ("M-C-<Left>",  lazy.layout.grow_left(), lazy.layout.shrink()),
    ("M-C-<Down>",  lazy.layout.grow_down()),
    ("M-C-<Up>",    lazy.layout.grow_up()),
    ("M-C-<Right>", lazy.layout.grow_right(), lazy.layout.grow()),

    ("M-C-h", lazy.layout.grow_left(), lazy.layout.shrink()),
    ("M-C-j", lazy.layout.grow_down()),
    ("M-C-k", lazy.layout.grow_up()),
    ("M-C-l", lazy.layout.grow_right(), lazy.layout.grow()),

    ("M-<bracketleft>",  lazy.layout.decrease_nmaster()),
    ("M-<bracketright>", lazy.layout.increase_nmaster()),

    # TODO meta alt
    ## Switch focus between two screens
    ("M-A-h",         lazy.screen.prev_group()),
    ("M-A-l",         lazy.screen.next_group()),
    ("M-A-S-<Left>",  lazy.screen.prev_group()),
    ("M-A-S-<Right>", lazy.screen.next_group()),
    # ("M-A-<Left>", lazy.to_screen(1)),
    # ("M-A-<Left>", lazy.prev_screen()),
    # ("M-A-<Right>", lazy.next_screen()),
    ("M-A-1",         lazy.to_screen(screen_order[0])),
    ("M-A-2",         lazy.to_screen(screen_order[1])),
    ("M-A-3",         lazy.to_screen(screen_order[2])),
    ("M-A-<Left>",    lazy.to_screen(screen_order[2])),
    ("M-A-<Down>",    lazy.to_screen(screen_order[1])),
    ("M-A-<Up>",      lazy.to_screen(screen_order[1])),
    ("M-A-<Right>",   lazy.to_screen(screen_order[0])),
    ("M-A-j",         lazy.prev_screen()),
    ("M-A-k",         lazy.next_screen()),
    ## Move the focused group to one of the screens and follow it
    # ("M-S-<bracketleft>", switch_screens(0), lazy.to_screen(0)),
    # ("M-S-<bracketright>", switch_screens(1), lazy.to_screen(1)),

    # Layouts
    ("M-<backslash>",   lazy.next_layout()),
    ("M-S-<backslash>", lazy.prev_layout()),
    ("M-r",             lazy.layout.rotate(), lazy.layout.flip(), lazy.layout.spaw_column_left(), lazy.layout.spaw_column_right()),
    # ("M-S-r", lazy.layout.flip()),
    ("M-<space>",       lazy.layout.toggle_split()),
    # ("M-f", lazy.prev_layout()),
    # ("M-f", lazy.prev_layout()),

    # Applications
    # Terms
    ("M-<Return>",   lazy.spawn(apps.terminal)),
    ("M-S-<Return>", lazy.group[scratch_name].dropdown_toggle("quake")),
    # FM
    ("M-e",          lazy.spawn(apps.filemanager)),
    ("M-S-e",        lazy.spawn(apps.filemanager_gui)),
    # Web
    ("M-w",          lazy.spawn(apps.mybrowser)),
    ("M-S-w",        lazy.spawn(apps.altbrowser)),
    ("M-S-s",        lazy.spawn("steam-runtime")),
    # Screen
    ("<Print>",      lazy.spawn("flameshot gui")),
    ("S-<Print>",    lazy.spawn("peek")),
    # Editor
    ("M-v",          lazy.spawn(apps.editor)),
    ("M-S-v",        lazy.spawn(apps.editor_gui)),
    ("M-p",          lazy.spawn("gpick")),
    # Draw
    ("M-d",          lazy.spawn(apps.osc_draw + " --toggle")),
    ("M-A-d",        lazy.spawn(apps.osc_draw + " --redo")),
    ("M-C-d",        lazy.spawn(apps.osc_draw + " --undo")),
    ("M-S-d",        lazy.spawn(apps.osc_draw + " --clear")),

    ("M-t",   lazy.spawn(apps.process_explr)),
    ("M-A-t", lazy.spawn("/bin/bash -c '" + apps.tabletscript + "'")),
    ("M-S-t", lazy.spawn("/bin/bash -c '" + apps.touchsscript + "'")),

    # Rofi
    ("M-<grave>",   lazy.spawn(apps.rofi_launcher)),
    ("M-S-<grave>", lazy.spawn(apps.rofi_run)),
    ("M-C-<grave>", lazy.spawn(apps.rofi_websearch)),
    ("M-A-<grave>", lazy.spawn(apps.rofi_powermenu)),
    ("M-<Tab>",     lazy.spawn(apps.rofi_windowcd)),
    ("M-S-<Tab>",  lazy.spawn(apps.rofi_window)),

    # Check keys
    ("M-<slash>",   funcs.getwmclass),
    ("M-S-<slash>", funcs.getwmtitle),

    # Windows
    ("M-f",             lazy.window.toggle_floating()),
    ("M-q",             lazy.window.kill()),
    ("M-A-r",           lazy.reload_config()),
    ("M-A-C-r",         lazy.restart()),
    ("M-A-C-q",         lazy.shutdown()),
    ("M-<Page_Down>",   lazy.spawn("Qminimize -m")),
    ("M-S-<Page_Down>", lazy.spawn("Qminimize -u")),
    ("M-<Page_Up>",     lazy.window.toggle_fullscreen()),
    ("M-S-<Page_Up>",   lazy.layout.maximize()),

    # Other
    ("M-n", lazy.layout.normalize()),
    ("M-s", lazy.spawn(apps.spawnshortcuts)),

    # Change the volume if your keyboard has special volume keys.
    ("<XF86AudioRaiseVolume>", funcs.increase_vol),
    ("<XF86AudioLowerVolume>", funcs.decrease_vol),
    ("<XF86AudioMute>",        funcs.mute_vol),
    ("<XF86AudioPlay>",        lazy.spawn("playerctl play-pause")),
    ("<XF86AudioPause>",       lazy.spawn("playerctl play-pause")),

    ("M-S-<Escape>", lazy.spawn("xkill")),
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
for _ix, group in enumerate(groups[:10]):
    # Index from 1-0 instead of 0-9
    ix = 0 if _ix == 9 else _ix + 1

    keys.extend([EzKey(k[0], *k[1:]) for k in [
        # M-ix = switch to that group
        ("M-%d" % ix, lazy.group[group.name].toscreen()),
        # ("M-%d" % ix, focus_or_switch(group.name)),
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

# def switch_screens(target_screen):
#     '''Send the current group to the other screen.'''
#     @lazy.function
#     def _inner(qtile):
#         current_group = qtile.screens[1 - target_screen].group
#         qtile.screens[target_screen].setGroup(current_group)
#
#     return _inner
#
#
# def focus_or_switch(group_name):
#     '''
#     Focus the selected group on the current screen or switch to the other
#     screen if the group is currently active there
#     '''
#     @lazy.function
#     def _inner(qtile):
#         # Check what groups are currently active
#         groups = [s.group.name for s in qtile.screens]
#
#         try:
#             # Jump to that screen if we are active
#             index = groups.index(group_name)
#             qtile.toScreen(index)
#         except ValueError:
#             # We're not active so pull the group to the current screen
#             qtile.currentScreen.setGroup(qtile.groupMap[group_name])
#
#     return _inner

