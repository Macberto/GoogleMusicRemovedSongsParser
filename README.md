# Google Music Removed Songs Finder
Google Music will randomly remove songs from their streaming service.  They will never show you which songs have been removed/expired.

I got very annoyed by that, so I created this program to find which songs were removed from your Google Music library by searching all the .csv files provided by your own account data from Google Takeout (https://takeout.google.com/).


How to get your Google Play Music data:

1. Go to https://takeout.google.com/ and login to your account that has your Google Play Music

2. Make sure you only have the option selected for Google Play Music

3. Click the "Next" button

4. Select how you want to download your data (the default settigns should be fine)

5. Click on "Create Archive" button

6. Wait a few minutes until your data is downloaded

7. Extract your downloade .zip file.  Inside of it you should see a Google Play Music folder that contains sub-folders with a bunch of 
.csv files for your Playlists, Radio Stations and Tracks


How to use this program:

1. Run my program with GoogleMusicRemovedSongsParser.exe or if you have Python 3.x installed, run GoogleMusicRemovedSongsParser.py with it.

2. Choose the source folder containing the Google Play Music .csv files you are trying to scan

3. Choose the destination folder where you want to save the results. (This must be a different folder than the source folder)

4. Chose a file name for the resulting file.

5. Click on the Search button

6. The program will tell you if it found songs that have been removed from Google Play Music

7. Open the resulting .csv file from wherever your destination folder was set to
