# Screen groups
from libqtile.config import Group, Match
from libqtile.config import ScratchPad, DropDown

from icons import icons

groups = [
    Group(name = "0", label = icons["group_www"], layout="columns", persist = True, init = True),
    Group(name = "1", label = icons["group_sys"], layout="columns", persist = True, init = True),
    Group(name = "2", label = icons["group_dev"], layout="columns", persist = True, init = True),
    Group(name = "3", label = icons["group_doc"], layout="columns", persist = True, init = True),
    Group(name = "4", label = icons["group_vbx"], layout="columns", persist = True, init = True),
    Group(name = "5", label = icons["group_cht"], layout="columns", persist = True, init = True),
    Group(name = "6", label = icons["group_mus"], layout="columns", persist = True, init = True),
    Group(name = "7", label = icons["group_vid"], layout="columns", persist = True, init = True),
    Group(name = "8", label = icons["group_gfx"], layout="columns", persist = True, init = True),
    Group(name = "9", label = icons["group_msc"], layout="columns", persist = True, init = True),
    ScratchPad(name = "scratch", dropdowns = [
        DropDown("term", "kitty -T QuakeTerminal",
            match=Match(title="QuakeTerminal"), width=1, x=0, height=0.45, on_focus_lost_hide=True
            ),
        ])
    ]

