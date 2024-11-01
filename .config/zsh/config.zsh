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

unsetopt BEEP
unsetopt bang_hist

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

