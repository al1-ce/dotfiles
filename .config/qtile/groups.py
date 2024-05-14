# Screen groups
from libqtile.config import Group, Match
from libqtile.config import ScratchPad, DropDown

from icons import icons

scratch_name = "P"

groups = [
    Group(name = "Q", label = icons["group_www"], layout="columns", persist = True, init = True),
    Group(name = "R", label = icons["group_sys"], layout="columns", persist = True, init = True),
    Group(name = "S", label = icons["group_dev"], layout="columns", persist = True, init = True),
    Group(name = "T", label = icons["group_doc"], layout="columns", persist = True, init = True),
    Group(name = "U", label = icons["group_vbx"], layout="columns", persist = True, init = True),
    Group(name = "V", label = icons["group_cht"], layout="columns", persist = True, init = True),
    Group(name = "W", label = icons["group_mus"], layout="columns", persist = True, init = True),
    Group(name = "X", label = icons["group_vid"], layout="columns", persist = True, init = True),
    Group(name = "Y", label = icons["group_gfx"], layout="columns", persist = True, init = True),
    Group(name = "Z", label = icons["group_msc"], layout="columns", persist = True, init = True),
    ScratchPad(name = scratch_name, dropdowns = [
        DropDown("quake", "kitty -T QuakeTerminal",
            match=Match(title="QuakeTerminal"), width=1, x=0, height=0.45, on_focus_lost_hide=True
            ),
        ])
    ]

