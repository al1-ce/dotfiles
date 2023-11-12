local function load(m, do_direct)
    do_direct = do_direct or false
    if do_direct then require(m) return end
    local ok, err = pcall(require, m)
    if not ok then
        require("msg").warn("Module \"" .. m .. "\" failed to load. \n\n" .. err)
        return
    end
    return ok
end

load("config", false)
load("mappings", true)
load("hydra", false)

