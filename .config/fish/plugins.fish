if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end

# Sends notification when long process is done
fundle plugin "franciscolourenco/done"
# Auto-pair
fundle plugin "laughedelic/pisces"
# Expand .., !! and !$
fundle plugin "nickeb96/puffer-fish"

fundle init
