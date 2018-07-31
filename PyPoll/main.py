# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:44:48 2018

@author: Natalie Matusevich
############# Important !!!!! ##################
election_data.csv source file location:
    Path to the source file is (Unix stile): 
        ./Resources/election_data.csv
        
    It means that the main.py code should be in 
    the same directory as the Resources subfolder.
###############################################
    
election_result.txt output file will be created in 
the same directory as the main.py code
"""

import csv
import os

vCount = 0  
#voteCastCount - dictionary of candidates 
voteCastCount = {}

filePath=os.path.join("Resources","election_data.csv")
with open(filePath,"r", newline="\n") as sourceFile:
    #skip the header
    next(sourceFile)
    sourceData = csv.reader(sourceFile, delimiter=",")
    for vLine in sourceData:
        vCount += 1
        key = vLine[2]
        if key in voteCastCount:
            voteCastCount[key] += 1
        else:    
            voteCastCount[key] = 1

#determine the winner
dictToList = [value for key, value in voteCastCount.items()]
winNumber = max(dictToList)
winner = [key for key, value in voteCastCount.items() if value==winNumber]

#generate the output string
outputStr = "Election Results\n"
outputStr += "  -------------------------\n"
outputStr += "  Total Votes: {}\n".format(vCount)
outputStr += "  -------------------------\n"

        #total = 0
for key in  voteCastCount:
    percentage =  100 * voteCastCount[key]/vCount
    outputStr += "  {0}: {1:2.3f}% ({2})\n".format(key, percentage, voteCastCount[key])

outputStr += "  -------------------------\n"
outputStr +="  Winner: {}\n".format(winner[0])
outputStr += "  -------------------------\n"    
print (outputStr)

#putput file
outputFile = open("election_result.txt","w")
outputFile.write(outputStr)
outputFile.close()
