stty -ixon

setopt histignorespace
setopt append_history
setopt hist_reduce_blanks
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

# case insensitive completion
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|='
zstyle ':completion:*' rehash true

