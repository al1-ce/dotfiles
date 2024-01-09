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

# alias logout "loginctl terminate-user $USER"
alias clear "printf '\033c'"
alias logoff "logout"
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
alias rm "rm -i"
alias ln "ln -i"

alias fs "cd -"

alias dcat "/usr/bin/cat"

alias dcat /usr/bin/cat
# bat
alias bat "bat --tabs 4 --color always --paging always --theme gruvbox-dark"
# copy-cat
alias cat "bat --plain"

alias line "hr ─"

alias getcat "pxv -U https://cataas.com/cat -s fit"

# help
alias bathelp='bat --plain --language=help'
function help
    $argv --help 2>&1 | bathelp
end
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
alias dvim /usr/bin/vim
alias vim nvim
alias vi nvim
alias v nvim
alias e "nvim (gum file)"

alias tb taskbook

alias yd yandex-disk

alias music musikcube

alias setcursor '~/.dotfiles/scripts/setcursor.sh'

alias ytmp3 "yt-dlp -f 'ba' -x --audio-format wav"
alias feh "feh -Tdefault"

# function sudo
#     gum input --password | /usr/sbin/sudo -nS $argv 2>/dev/null
# end

alias jspp jsppext
alias pub "dart pub"

# ---------------------------------- WEB CLI --------------------------------- #
alias google='googler -l en -g en -x -c en'

function search
    if count $argv > /dev/null
        google -j $(google --np -n 50 $argv | fzf | sed "s/\d*?\.\s*?//")
    else
        echo 'Please supply search terms'
    end
end

# yewtube
alias web 'links -g'
alias webt 'links'

# ------------------------------------ GIT ----------------------------------- #
function backup
    git add .
    if count $argv > /dev/null
        git commit -m $argv
    else
        git commit -m "Updated: $(date +'%Y-%m-%d %H:%M:%S')"
    end
    git push origin master
end

function branch
    git branch 2> /dev/null | fzf | sed "s/.* //" | awk "{print $argv[1]}" | xargs git checkout
end

alias ga "git add"
alias gc "git commit"
alias gp "git push"

# ----------------------------------- PROGS ---------------------------------- #
alias wttr 'curl wttr.in/Moscow'
alias remind 'cat ~/.dotfiles/remind'
alias clock 'tty-clock -s -c -C 7'
alias cmatrix 'cmatrix -C yellow'
alias nms 'nms -a'

alias clearvswap 'echo "Removing nvim swap."; rm -rf ~/.local/state/nvim/swap'

alias fixpacman 'sudo ntpd -qg && sudo hwclock -w'

# function godot
#     cd ~/Godot
#     ./Godot_* &
#     cd ~
# end
#
# function godot-quiet
#     set WD $PWD
#     cd ~/Godot
#     nohup ./Godot_* & 
#     cd $WD
# end

#jp2a --colors --color-depth=8 --chars=" .,:;!-~=+÷*JS?#%@AX" --width="${PV_WIDTH}" "${FILE_PATH}" && exit 4
#jp2a --colors --color-depth=8 --chars=" ░▒▓█" --width="${PV_WIDTH}" "${FILE_PATH}" && exit 4

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

set NAP_THEME gruvbox

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

    # cls
end
