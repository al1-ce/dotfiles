local modes = require("modes")
local io = require("stdio")

local js_popup_open = io.read_file(luakit.config_dir .. "/popup_open.js")
local js_popup_close = io.read_file(luakit.config_dir .. "/popup_close.js")

local function create_popup(w, text)
    w.view:eval_js(js_popup_open, {
        no_return = true,
        callback = function(_, e) w:error(e) end,
    })
end

local function delete_popup(w)
    w.view:eval_js(js_popup_close, {
        no_return = true,
        callback = function(_, e) w:error(e) end,
    })
end

modes.new_mode("hydra", "Hydra menu mode", {
    leave = function(w) delete_popup(w) end,
    reset_on_focus = true,
    reset_on_navigation = true,
}, false)

modes.new_mode("input_custom", [[Test input text]], {
    enter = function (w)
        w:set_prompt("!")
        w:set_input("")
    end,
    activate = function (w, text)
        w:set_input("")
        w:notify(text)
    end    -- history = {maxlen = 50},
})


local function set_mode(w, mode, reset_prompt)
    reset_prompt = reset_prompt or false
    if not w:is_mode("passthrough") then
        if reset_prompt then w:set_prompt() end
        w:set_mode(mode)
    end
    return not w:is_mode("passthrough")
end

local hintGit = [[
┌     git     ┐
  s: Status    
  b: Branches  
  c: Commits   
  S: Stash     
  g: GUI       
               
  q: Quit      
└             ┘]]


-- w stands for window
modes.add_binds("normal", {
    { "\\", "Open Hydra",
    function(w)
        w:notify(hintGit)
        set_mode(w, "hydra")
    end},
    { ";", "Open Popup",
    function(w)
        create_popup(w, "Test")
    end}
})

modes.add_binds("hydra", {
    { "s", "Test", function(w) w:notify("Status!!!"); set_mode(w, "normal") end },
    { "b", "Test", function(w) w:notify("Branches!!!"); set_mode(w, "normal") end },
    { "c", "Test", function(w) w:notify("Commits!!!"); set_mode(w, "normal") end },
    { "S", "Test", function(w) w:notify("Stash!!!"); set_mode(w, "normal") end },
    { "g", "Test", function(w) w:notify("GUI!!!"); set_mode(w, "normal") end },
    { "<Escape>", "Return to `normal` mode.", function(w) set_mode(w, "normal", true) end},
    { "q", "Return to `normal` mode.", function(w) set_mode(w, "normal", true) end},
    { "\\", "Return to `normal` mode.", function(w) set_mode(w, "normal", true) end},
})

