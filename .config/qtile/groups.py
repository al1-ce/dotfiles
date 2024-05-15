# Screen groups
from libqtile.config import Group, Match
from libqtile.config import ScratchPad, DropDown

from icons import icons

group_names = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "S",
]

groups = [
    Group(name = group_names[0], label = icons["group_www"], layout="columns", persist = True, init = True),
    Group(name = group_names[1], label = icons["group_sys"], layout="columns", persist = True, init = True),
    Group(name = group_names[2], label = icons["group_dev"], layout="columns", persist = True, init = True),
    Group(name = group_names[3], label = icons["group_doc"], layout="columns", persist = True, init = True),
    Group(name = group_names[4], label = icons["group_vbx"], layout="columns", persist = True, init = True),
    Group(name = group_names[5], label = icons["group_cht"], layout="columns", persist = True, init = True),
    Group(name = group_names[6], label = icons["group_mus"], layout="columns", persist = True, init = True),
    Group(name = group_names[7], label = icons["group_vid"], layout="columns", persist = True, init = True),
    Group(name = group_names[8], label = icons["group_gfx"], layout="columns", persist = True, init = True),
    Group(name = group_names[9], label = icons["group_msc"], layout="columns", persist = True, init = True),
    ScratchPad(name = group_names[10], dropdowns = [
        DropDown("quake", "kitty -T QuakeTerminal",
            match=Match(title="QuakeTerminal"), width=1, x=0, height=0.45, on_focus_lost_hide=True
            ),
        ])
    ]

