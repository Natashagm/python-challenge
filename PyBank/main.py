# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 06:28:09 2018

@author: Natalie Matusevich
############# Important !!!!! ##################
budget_data.csv source file location:
    Path to the source file is (Unix stile): 
        ./Resources/election_data.csv
        
    It means that the main.py code should be in 
    the same directory as the Resources subfolder.
###############################################
    
budget_result.txt output file will be created in 
the same directory as the main.py code
"""

import csv
import os

vCount = 0 
totalAmt = 0 
prevAmt = 0
#deltaList - list of monthly changes 
deltaList = []
#deltaDateList - list of dates associated with deltaList
deltaDateList= []

filePath=os.path.join("Resources","budget_data.csv")
with open(filePath,"r", newline="\n") as sourceFile:
    #skip the header
    next(sourceFile)
    sourceData = csv.reader(sourceFile, delimiter=",")
    for vLine in sourceData:
        currentAmt = int(vLine[1])
        vCount += 1
        totalAmt += int(vLine[1])
        if vCount > 1:
            delta = currentAmt - prevAmt
            deltaList.append(delta) 
            deltaDateList.append( vLine[0]) 
        prevAmt = currentAmt 

#average change
avgChange = 0.00
for i in deltaList:
    avgChange += i
avgChange=avgChange/(len(deltaList))   

#min and max values
Delta = max(deltaList)
idxMax = deltaList.index(Delta)

Delta = min(deltaList)
idxMin = deltaList.index(Delta)

#generate the output string
outputString = "\nFinancial Analysis\n"
outputString += "  ----------------------------\n"
outputString += "  Total Months: {}\n".format(vCount)
outputString += "  Total: ${}\n".format(totalAmt)
outputString += "  Average  Change: {}\n".format(avgChange)
outputString += "  Greatest Increase in Profits: {0} (${1})\n".format(deltaDateList[idxMax],deltaList[idxMax])
outputString += "  Greatest Decrease in Profits: {0} (${1})\n".format(deltaDateList[idxMin],deltaList[idxMin])

#output to terminal
print (outputString)

#output to budget_result.txt file
f=open("budget_result.txt","w")
f.write(outputString)
f.close()
