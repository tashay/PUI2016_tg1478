# Author: Tashay Green, NYU, September 2016
######################################
# Script written to fetch and display information of future bus stop locations using MTA API.
# for HW Assignment 2 of PUI2016
######################################

import json
import urllib.request as ulr
import os
import sys
import csv

# sets variables for arguments input by the user

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
WRITE_TO_FILE = sys.argv[3]

# url for fetching MTA API data with unique arguments passed in by the user

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BUS_LINE

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# sets shortcut variables for paths in MTA API json file

vehicle_activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
vehicle_location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']  

# for loop that adds latitude and longitude of every active bus to a list 

bus_latitude = []
bus_longitude = []

for i in vehicle_activity:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    bus_latitude.append(latitude)
    bus_longitude.append(longitude)

# for loop that adds stop_name and stop_status of every active bus to a list 

stop_name = []
stop_status = []

for i in vehicle_activity:
    name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    stop_name.append(name)
    stop_status.append(status)

# conditional stating, if there is no information for name or status, fill space with 'N/A'

    if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
        name = 'N/A'
        status = 'N/A'

# the following commands open and write information to a csv file
# a csv file is opened based on the 4th input of the user
# the for loop will print to the csv the longitude, latitude, stop_name, and stop_status of all active buses 

fout = csv.writer(open(sys.argv[3], 'w'))
fout.writerow('Latitude, Longitude, Stop Name, Stop Status')

for i in range (len(vehicle_activity)):
    fout.writerows(str(bus_latitude[i]) + ',' + str(bus_longitude[i]) + ',' + str(stop_name[i]) + ',' + str(stop_status[i]))


