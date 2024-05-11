// ==UserScript==
// @name dpldocs.info
// @match https://dpldocs.info/*
// @match https://*.dpldocs.info/*
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
    --fg: #f5f5f5;
    --code: #f0f0f0;
    --border: 1px solid #333;
    --back: #222020;
    --bg: #333030;
    --link: #9bc2e3;
}

body, th, tr, td, ul, li, dl, dt, .markdown-body, #top, #page-nav {
    color: var(--fg) !important;
    background-color: var(--bg) !important;
}

.markdown-body, .simplified-prototype {
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

.type-constructor, .builtin-type {
    color: #48db48 !important;
}

.member-list dt .simplified-prototype {
    color: var(--code) !important;
}

.kwrd, .highlighted-keyword, .lang-feature, .storage-class {
    color: #4883f9 !important;
}

.member-list dt .simplified-prototype:hover {
    background-color: var(--back);
    border: var(--border);
    box-shadow: none !important;
}

.function-prototype .attributes {
    color: #dbcb7b;
}

tt.D, .inline-code {
    color: var(--code);
    background-color: var(--back);
}

.com, .highlighted-comment {
    color: #ababab;
}
`)

