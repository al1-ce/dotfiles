local wezterm = require('wezterm')

-- https://github.com/Tecate/bitmap-fonts

local M = {
    -- https://github.com/microsoft/cascadia-code
    cascadia = {
        regular = {family = 'Cascadia Mono PL', weight = 'Regular', style = 'Normal', italic = false},
        size = 11,
        brighten = false,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Cascadia Mono PL', weight = 'Bold', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Cascadia Mono PL', weight = 'Regular', style = 'Italic', italic = true})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Cascadia Mono PL', weight = 'Bold', style = 'Italic', italic = true})
            },
        }
    },

    -- https://github.com/IdreesInc/Miracode
    miracode = {
        regular = {family = 'Miracode', weight = 'Regular', style = 'Normal', italic = false},
        size = 11,
        brighten = true,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Miracode', weight = 'Regular', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Miracode', weight = 'Regular', style = 'Normal', italic = true})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Miracode', weight = 'Regular', style = 'Normal', italic = true})
            },
        }
    },

    -- https://github.com/zshoals/Dina-Font-TTF-Remastered
    dina_remaster = {
        regular = {family = 'DinaRemaster', weight = 'Regular', style = 'Normal', italic = false},
        size = 12,
        brighten = false,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'DinaRemaster', weight = 'Bold', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'DinaRemaster', weight = 'Regular', style = 'Normal', italic = false})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'DinaRemaster', weight = 'Bold', style = 'Normal', italic = false})
            },
        }
    },

    -- https://github.com/sunaku/tamzen-font/
    tamzen = {
        regular = {family = 'Tamzen', weight = 'Regular', style = 'Normal', italic = false},
        size = 12,
        brighten = false,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Tamzen', weight = 'Bold', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Tamzen', weight = 'Regular', style = 'Normal', italic = false})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Tamzen', weight = 'Bold', style = 'Normal', italic = false})
            },
        }
    },

    -- https://www.dcmembers.com/jibsen/download/61/
    dina = {
        regular = {family = 'Dina', weight = 'Regular', style = 'Normal', italic = false},
        size = 12,
        brighten = false,
        cell_width = 0.7,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Dina', weight = 'Bold', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Dina', weight = 'Regular', style = 'Italic', italic = false})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Dina', weight = 'Bold', style = 'Italic', italic = false})
            },
        }
    },

    -- https://terminus-font.sourceforge.net/
    terminus = {
        regular = {family = 'Terminus', weight = 'Regular', style = 'Normal', italic = false},
        size = 12,
        brighten = false,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Terminus', weight = 'Bold', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Terminus', weight = 'Regular', style = 'Normal', italic = false})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Terminus', weight = 'Bold', style = 'Normal', italic = false})
            },
        }
    },

    -- https://github.com/slavfox/Cozette
    cozette = {
        regular = {family = 'Cozette', weight = 'Medium', style = 'Normal', italic = false},
        size = 12,
        brighten = true,
        cell_width = 1.0,
        line_height = 1.0,
        rules = {
            {
                intensity = "Bold", italic = false,
                font = wezterm.font({family = 'Cozette', weight = 'Medium', style = 'Normal', italic = false})
            },
            {
                intensity = "Normal", italic = true,
                font = wezterm.font({family = 'Cozette', weight = 'Medium', style = 'Normal', italic = false})
            },
            {
                intensity = "Bold", italic = true,
                font = wezterm.font({family = 'Cozette', weight = 'Medium', style = 'Normal', italic = false})
            },
        }
    },
}

return M
