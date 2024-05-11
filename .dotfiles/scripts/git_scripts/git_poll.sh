#!/bin/fish

for f in $(find . -maxdepth 1 -type d)
    if test -d $f/.git
        set git_poll_output $(git -C $f status --porcelain)
        if test -n "$git_poll_output"
            printf "\e[4m%-20s %-4s\e[0m\n" $(echo "$f" | cut -c 3-) "$(git -C $f status --porcelain | wc -l)"
        end
    end
end

