from sys import argv
from sys import stdout
import os
if argv[1] == '-e':
	os.system('i3-msg exit')
elif argv[1] == '-r':
	os.system('shutdown -r now')
elif argv[1] == '-s':
	os.system('shutdown now')
