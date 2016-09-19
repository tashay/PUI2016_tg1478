# Author: Tashay Green, NYU, September 2016
######################################
# Script written to fetch and display current information of active bus locations using MTA API.
# for HW Assignment 2 of PUI2016
######################################

import json
import urllib.request as ulr
import os
import sys

# sets variables for arguments input by the user

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

# url for fetching MTA API data with unique arguments passed in by the user

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# sets shortcut variables for paths in MTA API json file

vehicle_activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
vehicle_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']  

# counter to total the number of active buses according to the vehicle_activity

active_buses = 0

for i in vehicle_activity:
    active_buses += 1

# for loop that adds bus_latitude and bus_longitude of every active bus to a list 

bus_latitude = []
bus_longitude = []

for i in vehicle_activity:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    bus_latitude.append(latitude)
    bus_longitude.append(longitude)

# print statment that indicates which BUS_LINE the information pertains to
# print statement that indicates how many active_buses there are for the given line
# for loop that prints individual location information for each active bus 

print ('Bus Line: ' + BUS_LINE)
print ('Number of Active Buses: ' + str(active_buses))

for i in range (len(vehicle_activity)):
    print ('Bus ' + str(i) + ' is at latitude ' + str(bus_latitude[i]) + ' and longitude ' + str(bus_longitude[i]))
