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
    print (len(channel_values))
    #print (channel_values[800:819])


if __name__ == "__main__":
    readCharsFromFile(file)