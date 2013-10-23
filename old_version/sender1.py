import bit
import subprocess
import sys
import time
import thread

def send_bit(i,ip):
	#time.sleep(round(time.time())+0.5-time.time())
	#time.sleep(1)
	#if (int(time.time()/10)*10+5-time.time())<=0:
	#	time.sleep(int(time.time()/10+1)*10-time.time())
	#else:
		#time.sleep(int(time.time()/10+1)*10-5-time.time())
	#time.sleep(int(time.time()/2+1)*2-time.time())
	time.sleep(int(time.time())+1-time.time())
	#if i==1:
		#ping_result=subprocess.Popen("ping -c %d %s" %(i,ip),shell=True,stdout=subprocess.PIPE)
		#line=ping_result.stdout.readlines()
		#lines=line[-2].split()
		#if lines[3]>="10":
		#print "Bit 1 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())
		#time.sleep(1)
	#else:
		#print "Bit 0 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())
		#time.sleep(1)
	if i==1:
		for i in range(5*i):
			thread.start_new_thread(send,(1,ip))
		print "Bit 1 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())
	else:
		print "Bit 0 send successfully at %s" %time.strftime("%H:%M:%S",time.localtime())
	#time.sleep(1)

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
