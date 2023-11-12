(()=>{
    window.onscroll = function() {
        var box = document.getElementById("luakit_popup");
        var scroll = window.scrollY;
        box.style.top = "calc(" + scroll + "px + 50%)";
    };

    var __box = document.getElementById("luakit_popup");
    if (__box) __box.remove();

    let body = document.children[0];

    let div = document.createElement("div");
    div.innerHTML = "SOMETHING";
    div.id = "luakit_popup";
    div.style = "position: absolute;" +
                "right: 0; top: 50%;" +
                "color: red; background-color: white;";

    body.append(div);
    var box = document.getElementById("luakit_popup");
    var scroll = window.scrollY;
    box.style.top = "calc(" + scroll + "px + 50%)";
})();
