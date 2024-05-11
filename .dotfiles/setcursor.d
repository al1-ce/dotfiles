#!/usr/bin/env dub
/+ dub.sdl:
name "setcursor"
targetType "executable"
targetPath "bin/"
// dependency "depname" version="~>1.0.0"
+/

import std.stdio: writeln, write, File, readln;
import std.array: join;
import std.path: absolutePath, buildNormalizedPath, expandTilde;
import std.algorithm: canFind;
import std.process: wait, spawnProcess;
import std.conv: to;
import std.file: readText, isFile, exists, FileException;

string fixPath(string path) {
    return path.expandTilde.buildNormalizedPath.absolutePath;
}

void writeFile(string path, string content) {
    string file = path.fixPath();
    File f;
    f = File(file, "w");
    f.write(content);
    f.close();
}

string readFile(string path) {
    string file = path.fixPath();
    if (!file.exists) return "";
    if (!file.isFile) return "";
    return readText(file);
}

const string PATH_THEME = "~/.icons/default/index.theme";
const string PATH_GTK = "~/.config/gtk-3.0/settings.ini";
const string PATH_XRESOURCES = "~/.Xresources";
const int[] CURSOR_SIZES = [16, 20, 22, 24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96];

int main(string[] args) {
    if (args.canFind("-h") || args.canFind("--help") || args.length == 1) {
        writeln("Usage: setcursor CursorName - sets cursor to CursorName");
        writeln("       setcursor current    - prints current cursor settings");
        writeln("       setcursor list       - lists cursors installed in /usr/share/");
        writeln("       setcursor sizes      - lists allowed cursor sizes");
        writeln("Example:");
        writeln("       setcursor Breeze_Light");
        return 0;
    }
    string cursorName = args[1..$].join();

    if (cursorName == "current") {
        writeln("\033[2m", PATH_THEME, "\033[0m");
        writeln(readFile(PATH_THEME));
        writeln();
        writeln("\033[2m", PATH_GTK, "\033[0m");
        writeln(readFile(PATH_GTK));
        writeln();
        writeln("\033[2m", PATH_XRESOURCES, "\033[0m");
        writeln(readFile(PATH_XRESOURCES));
        return 0;
    }

    if (cursorName == "list") {
        writeln("\033[2mListing available cursor themes\033[0m");
        string[] dirs = listdir("/usr/share/icons/", true, false);
        import std.algorithm.sorting: sort;
        import std.range: array;
        dirs = sort(dirs).array;
        foreach (dir; dirs) {
            if (listdir("/usr/share/icons/" ~ dir, true, false).canFind("cursors")) {
                writeln(dir);
            }
        }
        return 0;
    }

    if (cursorName == "sizes") {
        import std.algorithm: map;
        writeln("Allowed cursor sizes: ", CURSOR_SIZES.map!(to!string).join(' '));
        return 0;
    }

    if (!prompt("Set cursor to \"" ~ cursorName ~ "\"?", false)) {
        writeln("Aborting.");
        return 0;
    }

    int cursorSize = prompt("Cursor size, default - 32: ", 32);
    if (!CURSOR_SIZES.canFind(cursorSize)) {
        writeln("Unknown cursor size. Using default size of 32");
        cursorSize = 32;
    }

    writeFile(PATH_THEME, "[icon theme]\nInherits=" ~ cursorName);
    writeFile(PATH_GTK, "[Settings]\ngtk-cursor-theme-name=" ~ cursorName ~ "\ngtk-cursor-theme-size: " ~ cursorSize.to!string);
    writeFile(PATH_XRESOURCES, "Xcursor.theme: " ~ cursorName ~ "\nXcursor.size: " ~ cursorSize.to!string);

    wait(spawnProcess([
        "xfconf-query",
        "--channel",
        "xsettings",
        "--property",
        "/Gtk/CursorThemeName",
        "--set",
        cursorName
    ]));

    if (prompt("Restart?", true)) {
        writeln("Restarting");
        spawnProcess(["shutdown", "-r", "0"]);
        return 0;
    }

    if (prompt("Logout?", true)) {
        import core.stdc.stdlib: getenv;
        import std.string: fromStringz;
        writeln("Terminating current user");
        spawnProcess(["loginctl", "terminate-user", getenv("USER").fromStringz]);
        return 0;
    }

    return 0;
}

bool prompt(string msg, bool p_default) {
    if (p_default) write(msg ~ " [Y/n]: "); else write(msg ~ " [y/N]: ");
    char answer = readln()[0];
    if (answer == '\n') return p_default;
    if (answer == 'y' || answer == 'Y') return true;
    if (answer == 'n' || answer == 'N') return false;
    writeln("Please type 'y' or 'n'");
    return prompt(msg, p_default);
}

string prompt(string msg, string p_default) {
    write(msg ~ ": ");
    string answer = readln()[0..$-1];
    if (answer.length == 0) return p_default;
    return answer;
}

int prompt(string msg, int p_default) {
    import std.conv: parse;
    import std.string: isNumeric;

    write(msg ~ ": ");
    string answer = readln()[0..$-1];
    if (answer.length == 0) return p_default;

    if (answer.isNumeric) return parse!int(answer);
    writeln("Please type a number");
    return prompt(msg, p_default);
}

import std.path : absolutePath, buildNormalizedPath, expandTilde, relativePath;

/**
Normalises path, expands tilde and builds absolute path
Params:
  path = Path
Returns:
 */
string buildAbsolutePath(string p) {
    return p.expandTilde.absolutePath.buildNormalizedPath;
}

/**
Normalises path, expands tilde and builds relative path
Params:
  path = Path
Returns:
 */
string buildRelativePath(string p) {
    return p.expandTilde.relativePath.buildNormalizedPath;
}

/**
Returns array of files/dirs from path
Params:
  path = Path to dir
Returns:
 */
string[] listdir(string path, bool listDirs = true, bool listFiles = true) {
    import std.algorithm;
    import std.array;
    import std.file;
    import std.path;

    path = buildAbsolutePath(path);
    if (!exists(path) || !isDir(path)) return [];

    return std.file.dirEntries(path, SpanMode.shallow)
        .filter!(a => listFiles ? true : a.isFile || listDirs ? true : a.isDir)
        .map!((return a) => baseName(a.name))
        .array;
}

