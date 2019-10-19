#!/usr/bin/env python

import os
os.system("sh /home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/find_touchscreen.sh")

vp = open("/home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/vendor_product.txt","r")
vendor = open("/home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/vendor.txt","w")
product = open("/home/ns/.local/share/gnome-shell/extensions/touchscreen@on.off/product.txt","w")
for line in vp:
	list = line.split(" ")
	for cenas in list:
		list2 = cenas.split("=")
		if list2[0]=="Vendor":
			print ["Vendor is ",list2[1]]
			vendor.write(list2[1])
		elif list2[0]=="Product":
			print ["Product is ",list2[1]]
			product.write(list2[1])
