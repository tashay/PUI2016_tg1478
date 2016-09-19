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

bus_latitude = []
bus_longitude = []

for i in vehicle_activity:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    bus_latitude.append(latitude)
    bus_longitude.append(longitude)

stop_name = []
stop_status = []

for i in vehicle_activity:
    name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    stop_name.append(name)
    stop_status.append(status)

for i in range (len(vehicle_activity)):
    print (str(bus_latitude[i]) + ',' + str(bus_longitude[i]) + ',' + str(stop_name[i]) + ',' + str(stop_status[i]))
