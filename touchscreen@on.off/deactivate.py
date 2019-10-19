#!/usr/bin/env python

import os

vendor_file = open("/home/$ns/.local/share/gnome-shell/extensions/touchscreen@on.off/vendor.txt","r")
product_file = open("/home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/product.txt","r")
vendor = vendor_file.readlines();
product = product_file.readlines()

os.system("sh /home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/toggle_touchscreen.sh 0 "+vendor[0]+" "+product[0])

