#!/usr/bin/python2
#
# SnowPI
#
# Marc Oggier
# Simon Filhol
#
# Updated December 9, 2013
# Version 2.0
#
#
#

import serial
import time
import os
#locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3', '/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3'] 
#for device in locations:device
#    try:
#        print "Trying...", device
#        arduino = serial.Serial(device,9600)
#        break
fl = open("log.log", "a")
#arduino = serial.Serial('/dev/ttyAMA0',9600)
arduino = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
arduino.write('u')
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tUSB ON\n")
time.sleep(5)
arduino.write('y')
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tLED ON\n")
time.sleep(1)
os.system("./snap.sh /mnt/data/pics")
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\ttaking picture\n")
time.sleep(5)
arduino.write('d');
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tUSB OFF\n")
time.sleep(1)
arduino.write('n') 
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tLED OFF\n")
time.sleep(0.5)
arduino.write('t');
fl.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tlogging temperature\n")
t1=arduino.readline()
t2=arduino.readline()
t3=arduino.readline()
t4=arduino.readline()
t5=arduino.readline()
t1=t1[0:len(t1)-2];
t2=t2[0:len(t2)-2];
t3=t3[0:len(t3)-2];
t4=t4[0:len(t4)-2];
t5=t5[0:len(t5)-2];
f = open("temp.txt", "r")
temp=f.readline()
temp=temp[0:len(temp)-1]
f.close()
temp= str(temp) + "\t" + str(float(t1)/100) +"\t"+str(float(t2)/100)+"\t"+str(float(t3)/100)+"\t"+str(float(t4)/100)+"\t"+ str(float(t5)/100)+"\n"
f = open("log.txt", "a")
f.write(temp)
f.close()
# Closing log file
fl.close()


