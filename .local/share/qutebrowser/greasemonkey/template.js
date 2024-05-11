// ==UserScript==
// @name template
// @match TEMPLATE_WEBSITE
// @match TEMPLATE_WEBSITE
// @description
// @include
// ==/UserScript==
/*
function add_css(css_string) {
    let head = document.head;

    let new_css = document.createElement("style");
    new_css.type = "text/css";
    new_css.innerHTML = css_string;

    head.append(new_css);
}

add_css(`

:root {
    --bg:      #282828;
    --gray:    #928374;
    --brgray:  #a89984;
    --fg:      #ebdbb2;
    --red:     #cc231d;
    --bred:    #fb4934;
    --green:   #98971a;
    --bgreen:  #b8bb26;
    --yellow:  #d79921;
    --byellow: #fabd2f;
    --blue:    #458588;
    --bblue:   #83a598;
    --purple:  #b16286;
    --bpurple: #d3869b;
    --aqua:    #689d6a;
    --baqua:   #8ec07c;
    --orange:  #d65d0e;
    --borange: #fe8019;
    --bg0_h:   #1d2021; /* bg0 hard */
    --bg0:     #282828;
    --bg0_s:   #32302f; /* bg0 soft */
    --bg1:     #3c3836;
    --bg2:     #504945;
    --bg3:     #665c54;
    --bg4:     #7c6f64;
    --bg5:     #928374;
    --fg4:     #a89984;
    --fg3:     #bdae93;
    --fg2:     #d5c4a1;
    --fg1:     #ebdbb2;
    --fg0:     #fbf1c7;
}

body, th, tr, td, ul, li, dl, dt {
    color: var(--fg) !important;
    background-color: var(--bg) !important;
}

code, input, button, blockquote {
    background-color: var(--bg0_h) !important;
    color: var(-0fg2) !important;
    border: none !important;
}
`)

