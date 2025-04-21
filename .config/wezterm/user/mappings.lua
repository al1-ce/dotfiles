---@diagnostic disable: undefined-field
local wezterm = require('wezterm')

local M = {}

M.keys = {
    { key = 'u',        mods = 'CTRL|SHIFT', action = wezterm.action.CharSelect({ copy_on_select = false, group = "RecentlyUsed" }) },
    { key = 'p',        mods = 'CTRL|SHIFT', action = wezterm.action.ActivateCommandPalette },
    { key = 'c',        mods = 'CTRL|SHIFT', action = wezterm.action.CopyTo("ClipboardAndPrimarySelection") },
    { key = 'Insert',   mods = 'CTRL',       action = wezterm.action.CopyTo("ClipboardAndPrimarySelection") },
    { key = 'v',        mods = 'CTRL|SHIFT', action = wezterm.action.PasteFrom("Clipboard") },
    { key = 'Insert',   mods = 'CTRL|SHIFT', action = wezterm.action.PasteFrom("Clipboard") },
    { key = 'PageUp',   mods = '',      action = wezterm.action.ScrollByPage(-0.5) },
    { key = 'PageDown', mods = '',      action = wezterm.action.ScrollByPage(0.5) },
    { key = 'F6',        mods = 'CTRL|SHIFT', action = wezterm.action.ShowDebugOverlay },
    { key = 'F5',        mods = 'CTRL|SHIFT', action = wezterm.action.ReloadConfiguration },
    { key = 'F9',        mods = 'CTRL|SHIFT', action = wezterm.action.DecreaseFontSize },
    { key = 'F10',        mods = 'CTRL|SHIFT', action = wezterm.action.IncreaseFontSize },
    { key = 'F11',        mods = 'CTRL|SHIFT', action = wezterm.action.ResetFontSize },
}

M.mouse = {
    {
        event = { Down = { streak = 1, button = 'Left' } },
        mods = 'CTRL',
        action = wezterm.action.OpenLinkAtMouseCursor,
    },
    {
        event = { Up = { streak = 1, button = 'Left' } },
        mods = 'NONE',
        action = wezterm.action.CompleteSelection('PrimarySelection'),
    },
    {
        event = { Up = { streak = 1, button = 'Left' } },
        mods = 'NONE',
        action = wezterm.action.CompleteSelection('PrimarySelection'),
    },
}

M.key_tables = {}

return M
