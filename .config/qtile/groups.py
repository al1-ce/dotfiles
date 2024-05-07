# Screen groups
from libqtile.config import Group, Match
from libqtile.config import ScratchPad, DropDown

from icons import icons

groups = [
    Group("WWW", label = icons["group_www"], layout="columns"),
    Group("SYS", label = icons["group_sys"], layout="columns"),
    Group("DEV", label = icons["group_dev"], layout="columns"),
    Group("DOC", label = icons["group_doc"], layout="columns"),
    Group("VBX", label = icons["group_vbx"], layout="columns"),
    Group("CHT", label = icons["group_cht"], layout="columns"),
    Group("MUS", label = icons["group_mus"], layout="columns"),
    Group("VID", label = icons["group_vid"], layout="columns"),
    Group("GFX", label = icons["group_gfx"], layout="columns"),
    ScratchPad("scratchpad", [
        DropDown("term", "kitty -T QuakeTerminal",
            match=Match(title="QuakeTerminal"), width=1, x=0, height=0.45, on_focus_lost_hide=True
            ),
        ])
    ]

