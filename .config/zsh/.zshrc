
[ ! -n "$ZSH_ENV_WAS_SOURCED" ] && source "$HOME/.zshenv"

# No sense to load those things in non-tty mode
# if they're not touching env plus it'd pollute
# possible calls from other programs
if [[ $- == *i* ]]; then
    __has() {
        command -v $@ 2>&1 >/dev/null && return 0 || return 1
    }

    __zsource() {
        [ -e $@ ] && source $@
    }

    __zsource $ZDOTDIR/plugins.zsh

    __zsource $ZDOTDIR/aliases.zsh
    __zsource $ZDOTDIR/functions.zsh

    __zsource $ZDOTDIR/config.zsh
    __zsource $ZDOTDIR/keymap.zsh

    __zsource $ZDOTDIR/hooks.zsh

    __zsource $ZDOTDIR/motd.zsh
    __zsource $ZDOTDIR/prompt.zsh

    # For some reason it must be in zshrc???????
    typeset -A ZSH_HIGHLIGHT_STYLES

    ZSH_HIGHLIGHT_STYLES[alias]="fg=12"
    ZSH_HIGHLIGHT_STYLES[builtin]="fg=12"
    ZSH_HIGHLIGHT_STYLES[function]="fg=12"
    ZSH_HIGHLIGHT_STYLES[command]="fg=12"
    ZSH_HIGHLIGHT_STYLES[hashed-command]="fg=12"

    ZSH_HIGHLIGHT_STYLES[unknown-token]="fg=9"

    ZSH_HIGHLIGHT_STYLES[single-quoted-argument]="fg=10"
    ZSH_HIGHLIGHT_STYLES[double-quoted-argument]="fg=10"
fi

