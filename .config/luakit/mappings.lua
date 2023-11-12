local webview = require("webview")
local modes = require("modes")
local settings = require("settings")

local actions = {
    yank_select = {
        desc = "Yank selection.",
        func = function(w)
            local text = luakit.selection.primary
            if not text then
                w:error("Empty selection.")
                return
            end
            luakit.selection.clipboard = text
            w:notify("Yanked selection: " .. text)
            luakit.selection.primary = ""
        end,
    },
    back = {
        desc = "Go back in history",
        func = function(w, m) w:back(m.count) end
    },
    forward = {
        desc = "Go forward in history",
        func = function(w, m) w:forward(m.count) end
    },
    reload = {
        desc = "Reload page",
        func = function(w) w:reload() end
    },
    open_under_cursor = {
        desc = "Open link under cursor",
        func = function(w, m)
            -- Ignore button 2 clicks in form fields
            if not m.context.editable then
                -- Open hovered uri in new tab
                local uri = w.view.hovered_uri
                if uri then
                    w:new_tab(uri, { switch = false, private = w.view.private })
                end
            end
        end
    },
    open_clip_in_new = {
        desc = "Open clipboard in new tab",
        func = function(w, m)
            local uri = luakit.selection.clipboard
            -- Ignore multi-line selection contents
            if uri then
                w:new_tab(uri, { switch = true, private = w.view.private })
            end
        end
    },
    open_sel_in_new = {
        desc = "Open selection in new tab",
        func = function(w, m)
            local uri = luakit.selection.primary
            -- Ignore multi-line selection contents
            if uri then
                w:new_tab(uri, { switch = true, private = w.view.private })
            end
        end
    },
}

modes.remove_binds("normal", {
    "d",
    "pp", "pt", "pw", "PP", "PT", "PW",
    "<Control-a>", "<Control-x>",
    "O", "T", "W", "Y",
})

modes.remap_binds("normal", {
    { "s",           "f",           false },
    { "<Control-v>", "<control-z>", false },
    { "<Control-l>", "<shift-o>", false },
    { "O", "t", false },
    { "<Control-O>", "w", false },
})

modes.add_binds("normal", {
    { "y",           actions.yank_select },
    { "u",           actions.back },
    { "<Mouse8>",    actions.back },
    { "<Back>",      actions.back },
    { "<Control-r>", actions.reload },
    { "<F5>",        actions.reload },
    { "<Mouse9>",    actions.forward },
    { "<Forward>",   actions.forward },
    { "<Mouse2>",    actions.open_under_cursor },
    { "p",           actions.open_clip_in_new },
    { "P",           actions.open_sel_in_new },
    -- { "<any>", "test", function(w, m) w:notify(tostring(m.key)) end }
})

modes.add_cmds({ { ":yank", actions.yank_select }, })
-- w stands for window
-- modes.add_binds("normal", {})

modes.add_binds("all", {
    { "<Scroll>", "Scroll the current page.", function(win, opts)
        win:scroll({ yrel = settings.get_setting("window.scroll_step") * opts.dy })
    end },
    -- { "<Mouse1>", "" }
})



-- v stands for view
-- webview.add_signal("init", function(view)
--     view:add_signal("populate-popup", function(v, menu)
--         -- local prettyPrint = require 'vendor/inspect'
--         -- local prettyPrint = require('pl.pretty').dump
--         table.insert(menu, { "New Reload", 13 })
--         table.insert(menu, true)
--         table.insert(menu, { "Test", function() webview.window(v):notify("Test") end })
--         -- table.insert(menu, {"Test", function () prettyPrint("asd") end})
--         -- prettyPrint(menu)
--     end)
-- end)
