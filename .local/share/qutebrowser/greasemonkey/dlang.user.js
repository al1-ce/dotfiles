// ==UserScript==
// @name dlang.org
// @match https://dlang.org/
// @match https://dlang.org/*
// @description
// @include
// ==/UserScript==

function add_css(css_string) {
    let head = document.head;

    let new_css = document.createElement("style");
    new_css.type = "text/css";
    new_css.innerHTML = css_string;

    head.append(new_css);
}

add_css(`
body, th, tr, td {
    color: #f5f5f5 !important;
    background-color: #222020 !important;
}

code {
    background-color: #222020 !important;
    color: #f0f0f0 !important;
    border: 1px solid #333 !important;
}

pre code {
    background: #222020 !important;
    border: none !important;
}

.d_decl, .quickindex, subnav,
.subnav-helper, d_code, .d_code2,
.post-info, pre, .subnav {
    background-color: #222020 !important;
}

.hljs-keyword, .hljs-selector-tag, .hljs-built_in, .hljs-name, .hljs-tag {
    color: #9bc2e3 !important;
}

.site {
    background-color: #222020 !important;
}

.site-header h1 a, .site-header h2 a {
    color: #f5f5f5;
}
`)

