#Twitter file organizer.
#By Catherine King
import os
from pathlib import Path

path = r"C:\Users\Catherine\Desktop\Misc\Saved art\Art\Individual twitter downloads\\"
#Must end in \\, since this creates and searches for subfolders. For some reason, a single slash doesn't work on the end of a line.
Username = r"\\"
newpath = path+Username

currentitem = "" #The item name used in operations.

def FolderCreator():
    newpath = path+Username
    print(newpath)
    if not os.path.exists(str(newpath)):
    #Checks if a folder with the name specified below exists. 
        print("No path exists! Making new folder")
        updatepath = os.makedirs(str(newpath))
        #print("updatepath:",updatepath,"")
        #print("oldpath"+path+currentitem)
        #print("newpath"+newpath+"\\"+currentitem)
        #Some test print lines. 
        Path(path+currentitem).rename(newpath+"\\"+currentitem)
        #Moves the file to new folder.
    else:
        Path(path+currentitem).rename(newpath+"\\"+currentitem)
        #If it does exist, just moves the file there.
        
with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)
        if(".zip" in entry.name):
        #Only works on files ending with .zip. Change as needed or remove entirely (Though doing so may make it operate on folders themselves?)
            nameentrystring = entry.name
            Username = ""
            for element in nameentrystring:
            #For every letter in the file name.
                if(element == "-"):
                #If the letter is -, stop adding letters to the new folders name (or the folder to search for)
                #The twitter downloader I use output .zips of accounts with names like ArtistMcArtistFace-twitter-945953, so this script would search for/create a folder named ArtistMcArtistFace by splitting at the -.
                    #print(entry.name)
                    currentitem = entry.name
                    FolderCreator()
                    Username = ""
                    break;
                else:
                    Username += element
                    #Adds the current letter to the name of the new folder.
            print("ZIP");



