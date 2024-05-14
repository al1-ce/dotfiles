#! /bin/bash

# DISABLING FKN GAOMON TOUCH STRIP; TURN OFF AND RUN xinput list TO SEE WHERE IT IS NOW IF IT ISNT WORKING
# xinput disable 9

# ---------------------------------------------------------------------------- #
#                                     BASH                                     #
# ---------------------------------------------------------------------------- #

# --------------------------------- COMMANDS --------------------------------- #
alias clear="printf '\033c'"
alias logoff='logout'
# alias cls='clear && neofetch'
alias please='sudo $(history -p !!)'
alias ..='cd ../'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias mkdir='mkdir -pv'
alias srcrc='source ~/.bashrc'
alias cwd=pwd
alias alt='tput smcup && tput clear'
alias nrm='tput rmcup'

# -------------------------- alias apt='sudo pamac' -------------------------- #
# apt() {
#     if [ $# -gt 0 ]; then
#         if [ "$1" = "search" ] || [ "$1" = "info" ] || [ "$1" = "list" ] || [ "$1" = "checkupdates" ]; then 
#             pamac "$@"
#         else
#             sudo pamac "$@"
#         fi
#     else
#         pamac "$@"
#     fi
# }



# ------------------------------- CONFIRMATIONS ------------------------------ #
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
alias ln='ln -i'

# ---------------------------------- EXA/LS ---------------------------------- #
alias ls='exa'
alias l='ls -l'
alias lf='ls -lF'
alias la='ls -a'
alias ll='ls -aghl'

# ------------------------------------ CAT ----------------------------------- #
# default cat
alias dcat=/usr/bin/cat
# bat
alias bat='bat --tabs 4 --color always --paging always --theme gruvbox-dark'
# copy-cat
alias cat='bat --plain'
# hr line alias
line() {
    hr ─
}
# git diff, overrides gnu diff
diff() {
    git diff --name-only --relative --diff-filter=d | xargs bat --paging always --diff --plain --style changes,header-filename,rule,numbers,snip
}
# pretty man
export MANPAGER="sh -c 'col -bx | bat --tabs 4 --color always --paging always -l man -p'"
# help
alias bathelp='bat --plain --language=help'
help() {
    "$@" --help 2>&1 | bathelp
}
export DELTA_PAGER='less -+X' # less -RF 

# ---------------------------------- ALIASES --------------------------------- #
# alias alias-update='source ~/.dotfiles/.bash_aliases'
# alias alias-edit='vim ~/.dotfiles/.bash_aliases'

# ---------------------------------------------------------------------------- #
#                                     APPS                                     #
# ---------------------------------------------------------------------------- #

# ------------------------------------ cli ----------------------------------- #
alias neofetch='neofetch --config ~/.dotfiles/.neofetch-themes/basic.conf'
alias calendar='ncal -yMb'
alias doomsday='~/.dotfiles/doomsday-clock'
alias dvim=/usr/bin/vim
alias vim=nvim
alias vi=nvim
alias v=nvim

alias jspp=jsppext

git-ls () {
	find . -maxdepth 1 -mindepth 1 -type d -exec sh -c "cd {} && git rev-parse --is-inside-work-tree > /dev/null && echo -n '\e[1m' && echo -n {} && echo -n '\e[0m \e[91m' &&  git status --porcelain | awk '/[MD?]+ /{c++} END {print \"M: \", c}' && rm -f statusShort && echo -n '\e[0m'" \;
}

# ---------------------------------- WEB CLI --------------------------------- #
alias google='googler -l en -g en -x -c en'
search () {
    if [ $# -eq 0 ]; then
        echo 'Please supply search terms'
        return
    fi
    google -j $(google --np -n 50 "$@" | luneta | sed "s/\d*?\.\s*?//")
}
# yewtube
alias web='links -g'
alias webt='links'

# ------------------------------------ GIT ----------------------------------- #
backup () {
    git add .
    if [ $# -gt 0 ]; then
        str="$*"
        git commit -m "$str"
    else
        git commit -m "Updated: `date +'%Y-%m-%d %H:%M:%S'`"
    fi
    git push origin master
}

branch() {
    git branch 2> /dev/null | luneta | sed "s/.* //" | awk '{print $1}' | xargs git checkout
}
# ---------------------------------- NOHUP & --------------------------------- #
# alias doomml='mono ~/.apps/dml/dml.exe &'
# alias nemo='nohup nemo &'
# alias kate='nohup kate &'
# alias cool-retro-term='nohup cool-retro-term &'
# alias gedit='nohup gedit &'
# personal fav
# alias blanket='nohup blanket &'
# gnome
# alias kvantummanager='nohup kvantummanager &'
# alias store='sudo synaptic'
# alias gnome-tweaks='nohup gnome-tweaks &'
# alias gnome-control-center='nohup gnome-control-center &'
# ui creators
# alias glade='nohup glade &'
# alias qtcreator='nohup qtcreator &'
# alias qml-launcher='nohup ~/.apps/qml-launcher/build/qml-launcher &'

run-quiet () {
        [[ $# -eq 0 ]] && echo "usage: run_quiet [program] [program_arg] [output_file]" && return 0

        nohup $1 -u $2 > $3 &
}

# ----------------------------------- PROGS ---------------------------------- #
alias wttr='curl wttr.in/Moscow'
alias remind='cat ~/.dotfiles/.command-reminder'
alias clock='tty-clock -s -c -C 7'
alias cmatrix='cmatrix -C yellow'
alias enter-the-shell='mpv --quiet -vo=caca .dotfiles/gits-op.mp4'
alias nms='nms -a'

godot () {
    cd ~/Godot
    ./Godot_* &
    cd ~
}

godot-quiet () {
    WD=$PWD
    cd ~/Godot
    nohup ./Godot_* & 
    cd $WD 
}

#jp2a --colors --color-depth=8 --chars=" .,:;!-~=+÷*JS?#%@AX" --width="${PV_WIDTH}" "${FILE_PATH}" && exit 4
#jp2a --colors --color-depth=8 --chars=" ░▒▓█" --width="${PV_WIDTH}" "${FILE_PATH}" && exit 4

# ---------------------------------- Telnet ---------------------------------- #
alias mapscii='telnet mapscii.me'

# ---------------------------------- SERVERS --------------------------------- #
alias server-start='python3 -m http.server 8080 --bind 127.0.0.1'
# http-server

psearch () {
        [[ $# -eq 0 ]] && echo "Please supply process name" && return 0
        ps axu | grep -- "$1"
}

# ---------------------------------------------------------------------------- #
#                                     X GUI                                    #
# ---------------------------------------------------------------------------- #

rotate-screen () {
    [[ $# -eq 0 ]] && printf "usage: rotate-screen [screen] [orientation]\nscreen: left, center, right\norientation: normal, left, right, inverted\n" && return 0
    [[ "$1" == "left" ]] && xrandr --output DP-1 --rotate $2 && return 0
    [[ "$1" == "center" ]] && xrandr --output DP-2 --rotate $2 && return 0
    [[ "$1" == "right" ]] && xrandr --output HDMI-0 --rotate $2 && return 0
    echo "Screen is incorrect"
}

# ---------------------------------------------------------------------------- #
#                               ENV CUSTOMISATION                              #
# ---------------------------------------------------------------------------- #

export NAP_THEME=gruvbox

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

alias cls="clear && ~/.dotfiles/bin/fetch"

cls
