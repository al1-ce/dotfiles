// ==UserScript==
// @name code.dlang.org
// @match https://code.dlang.org/
// @match https://code.dlang.org/*
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

:root {
    --fg: #f5f5f5;
    --code: #f0f0f0;
    --border: 1px solid #333;
    --back: #222020;
    --bg: #333030;
    --link: #9bc2e3;
}

body, th, tr, td, ul, li, dl, dt, .markdown-body, #top {
    color: var(--fg) !important;
    background-color: var(--bg) !important;
}

.markdown-body {
    border: var(--border) !important;
}

code, input, button, blockquote {
    background-color: var(--back) !important;
    color: var(--code) !important;
    border: var(--border) !important;
}

button img {
    -webkit-filter: invert(100%);
    filter: invert(100%);
}

pre code {
    background: var(--back) !important;
    border: none !important;
}

.d_decl, .quickindex, subnav,
.subnav-helper, d_code, .d_code2,
.post-info, pre, .subnav {
    background-color: var(--back) !important;
}

.hljs-keyword, .hljs-selector-tag, .hljs-built_in, .hljs-name, .hljs-tag {
color: var(--link) !important;
}

.subtabsHeader+div.repositoryReadme, section.pkgconfig {
    background-color: var(--back) !important;
    border: 1px solid var(--border) !important;
}
`)

