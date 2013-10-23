from bit import *
import sys
import time
from scapy.all import *

def get_bit(ip):
	time.sleep((int(time.time()*10)+1)/10.0-time.time())
	global pre_id
	packet=sr1(IP(dst=ip)/ICMP())
	differ=0
	temp=pre_id
	pre_id=packet[0][0].id
	#print "IPID",pre_id
	if (packet[0][0].id-1)<temp:
		differ=packet[0][0].id+65535-temp
	else:
		differ=packet[0][0].id-1-temp
	if(differ>=4):
		return 1
	else:
		return 0

if __name__=="__main__":
	conf.verb=0
	pre_id=0
	ip=raw_input("Type in the ip you wanna receive message from:")
	print "Receiving message......."
	bit=get_bit(ip)
	bits=[]
	flag=0
	char=[]
	while True:
		bit=get_bit(ip)
		if bit==1:
			flag=flag+1
		else:
			flag=0
		if flag==3:
			break
	while True:
		for i in range(8):
			bit=get_bit(ip)
			bits.append(bit)
			if i==2 and bits[0]==1 and bits[1]==1 and bits[2]==1:
				break
		if len(bits)==3:
			break
		print frombits(bits)
		char.append(frombits(bits))
		bits=[]
	print " "
	print "The message you have received is "+''.join(char)
