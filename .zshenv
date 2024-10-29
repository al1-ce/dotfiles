# XDG directories
export XDG_DATA_HOME=$HOME/.local/share
export XDG_CONFIG_HOME=$HOME/.config
export XDG_STATE_HOME=$HOME/.local/state
export XDG_DATA_DIRS=$HOME/.local/share:/usr/local/share:/usr/share
export XDG_CONFIG_DIRS=$HOME/.config:/etc/xdg
export XDG_CACHE_HOME=$HOME/.cache
export XDG_RUNTIME_DIR=/run/user/$(id -u)

# Normal path
typeset -U path PATH

path=($HOME/.appimages $path)
path=($HOME/.bin $path)
path=($HOME/.cargo/bin $path)
path=($HOME/.dotfiles/bin $path)
path=($HOME/.dotfiles/scripts $path)
path=($HOME/.dotfiles/scripts/git_scripts $path)
path=($HOME/.dotnet/ $path)
path=($HOME/.go/bin $path)
path=($HOME/.local/bin $path)
path=($HOME/.local/bin $path)
path=($HOME/.local/scripts $path)
path=($HOME/.local/share/bin $path)
path=($HOME/.local/share/npm/bin $path)
path=(/bin $path)
path=(/home/linuxbrew/.linuxbrew/bin $path)
path=(/sbin $path)
path=(/usr/bin $path)
path=(/usr/local/bin $path)
path=(/usr/local/homebrew/bin $path)
path=(/usr/sbin $path)
path=(/var/lib/flatpak/exports/bin/ $path)

# zsh config
export ZDOTDIR=$XDG_CONFIG_HOME/zsh
export HISTFILE=$XDG_DATA_HOME/zsh/history
export HISTZIE="12800"
export SAVEHIST="12800"

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

# Program path env
export CARGO_HOME=$HOME/.cargo/
export GOPATH=$HOME/.go/
export INVDIR="$HOME/.local/share/inventory"
export NODE_PATH="$(/bin/npm root --quiet -g)"
export RUBY_GEMS=$XDG_DATA_HOME/gem/ruby/3.0.0/
export RUBY_ROOT=/usr/lib/ruby/gems/3.0.0
export RUSTUP_HOME=$HOME/.rustup/
export ZK_NOTEBOOK_DIR="$HOME/zk"

# Program dependant path
path=($RUBY_GEMS $path)
path=($RUBY_ROOT $path)

export PATH
