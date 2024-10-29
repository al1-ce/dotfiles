__has() {
    command -v $@ 2>&1 >/dev/null && return 0 || return 1
}

detach() {
    $@ & disown
}

silent() {
    tfile="$(mktemp)"
    echo "Redirecting output to '$tfile'"
    nohup $@ > $tfile &
}

clean-dir() {
    /bin/rm -rf ".Trash-1000"
    /bin/rm -rf "\$RECYCLE.BIN"
    /bin/rm -rf "System Volume Information"
    /bin/rm -rf "pagefile.sys"
}

clean-dir-force() {
    sudo /bin/rm -rf ".Trash-1000"
    sudo /bin/rm -rf "\$RECYCLE.BIN"
    sudo /bin/rm -rf "System Volume Information"
    sudo /bin/rm -rf "pagefile.sys"
}

psearch() {
    if [ $# -gt 0 ]; then
        ps axu | grep $@[1]
    else
        echo "Please supply process name"
    fi
}

scrape() {
    if [ $# -gt 0 ]; then
        ddir="$(echo $@ | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/')-$(date +'%Y-%m-%d')"
        echo -e "\e[1mWebsite \"$@\" will now be scraped\e[0m"
        echo -e "\e[1mDownload dir is \"$ddir\"\e[0m"
        echo -e "\e[2mThis will take a while since\e[0m"
        echo -e "\e[2meach request will be made in\e[0m"
        echo -e "\e[2mbetween 1 and 3 seconds\e[0m"
        echo ""
        wget -r -p -l 10 -E -k -N -w 2 --random-wait $@ -P $ddir
    else
        echo "Please supply website address"
    fi
}

remetamp3() {
    filein=$@

    read -P "Title: " title
    read -P "Artist: " artist
    read -P "Album artist: " album_artist
    read -P "Album: " album
    read -P "Year: " year
    read -P "Track: " track
    read -P "Genre: " genre
    read -P "Comment: " comment

    ffmpeg -loglevel panic -i $filein \
        -metadata title=$title \
        -metadata artist=$artist \
        -metadata album_artist=$album_artist \
        -metadata album=$album \
        -metadata year=$year \
        -metadata track=$track \
        -metadata genre=$genre \
        -metadata comment=$comment \
        -c:a copy "$track. $artist - $title - out.mp3"
}

if __has $HOME/.dotfiles/unbin/confed; then
    conf() {
        if [ $# -gt 0 ]; then
            if [[ "$@" == "-"* ]]; then
                ~/.dotfiles/unbin/confed $@
                return 0
            fi
            tmp_path="$(~/.dotfiles/unbin/confed -p $@)"
            if [ "$tmp_path" = "" ]; then
                echo "Failed to find config or encoutered an error"
            else
                [ -f $tmp_path ] && cd "$(dirname $tmp_path)" || cd $tmp_path
                $EDITOR $tmp_path
            fi
        else
            echo "Please supply config name"
        fi
    }
fi

if __has selectrepodir.js; then
    repos() {
        cd $(selectrepodir.js)
    }
fi

if __has nvim; then
    nvim-switch() {
        nvim_current="$(basename $(readlink ~/.config/nvim))"
        rm ~/.config/nvim
        if [ test $nvim_current = "monolith.nvim" ]; then
            echo "Current configuration is $nvim_current"
            ln -sf ~/.config/despair.nvim ~/.config/nvim
        else
            echo "Current configuration is $nvim_current"
            ln -sf ~/.config/monolith.nvim ~/.config/nvim
        fi
        echo "Set Neovim configuration to $(basename $(readlink ~/.config/nvim))"
    }
fi

if __has yadm; then
    yadm-add() {
        yadm add -u
        yadm add ~/.local/share/nvim/templates -f
        yadm add ~/.local/share/qutebrowser/greasemonkey -f
        yadm add ~/.dotfiles
        yadm add ~/.config/wezterm
        yadm add ~/.config/qtile
    }
fi
