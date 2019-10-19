#!/bin/sh
if [ $# -ne 3 ]; then
	echo "Usage: sh toggle_touchscreen.sh <0 or 1> <vendor> <product_id>"
	echo "eg. sh toggle_touchscreen.sh 0 04f3 012d"
	exit 1
fi

if [ $# -eq 3 ]; then
	echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"$2\", ATTRS{idProduct}==\"$3\", ATTR{authorized}=\"$1\"" > /home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/80-touchscreen.rules
	cp /home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/80-touchscreen.rules /etc/udev/rules.d/80-touchscreen.rules
	udevadm control --reload-rules
	udevadm trigger
fi
