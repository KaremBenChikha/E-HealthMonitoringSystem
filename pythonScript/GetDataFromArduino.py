#Libraries 
import serial
import time
import csv
from itertools import zip_longest
from Adafruit_IO import Client, Feed
#test test test 

#import matplotlib.pyplot as plt
#install matplotlib

#Variables
# com 5 for karem and com 9 for hoss
#COM = 'COM5'

COM = 'COM9'
Baud = 9600
csvfile = "test.csv"

#Adafruit Credentials
#make account for ehealth
ADAFRUIT_IO_KEY = 'aio_xfkZ266E9Tzd2U1xM28DleUNaWbE'
ADAFRUIT_IO_USERNAME = 'DigiHealth'

#connect to Adafruit IO
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Arduino Port 
Arduino = serial.Serial(COM,Baud)

#test
print(Arduino.readline())

# empty list to store the data
TemperatureData = []  
BMPData = []
OData = []
ECGData = []

for i in range(10000):
    serialLine = Arduino.readline()         # read a byte string
    serialLine = serialLine.decode()        # decode byte string into Unicode  
    serialLine = serialLine.rstrip()        # remove \n and \r
    multiData = serialLine.split(',')

    Temperature = float(multiData[0])
    BMP = float(multiData[1])
    O = float(multiData[2])
    ECG = float(multiData[3])

    print("BMP: ",BMP)
    BMPFeed = aio.feeds('bmp')
    aio.send(BMPFeed.key, str(BMP))
    BMPData.append(BMP)   # add to the end of data list
    
    # print("O2: ",O)
    # O2Feed = aio.feeds('o2')
    # aio.send(O2Feed.key, str(O))
    # OData.append(O)
    #print("ECG: ",ECG)
    #ECGData.append(ECG)
    print("Temperatue: ",Temperature)
    temperatureFeed = aio.feeds('temperatureio')
    aio.send(temperatureFeed.key, str(Temperature))
    TemperatureData.append(Temperature)


    time.sleep(0.4)             # wait (sleep) 0.1 seconds

Arduino.close()

Fields = ['Temperature','BMP','SPO2','ECG']  

Rows = [TemperatureData,BMPData,OData,ECGData]
Rows = zip_longest(*Rows, fillvalue = '')

#Write to CSV
with open(csvfile, 'w+') as f: 
    write = csv.writer(f) 
    write.writerow(Fields) 
    write.writerows(Rows)

#things to be added: 
# auto detect arduino port
# add publishers to Adafruit

