#!/usr/bin/env python

import os

vendor_file = open("/usr/tmp/touchscreen@on.off/vendor.txt","r")
product_file = open("/usr/tmp/touchscreen@on.off/product.txt","r")
vendor = vendor_file.readlines();
product = product_file.readlines()

os.system("sh /usr/tmp/touchscreen@on.off/toggle_touchscreen.sh 0 "+vendor[0]+" "+product[0])

