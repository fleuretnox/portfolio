# portfolio

Summary:
The project web crawls and fetches JFK's Airport number of departure on daily basis statistics.
Based on the historical pattern, it forecasts the future period based on the module provided by Facebook. 

Along the way, the project provides a fundamental concept of data warehousing along with administering from an operational standpoint.



Pre-Requisites:
*Application to run Python with ability to open Pandas, Matplotlib
* Chrome web browser


Steps:
1. Execute "main.py"
2. The code initially creates a csv file with given column names
3. It then web crawls to https://www.flightradar24.com/data/airports/jfk/statistics
3. It will click the menu button, View Data Table, and  fetch the table by exporting to the created csv file
4. Because the csv data requires a clean up, row data shifts to each cell by delimeter, which applies to each column that was created on #2
5. It then creates a new column called "Accuracy", which calculates the accurate percentage between scheduled and actual number of flights
6. When the outcome is generated, this csv will also make a backup file to "Backup Server"
7. Based on the given data, FBProphet module is used to forecast the number of expected flights for the upcoming month on a daily basis
8. It will generate a graph plot
9. The graph will also be backed up to "Backup Server"
10. Both CSV and Graph will also get backed up to "DR Server" for failover.


Notes:
Any unexpected encountered bugs or enhancement will be modified on an agile, scrum-based approach. 
