# PUI 2016 HW 2.

# Assignment 1:  Tracking Each Vehicle for a Line

In this assignment I wrote a Python script that fetches and displays current information of active bus locations using the
MTA API. The script takes 2 inputs from the user in the following format: 

```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

The program outputs the following to the console: 
- The bus name 
- The number of active vehicles
- The current position of the vehicles

###SAMPLE OUTPUT:
```
Bus Line : M10
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```


# Assignment 2: Future Stop Information

In this assignment I wrote a Python script that fetches and displays future location information of active buses using the
MTA API. The script also prints the information to a csv file per the users input in the following format:

```
python get_bus_info.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv
```

###SAMPLE OUTPUT:
```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```


# Assignment 3: Read CSV files with Pandas

In this assignment I created a Jupyter Notebook that contains code for reading a csv file with pandas. 

- I used pandas to read in a CSV file from the NYU CUSP Data Facility 
- I have displayed the top few rows of the data file in my notebook. The table is rendered.
- I removed all but 2 numerical values columns using the drop method of the pandas dataframe.
- I have displayed the reducted dataframe. The table is rendered. 
- I plotted the two numerical values columns against one another in a scatter plot using the dataframe plot method. The plot is rendered. 
