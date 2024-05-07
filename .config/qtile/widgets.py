# Widgets

from libqtile import widget, qtile

from icons import icons

import apps as apps

bar_margin = [5, 5, 2, 5]
bar_opacity = "bb"
bar_color =   "#282828" + bar_opacity

icon_font =   "Material Design Icons"

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
    "font":       "Cascadia Mono PL",
    "fontsize":   13,
    "padding":    3,
    "foreground": colors["accent"]
}

sep_def = {
    "linewidth": 1,
    "padding":   6
    }

spacer_def = {
    "length": 12
    }

fa_def = {
    "foreground": colors["main"],
    "padding":    0,
    "font":       icon_font,
    # "fontsize":   36,
    "fontsize":   31,
    }

widget_volume = widget.PulseVolume(
    step = 5,
    fmt =  "{}",
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
            custom_command = "yay -Qu",
            custom_command_modify = lambda x: x - 1,
            update_interval = 1800,
            display_format = "{updates}",
            no_update_string = " 0",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'yay -Qu' + apps.term_wait)},
            colour_have_updates = colors["accent"],
            colour_no_updates = colors["off"],
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["disk"] ),
        widget.DF(
            **widget_defaults,
            format="{r:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
            visible_on_warn = False
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["ram"] ),
        widget.Memory(
            format="{MemPercent:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["cpu"] ),
        widget.CPU(
            **widget_defaults,
            format="{load_percent:2.0f}%",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.terminal + ' btop')},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["volume"] ),
        widget_volume,

        # widget.Spacer(**spacer_def),
        # widget.TextBox( **fa_def, text = icons["uptime"] ),
        # widget.GenPollText(
        #     **widget_defaults,
        #     func = get_uptime,
        #     update_interval = 60
        #     ),

        # widget.Spacer(**spacer_def),
        # widget.TextBox( **fa_def, text = icons["doomsday"] ),
        # widget.GenPollText(
        #     **widget_defaults,
        #     func = get_doomsday,
        #     update_interval = 60 * 60 * 6
        #     ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["calendar"] ),
        widget.Clock(
            **widget_defaults,
            format="%d/%m",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["clock"] ),
        widget.Clock(
            **widget_defaults,
            format="%H:%M:%S",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
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
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
            ),

        widget.Spacer(**spacer_def),
        widget.TextBox( **fa_def, text = icons["clock"] ),
        widget.Clock(
            **widget_defaults,
            format="%H:%M:%S",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(apps.term_exec + 'ncal -yMb' + apps.term_wait)},
            ),

        widget.Spacer(**spacer_def),

        widget.WidgetBox(
            **fa_def,
            close_button_location='right',
            text_closed=icons["systray_closed"],
            text_open=icons["systray_opened"],
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


