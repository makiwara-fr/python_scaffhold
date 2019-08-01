# -*- coding: utf-8 -*-
# ###################################################################################
#
# 			Your text
#
#	License:
#	Author: 
#
#	                __   .__                              
#	  _____ _____  |  | _|__|_  _  _______ ____________   
#	 /     \\__  \ |  |/ /  \ \/ \/ /\__  \\_  __ \__  \  
#	|  Y Y  \/ __ \|    <|  |\     /  / __ \|  | \// __ \_
#	|__|_|  (____  /__|_ \__| \/\_/  (____  /__|  (____  /
#	      \/     \/     \/                \/           \/ 
#
# ###################################################################################




import sys
from datetime import datetime
import getopt
import os
import settings as CONFIG
from settings import log as log

def usage():
	print("Recognised options")
	print("-d, --debug set debug mode to ON")
	print("-h, --help show this help")
	
	



def main(arg_list):
	
	# get params if needed
	# set all parameters according to command line
	# --------------------------------------------
	try:
		opts, args = getopt.getopt(arg_list, "hd", ["help", "debug"])
	except getopt.GetoptError as err:
		log(err, "error")
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ('-d', 'debug'):
			CONFIG.debug = True
			log("Debug mode ON")
#		elif opt in ("-o, --output"):
#			exported_file = arg
		
	
	# import data with numpy
	#-----------------------
	
	# train the model
	# ---------------
	
	# store the model
	# ---------------
	
	# play on a larger sample
	# -----------------------
	
	# Export results on larger sample
	# -------------------------------


if __name__ == "__main__":
	main(sys.argv[1:])
