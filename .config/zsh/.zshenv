# Normal PATH
# typeset -U PATH PATH

export PATH="$HOME/.appimages:$PATH"
export PATH="$HOME/.bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"
export PATH="$HOME/.dotfiles/scripts:$PATH"
export PATH="$HOME/.dotfiles/scripts/git_scripts:$PATH"
export PATH="$HOME/.dotnet/:$PATH"
export PATH="$HOME/.go/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.local/scripts:$PATH"
export PATH="$HOME/.local/share/bin:$PATH"
export PATH="$HOME/.local/share/npm/bin:$PATH"
export PATH="/bin:$PATH"
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
export PATH="/sbin:$PATH"
export PATH="/usr/bin:$PATH"
export PATH="/usr/local/bin:$PATH"
export PATH="/usr/local/homebrew/bin:$PATH"
export PATH="/usr/sbin:$PATH"
export PATH="/var/lib/flatpak/exports/bin/:$PATH"

# zsh config
export HISTFILE="$XDG_DATA_HOME/zsh/history"
export HISTZIE="8192"
export SAVEHIST="8192"

# Misc env
export DXVK_ASYNC=1
export EDITOR="/usr/sbin/nvim"
export FILE_PICKER_CMD="ranger"
export HAS_ALLOW_UNSAFE="y"
export HOMEBREW_NO_ENV_HINTS=true
export MANPAGER="$PAGER"
export NAP_THEME="gruvbox"
export PAGER="less --use-color -R"
export RANGER_LOAD_DEFAULT_RC=false
export SHELL=/bin/zsh
export STARSHIP_LOG="error"
export TERM="xterm-256color"
export WEBKIT_DISABLE_COMPOSITING_MODE=1

# artix-dark-theme-git
export GTK_THEME="Artix-dark"
export QT_QPA_PLATFORMTHEME="qt5ct"

# Program PATH env
export CARGO_HOME=$HOME/.cargo/
export GOPATH=$HOME/.go/
export INVDIR="$HOME/.local/share/inventory"
export NODE_PATH="$(/bin/npm root --quiet -g)"
export BUNDLE_PATH=$XDG_DATA_HOME/gem/
# export RUBY_ROOT=/usr/lib/ruby/gems/3.0.0
export RUSTUP_HOME=$HOME/.rustup/
export ZK_NOTEBOOK_DIR="$HOME/zk"
export LYNX_CFG="$XDG_CONFIG_HOME/lynx/lynx.cfg"
[ -d "/g" ] && export DEVDOCS_DIR="/g/devdocs/" || export DEVDOCS_DIR="$XDG_DATA_HOME/devdocs/"

# Program dependant PATH
# PATH="$RUBY_GEMS:$PATH"
# PATH="$RUBY_ROOT:$PATH"

for dir in $XDG_DATA_HOME/gem/ruby/*/bin; do
    [ -d "$dir" ] && export PATH="$dir:$PATH"
done

export PATH="$(echo "$PATH" | awk -v RS=':' -v ORS=":" '!a[$1]++{if (NR > 1) printf ORS; printf $a[$1]}')"

