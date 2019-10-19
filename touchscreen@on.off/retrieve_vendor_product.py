#!/usr/bin/env python

import os
os.system("sh /usr/tmp/touchscreen@on.off/find_touchscreen.sh")

vp = open("/usr/tmp/touchscreen@on.off/vendor_product.txt","r")
vendor = open("/usr/tmp/touchscreen@on.off/vendor.txt","w")
product = open("/usr/tmp/touchscreen@on.off/product.txt","w")
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
