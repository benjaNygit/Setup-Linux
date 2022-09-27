from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
cmd = ["setxkbmap latam", "feh --bg-fill ~/Imágenes/Fondos\ de\ escritorio/dibujo-bosque-minimalista.jpg"]
for x in cmd:
    os.system(x)

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # mis atajos
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Spawn rofi in mode run"),
    Key([mod], "n", lazy.spawn("rofi -show window"), desc="Spawn rofi in mode window"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Open firefox"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -6%"), desc="turn up the volumen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +6%"), desc="volumen down"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ toggle"), desc="mute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10"), desc="turn up brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10-"), desc="brightness down"),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Floating(border_focus='#0000ff'),
    layout.Columns(border_focus_stack=["#0000ff", "#0000ff"], border_width=3, border_normal='#000000', border_focus='#0000ff', margin=3),
    # layout.Max(),
    layout.Tile(margin=2, border_width=3),
    # layout.Stack(num_stacks=2),
    # layout.Zoomy(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

widget_defaults = dict(
    font="mononoki",
    fontsize=8,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.CurrentScreen(), widget.Sep(),
                widget.GroupBox(highlight_method='line', background='#483D8B', block_highlight_text_color='#ff0000', borderwidth=1, fontsize=10, inactive='#000000'), widget.Sep(),
                widget.WindowName(),
                widget.CheckUpdates(distro='Ubuntu', no_update_string='No updates'),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.OpenWeather(location='Santiago, CL', background='#0000ff', fontsize=10, language='es'),
                widget.Notify(),
                widget.Net(),
                widget.ThermalSensor(background='#0000ff', fontsize=10),
                widget.Memory(measure_mem='G'),
                widget.CPU(),
                widget.Volume(background='#ffffff', foreground='#000000', fontsize=10),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Battery(
                    background='#0000ff',
                    fontsize=10,
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                    low_background='#ff0000',
                    low_foreground='ffffff',
                    low_percentage=0.16,
                    notify_below=0.2,
                ),
                widget.QuickExit(),
            ],
            16,
            margin=2,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.CurrentScreen(), widget.Sep(),
                widget.GroupBox(highlight_method='line', background='#483D8B', block_highlight_text_color='#ff0000', borderwidth=1, fontsize=10, inactive='#000000'), widget.Sep(),
                widget.WindowName(),
                widget.OpenWeather(location='Santiago, CL', background='#0000ff', fontsize=10, language='es'),
            ],
            16,
            margin=2,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
