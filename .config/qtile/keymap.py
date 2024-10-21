# Key mappings

from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.config import EzKey
from libqtile.lazy import lazy

import apps as apps
import functions as funcs
from groups import groups, group_names
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
keys = [EzKey(k[0], *k[1:-1], desc = k[-1]) for k in [
    # Navigation
    # Swtich focus between panes
    ("M-<Left>",  lazy.layout.left(), "Switch to left pane"),
    ("M-<Down>",  lazy.layout.down(), "Switch to lower page"),
    ("M-<Up>",    lazy.layout.up(), "Switch to upper pane"),
    ("M-<Right>", lazy.layout.right(), "Switch to right pane"),

    ("M-h", lazy.layout.left(), "Switch to left pane"),
    ("M-j", lazy.layout.down(), "Switch to lower pane"),
    ("M-k", lazy.layout.up(), "Switch to upper pane"),
    ("M-l", lazy.layout.right(), "Switch to right pane"),

    # Swap panes: target relative to active.
    ("M-S-<Left>",  lazy.layout.shuffle_left(), lazy.layout.swap_left(), "Move pane left"),
    ("M-S-<Down>",  lazy.layout.shuffle_down(), lazy.layout.section_down(), "Move pane down"),
    ("M-S-<Up>",    lazy.layout.shuffle_up(), lazy.layout.section_up(), "Move pane up"),
    ("M-S-<Right>", lazy.layout.shuffle_right(), lazy.layout.swap_right(), "Move pane right"),

    ("M-S-h", lazy.layout.shuffle_left(), lazy.layout.swap_left(), "Move pane left"),
    ("M-S-j", lazy.layout.shuffle_down(), lazy.layout.section_down(), "Move pane down"),
    ("M-S-k", lazy.layout.shuffle_up(), lazy.layout.section_up(), "Move pane up"),
    ("M-S-l", lazy.layout.shuffle_right(), lazy.layout.swap_right(), "Move pane right"),

    # Grow/shrink the main the focused window
    ("M-C-<Left>",  lazy.layout.grow_left(), lazy.layout.shrink(), "Grow/Shrink pane left"),
    ("M-C-<Down>",  lazy.layout.grow_down(), "Grow/Shrink pane down"),
    ("M-C-<Up>",    lazy.layout.grow_up(), "Grow/Shrink pane up"),
    ("M-C-<Right>", lazy.layout.grow_right(), lazy.layout.grow(), "Grow/Shrink pane right"),

    ("M-C-h", lazy.layout.grow_left(), lazy.layout.shrink(), "Grow/Shrink pane left"),
    ("M-C-j", lazy.layout.grow_down(), "Grow/Shrink pane down"),
    ("M-C-k", lazy.layout.grow_up(), "Grow/Shrink pane up"),
    ("M-C-l", lazy.layout.grow_right(), lazy.layout.grow(), "Grow/Shrink pane right"),

    ("M-<bracketleft>",  lazy.layout.decrease_nmaster(), "Decrease nummber of master windows"),
    ("M-<bracketright>", lazy.layout.increase_nmaster(), "Increase nummber of master windows"),

    # TODO meta alt
    ## Switch focus between two screens
    ("M-A-h",         lazy.screen.prev_group(), "Switch to previous group"),
    ("M-A-l",         lazy.screen.next_group(), "Switch to next group"),
    ("M-A-S-<Left>",  lazy.screen.prev_group(), "Switch to previous group"),
    ("M-A-S-<Right>", lazy.screen.next_group(), "Switch to next group"),
    # ("M-A-<Left>", lazy.to_screen(1)),
    # ("M-A-<Left>", lazy.prev_screen()),
    # ("M-A-<Right>", lazy.next_screen()),
    ("M-A-1",         lazy.to_screen(screen_order[2]), "Switch to left screen"),
    ("M-A-2",         lazy.to_screen(screen_order[1]), "Switch to middle screen"),
    ("M-A-3",         lazy.to_screen(screen_order[0]), "Switch to right screen"),
    ("M-A-<Left>",    lazy.to_screen(screen_order[2]), "Switch to left screen"),
    ("M-A-<Down>",    lazy.to_screen(screen_order[1]), "Switch to middle screen"),
    ("M-A-<Up>",      lazy.to_screen(screen_order[1]), "Switch to middle screen"),
    ("M-A-<Right>",   lazy.to_screen(screen_order[0]), "Switch to right screen"),
    ("M-A-j",         lazy.prev_screen(), "Switch to previous screen"),
    ("M-A-k",         lazy.next_screen(), "Switch to next screen"),
    ## Move the focused group to one of the screens and follow it
    # ("M-S-<bracketleft>", switch_screens(0), lazy.to_screen(0)),
    # ("M-S-<bracketright>", switch_screens(1), lazy.to_screen(1)),

    # Layouts
    ("M-<backslash>",   lazy.next_layout(), "Next layout"),
    ("M-S-<backslash>", lazy.prev_layout(), "Previous layout"),
    ("M-r",             lazy.layout.rotate(), lazy.layout.flip(), lazy.layout.spaw_column_left(), lazy.layout.spaw_column_right(), "Rotate layout"),
    # ("M-S-r", lazy.layout.flip()),
    ("M-<space>",       lazy.layout.toggle_split(), "Toggle split"),
    # ("M-f", lazy.prev_layout()),
    # ("M-f", lazy.prev_layout()),

    # Applications
    # Terms
    ("M-<Return>",   lazy.spawn(apps.terminal), "Spawn terminal"),
    ("M-S-<Return>", lazy.group[group_names[10]].dropdown_toggle("quake"), "Spawn dropdown terminal"),
    # FM
    ("M-e",          lazy.spawn(apps.filemanager), "Spawn TUI file manager"),
    ("M-S-e",        lazy.spawn(apps.filemanager_gui), "Spawn GUI file manager"),
    ("M-m",          lazy.spawn(apps.music_player), "Spawn music player"),
    # Web
    ("M-w",          lazy.spawn(apps.mybrowser), "Spawn browser"),
    ("M-S-w",        lazy.spawn(apps.altbrowser), "Spawn alt browser"),
    ("M-S-s",        lazy.spawn(apps.steam), "Spawn Steam"),
    ("M-S-b",        lazy.spawn(apps.beeper), "Spawn Beeper"),
    ("M-S-r",        lazy.spawn(apps.rustdesk), "Spawn RustDesk"),
    # Screen
    ("<Print>",      lazy.spawn(apps.screenshot), "Take screenshot"),
    ("S-<Print>",    lazy.spawn(apps.screenrec), "Spawn screen recorder"),
    # Editor
    ("M-v",          lazy.spawn(apps.editor), "Spawn TUI text editor"),
    ("M-S-v",        lazy.spawn(apps.editor_gui), "Spawn GUI text editor"),
    ("M-p",          lazy.spawn(apps.color_pick), "Spawn color picker"),
    # Draw
    ("M-d",          lazy.spawn(apps.osc_draw + " --toggle"), "Toggle drawing on screen"),
    ("M-A-d",        lazy.spawn(apps.osc_draw + " --redo"), "Redo screen drawing"),
    ("M-C-d",        lazy.spawn(apps.osc_draw + " --undo"), "Undo screen drawing"),
    ("M-S-d",        lazy.spawn(apps.osc_draw + " --clear"), "Clear screen drawing"),

    ("M-t",   lazy.spawn(apps.process_explr), "Spawn task manager"),
    # ("M-A-t", lazy.spawn("/bin/bash -c '" + apps.tabletscript + "'")),
    # ("M-S-t", lazy.spawn("/bin/bash -c '" + apps.touchsscript + "'")),

    # Rofi
    ("M-<semicolon>",   lazy.spawn(apps.rofi_launcher), "Spawn launcher"),
    ("M-<grave>",   lazy.spawn(apps.rofi_launcher), "Spawn launcher"),
    ("M-S-<grave>", lazy.spawn(apps.rofi_run), "Spawn binary launcher"),
    ("M-C-<grave>", lazy.spawn(apps.rofi_websearch), "Spawn web search"),
    ("M-A-<grave>", lazy.spawn(apps.rofi_powermenu), "Spawn power menu"),
    ("M-A-p",       lazy.spawn(apps.rofi_pass), "Spawn password manager"),
    ("M-<Tab>",     lazy.spawn(apps.rofi_windowcd), "Switch to current group window"),
    ("M-S-<Tab>",   lazy.spawn(apps.rofi_window), "Switch to any window"),

    # Check keys
    ("M-<slash>",   funcs.getwmclass, "Get window class"),
    ("M-S-<slash>", funcs.getwmtitle, "Get window title"),

    # Windows
    ("M-f",             lazy.window.toggle_floating(), "Toggle window floating"),
    ("M-q",             lazy.window.kill(), "Kill window"),
    ("M-A-r",           lazy.reload_config(), "Reload window manager config"),
    ("M-<Page_Down>",   lazy.spawn("Qminimize -m"), "Minimize window"),
    ("M-S-<Page_Down>", lazy.spawn("Qminimize -u"), "Unminimize window"),
    ("M-<Page_Up>",     lazy.window.toggle_fullscreen(), "Toggle window fullscreen"),
    ("M-S-<Page_Up>",   lazy.layout.maximize(), "Maximize window"),

    # Other
    ("M-n", lazy.layout.normalize(), "Normalize layout"),
    ("M-s", lazy.spawn(apps.spawnshortcuts), "Spawn keybind helper"),

    # Change the volume if your keyboard has special volume keys.
    ("<XF86AudioRaiseVolume>", funcs.increase_vol, "Increase volume"),
    ("<XF86AudioLowerVolume>", funcs.decrease_vol, "Decrease volume"),
    ("<XF86AudioMute>",        funcs.mute_vol, "Mute volume"),
    ("<XF86AudioPlay>",        lazy.spawn("playerctl play-pause"), "Play/Pause"),
    ("<XF86AudioPause>",       lazy.spawn("playerctl play-pause"), "Play/Pause"),

    ("M-A-C-r", lazy.restart()     , "Restart window manager"),
    ("M-A-C-q", lazy.shutdown()    , "Shutdown")              ,
    ("M-A-C-k", lazy.spawn("xkill"), "Spawn xkill")           ,
]]


keys += [

    # Umlauts
    # KeyChord([mod], "semicolon", [
    #     Key(["shift"], "a", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+adiaeresis'")),
    #     Key(["shift"], "o", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+odiaeresis'")),
    #     Key(["shift"], "u", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+udiaeresis'")),
    #     Key(["shift"], "s", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key shift+ssharp'")),
    #
    #     Key([], "a", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key adiaeresis'")),
    #     Key([], "o", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key odiaeresis'")),
    #     Key([], "u", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key udiaeresis'")),
    #     Key([], "s", lazy.spawn("/bin/bash -c 'sleep 0.25 && xdotool key ssharp'")),
    # ]),

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

    keys.extend([EzKey(k[0], *k[1:], desc = k[-1]) for k in [
        # M-ix = switch to that group
        ("M-%d" % ix, lazy.group[group.name].toscreen(), f"Switch to group {ix}"),
        # ("M-%d" % ix, focus_or_switch(group.name)),
        # M-S-ix = switch to & move focused window to that group
        ("M-S-%d" % ix, lazy.window.togroup(group.name), f"Move pane to group {ix}"),
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

