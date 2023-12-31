# Autogenerated config.py
config.load_autoconfig(True)

c.aliases = {
    'w': 'session-save',
    'q': 'close',
    'qa': 'quit',
    'wq': 'quit --save',
    'wqa': 'quit --save',
    'o': 'open',
    'yt': 'open https://youtube.com/',
    'gh': 'open https://github.com/al1-ce',
    'gl': 'open https://gitlab.com/',
    'tg': 'open https://web.telegram.org/k/',
    's': 'open',
    'g': 'open',
    'rund': 'open http://run.dlang.io/',
    'discord': 'open https://discord.com/channels/@me',
    'tg': 'open https://web.telegram.org/k/#',
    'ym': 'https://music.yandex.ru/home',
}

c.url.default_page = 'https://al1-ce.github.io/homepage/'
c.url.open_base_url = True

c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'p': 'https://phind.com/search?q={}',
    'g': 'https://google.com/search?q={}',
    'd': 'https://google.com/search?domains=dlang.org&q={}+site:dlang.org/phobos',
    'D': 'https://code.dlang.org/search?q={}',
    'a': 'https://wiki.archlinux.org/index.php?search={}',
    'gh': 'https://github.com/search?q={}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'tg': 'https://web.telegram.org/k/#?null={}',
    'ym': 'https://music.yandex.ru/home?null={}',
}

c.url.start_pages = ['https://al1-ce.github.io/homepage/']


c.auto_save.interval = 15000
c.auto_save.session = True

c.backend = 'webengine'

c.changelog_after_upgrade = 'minor'

# Background color for webpages if unset (or empty to use the theme's color).
c.colors.webpage.bg = '#282828'

# c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
# c.colors.webpage.darkmode.enabled = True
# c.colors.webpage.darkmode.grayscale.all = False
# c.colors.webpage.darkmode.grayscale.images = 0.0
# c.colors.webpage.darkmode.policy.images = 'smart'
# c.colors.webpage.darkmode.policy.page = 'smart'
# c.colors.webpage.darkmode.threshold.background = 205
# c.colors.webpage.darkmode.threshold.text = 150
# c.colors.webpage.preferred_color_scheme = 'auto'

# Completion
c.completion.cmd_history_max_items = 100
c.completion.delay = 0

# Default filesystem autocomplete suggestions for :open.
c.completion.favorite_paths = []

c.completion.height = '30%'
c.completion.min_chars = 1

c.completion.open_categories = [
    'searchengines',
    'quickmarks',
    'bookmarks',
    'history',
    'filesystem'
]

# Move on to the next part when there's only one possible completion left.
c.completion.quick = True

# Padding (in pixels) of the scrollbar handle in the completion window.
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 6
c.completion.show = 'always'
c.completion.shrink = True

c.completion.timestamp_format = '%H:%M %d/%m/%Y'

# Execute the best-matching command on a partial match.
c.completion.use_best_match = True

c.completion.web_history.exclude = []
# Number of URLs to show in the web history. 0: no history / -1: unlimited
c.completion.web_history.max_items = -1

c.confirm_quit = ['never']

c.content.autoplay = False

c.content.blocking.enabled = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.whitelist = []
c.content.headers.do_not_track = True

c.content.images = True

c.content.cookies.store = True
c.content.cookies.accept = "no-unknown-3rdparty"

# USER STYLE SHEETS
c.content.user_stylesheets = []

c.content.webgl = True
c.content.javascript.clipboard = "access-paste"

c.downloads.location.directory = "~/downloads/"
c.downloads.location.prompt = False
c.downloads.location.remember = True
c.downloads.location.suggestion = 'path'
# c.downloads.open_dispatcher = None
c.downloads.position = 'top'
c.downloads.remove_finished = 4000

c.editor.command = ['kitty', 'nvim', '-c', 'normal {line}G{column0}l', '--', '{file}']
c.editor.encoding = 'utf-8'
c.editor.remove_file = True

c.fileselect.folder.command = ['kitty', 'ranger', '--choosedir={}']
c.fileselect.handler = 'external'
c.fileselect.multiple_files.command = ['kitty', 'ranger', '--choosefiles={}']
c.fileselect.single_file.command = ['kitty', 'ranger', '--choosefile={}']

c.fonts.completion.category = 'bold default_size default_family'
c.fonts.completion.entry = 'default_size default_family'
c.fonts.contextmenu = 'default_size default_family'
c.fonts.debug_console = 'default_size default_family'
c.fonts.default_family = ['Cascadia Mono PL SemiLight']
c.fonts.default_size = '10pt'
c.fonts.hints = 'bold default_size default_family'
c.fonts.messages.error = 'bold default_size default_family'

# ############################### HINTS ############################# #
c.hints.auto_follow = 'unique-match'
c.hints.auto_follow_timeout = 0
c.hints.border = '1px solid #E1D2AB 0 0'
c.hints.chars = 'asdghklqwertyuiopzxcvbnmfj;'
# c.hints.dictionary = '/usr/share/dict/words'
# c.hints.hide_unmatched_rapid_hints = True
c.hints.leave_on_load = True
c.hints.min_chars = 1
c.hints.mode = 'letter'
c.hints.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
c.hints.radius = 0
c.hints.scatter = True
c.hints.uppercase = False
# c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']
# c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']
# c.hints.selectors = {'all': ['a', 'area', 'textarea', 'select', 'input:not([type="hidden"])', 'button', 'frame', 'iframe', 'img', 'link', 'summary', '[contenteditable]:not([contenteditable="false"])', '[onclick]', '[onmousedown]', '[role="link"]', '[role="option"]', '[role="button"]', '[role="tab"]', '[role="checkbox"]', '[role="menuitem"]', '[role="menuitemcheckbox"]', '[role="menuitemradio"]', '[ng-click]', '[ngClick]', '[data-ng-click]', '[x-ng-click]', '[tabindex]:not([tabindex="-1"])'], 'links': ['a[href]', 'area[href]', 'link[href]', '[role="link"][href]'], 'images': ['img'], 'media': ['audio', 'img', 'video'], 'url': ['[src]', '[href]'], 'inputs': ['input[type="text"]', 'input[type="date"]', 'input[type="datetime-local"]', 'input[type="email"]', 'input[type="month"]', 'input[type="number"]', 'input[type="password"]', 'input[type="search"]', 'input[type="tel"]', 'input[type="time"]', 'input[type="url"]', 'input[type="week"]', 'input:not([type])', '[contenteditable]:not([contenteditable="false"])', 'textarea']}


c.input.forward_unbound_keys = 'auto'
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True
c.input.insert_mode.auto_load = False
c.input.insert_mode.leave_on_load = True
c.input.partial_timeout = 0
c.input.mouse.rocker_gestures = True

# Mode to change to when focusing on a tab/URL changes.
# Type: String
# Valid values:
# - normal
# - insert
# - passthrough
# c.input.mode_override = None

c.input.mouse.back_forward_buttons = True

c.keyhint.blacklist = []
c.keyhint.delay = 0
c.keyhint.radius = 0

c.new_instance_open_target = 'tab'
c.new_instance_open_target_window = 'last-focused'
c.prompt.filebrowser = True
c.prompt.radius = 0

# Additional arguments to pass to Qt, without leading `--`. With
c.qt.args = []

c.qt.chromium.process_model = "process-per-site"

c.session.lazy_restore = True


# Additional environment variables to set.
# c.qt.environ = {}

# - always: Always show the scrollbar.
# - never: Never show the scrollbar.
# - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
# - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'never'
# c.scrolling.smooth = False

# c.search.ignore_case = 'smart'
# c.search.incremental = True
# c.search.wrap = True

# Padding (in pixels) for the statusbar.
c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}
c.statusbar.position = 'bottom'
c.statusbar.show = 'always'
# - url: Current page URL.
# - scroll: Percentage of the current page position like `10%`.
# - scroll_raw: Raw percentage of the current page position like `10`.
# - history: Display an arrow when possible to go back/forward in history.
# - tabs: Current active tab, e.g. `2`.
# - keypress: Display pressed keys when composing a vi command.
# - progress: Progress bar for the current page loading.
# - text:foo: Display the static text after the colon, `foo` in the example.
c.statusbar.widgets = ['keypress', 'url', 'scroll_raw', 'progress']

c.tabs.background = True
# c.tabs.favicons.scale = 1.0
# - always: Always show favicons.
# - never: Always hide favicons.
# - pinned: Show favicons only on pinned tabs.
c.tabs.favicons.show = 'pinned'
# c.tabs.focus_stack_size = 10
# c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}
c.tabs.indicator.width = 1
c.tabs.last_close = 'default-page'
c.tabs.mousewheel_switching = False
# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}
# c.tabs.pinned.frozen = True
# c.tabs.pinned.shrink = True
c.tabs.position = 'top'
# - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
# - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
# - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'prev'
# - always: Always show the tab bar.
# - never: Always hide the tab bar.
# - multiple: Hide the tab bar if only one tab is open.
# - switching: Show the tab bar when switching tabs.
# c.tabs.show = 'always'
c.tabs.tabs_are_windows = False
# c.tabs.title.alignment = 'left'
c.tabs.title.format = '{audio}{current_title}'
c.tabs.title.format_pinned = ''
c.tabs.tooltips = False
c.tabs.wrap = True

c.window.hide_decoration = True
c.window.title_format = '{current_title}{title_sep}qutebrowser'

c.window.transparent = True

# Default zoom level.
# c.zoom.default = '100%'
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
# c.zoom.mouse_divider = 512
# c.zoom.text_only = False

c.bindings.default = {}
c.bindings.key_mappings = {
    # '<Ctrl-[>': '<Escape>',
    # '<Ctrl-6>': '<Ctrl-^>',
    # '<Ctrl-M>': '<Return>',
    # '<Ctrl-J>': '<Return>',
    # '<Ctrl-I>': '<Tab>',
    # '<Shift-Return>': '<Return>',
    '<Enter>': '<Return>',
    '<Shift-Enter>': '<Shift-Return>',
    '<Ctrl-Enter>': '<Ctrl-Return>',
}

c.aliases.update({
    # '_File': 'fake-key --global |f',
    '_Page': 'fake-key --global |p',
    '_Tabs': 'fake-key --global |t',
    '_Marks': 'fake-key --global |m',
    '_Download': 'fake-key --global |d',
    '_Hint': 'fake-key --global |h',
    '_Config': 'fake-key --global |c',
    '_Menu': 'fake-key --global <Escape>\\',
})

# config.bind('\\f', '_File')
config.bind('\\p', '_Page')
config.bind('\\t', '_Tabs')
config.bind('\\m', '_Marks')
config.bind('\\d', '_Download')
config.bind('\\h', '_Hint')
config.bind('\\c', '_Config')
config.bind('\\Q', 'quit')
config.bind('\\q', 'quit --save')
config.bind('\\w', 'save')

# File

# Page
config.bind('|pu', 'navigate up -t')
config.bind('|ps', 'view-source')
config.bind('|pd', 'devtools')
config.bind('|pf', 'devtools-focus')
config.bind('|ph', 'devtools left')
config.bind('|pj', 'devtools bottom')
config.bind('|pk', 'devtools top')
config.bind('|pl', 'devtools right')
config.bind('|pw', 'devtools window')
config.bind('|p\\', '_Menu')

# Tabs
config.bind('|tc', 'tab-clone')
config.bind('|tg', 'tab-give')
config.bind('|to', 'tab-only')
# config.bind('|tc', 'tab-close')
config.bind('|tC', 'tab-close -o')
config.bind('|t\\', '_Menu')
config.bind('|tR', 'set input.mouse.rocker_gestures true')
config.bind('|tr', 'set input.mouse.rocker_gestures false')

# Marks
config.bind('|mq', 'cmd-set-text -s :quickmark-load')
config.bind('|mQ', 'cmd-set-text -s :quickmark-load -t')
config.bind('|mw', 'cmd-set-text -s :quickmark-load -w')
config.bind('|mh', 'history')
config.bind('|ma', 'bookmark-add')
config.bind('|ml', 'bookmark-list')
config.bind('|mL', 'bookmark-list --jump')
config.bind('|mb', 'cmd-set-text -s :bookmark-load')
config.bind('|mB', 'cmd-set-text -s :bookmark-load -t')
config.bind('|mW', 'cmd-set-text -s :bookmark-load -w')
config.bind('|m\\', '_Menu')

# Downloads
config.bind('|dd', 'download')
config.bind('|dc', 'download-cancel')
config.bind('|dC', 'download-clear')
config.bind('|d\\', '_Menu')

# Hint
config.bind('|hi', 'hint images')
config.bind('|hI', 'hint images tab')
config.bind('|hl', 'hint links fill :open {hint-url}')
config.bind('|hL', 'hint links fill :open -t -r {hint-url}')
config.bind('|hr', 'hint --rapid links tab-bg')
config.bind('|hR', 'hint --rapid links window')
config.bind('|ha', 'hint all tab-fg')
config.bind('|hA', 'hint all tab-bg')
config.bind('|hw', 'hint all window')
config.bind('|hd', 'hint links download')
config.bind('|hD', 'hint images download')
config.bind('|hh', 'hint all hover')
config.bind('|ht', 'hint inputs')
config.bind('|hT', 'hint inputs --first')
config.bind('|hy', 'hint links yank')
config.bind('|hY', 'hint links yank-primary')
config.bind('|h\\', '_Menu')

# Config
config.bind('|cc', 'config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload')
config.bind('|cC', 'config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
config.bind('|ci', 'config-cycle -p -t -u {url} content.images ;; reload')
config.bind('|cI', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
config.bind('|cp', 'config-cycle -p -t -u {url} content.plugins ;; reload')
config.bind('|cP', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
config.bind('|cj', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
config.bind('|cJ', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
config.bind('|cr', 'config-source')
config.bind('|c\\', '_Menu')


# Bindings for normal mode
config.bind("`", 'mode-enter jump_mark')
config.bind('m', 'mode-enter set_mark')
config.bind('~', 'cmd-set-text -s :quickmark-load -t')
config.bind('M', 'quickmark-save')

config.bind('<Ctrl-V>', 'mode-enter passthrough')
config.bind('V', 'mode-enter caret ;; selection-toggle --line')
config.bind('i', 'mode-enter insert')
config.bind('v', 'mode-enter caret')

config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')
config.bind('=', 'zoom')

config.bind('.', 'cmd-repeat-last')
config.bind('/', 'cmd-set-text /')
config.bind(':', 'cmd-set-text :')
config.bind('?', 'cmd-set-text ?')
config.bind('@', 'macro-run')
config.bind('s', 'hint')
config.bind('S', 'hint all tab')
config.bind('<Ctrl-Shift-S>', 'hint all tab-bg')
config.bind('H', 'back')
config.bind('L', 'forward')
config.bind('n', 'search-next')
config.bind('N', 'search-prev')
config.bind('o', 'cmd-set-text -s :open')
config.bind('O', 'cmd-set-text -s :open -t')
config.bind('<Ctrl-Shift-O>', 'cmd-set-text -s :open -w')
config.bind('R', 'reload -f')
config.bind('P', 'open -t -- {primary}')
config.bind('p', 'open -t -- {clipboard}')

config.bind('<Ctrl-Shift-M>', 'spawn --detach mpv --force-window {url}')
config.bind('<Ctrl-M>', 'hint links spawn --detach mpv --force-window {hint-url}')

config.bind('<Ctrl-l>', 'cmd-set-text :open {url:pretty}')
config.bind('<Ctrl-1>', 'tab-focus 1')
config.bind('<Ctrl-2>', 'tab-focus 2')
config.bind('<Ctrl-3>', 'tab-focus 3')
config.bind('<Ctrl-4>', 'tab-focus 4')
config.bind('<Ctrl-5>', 'tab-focus 5')
config.bind('<Ctrl-6>', 'tab-focus 6')
config.bind('<Ctrl-7>', 'tab-focus 7')
config.bind('<Ctrl-8>', 'tab-focus 8')
config.bind('<Ctrl-9>', 'tab-focus -1')
config.bind('<Alt-m>', 'tab-mute')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-B>', 'scroll-page 0 -1')
# config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
config.bind('<Ctrl-F5>', 'reload -f')
config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
config.bind('<F11>', 'fullscreen')
config.bind('<F5>', 'reload')
config.bind('<Return>', 'selection-follow')
config.bind('<back>', 'back')
config.bind('<forward>', 'forward')
# config.bind('<Ctrl-F>', 'scroll-page 0 1')
config.bind('<Ctrl-N>', 'open -w')
config.bind('<Ctrl-Shift-N>', 'open -p')

config.bind('<Alt-,>', 'tab-prev')
config.bind('<Alt-.>', 'tab-next')
config.bind('<Ctrl-W>', 'tab-close')

# https://github.com/qutebrowser/qutebrowser/issues/3736
config.bind('<', 'tab-move -')
config.bind('>', 'tab-move +')
config.bind('<Alt-Shift-,>', 'tab-move -')
config.bind('<Alt-Shift-.>', 'tab-move +')

config.bind('<Ctrl-Q>', 'quit')
config.bind('<Ctrl-Return>', 'selection-follow -t')
config.bind('<Ctrl-Shift-T>', 'undo')
config.bind('<Ctrl-Shift-W>', 'close')
config.bind('<Ctrl-T>', 'open -t')
config.bind('<Shift-Space>', 'scroll-page 0 -0.5')
config.bind('<Ctrl-Space>', 'scroll-page 0 -0.5')
config.bind('<Space>', 'scroll-page 0 0.5')
config.bind('<PgUp>', 'scroll-page 0 -1')
config.bind('<PgDown>', 'scroll-page 0 1')
config.bind('<Ctrl-h>', 'home')
config.bind('<Ctrl-p>', 'tab-pin')
config.bind('<Ctrl-s>', 'stop')


config.bind('gg', 'scroll-to-perc 0')
config.bind('G', 'scroll-to-perc')
config.bind('gt', 'cmd-set-text -s :tab-select')
config.bind('gd', 'navigate next')
config.bind('gu', 'navigate prev')
config.bind('gU', 'navigate up')
config.bind('gi', 'hint inputs')
config.bind('gl', 'hint links')

config.bind('h', 'scroll left')
config.bind('j', 'scroll down')
config.bind('k', 'scroll up')
config.bind('l', 'scroll right')

config.bind('q', 'macro-record')
config.bind('r', 'reload')

config.bind('t', 'cmd-set-text -sr :tab-focus')
config.bind('u', 'back --quiet')
config.bind('U', 'undo -w')
config.bind('<Ctrl-R>', 'forward --quiet')
config.bind('<Ctrl-Shift-R>', 'forward -t --quiet')
config.bind('YD', 'yank domain -s')
config.bind('YM', 'yank inline [{title}]({url}) -s')
config.bind('YP', 'yank pretty-url -s')
config.bind('YT', 'yank title -s')
config.bind('Yy', 'yank')
config.bind('YY', 'yank -s')
config.bind('Yd', 'yank domain')
config.bind('Ym', 'yank inline [{title}]({url})')
config.bind('Yp', 'yank pretty-url')
config.bind('Yt', 'yank title')
config.bind('y', 'yank selection')
# config.bind('<Ctrl+Shift+C>', 'yank selection')

# Bindings for caret mode
config.bind('$', 'move-to-end-of-line', mode='caret')
config.bind('0', 'move-to-start-of-line', mode='caret')
config.bind('<Ctrl-Space>', 'selection-drop', mode='caret')
config.bind('<Escape>', 'mode-leave', mode='caret')
config.bind('<Return>', 'yank selection', mode='caret')
config.bind('<Space>', 'selection-toggle', mode='caret')
config.bind('G', 'move-to-end-of-document', mode='caret')
config.bind('H', 'scroll left', mode='caret')
config.bind('J', 'scroll down', mode='caret')
config.bind('K', 'scroll up', mode='caret')
config.bind('L', 'scroll right', mode='caret')
config.bind('V', 'selection-toggle --line', mode='caret')
config.bind('Y', 'yank selection -s', mode='caret')
config.bind('[', 'move-to-start-of-prev-block', mode='caret')
config.bind(']', 'move-to-start-of-next-block', mode='caret')
config.bind('b', 'move-to-prev-word', mode='caret')
config.bind('c', 'mode-enter normal', mode='caret')
config.bind('e', 'move-to-end-of-word', mode='caret')
config.bind('gg', 'move-to-start-of-document', mode='caret')
config.bind('h', 'move-to-prev-char', mode='caret')
config.bind('j', 'move-to-next-line', mode='caret')
config.bind('k', 'move-to-prev-line', mode='caret')
config.bind('l', 'move-to-next-char', mode='caret')
config.bind('o', 'selection-reverse', mode='caret')
config.bind('v', 'selection-toggle', mode='caret')
config.bind('w', 'move-to-next-word', mode='caret')
config.bind('y', 'yank selection', mode='caret')
config.bind('{', 'move-to-end-of-prev-block', mode='caret')
config.bind('}', 'move-to-end-of-next-block', mode='caret')

# Bindings for command mode
config.bind('<Alt-B>', 'rl-backward-word', mode='command')
config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
config.bind('<Alt-D>', 'rl-kill-word', mode='command')
config.bind('<Alt-F>', 'rl-forward-word', mode='command')
config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
config.bind('<Ctrl-N>', 'command-history-next', mode='command')
config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
config.bind('<Ctrl-Shift-W>', 'rl-filename-rubout', mode='command')
config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
config.bind('<Ctrl-W>', 'rl-rubout " "', mode='command')
config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
config.bind('<Down>', 'completion-item-focus --history next', mode='command')
config.bind('<Escape>', 'mode-leave', mode='command')
config.bind('<PgDown>', 'completion-item-focus next-page', mode='command')
config.bind('<PgUp>', 'completion-item-focus prev-page', mode='command')
config.bind('<Return>', 'command-accept', mode='command')
config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
config.bind('<Tab>', 'completion-item-focus next', mode='command')
config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

# Bindings for hint mode
config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
config.bind('<Ctrl-F>', 'hint links', mode='hint')
config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
config.bind('<Escape>', 'mode-leave', mode='hint')
config.bind('<Return>', 'hint-follow', mode='hint')

# Bindings for insert mode
config.bind('<Ctrl-E>', 'edit-text', mode='insert')
config.bind('<Escape>', 'mode-leave', mode='insert')
config.bind('<Shift-Escape>', 'fake-key <Escape>', mode='insert')
config.bind('<Shift-Ins>', 'insert-text -- {primary}', mode='insert')

# Bindings for passthrough mode
config.bind('<Shift-Escape>', 'mode-leave', mode='passthrough')

# Bindings for prompt mode
config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
config.bind('<Ctrl-Shift-W>', 'rl-filename-rubout', mode='prompt')
config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
config.bind('<Ctrl-W>', 'rl-rubout " "', mode='prompt')
config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
config.bind('<Escape>', 'mode-leave', mode='prompt')
config.bind('<Return>', 'prompt-accept', mode='prompt')
config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

# Bindings for register mode
config.bind('<Escape>', 'mode-leave', mode='register')

# Bindings for yesno mode
config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
config.bind('<Escape>', 'mode-leave', mode='yesno')
config.bind('<Return>', 'prompt-accept', mode='yesno')
config.bind('N', 'prompt-accept --save no', mode='yesno')
config.bind('Y', 'prompt-accept --save yes', mode='yesno')
config.bind('n', 'prompt-accept no', mode='yesno')
config.bind('y', 'prompt-accept yes', mode='yesno')

# ######################## THEMES ######################## #

# color of the completion widget category headers.
c.colors.completion.category.bg = '#A1937F'
c.colors.completion.category.border.bottom = '#A1937F'
c.colors.completion.category.border.top = '#A1937F'
c.colors.completion.category.fg = '#282828'

# color of the completion widget.
c.colors.completion.even.bg = '#4e4743'
c.colors.completion.odd.bg = '#4e4743'
c.colors.completion.fg = '#fbf1c7'
c.colors.completion.item.selected.bg = '#7e9f92'
c.colors.completion.item.selected.border.bottom = '#7e9f92'
c.colors.completion.item.selected.border.top = '#7e9f92'
c.colors.completion.item.selected.fg = '#282828'
c.colors.completion.item.selected.match.fg = '#2d3d2d'
c.colors.completion.match.fg = '#7e9f92'

# color of completion scrollbar
c.colors.completion.scrollbar.bg = '#4e4743'
c.colors.completion.scrollbar.fg = '#A1937F'

# color of items in the context menu
c.colors.contextmenu.disabled.bg = '#282828'
c.colors.contextmenu.disabled.fg = '#a89984'
c.colors.contextmenu.menu.bg = '#282828'
c.colors.contextmenu.menu.fg = '#fbf1c7'
c.colors.contextmenu.selected.bg = '#4e4743'
c.colors.contextmenu.selected.fg = '#fbf1c7'

# color for the download bar.
c.colors.downloads.bar.bg = '#282828'
c.colors.downloads.error.bg = '#cc241d'
c.colors.downloads.error.fg = '#fbf1c7'
c.colors.downloads.start.bg = '#689D6A'
c.colors.downloads.start.fg = '#fbf1c7'
c.colors.downloads.stop.bg = '#689D6A'
c.colors.downloads.stop.fg = '#fbf1c7'
c.colors.downloads.system.bg = 'none'
c.colors.downloads.system.fg = 'none'

# color for hints
c.colors.hints.bg = '#E1D2AB'
c.colors.hints.fg = '#282828'
c.colors.hints.match.fg = '#D65D0E'

# color of the keyhint widget.
c.colors.keyhint.bg = '#282828'
c.colors.keyhint.fg = '#fbf1c7'
c.colors.keyhint.suffix.fg = '#7e9f92'

# Background color of an error message.
c.colors.messages.error.bg = '#282828'
c.colors.messages.error.border = '#282828'
c.colors.messages.error.fg = '#FB4934'

# Background color of an info message.
c.colors.messages.info.bg = '#282828'
c.colors.messages.info.border = '#282828'
c.colors.messages.info.fg = '#83a598'

# Background color of a warning message.
c.colors.messages.warning.bg = '#282828'
c.colors.messages.warning.border = '#282828'
c.colors.messages.warning.fg = '#fe8019'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#282828'
c.colors.prompts.border = '1px solid #282828 0 0 0'
c.colors.prompts.fg = '#fbf1c7'
c.colors.prompts.selected.bg = '#4e4743'
c.colors.prompts.selected.fg = '#fbf1c7'

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = '#fe8019'
c.colors.statusbar.caret.fg = '#282828'
# line selection
c.colors.statusbar.caret.selection.bg = '#fe8019'
c.colors.statusbar.caret.selection.fg = '#282828'

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = '#282828'
c.colors.statusbar.command.fg = '#fbf1c7'

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = '#282828'
c.colors.statusbar.command.private.fg = '#fbf1c7'

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = '#83a598'
c.colors.statusbar.insert.fg = '#282828'

# Background color of the statusbar.
c.colors.statusbar.normal.bg = '#282828'
c.colors.statusbar.normal.fg = '#fbf1c7'

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = '#83a598'
c.colors.statusbar.passthrough.fg = '#282828'

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = '#282828'
c.colors.statusbar.private.fg = '#83a598'

# Background color of the progress bar.
c.colors.statusbar.progress.bg = '#4e4743'

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = '#fb4934'
c.colors.statusbar.url.fg = '#fbf1c7'
c.colors.statusbar.url.hover.fg = '#fbf1c7'
c.colors.statusbar.url.success.http.fg = '#fbf1c7'
c.colors.statusbar.url.success.https.fg = '#fbf1c7'
c.colors.statusbar.url.warn.fg = '#fe8019'

# Background color of the tab bar.
c.colors.tabs.bar.bg = '#282828'

# Background color of unselected even tabs.
c.colors.tabs.even.bg = '#282828'
c.colors.tabs.even.fg = '#786b60'
c.colors.tabs.odd.bg = '#282828'
c.colors.tabs.odd.fg = '#786b60'

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = '#fb4934'
c.colors.tabs.indicator.start = '#8ec07c'
c.colors.tabs.indicator.stop = '#8ec07c'
c.colors.tabs.indicator.system = 'none'


# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = '#282828'
c.colors.tabs.pinned.even.fg = '#786b60'
c.colors.tabs.pinned.odd.bg = '#282828'
c.colors.tabs.pinned.odd.fg = '#786b60'

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = '#3b3735'
c.colors.tabs.pinned.selected.even.fg = '#fbf1c7'
c.colors.tabs.pinned.selected.odd.bg = '#3b3735'
c.colors.tabs.pinned.selected.odd.fg = '#fbf1c7'

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = '#3b3735'
c.colors.tabs.selected.even.fg = '#fbf1c7'
c.colors.tabs.selected.odd.bg = '#3b3735'
c.colors.tabs.selected.odd.fg = '#fbf1c7'

