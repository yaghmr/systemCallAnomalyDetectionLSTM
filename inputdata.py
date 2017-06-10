#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="Ktian"
import os


def readfilesfromAdir(dataset):
    #read a list of files
    files = os.listdir(dataset)
    files_absolute_paths = []
    for i in files:
        files_absolute_paths.append(dataset+str(i))
    return files_absolute_paths



file = "ADFA-LD/Training_Data_Master/UTD-0001.txt"
#this is used to read a char sequence from
def readCharsFromFile(file):
    channel_values = open(file).read().split()
    #print (len(channel_values))
    #channel_values is a list
    return channel_values
    #print (channel_values[800:819])



def get_all_call_sequences(dire):
    files = readfilesfromAdir(dire)
    allthelist = []
    print (len(files))

    for eachfile in files:
        if eachfile.endswith("txt"):
            allthelist.append(readCharsFromFile(eachfile))
        else:
            print (eachfile)

    elements = []
    for item in allthelist:
        for key in item:
            if key not in elements:
                elements.append(key)

    elements = map(int,elements)
    elements = sorted(elements)
    print ("The total elements:")
    print (elements)

    print ("The length elements:")
    print (len(elements))
    print (len(allthelist))


if __name__ == "__main__":
    dirc = "ADFA-LD/Training_Data_Master/"
    get_all_call_sequences(dirc)