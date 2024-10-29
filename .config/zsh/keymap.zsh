# LINK: https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Standard-Widgets
bindkey "^H" backward-kill-word # C-backspace C-h
bindkey "^D" kill-word          # C-del

bindkey "^[[1;5D" backward-word # C-left
bindkey "^[[1;5C" forward-word  # C-right

bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line
bindkey "^[[3~" delete-char
bindkey "^[[2~" self-insert-unmeta

bindkey -r "^S"                 # C-s (evil freeze thing?)

__zsource $ZDOTDIR/scripts/sudo.zsh
# Defined shortcut keys: [Esc] [Esc]
bindkey -M emacs '^[s' __sudo-command-line
bindkey -M vicmd '^[s' __sudo-command-line
bindkey -M viins '^[s' __sudo-command-line
