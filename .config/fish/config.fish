#!/bin/fish

function _has
    command -v $argv 2>&1 >/dev/null && return 0 || return 1
end

function __on_pwd_change --on-variable PWD --description 'Do rvm stuff'
    status --is-command-substitution; and return
    # Uncomment for instant fetch
    if test -e .git
        _has onefetch && gitshort || git status
        echo -e "\n"
    else if test $PWD -ef $HOME
        # ~/.dotfiles/bin/fetch
    end

    # Uncomment for instant LS
    ls
end

# PATH
fish_add_path -Ppg /usr/bin /bin /usr/sbin /sbin /usr/local/homebrew/bin /usr/local/bin
fish_add_path -Ppg $HOME/.bin  $HOME/.local/bin /var/lib/flatpak/exports/bin/
fish_add_path -Ppg ~/.cargo/bin
fish_add_path -Ppg ~/.local/bin
fish_add_path -Ppg ~/.local/scripts
fish_add_path -Ppg ~/.local/share/bin
fish_add_path -Ppg ~/.local/share/npm/bin
fish_add_path -Ppg ~/.appimages
fish_add_path -Ppg ~/.dotnet/
fish_add_path -Ppg ~/.dotfiles/bin
fish_add_path -Ppg ~/.dotfiles/scripts
fish_add_path -Ppg ~/.dotfiles/scripts/git_scripts
fish_add_path -Ppg /home/linuxbrew/.linuxbrew/bin
fish_add_path -Ppg ~/.go/bin

set -xg CARGO_HOME ~/.cargo/
set -xg RUSTUP_HOME ~/.rustup/
set -xg GOPATH ~/.go/
set -xg RUBY_GEMS ~/.local/share/gem/ruby/3.0.0/
set -xg RUBY_ROOT /usr/lib/ruby/gems/3.0.0
set -xg NODE_PATH "$(/bin/npm root --quiet -g)"
set -xg SHELL /bin/fish

fish_add_path -Ppg $RUBY_GEMS
fish_add_path -Ppg $RUBY_ROOT

# OTHER
set fish_greeting
set -xg TERM "xterm-256color"
set -xg EDITOR nvim
set -xg PAGER "less --use-color -R"
set -xg MANPAGER "$PAGER"
set -xg HOMEBREW_NO_ENV_HINTS true
set -xg HAS_ALLOW_UNSAFE y
set -xg RANGER_LOAD_DEFAULT_RC false
set -xg FILE_PICKER_CMD ranger
set -xg DXVK_ASYNC 1
set -xg WEBKIT_DISABLE_COMPOSITING_MODE 1
set -xg NAP_THEME gruvbox
set -xg INVDIR "$HOME/.local/share/inventory"
set -xg STARSHIP_LOG "error"
set -xg ZK_NOTEBOOK_DIR "$HOME/zk"

# set -xg MANPAGER "sh -c 'col -bx | bat --tabs 4 --color always --paging always -l man -p'"
# set -xg DELTA_PAGER "less -+X" # less -RF

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

function fish_should_add_history
    for cmd in ls fg bg ranger-cd
       string match -qr "^$cmd" -- $argv; and return 1
    end
    return 0
end

source ~/.config/fish/plugins.fish
source ~/.config/fish/aliases.fish

if status --is-interactive
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

    stty -ixon

    bind \ch backward-kill-word
    bind \e\[3\;5~ kill-word
    # IDK what it was
    bind \e\[1\;3P ''
    bind \e\[1\;5A ''
    bind \e\[1\;5B ''

    alias srcrc "source ~/.config/fish/config.fish"

    # bind \b backward-kill-word

    _has starship && starship init fish | source
    _has jj && jj util completion fish | source

    # ~/.config/fish/functions/ranger.fish
    if _has ranger
        function ranger-cd
            set tempfile (mktemp -t tmp.XXXXXX)
            command ranger --choosedir=$tempfile $argv
            set return_value $status

            if test -s $tempfile
                set ranger_pwd (cat $tempfile)
                if test -n $ranger_pwd -a -d $ranger_pwd
                    cd -- $ranger_pwd
                else
                    echo $ranger_pwd "is not a directory"
                end
            end

            command rm -f -- $tempfile
            return $return_value
        end

        bind \cs "commandline ranger-cd; commandline -f execute"
    end
end
