stty -ixon

setopt histignorespace
# setopt append_history
setopt hist_reduce_blanks
setopt hist_ignore_dups
setopt hist_expire_dups_first
setopt share_history
setopt auto_cd
setopt no_beep
# setopt inc_append_history

set -o emacs
# set -o vi

unsetopt BEEP
unsetopt bang_hist
# unsetopt zle

autoload -Uz compinit && compinit

autoload -Uz run-help
(( ${+aliases[run-help]} )) && unalias run-help
alias help=run-help

autoload -z edit-command-line
zle -N edit-command-line
bindkey "^X^E" edit-command-line

# case insensitive completion
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|='
zstyle ':completion:*' rehash true

autoload -U add-zle-hook-widget

export VI_KEYMAP="INS"

function line_pre_redraw {
    local previous_vi_keymap="${VI_KEYMAP}"
    # echo "${ZLE_STATE}"

    case "${KEYMAP}" in
        vicmd)
            case "${REGION_ACTIVE}" in
                1)
                    export VI_KEYMAP="VIS"
                    ;;
                2)
                    export VI_KEYMAP="V-L"
                    ;;
                *)
                    export VI_KEYMAP="NOR"
                    ;;
            esac
            ;;
        viins|main)
            if [[ "${ZLE_STATE}" == *overwrite* ]]; then
                export VI_KEYMAP="REP"
            else
                export VI_KEYMAP="INS"
            fi
            ;;
    esac

    if [[ "${VI_KEYMAP}" != "${previous_vi_keymap}" ]]; then
        zle reset-prompt
        export VI_KEYMAP="INS"
    fi

}
add-zle-hook-widget zle-line-pre-redraw line_pre_redraw

