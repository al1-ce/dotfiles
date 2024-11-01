local wezterm = require('wezterm')

local M = {}

local scheme_name = "none";
local theme = {}

M.color_scheme = function () return scheme_name end

M.colors = function () return {
    tab_bar = {
        -- The color of the strip that goes along the top of the window
        -- (does not apply when fancy tab bar is in use)
        background = theme.background,

        -- The active tab is the one that has focus in the window
        active_tab = {
            bg_color = theme.background,
            fg_color = theme.foreground,
            intensity = 'Normal',
            underline = 'None',
            italic = false,
            strikethrough = false,
        },

        ---@diagnostic disable-next-line: missing-fields
        inactive_tab = {
            bg_color = theme.background,
            fg_color = theme.brights[1],
        },

        ---@diagnostic disable-next-line: missing-fields
        inactive_tab_hover = {
            bg_color = theme.background,
            fg_color = theme.foreground,
        },

        ---@diagnostic disable-next-line: missing-fields
        new_tab = {
            bg_color = theme.background,
            fg_color = theme.brights[1],
        },

        ---@diagnostic disable-next-line: missing-fields
        new_tab_hover = {
            bg_color = theme.background,
            fg_color = theme.foreground,
        },
    },
    selection_bg = theme.foreground,
    selection_fg = theme.background,
    cursor_bg = theme.foreground,
    cursor_fg = theme.background,
} end

M.init = function (name)
    scheme_name = name
    if scheme_name == "gruvbox" then scheme_name = "GruvboxDark" end
    ---@diagnostic disable-next-line: unused-local, undefined-field
    theme = wezterm.color.get_builtin_schemes()[scheme_name]
    if theme == nil then
        theme = wezterm.color.load_scheme(wezterm.home_dir .. "/.config/wezterm/colors/" .. scheme_name .. ".toml")
    end

    return M
end

return M

