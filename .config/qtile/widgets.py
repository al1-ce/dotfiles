# Widgets

from libqtile import widget, qtile

from icons import icons, images

import apps as apps

bar_margin = [5, 5, 2, 5]
bar_opacity = "bb"
bar_color =   "#282828" + bar_opacity

# colors = {
#     "main": "#e27100",
#     "accent": "#d8ceb8",
#     "off": "#606060",
#     }

colors = {
    "main":   "#d65d0e",
    "accent": "#ebdbb2",
    "off":    "#665c54",
}

widget_defaults = {
    "font":       "DinaRemaster",
    "fontsize":   16,
    "padding":    2,
    # "font":       "Cascadia Mono PL",
    # "fontsize":   13,
    # "padding":    3,
    "foreground": colors["accent"]
}

sep_def = {
    "linewidth": 1,
    "padding":   6
}

spacer_def = {
    "length": 12
}

gr_def = {
    "foreground": colors["main"],
    "padding":    0,

    "font":       "Cascadia Mono PL",
    "fontsize":   16,
}

fa_def = {
    "foreground": colors["main"],
    "padding":    0,

    "font":       "Cascadia Mono PL",
    # "font":       "Material Design Icons",
    "fontsize":   30, # 36
}

im_def = {
    "margin": 0,
    "scale": False
}

widget_volume = widget.PulseVolume(
    step = 5,
    fmt =  "{}",
    **widget_defaults
)

# ---------------------------------------------------------------------------- #
#                                MAIN SCREEN BAR                               #
# ---------------------------------------------------------------------------- #

widgets = {
    "groups": (lambda: widget.GroupBox(
        disable_drag = True,
        rounded = False,
        highlight_method = "block",
        active = colors["main"],
        inactive = colors["off"],
        this_current_screen_border = "#504945" + bar_opacity,
        other_current_screen_border = "#282828" + "22",
        this_screen_border = "#504945" + bar_opacity,
        other_screen_border = "#282828" + "22",
        **gr_def
    )),

    "spacer": (lambda: widget.Spacer(**spacer_def)),

    "window_name": (lambda: widget.WindowName(
        **widget_defaults,
        parse_text = lambda text: text.rsplit("— ", 1)[1]
    )),

    "update_text": (lambda: widget.CheckUpdates(
        **widget_defaults,
        # distro = "Arch",
        custom_command = "yay -Qu",
        custom_command_modify = lambda x: x - 1,
        update_interval = 1800,
        display_format = "{updates}",
        no_update_string = " 0",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'yay -Qu' + apps.term_wait)},
        colour_have_updates = colors["accent"],
        colour_no_updates = colors["off"],
    )),

    "disk_text": (lambda: widget.DF(
        **widget_defaults,
        format="{r:2.0f}%",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
        visible_on_warn = False
    )),

    "ram_text": (lambda: widget.Memory(
        **widget_defaults,
        format="{MemPercent:2.0f}%",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
    )),

    "cpu_text": (lambda: widget.CPU(
        **widget_defaults,
        format="{load_percent:2.0f}%",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
    )),

    "volume_text": (lambda: widget_volume),

    "calendar_text": (lambda: widget.Clock(
        **widget_defaults,
        format="%d/%m",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
    )),

    "clock_text": (lambda: widget.Clock(
        **widget_defaults,
        format="%H:%M:%S",
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
    )),

    "systray": (lambda: widget.WidgetBox(
        **fa_def,
        close_button_location='right',
        text_closed = icons["systray_opened"],
        text_open = icons["systray_closed"],
        widgets = [
            widget.Systray(**fa_def),
            widget.Spacer(**spacer_def),
            widget.CurrentLayoutIcon(**fa_def, custom_icon_paths = ["~/.config/qtile/icons/layouts/"]),
            widget.Spacer(**spacer_def),
        ]
    )),

    "screen": (lambda: widget.CurrentScreen(
        **fa_def,
        active_text = icons["screen_focus"],
        inactive_text = icons["screen_nofocus"],
        active_color = colors["main"],
        inactive_color = colors["off"],
    )),


    "update_icon"  : (lambda: widget.Image( **im_def, filename = images["update"])),
    "disk_icon"    : (lambda: widget.Image( **im_def, filename = images["disk"])),
    "ram_icon"     : (lambda: widget.Image( **im_def, filename = images["ram"])),
    "cpu_icon"     : (lambda: widget.Image( **im_def, filename = images["cpu"])),
    "volume_icon"  : (lambda: widget.Image( **im_def, filename = images["volume"])),
    "calendar_icon": (lambda: widget.Image( **im_def, filename = images["calendar"])),
    "clock_icon"   : (lambda: widget.Image( **im_def, filename = images["clock"])),
}

def init_widgets():
    return [
        widgets["groups"](),

        widgets["window_name"](),

        widgets["update_icon"](),
        widgets["update_text"](),

        widgets["spacer"](),
        widgets["disk_icon"](),
        widgets["disk_text"](),

        widgets["spacer"](),
        widgets["ram_icon"](),
        widgets["ram_text"](),

        widgets["spacer"](),
        widgets["cpu_icon"](),
        widgets["cpu_text"](),

        widgets["spacer"](),
        widgets["volume_icon"](),
        widgets["volume_text"](),

        widgets["spacer"](),
        widgets["calendar_icon"](),
        widgets["calendar_text"](),

        widgets["spacer"](),
        widgets["clock_icon"](),
        widgets["clock_text"](),

        widgets["spacer"](),
        widgets["systray"](),

        widgets["spacer"](),
        widgets["screen"](),

        widgets["spacer"](),
    ]


# ---------------------------------------------------------------------------- #
#                                SIDE SCREEN BAR                               #
# ---------------------------------------------------------------------------- #

def init_widgets_part():
    return [
        widgets["groups"](),
        widgets["window_name"](),

        widgets["calendar_icon"](),
        widgets["calendar_text"](),

        widgets["spacer"](),
        widgets["clock_icon"](),
        widgets["clock_text"](),

        widgets["spacer"](),
        widgets["screen"](),

        widgets["spacer"](),

    ]


