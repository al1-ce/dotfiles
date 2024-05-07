# pylint disable=all

from apps import *
from groups import *
from keymap import *
from layouts import *
from screens import *

from typing import List

# ---------------------------------------------------------------------------- #
#                               ADDITIONAL CONFIG                              #
# ---------------------------------------------------------------------------- #

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
x11_drag_polling_rate = 60

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


# @hook.subscribe.client_new
# def func(c):
#     set_screen_groups()
#     if c.name == "Desktop — Plasma":
#         c.cmd_kill()

