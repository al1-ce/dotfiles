#!/bin/fish

# alias ls    "eza   --color=auto"
alias grep  "grep  --color=auto"
alias fgrep "fgrep --color=auto"
alias egrep "egrep --color=auto"

# alias ll "ls -alF"
# alias la "ls -A"
# alias l  "ls -CF"

alias ls "eza"
alias l  "ls -l"
alias lf "ls -lF"
alias la "ls -a"
alias ll "ls -aghl"

alias pkg "pkm"

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
alias alt 'tput smcup && tput clear'
alias nrm 'tput rmcup'

alias mv "mv -i"
alias cp "cp -i"
# rm -I gonna ask after 3 files. rm -i always asks
alias rm "rm -I"
alias ln "ln -i"

alias fs "cd -"

# alias dcat "/usr/bin/cat"

# alias dcat /usr/bin/cat
# bat
# alias bat "bat --tabs 4 --color always --paging always --theme gruvbox-dark"
# copy-cat
alias bat "bat --plain"

alias line "hr ─"

alias getcat "pxv -U https://cataas.com/cat -s fit"

# help
alias bathelp='bat --plain --language=help'
# function help
#     $argv --help 2>&1 | bathelp
# end
# ---------------------------------- ALIASES --------------------------------- #
# alias alias-update='source ~/.dotfiles/.bash_aliases'
# alias alias-edit='vim ~/.dotfiles/.bash_aliases'

# ---------------------------------------------------------------------------- #
#                                     APPS                                     #
# ---------------------------------------------------------------------------- #

# ------------------------------------ cli ----------------------------------- #
alias neofetch 'neofetch --config ~/.dotfiles/.neofetch-themes/basic.conf'
alias onefetch 'onefetch --true-color never --no-title -d authors -d churn -d lines-of-code -d commits --no-color-palette'
alias gitfetch 'onefetch -d created -d last-change -d project -d url -d size --no-art -d languages -d contributors -d version -d license'
alias gitshort 'gitfetch | tr "\n" " "'
alias calendar 'ncal -yMb'
alias doomsday '~/.dotfiles/bin/doomsday-clock'
alias v nvim
alias e "nvim (gum file)"
alias awesome-check "Xephyr :5 & sleep 1 ; DISPLAY=:5 awesome"
alias ls-fonts 'fc-list  --format="%{family[0]} %{style[0]}\n" | sort | uniq | fzf'

alias tb taskbook

alias music musikcube
alias fman "fman --theme gruvbox --icons none"

function detach
    $argv & disown
end

# alias setcursor '~/.dotfiles/scripts/setcursor.sh'

# alias ytmp3 "yt-dlp -f 'ba' --embed-metadata --embed-thumbnail -x --audio-format mp3"
alias feh "feh -Tdefault"
# alias scrape "wget -r -p -l 10 -E -k -N -w 2 --random-wait"

function scrape
    if count $argv > /dev/null
        echo -e "\e[1mWebsite \"$argv\" will now be scraped\e[0m"
        echo -e "\e[2mThis will take a while since\e[0m"
        echo -e "\e[2meach request will be made in\e[0m"
        echo -e "\e[2mbetween 1 and 3 seconds\e[0m"
        echo ""
        wget -r -p -l 10 -E -k -N -w 2 --random-wait $argv
    else
        echo "Please supply website address"
    end
end

alias pub "dart pub"
alias make-ls "grep : Makefile | awk -F: '/^[^.]/ {print $1;}'"

# ---------------------------------- WEB CLI --------------------------------- #
alias google='googler -l en -g en -x -c en'

function search
    if count $argv > /dev/null
        google -j $(google --np -n 50 $argv | fzf | sed "s/\d*?\.\s*?//")
    else
        echo 'Please supply search terms'
    end
end

alias reuse "reuse --suppress-deprecation"

# ----------------------------------- PROGS ---------------------------------- #
alias wttr 'curl wttr.in/Moscow'
alias remind 'cat ~/.dotfiles/remind'
alias clock 'tty-clock -s -c -C 7'
alias cmatrix 'cmatrix -C yellow'
alias nms 'nms -a'

alias clearvswap 'echo "Removing nvim swap."; rm -rf ~/.local/state/nvim/swap'

alias pacman-time 'sudo ntpd -qg && sudo hwclock -w'
alias pacman-clean 'pacman -Qtdq | sudo pacman -Rns -'

alias qtile-restart 'qtile cmd-obj -o cmd -f restart'

# ---------------------------------- Telnet ---------------------------------- #
alias mapscii 'telnet mapscii.me'

# ---------------------------------- SERVERS --------------------------------- #
alias server-start 'python3 -m http.server 8080 --bind 127.0.0.1'
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

# alias cls=bash-startup-func
#
# bash-startup-func() {
#     clear
#     # neofetch
#
#     echo "   ___  __  __       ____  ____"
#     echo "  / _ |/ /_/ /  ___ / __ \/ __/"
#     echo " / __ / __/ _ \/ -_) /_/ /\ \  "
#     echo "/_/ |_\__/_//_/\__/\____/___/  "
# }
if status --is-interactive
    cod init $fish_pid fish | source
    alias cls "clear && ~/.dotfiles/bin/fetch"

    ~/.dotfiles/bin/fetch

    set -l fish_version (fish -v)
    [ $fish_version != "fish, version 3.7.1" ] && figlet "FIX BLOCK HISTORY THING"

    function __starship_prompt_builder --on-event fish_prompt
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
        string match -qr '^fg' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^bg' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
        string match -qr '^ranger-cd' -- $argv
        and history delete --exact --case-sensitive -- (string trim -r $argv)
    end
end
