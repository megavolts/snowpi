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
f = open("log.log","a")
time.sleep(1)
arduino.write('d')
f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tUSB ON\n")
arduino.write('y')
f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\tLEDx ON\n")
f.close()
