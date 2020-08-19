import pandas as pd
import numpy as np
import math
import sys
import tkinter as tk
woodLength = 8*12
woodWidth = 4*12
allRips = pd.DataFrame()
filePath = sys.argv[1:]

def csvConverter(csvLink, output_file):
    xl = pd.ExcelFile(csvLink)
    print(len(xl.sheet_names))
    for x in xl.sheet_names:
        xlFile = xl.parse(sheet_name = x, header=None)
        dfSorted(xlFile.to_numpy(),x, output_file)
    return xlFile.to_numpy()
    

def sorter (woodSize):
    sortedWood = woodSize[np.argsort(woodSize[:, 1])[::-1]]
    sortedWood = sortedWood[np.argsort(sortedWood[:, 0])]
    return(sortedWood)

def dfSorted(woodSize, sheet_name, output_file):
    sortedWood = sorter(woodSize)
    allRips = pd.DataFrame()
    npWood = np.array(sortedWood)
    uniqueRips = np.unique(npWood[:,0])
    for rip in uniqueRips:
        ripHolder = npWood[npWood[:,0] == rip] #creates a numpy array of just one rip
        ripSorter(ripHolder[:,1], rip, allRips)
    with pd.ExcelWriter(output_file ,mode="a", engine="openpyxl") as writer:
        allRips.to_excel(writer,sheet_name=str(sheet_name))
    
    
# takes all values of a rip length and creates cuts for that rip
def ripSorter(a,ripSize, allRips):
    print(ripSize)
    riplist = ([])
    cutTotal = 0
    j = 0
    a  =  np.sort(a)
    a = a[::-1]
    while a.size != 0:
        if((cutTotal + a[0]) <= woodLength):
            riplist = np.append(riplist, a[0])
            cutTotal += a[0]
            a = np.delete(a,0)
        else:
            holder = []
            for x in range (len(a)):
                if(cutTotal + a[x] <= woodLength):
                    riplist = np.append(riplist,a[x])
                    cutTotal += a[x]
                    holder.append(x)
            for y in holder:
                a = np.delete(a,y)
            while(len(riplist) < 5):
                riplist = np.append(riplist, np.NaN)
            allRips[(str(ripSize) + "v" + str(j))] = pd.Series(riplist)
            j += 1
            riplist = ([])
            cutTotal = 0
    while(len(riplist) < 5):
                riplist = np.append(riplist, np.NaN)
    if(riplist.size != 0):
        allRips[(str(ripSize) + "v" + str(j))] = pd.Series(riplist)
    print(allRips)
