#!/bin/fish

# if stats is-login
    # if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        # exec startx -- -keeptty
    # end
# end

function fish_prompt
    # set_color $fish_color_cwd
    # echo -n (prompt_pwd)
    # set_color normal
    # echo -n ' > '
    # powerline-shell --shell bare $status
end

function fish_right_prompt -d "Write out the right prompt"
    # set_color brblack
    # date '+%H:%M:%S'
    # set_color normal
end

function __on_pwd_change --on-variable PWD --description 'Do rvm stuff'
    status --is-command-substitution; and return
    # Uncomment for instant fetch
    if test -e .git
        gitshort
        echo -e "\n"
    else if test $PWD -ef $HOME
        # ~/.dotfiles/bin/fetch
    end

    # Uncomment for instant LS
    ls
end

# IDK what it was
bind \e\[1\;3P ''

function tere
    set --local result (command tere $argv)
    [ -n "$result" ] && cd -- "$result"
end

# Maybe https://gist.github.com/britishtea/39ad478fa5180e1432a2

# If ~/.inputrc doesn't exist yet: First include the original /etc/inputrc
# so it won't get overriden
# if test -e ~/.inputrc
#     echo '$include /etc/inputrc' > ~/.inputrc
# end

# Add shell-option to ~/.inputrc to enable case-insensitive tab completion
echo '$include /etc/inputrc' > ~/.inputrc
echo 'set completion-ignore-case On' >> ~/.inputrc
echo '"\e[5~": previous-history' >> ~/.inputrc
echo '"\e[6~": next-screen-line' >> ~/.inputrc
echo '"\e[1;3P": ""' >> ~/.inputrc
# echo '"\\C-H": "backward-kill-word"' >> ~/.inputrc
# stty werase \^H
# echo '"\\C-H": "\\C-W"' >> ~/.inputrc
# already defined rc
# echo '"\e[3;5~": kill-word' >> ~/.inputrc
# echo '"\e[H": beginning-of-line' >> ~/.inputrc
# echo '"\e[F": end-of-line' >> ~/.inputrc

# PATH 
fish_add_path -Ppg /usr/bin /bin /usr/sbin /sbin /usr/local/homebrew/bin /usr/local/bin
fish_add_path -Ppg $HOME/.bin  $HOME/.local/bin /var/lib/flatpak/exports/bin/ 
fish_add_path -Ppg ~/.cargo/bin
fish_add_path -Ppg ~/.local/bin
fish_add_path -Ppg ~/.local/scripts
fish_add_path -Ppg ~/.local/share/bin
fish_add_path -Ppg ~/.appimages
fish_add_path -Ppg ~/.dotnet/
fish_add_path -Ppg ~/.dotfiles/bin
fish_add_path -Ppg /home/linuxbrew/.linuxbrew/bin

set CARGO_HOME ~/.cargo/
set RUSTUP_HOME ~/.rustup/
set GOPATH ~/.go/
set RUBY_GEMS ~/.local/share/gem/ruby/3.0.0/
set RUBY_ROOT /usr/lib/ruby/gems/3.0.0

set SHELL /bin/fish

fish_add_path -Ppg $RUBY_GEMS
fish_add_path -Ppg $RUBY_ROOT

# OTHER
set fish_greeting
set -g -x TERM "xterm-256color"
set -g -x EDITOR nvim
set HOMEBREW_NO_ENV_HINTS true
set HAS_ALLOW_UNSAFE y
set -g -x RANGER_LOAD_DEFAULT_RC false
set -g -x FILE_PICKER_CMD ranger
set -g -x DXVK_ASYNC 1

set MANPAGER "sh -c 'col -bx | bat --tabs 4 --color always --paging always -l man -p'"
set DELTA_PAGER "less -+X" # less -RF 

set fish_color_normal brwhite
set fish_color_autosuggestion brblack
set fish_color_command brblue
# set fish_color_error brwite -i
set fish_color_error brred
set fish_color_param brwhite
set fish_color_quote brgreen
set fish_color_redirection brcyan
set fish_color_end brcyan


function setmode
    if count $argv > /dev/null
        if test "$argv[1]" = "v"
            fish_vi_key_bindings
        else
            fish_default_key_bindings
        end
    else
        echo "Mode must be [n] or [v]"
    end
end

function git-ls
    find . -maxdepth 1 -mindepth 1 -type d -exec sh -c "cd {} && git rev-parse --is-inside-work-tree > /dev/null && echo -n '\e[1m' && echo -n {} && echo -n '\e[0m \e[91m' &&  git status --porcelain | awk '/[MD?]+ /{c++} END {print \"M: \", c}' && rm -f statusShort && echo -n '\e[0m'" \;
end

# function ex
#     if test -f $argv[1]
#         switch "$argv[1]"
#             case   '*.tar.bz2'    tar xjf $1   
#             case   "*.tar.gz"    tar xzf $1   
#             case   "*.bz2"       bunzip2 $1   
#             case   "*.rar"       unrar x $1   
#             case   "*.gz"        gunzip $1    
#             case   "*.tar"       tar xf $1    
#             case   "*.tbz2"      tar xjf $1   
#             case   "*.tgz"       tar xzf $1   
#             case   "*.zip"       unzip $1     
#             case   "*.Z"         uncompress $1
#             case   "*.7z"        7z x $1      
#             case   '*'           echo "'$1' cannot be extracted via ex()"
#         end
#     else
#         echo "'$1' is not a valid file"
#     end
# end
# funcsave setmode

alias srcrc "source ~/.config/fish/config.fish"

source ~/.config/fish/plugins.fish
source ~/.config/fish/aliases.fish

bind \ch backward-kill-word
# bind \b backward-kill-word

starship init fish | source
