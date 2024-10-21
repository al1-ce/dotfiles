#!/bin/fish

# alias ls    "eza   --color=auto"
_has grep  && alias grep  "grep  --color=auto"
_has fgrep && alias fgrep "fgrep --color=auto"
_has egrep && alias egrep "egrep --color=auto"

# alias ll "ls -alF"
# alias la "ls -A"
# alias l  "ls -CF"

_has eza && alias ls "eza"
alias l  "ls -l"
alias lf "ls -lF"
alias la "ls -a"
alias ll "ls -aghl"

_has pkm && alias pkg "pkm"

# alias logout "loginctl terminate-user $USER"
alias clear "printf '\033c'"
alias logout "exit"
alias logoff "exit"
alias logon "login"

# Better use Alt + S
# alias please 'sudo $(history -p !!)'
alias .. 'cd ../'
alias ... 'cd ../..'
alias .... 'cd ../../..'
alias ..... 'cd ../../../..'
alias mkdir 'mkdir -pv'
# alias srcrc 'source ~/.bashrc'
alias cwd pwd
alias scratch 'tput smcup && tput clear'
alias normal 'tput rmcup'

alias mv "mv -i"
alias cp "cp -i"
# rm -I gonna ask after 3 files. rm -i always asks
# alias rm "rm -I"
_has trash && alias rm "trash"
alias ln "ln -i"

alias fs "cd -"

# alias dcat "/usr/bin/cat"

# alias dcat /usr/bin/cat
# bat
# alias bat "bat --tabs 4 --color always --paging always --theme gruvbox-dark"
# copy-cat
_has bat && alias bat "bat --plain"

_has hr && alias line "hr ─"

_has pxv && alias getcat "pxv -U https://cataas.com/cat -s fit"

# help
_has bat && alias bathelp='bat --plain --language=help'
# function help
#     $argv --help 2>&1 | bathelp
# end
# ---------------------------------- ALIASES --------------------------------- #
# alias alias-update='source ~/.dotfiles/.bash_aliases'
# alias alias-edit='vim ~/.dotfiles/.bash_aliases'

alias npm "~/.dotfiles/scripts/npm.js"

alias trruen "trans -e google -I -hl ru -t en"
alias trenru "trans -e google -I -hl en -t ru"

abbr !! --position anywhere --function last_history_item

function last_history_item --description 'Last command for !! abbreviation'
    echo $history[1]
end

# ---------------------------------------------------------------------------- #
#                                     APPS                                     #
# ---------------------------------------------------------------------------- #

# ------------------------------------ cli ----------------------------------- #
_has neofetch && alias neofetch 'neofetch --config ~/.dotfiles/.neofetch-themes/basic.conf'
if _has onefetch
    alias onefetch 'onefetch --true-color never --no-title -d authors -d churn -d lines-of-code -d commits --no-color-palette'
    alias gitfetch 'onefetch -d created -d last-change -d project -d url -d size --no-art -d languages -d contributors -d version -d license'
    alias gitshort 'gitfetch | tr "\n" " "'
end
_has ncal && alias calendar 'ncal -yMb'
alias doomsday '~/.dotfiles/bin/doomsday-clock'

if _has nvim
    # alias v nvim
    alias nv nvim
    alias e "nvim (gum file)"
end
# alias awesome-check "Xephyr :5 & sleep 1 ; DISPLAY=:5 awesome"
alias ls-fonts 'fc-list  --format="%{family[0]} %{style[0]}\n" | sort | uniq | fzf'

_has taskbook && alias tb taskbook

_has musikcube && alias music musikcube
_has fman && alias fman "fman --theme gruvbox --icons none"

if _has buckle
    alias buckle-start 'buckle -f & disown'
    alias buckle-stop 'pkill buckle'
end

if _has yadm
    function yadm-add
        yadm add -u
        yadm add ~/.local/share/nvim/templates -f
        yadm add ~/.local/share/qutebrowser/greasemonkey -f
        yadm add ~/.dotfiles
        yadm add ~/.config/wezterm
        yadm add ~/.config/qtile
    end
end

function detach
    $argv & disown
end

function silent
    set -l tfile "$(mktemp)"
    echo "Redirecting output to '$tfile'"
    nohup $argv > $tfile &
end

function clean-dir
    /bin/rm -rf ".Trash-1000"
    /bin/rm -rf "\$RECYCLE.BIN"
    /bin/rm -rf "System Volume Information"
    /bin/rm -rf "pagefile.sys"
end

function clean-dir-force
    sudo /bin/rm -rf ".Trash-1000"
    sudo /bin/rm -rf "\$RECYCLE.BIN"
    sudo /bin/rm -rf "System Volume Information"
    sudo /bin/rm -rf "pagefile.sys"
end

# alias setcursor '~/.dotfiles/scripts/setcursor.sh'

# alias ytmp3 "yt-dlp -f 'ba' --embed-metadata --embed-thumbnail -x --audio-format mp3"
_has feh && alias feh "feh -Tdefault"
# alias scrape "wget -r -p -l 10 -E -k -N -w 2 --random-wait"

function scrape
    if count $argv > /dev/null
        set -l ddir "$(echo $argv | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/')-$(date +'%Y-%m-%d')"
        echo -e "\e[1mWebsite \"$argv\" will now be scraped\e[0m"
        echo -e "\e[1mDownload dir is \"$ddir\"\e[0m"
        echo -e "\e[2mThis will take a while since\e[0m"
        echo -e "\e[2meach request will be made in\e[0m"
        echo -e "\e[2mbetween 1 and 3 seconds\e[0m"
        echo ""
        wget -r -p -l 10 -E -k -N -w 2 --random-wait $argv -P $ddir
    else
        echo "Please supply website address"
    end
end

_has dart && alias pub "dart pub"
alias make-ls "grep : Makefile | awk -F: '/^[^.]/ {print $1;}'"

# ---------------------------------- WEB CLI --------------------------------- #
# _has googler && alias googler'googler -l en -g en -x -c en'
# _has s && alias s 's --provider=duckduckgo'
#
# function search
#     if count $argv > /dev/null
#         google -j $(google --np -n 50 $argv | fzf | sed "s/\d*?\.\s*?//")
#     else
#         echo 'Please supply search terms'
#     end
# end

function remetamp3
    set -l filein $argv

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
end

_has reuse && alias reuse "reuse --suppress-deprecation"

# ----------------------------------- PROGS ---------------------------------- #
alias wttr 'curl wttr.in/Moscow'
# alias remind 'cat ~/.dotfiles/remind'
_has tty-clock && alias clock 'tty-clock -s -c -C 7'
_has cmatrix && alias cmatrix 'cmatrix -C yellow'
_has nms && alias nms 'nms -a'

alias clearvswap 'echo "Removing nvim swap."; rm -rf ~/.local/state/nvim/swap'

alias pacman-time 'sudo ntpd -qg && sudo hwclock -w'
alias pacman-clean 'pacman -Qtdq | sudo pacman -Rns -'

_has qtile && alias qtile-restart 'qtile cmd-obj -o cmd -f restart'

# ---------------------------------- Telnet ---------------------------------- #
_has telnet && alias mapscii 'telnet mapscii.me'

# ---------------------------------- SERVERS --------------------------------- #
# alias server-start 'python3 -m http.server 8080 --bind 127.0.0.1'
# http-server

function psearch
    if count $argv > /dev/null
        ps axu | grep $argv[1]
    else
        echo "Please supply process name"
    end
end

# TODO: extract

# ---------------------------------------------------------------------------- #
#                                     X GUI                                    #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                               ENV CUSTOMISATION                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                STARTUP SCRIPT                                #
# ---------------------------------------------------------------------------- #

alias j jobs

function unalias
    gum confirm "Do you want to unalias $argv?" --selected.background="208" && \
    functions --erase $argv
end

# alias cls=bash-startup-func
#
# bash-startup-func() {
#     clear
#     # neofetch
#
#     echo "   ___  __  __       ____  ____"
#     echo "  / _ |/ /_/ /  ___ / __ \/ __/"
#     echo " / __ / __/ _ \/ -_ /_/ /\ \  "
#     echo "/_/ |_\__/_//_/\__/\____/___/  "
# }
if status --is-interactive
    alias cls "clear && ~/.dotfiles/bin/fetch"

    ~/.dotfiles/bin/fetch

    set -l fish_version (fish -v)
    [ $fish_version != "fish, version 3.7.1" ] && figlet "FIX BLOCK HISTORY THING"

    function __starship_prompt_builder --on-event fish_prompt
        # hr "─"
        set -xg JOB_COUNT (jobs | wc -l)
        if jobs | grep -q nvim
            set -xg STARSHIP_SHOW_NVIM true
        else
            set -xg STARSHIP_SHOW_NVIM false
        end

        if begin; [ $STARSHIP_SHOW_NVIM = false ] ;and [ $JOB_COUNT -gt 0 ] ;end ;or begin; [ $STARSHIP_SHOW_NVIM = true ] ;and [ $JOB_COUNT -gt 1 ] ;end
            set -xg STARSHIP_SHOW_JOBS true
        else
            set -xg STARSHIP_SHOW_JOBS false
        end
    end

    function __delete_history --on-event fish_postexec
        string match -qr '^fg$' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^j$' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^jobs$' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^bg$' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^ranger-cd$' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^s ' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
    end
end
