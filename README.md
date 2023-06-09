# Aeroplano Graveyardo by aTriceratopy
## Roster:
(PM) Verit Li - Database  
Brian Yang - Map page  
Jonathan Song - Summary page   
Prattay Dey - Trends page  
## Description:
Aeroplano Graveyardo is a global map showing all civil aviation accidents from 1908 to 2019. Users will be able to see points on a globe of locations of crashes, select a crash and see the plane’s intended path, interact with filters like aircraft type, country of crash, deadliness, and accident year. Users will also be able to see trends in the database file. 
## APIs Used:  
- [Bing Maps](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_BingMaps.md)
- [Mapbox](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_Mapbox.md)
## Launch Codes: 
1. Create virtual environment  
`python -m venv squowel`  
1. activate virtual environment  
`. squowel/bin/activate`  
1. Install packages  
`pip install -r requirements.txt`  
1. Clone repository  
`git clone git@github.com:leriivt/p4-aTriceratopy.git`  
1. cd into app directory  
`cd p4-aTriceratopy/app`  
1. Download CSV data from https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908 to `p4-aTriceratopy/app`
1. If this is your first time running the app, run reset.py with
`python reset.py`. This will populate all the tables in the database and will take about 20 minutes to run.
1. Start Flask server  
`python __init__.py`  
Go to http://127.0.0.1:5000/ in browser  
## Data:  
- Description: Data of all crashes around the world from 1908-2019 with information including Date, Time, Location, Operator (Airline or operator of the aircraft), takeoff, destination, Aircraft type(model), crew #, passengers #, fatalities #
- Source: https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908 
