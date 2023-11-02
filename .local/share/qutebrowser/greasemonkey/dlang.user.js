// ==UserScript==
// @name dlang.org
// @match https://dlang.org/
// @match https://dlang.org/*
// @match https://*.dlang.org/*
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
body {
    color: #f5f5f5;
    background-color: #222020;
}

.columns .right-column .content-page {
    background-color: #333030;
}

.right-column {
    background-color: #222020;
}

code {
    background-color: #222020;
    color: #f0f0f0;
    border: 1px solid #333;
}

pre code {
    background: #222020;
    border: none;
}

.d_decl {
    background: #222020;
}

.quickindex {
    background: #222020;
}

.subnav, .subnav-helper {
    background: #222020;
}

.d_code, .d_code2 {
    background-color: #222020;
}
`)

