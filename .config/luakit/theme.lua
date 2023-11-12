--------------------------
-- Default luakit theme --
--------------------------

local theme = {}

local bg =      "#282828"
local gray =    "#928374"
local brgray =  "#a89984"
local fg =      "#ebdbb2"
local red =     "#cc231d"
local bred =    "#fb4934"
local green =   "#98971a"
local bgreen =  "#b8bb26"
local yellow =  "#d79921"
local byellow = "#fabd2f"
local blue =    "#458588"
local bblue =   "#83a598"
local purple =  "#b16286"
local bpurple = "#d3869b"
local aqua =    "#689d6a"
local baqua =   "#8ec07c"
local orange =  "#d65d0e"
local borange = "#fe8019"
local bg0_h =   "#1d2021"
local bg0 =     "#282828"
local bg0_s =   "#32302f"
local bg1 =     "#3c3836"
local bg2 =     "#504945"
local bg3 =     "#665c54"
local bg4 =     "#7c6f64"
local bg5 =     "#928374"
local fg4 =     "#a89984"
local fg3 =     "#bdae93"
local fg2 =     "#d5c4a1"
local fg1 =     "#ebdbb2"
local fg0 =     "#fbf1c7"

-- Default settings
theme.font = "12px monospace"
theme.fg   = fg
theme.bg   = bg

-- Genaral colours
theme.success_fg = baqua
theme.loaded_fg  = bblue
theme.error_fg = fg
theme.error_bg = bred

-- Warning colours
theme.warning_fg = bred
theme.warning_bg = bg

-- Notification colours
theme.notif_fg = fg
theme.notif_bg = bg3

-- Menu colours
theme.menu_fg                   = fg
theme.menu_bg                   = bg
theme.menu_selected_fg          = bg0_h
theme.menu_selected_bg          = bblue
theme.menu_title_bg             = bg5
theme.menu_primary_title_fg     = bg
theme.menu_secondary_title_fg   = bg1

theme.menu_disabled_fg = bg4
theme.menu_disabled_bg = theme.menu_bg
theme.menu_enabled_fg = theme.menu_fg
theme.menu_enabled_bg = theme.menu_bg
theme.menu_active_fg = baqua
theme.menu_active_bg = theme.menu_bg

-- Proxy manager
theme.proxy_active_menu_fg      = fg
theme.proxy_active_menu_bg      = bg
theme.proxy_inactive_menu_fg    = fg2
theme.proxy_inactive_menu_bg    = bg2

-- Statusbar specific
theme.sbar_fg         = fg
theme.sbar_bg         = bg

-- Downloadbar specific
theme.dbar_fg         = fg
theme.dbar_bg         = bg
theme.dbar_error_fg   = red

-- Input bar specific
theme.ibar_fg           = fg
theme.ibar_bg           = "rgba(0,0,0,0)"

-- Tab label
theme.tab_fg            = fg3
theme.tab_bg            = bg0_h
theme.tab_hover_bg      = bg0_s
theme.tab_ntheme        = fg2
theme.selected_fg       = fg
theme.selected_bg       = bg
theme.selected_ntheme   = fg2
theme.loading_fg        = baqua
theme.loading_bg        = bg

theme.selected_private_tab_bg = purple
theme.private_tab_bg    = bpurple

-- Trusted/untrusted ssl colours
theme.trust_fg          = green
theme.notrust_fg        = red

-- Follow mode hints
theme.hint_font = "12px monospace, courier, sans-serif"
theme.hint_fg = bg
theme.hint_bg = fg
theme.hint_border = "none" -- css value
theme.hint_opacity = "0.3"
theme.hint_overlay_bg = bg3
theme.hint_overlay_border = "none"
theme.hint_overlay_selected_bg = bg3
theme.hint_overlay_selected_border = theme.hint_overlay_border

-- General colour pairings
theme.ok = { fg = fg, bg = bg }
theme.warn = { fg = red, bg = fg }
theme.error = { fg = fg, bg = red }

-- Gopher page style (override defaults)
theme.gopher_light = { bg = bg, fg = fg, link = blue }
theme.gopher_dark  = { bg = bg0_h, fg = fg, link = borange }

return theme

-- vim: et:sw=4:ts=8:sts=4:tw=80

