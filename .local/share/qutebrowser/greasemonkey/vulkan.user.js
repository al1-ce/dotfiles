// ==UserScript==
// @name vulkan-tutorial.com
// @match https://vulkan-tutorial.com/
// @match https://vulkan-tutorial.com/*
// @match https://*.vulkan-tutorial.com/*
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

a {
    color: #9bc2e3;
    text-decoration: none;
    border: none;
}

a:hover {
    color: #cbcef0;
    text-decoration: none;
    border: none;
}
`)
