import json
import urllib.request as ulr
import os
import sys

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicle_activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
vehicle_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']  

active_buses = 0

for i in vehicle_activity:
    active_buses += 1

bus_latitude = []
bus_longitude = []

for i in vehicle_activity:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    bus_latitude.append(latitude)
    bus_longitude.append(longitude)
    
print ('Bus Line: ' + BUS_LINE)
print ('Number of Active Buses: ' + str(active_buses))

for i in range (len(vehicle_activity)):
    print ('Bus ' + str(i) + ' is at latitude ' + str(bus_latitude[i]) + ' and longitude ' + str(bus_longitude[i]))
