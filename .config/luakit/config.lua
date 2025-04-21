local downloads = require("downloads")
local settings = require("settings")
local select = require("select")
local follow = require("follow")
local newtab_chrome = require("newtab_chrome")

downloads.default_dir = os.getenv("HOME") .. "/downloads"

downloads.add_signal("download-location", function(uri, file)
    if not file or file == "" then
        file = (string.match(uri, "/([^/]+)$")
            or string.match(uri, "^%w+://(.+)")
            or string.gsub(uri, "/", "_")
            or "untitled")
    end
    return downloads.default_dir .. "/" .. file
end)


settings.application.prefer_dark_mode = true

settings.completion.history.order = "visits"
settings.completion.max_items = 50

settings.session.always_save = true

require("lousy.widget.tablist") -- required to load
settings.tablist.always_visible = true

-- settings.webview.cursive_font_family = "serif"
-- settings.webview.fantasy_font_family = "serif"
-- settings.webview.monospace_font_family = "serif"
-- settings.webview.pictograph_font_family = "serif"
-- settings.webview.sans_serif_font_family = "serif"
-- settings.webview.serif_font_family = "serif"

settings.webview.enable_smooth_scrolling = true
settings.webview.enable_spatial_navigation = true
settings.webview.enable_webaudio = true
settings.webview.enable_webgl = true
settings.webview.enable_accelerated_2d_canvas = false
settings.webview.hardware_acceleration_policy = "never"

settings.webview.enable_developer_extras = true

settings.webview.allow_modal_dialogs = true

settings.webview.javascript_can_access_clipboard = true

settings.window.default_search_engine = "duckduckgo"
settings.window.home_page = "https://home.al1-ce.dev/"
settings.window.new_tab_page = "https://home.al1-ce.dev/"

settings.window.home_page = "https://home.al1-ce.dev/"

settings.window.search_engines = {
    ["default"] = "https://duckduckgo.com/?q=%s",
    ["duckduckgo"] = "https://duckduckgo.com/?q=%s",
    ["github"] = "https://github.com/search?q=%s",
    ["google"] = "https://google.com/search?q=%s",
    ["wikipedia"] = "https://en.wikipedia.org/wiki/Special:Search?search=%s",
}

-- newtab_chrome.new_tab_file = "https://home.al1-ce.dev/"
newtab_chrome.new_tab_src = [[ <script>window.location.href = 'https://home.al1-ce.dev/'</script> ]]

select.label_maker = function()
    ---@diagnostic disable-next-line: undefined-global
    -- local chars = interleave("asdgqwertzxcvbmf", "klhyuiopnj;")
    ---@diagnostic disable-next-line: undefined-global
    local chars = charset("asdghklqwertyuiopzxcvbnmfj;")
    ---@diagnostic disable-next-line: undefined-global
    return trim(reverse(chars))
end

follow.pattern_maker = follow.pattern_styles.match_label
