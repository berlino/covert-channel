import bit
import subprocess
import sys
import time
import thread

def send_bit(i,ip):
	time.sleep((int(time.time()*10)/2+1)*2/10.0-time.time())
	if i==1:
		for i in range(5):
			thread.start_new_thread(send,(1,ip))
		print "Bit 1 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())
	else:
		print "Bit 0 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())

def send(i,ip):
	ping_result=subprocess.Popen("ping -c %d %s" %(i,ip),shell=True,stdout=subprocess.PIPE)
	#print "Bit %d send successfully at %s" %(i,time.strftime("%H:%M:%S",time.localtime()))
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
