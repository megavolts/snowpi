#!/usr/bin/python2
import serial
import time
import os
#locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3', '/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3'] 
#for device in locations:device
#    try:
#        print "Trying...", device
#        arduino = serial.Serial(device,9600)
#        break
#arduino = serial.Serial('/dev/ttyAMA0',9600)
arduino = serial.Serial('/dev/ttyACM0',9600)
dir='/mnt/data/data'
f= open(dir+"/log.txt","a")
time.sleep(2)
arduino.write('t')
t1=arduino.readline()
t2=arduino.readline()
t3=arduino.readline()
t4=arduino.readline()
t5=arduino.readline()
t1=t1[0:len(t1)-2]; print t1
t2=t2[0:len(t2)-2]; print t2
t3=t3[0:len(t3)-2]; print t3
t4=t4[0:len(t4)-2]; print t4
t5=t5[0:len(t5)-2]; print t5
temp= "no picture\t"+str(int(time.time()))+"\t - \t" + str(float(t1)/100) +"\t"+str(float(t2)/100)+"\t"+str(float(t3)/100)+"\t"+str(float(t4)/100)+"\t"+ str(float(t5)/100)+"\n"
f.write(temp)
f.close()
f = open(dir+"/log.log","a")
f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tlogging temperature\n")
f.close()
