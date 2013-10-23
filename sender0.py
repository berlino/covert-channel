import bit
import subprocess
import sys
import time
import thread
import config

def send_bit(i,ip):
	v=config.interval
	time.sleep(((int(time.time()*100)/v+1)*v/100.0)-time.time())
	if i==1:
		for i in range(5*i):
			thread.start_new_thread(send,(1,ip))

def send(i,ip):
	ping_result=subprocess.Popen("ping -c %d %s" %(i,ip),shell=True,stdout=subprocess.PIPE)
	thread.exit_thread()

if __name__=='__main__':
	ip=raw_input("Type in the innocent ip address:")
	message=raw_input("Type in the message you wanna send:")
	print "Sending message...."
	for i in range(3):
		send_bit(1,ip)
	bits=bit.tobits(message)
	for i in bits:
		send_bit(i,ip)
	for i in range(3):
		send_bit(1,ip)
	time.sleep(1)
