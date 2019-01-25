#! python3
# Google Music Removed Songs Parser v1.1
# Parses all .csv files in a specified folder for songs that have been tagged as "Removed".
# Writes out a .csv file that lists the removed songs.
# These .csv files should be provided by Google Takeout (takeout.google.com)

import sys, csv, os, tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog

gui = tkinter.Tk()
gui.geometry("1000x128")
gui.title("Google Music Removed Songs Parser v1.1")

folders = {"sourceFolder": None, "destinationFolder": None }


def getFolderPath(windowTitle, folderName, entryToUpdate):
    """
    Called when users press the 'Browse' button in order to choose a path on their system
    """
    folders[folderName] = filedialog.askdirectory(title=windowTitle)
    entryToUpdate.delete(0, 'end')
    entryToUpdate.insert(0, folders[folderName])

def startSearching(outputLabel):
    """
    Will try to parse through all .csv files in the source folder,
    then creates a new .csv file with the source folder's name that
    contains all the songs it found that have been tagged as removed.
    """
    directory = os.listdir(folders["sourceFolder"])
    totalRemoved = 0
    removedSongsRows = []

    # Loop through every file in the specified folder directory
    for csvFileName in directory:
        if not csvFileName.endswith(".csv"):
            continue # skip non-csv files
        
        # Read the csv file
        csvFileObj = open( os.path.join(folders["sourceFolder"], csvFileName) )
        readerObj = csv.DictReader(csvFileObj)

        for row in readerObj:
            # Make sure to save the column names only once
            if [] == removedSongsRows:
                removedSongsRows.append(row.keys())
            
            if "" != row["Title"] and "" != row["Artist"] and "Yes" == row["Removed"]:
                totalRemoved += 1
                removedSongsRows.append(row.values())
        csvFileObj.close()

    if(totalRemoved > 0):
        # Write out a csv file that only contains the songs removed
        with open( os.path.join(folders["destinationFolder"], fileNameEntry.get() + ".csv"), "w", newline='') as csvRemovedFile:
            writerObj = csv.writer(csvRemovedFile)
            writerObj.writerows(removedSongsRows)
        csvRemovedFile.close()

    outputLabel.config(text='Scanned a total of ' + str(len(directory)) + ' files.    Found ' + str(totalRemoved) + ' songs tagged as "Removed".', foreground='green' )

# Choose source folder UI
sourceDescription = "1. Source folder containing your Google Music .csv files"
sourceDescriptionLabel = Label(gui, text=sourceDescription, anchor='w', width=52)
sourceDescriptionLabel.grid(column=0, row=0)
sourceEntry = Entry(gui, width=75)
sourceEntry.grid(column=2, row=0)
sourceButton = Button(gui, width=20, text="Browse...", command=lambda *args: getFolderPath(sourceDescription, "sourceFolder", sourceEntry))
sourceButton.grid(column=1, row=0)

# Choose destination folder UI
destinationDesciption = "2. Destination folder to save results (Cannot be same as above folder)"
destinationDescriptionLabel = Label(gui, text=destinationDesciption, anchor='w', width=52)
destinationDescriptionLabel.grid(column=0, row=1)
destinationEntry = Entry(gui, width=75)
destinationEntry.grid(column=2, row=1)
destinationButton = Button(gui, width=20, text="Browse...", command=lambda *args: getFolderPath(destinationDesciption, "destinationFolder", destinationEntry))
destinationButton.grid(column=1, row=1)

# Choose saved file name
saveDescriptionLabel = Label(gui, text="3. Save File Name as: ", anchor='w', width=52)
saveDescriptionLabel.grid(column=0, row=2)
fileNameEntry = Entry(gui, width=22)
fileNameEntry.grid(column=1, row=2)
fileNameEntry.insert(0, "RemovedSongs")

# Results label
resultsLabel = Label(gui)
resultsLabel.grid(column=0, columnspan=2,row=3)

# Search button
searchButton = Button(gui, text="Search", command=lambda *args: startSearching(resultsLabel))
searchButton.grid(column=1, row=4)

gui.mainloop()