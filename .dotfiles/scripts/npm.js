#!/usr/bin/env -S npx jsh
/// <reference path="/home/al1-ce/.dotfiles/nvdefs/js/jsh.d.ts" />
/// https://github.com/bradymholt/jsh

// const text = readFile(env["HOME"] + "/.dotfiles/remind");
// const lines = text.split("\n");
//
// for (let i = 0; i < lines.length - 1; ++i) {
//     const line = lines[i];
//     if (line.startsWith("#")) {
//         echo("\x1b[2m\x1b[4m" + line + "\x1b[0m");
//     } else {
//         echo(line);
//     }
// }

echo.gray = function (content) { echo("\x1b[37m%s\x1b[0m", content); }

function join_array(arr, sep) {
    let str = "";
    for (let i = 0; i < arr.length; ++i) {
        if (i != 0) str += sep;
        str += arr[i];
    }
    return str;
}

function npx(arg) {
    // echo(join_array(arg, ' '));
    exec(`/bin/npm ${join_array(arg, ' ')}`);
}

function confirm(text, p_default) {
    let answer = read(() => { printf(text + (p_default ? " [Y/n]: " : " [y/N]: ")) }).toLowerCase()[0];
    if (answer == '\n' || answer == undefined) return p_default;
    if (answer == 'y') return true;
    if (answer == 'n') return false;
    echo("Please type 'y' or 'n'");
    return confirm(text, p_default);
}

usage(`\
Usage:
    ${$0} [flags] [command]

Flags:
    --global, -g : Do command globally

Commands:
    install, i : Installs package
    remove, r : Removes package
`);

let npm_args = [];
let argv = [$0].concat(args);
for (let i = 0; i < argv.length; ++i) {
    if (argv[i].startsWith('-')) {
        argv.splice(i, 1);
        --i;
    }
}
let argc = argv.length;

let global = args.g || args.global;

if (global) {
    npm_args.push("--global");
}

if (argc == 1) { usage.printAndExit(0); }

function get_global_state(global) {
    return "\x1b[1m" + (global ? "\x1b[4mglobal" : "\x1b[31mlocal") + "\x1b[0m";
}

function print_package(package) {
    try {
        let result = $(`/bin/npm info ${package}`);
        // echo(result);
        let skip_space = false;
        let tab_space = false;
        for (let line of result.split('\n')) {
            if (skip_space && line != "") continue;
            if (skip_space && line == "") { skip_space = false; continue; }
            if (tab_space && line == "") { tab_space = false; }
            if (line.startsWith("keywords")) { skip_space = true; continue; }
            if (line.startsWith("dist")) { skip_space = true; continue; }
            if (line.startsWith("maintainers")) { skip_space = true; continue; }
            if (line.startsWith("dist-tags")) { skip_space = true; continue; }
            if (line.startsWith("published")) { skip_space = true; continue; }
            // if (line.startsWith("")) { skip_space = true; continue; }
            if (line.includes("deps: ")) { echo.green(line); } else
                if (line.startsWith("https")) { echo.gray(line); } else
                    if (tab_space) { echo.gray("    " + line); } else
                        echo(line);
            if (line.startsWith("dependencies")) { tab_space = true; }
        }
        echo.gray("----------------------------------------------");
        return true;
    } catch (err) {
        echo.red(`Package ${package} was not found`);
        return false;
    }
}

function print_packages(packages) {
    let pkgs = [];
    for (let package of packages) {
        if (print_package(package)) pkgs.push(package);
    }
    return pkgs;
}

if (argv[1] == "i" || argv[1] == "install") {
    if (argc == 2) {
        echo("Installinf packages from package.json");
        npm_args.push("install");
        npx(npm_args);
        exit(0);
    }
    let pkgnames = argv; pkgnames.splice(0, 2);
    pkgnames = print_packages(pkgnames);
    if (pkgnames.length == 0) { echo("No packages available for intallation"); }
    let do_install = confirm(`\nInstall ${get_global_state(global)} package(s) '${join_array(pkgnames, ", ")}'?`);
    if (do_install) {
        echo(`Installing '${join_array(pkgnames, ", ")}'`);
        npm_args.push("install");
        npm_args = npm_args.concat(pkgnames);
        npx(npm_args);
    } else {
        echo("Aborted");
    }
    exit(0);
}

if (argv[1] == "r" || argv[1] == "remove") {
    if (argc == 2) { error("Must provide package name", 1); }
    let pkgnames = argv; pkgnames.splice(0, 2);
    let do_remove = confirm(`Remove ${get_global_state(global)} package(s) '${join_array(pkgnames, ", ")}'?`);
    if (do_remove) {
        echo(`Removing '${join_array(pkgnames, ", ")}'`);
        npm_args.push("remove");
        npm_args = npm_args.concat(pkgnames);
        npx(npm_args);
    } else {
        echo("Aborted");
    }
    exit(0);
}

echo("Unhandled command, executing as is");
npx(args)
