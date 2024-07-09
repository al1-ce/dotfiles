# Layouts

import re

from libqtile import layout, hook, qtile
from libqtile.config import Match

# layout_theme = {
#     "margin": 5,
#     "border_width": 2,
#     "border_focus": "#c58265",
#     "border_normal": "#2d3542",
#     "border_focus_stack": "#c89265",
#     "border_normal_stack": "#7d634c"
#     }

layout_theme = {
    "border_width":        1,
    # "border_width":        2,
    "border_focus":        "#4e3f39",
    "border_normal":       "#262626",
    "border_focus_stack":  "#58493c",
    "border_normal_stack": "#413b37"
    }

layouts = [
    # layout.MonadWide(**layout_theme, align=layout.MonadTall._left, margin=12),
    layout.Columns(**layout_theme, margin=6),
    layout.Tile(**layout_theme, margin=6, shift_windows = True),
    # layout.VerticalTile(**layout_theme, margin=6),
    # layout.MonadTall(**layout_theme, align=layout.MonadTall._right, margin=12),
    # layout.Floating(**layout_theme),
    # layout.Spiral(**layout_theme, margin=6),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme, margin=6),
    # layout.Matrix(**layout_theme, margin=6),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_width = 1,
    # border_width = 2,
    border_focus = "#273230",
    # border_focus = "#65c5b2",
    border_normal = "#2d3542",

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
        Match(wm_class="feh"),
        Match(title="branchdialog"),
        Match(title="pinentry"),  # GPG key password entry
        # xfce
        Match(wm_class="xfce4-appearance-settings"),
        # godot
        Match(wm_class="Godot_ProjectList"),
        Match(title="Load Errors"),
        Match(title="Open With"),
        # steam
        Match(title=re.compile(r"Steam \- News.*")),
        # sideapps
        Match(wm_class="gpick"),
        # qtile
        Match(title=re.compile(r"Krita \- Edit.*")),
        # Match(title=".shortcuts.html - qutebrowser"),
        # Match(title="V .shortcuts.html - qutebrowser"),
        # web
        Match(title=re.compile(r".*Settings.*")),
        Match(title=re.compile(r"Create.*New.*")),
        Match(title=re.compile(r".*Confirm.*")),
    ]
)

@hook.subscribe.client_new
def disable_floating(window):
    rules = [
        Match(wm_class="qutebrowser")
    ]

    if any(window.match(rule) for rule in rules):
        window.togroup(qtile.current_group.name)
        window.disable_floating()

