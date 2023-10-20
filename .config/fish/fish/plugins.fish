if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

# Sends notification when long process is done
fundle plugin "franciscolourenco/done"
# Simple bash usage "bass export X=0"
fundle plugin "edc/bass"
# Auto-pair
fundle plugin "laughedelic/pisces"
# Bang bang
# fundle plugin "oh-my-fish/plugin-bang-bang"
# Auto-clean history from errors
fundle plugin "meaningful-ooo/sponge"
# Expand .., !! and !$
fundle plugin "nickeb96/puffer-fish"
# Go "to project"
fundle plugin "joehillen/to-fish"

fundle init
