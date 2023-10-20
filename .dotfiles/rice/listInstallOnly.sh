yay -S --needed $(awk '!/^ *#/ && NF' pkglist.conf) --nodiffmenu --noeditmenu --nouseask --nocleanmenu
