import json
import urllib.request as ulr
import os
import sys
import csv

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
BUS_LINE.csv = sys.argv[3]


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicle_activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
vehicle_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']  

latitude = vehicle_location['Latitude']
longitude = vehicle_location['Longitude']

stop_name = 
stop_status = 

fout = open(sys.argv[3], "w")
fout.writerow('Latitude, Longitude, Stop Name, Stop Status\n')

#for i in (vehicle_activity):
    #fout.writerow(latitude, longitude, stop_name, stop_status)

