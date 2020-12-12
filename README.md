## Scanning for calibration
1. Place the scanner at the distance required
2. Edit the beacon filters to only include the beacon that is being calibrated
2. Edit the callback function in scan.py to only write rssi
3. Run the scanner and save output to a file
```
python scan.py > file.txt
```
Recorded calibration files in folder calibration_files
## Scanning for an experiment
1. Setup the experiment
2. Run the scanner and save output to a file
```
python scan.py > file.txt
```
Recorded experiment scans in experiment_scans folderww

## Generate curve fit parameters

1. The files are named as beaconname_distance.txt. Set the used beacon name and distances in curve_all_data.py in the variables beacons and ds
2. Run the code to generate a curve
```
python curve_all_data.py
```
The results from my run are mentioned as comments in curve_all_data.py

## Generate curves based on averages
1. Calculate the averages using averages.py
1. Use these averages in curve_fit.py to calculate the curves
