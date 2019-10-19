const St = imports.gi.St;
const Me = imports.misc.extensionUtils.getCurrentExtension();
const Main = imports.ui.main;
const GLib = imports.gi.GLib;
const Gio = imports.gi.Gio;
const Util = imports.misc.util;

let button,icon,enabled;
let vendor,product;

function _cmdexec(cmd) {
    GLib.spawn_command_line_sync(cmd);
}

function _disable_touchscreen() {
	  Util.spawn(['/bin/bash', '-c', "sudo python /home/$USER/.local/share/gnome-shell/extensions/touchscreen@on.off/deactivate.py"]);
	  enabled=false;
}

function _enable_touchscreen() {
    Util.spawn(['/bin/bash', '-c', "sudo python /home/$USER/.local/share/gnome-shell/extensions/touchscreen@on.off/activate.py"]);
    enabled=true;
}

function init() {
    Util.spawn(['/bin/bash', '-c', "python /home/$USER/.local/share/gnome-shell/extensions/touchscreen@on.off/retrieve_vendor_product.py"]);
	Util.spawn(['/bin/bash', '-c', "sudo python /home/$USER/.local/share/gnome-shell/extensions/touchscreen@on.off/activate.py"]);
	enabled=true;
    button = new St.Bin(
        {
            style_class: 'panel-button',
            reactive: true,
            can_focus: true,
            x_fill: true,
            y_fill: false,
            track_hover: true});

    icon = new St.Icon({style_class: "touchscreen-icon"});
    button.set_child(icon);

    button.connect('button-press-event', function(){
        if(enabled) {
            _disable_touchscreen();
            icon = new St.Icon({style_class: "touchscreen-icon-disabled"});
        } else {
            _enable_touchscreen();
            icon = new St.Icon({style_class: "touchscreen-icon"});
        }
        button.set_child(icon);
    });
}

function enable() {
    Main.panel._rightBox.insert_child_at_index(button, 0);
}

function disable() {
    Main.panel._rightBox.remove_child(button);
}
