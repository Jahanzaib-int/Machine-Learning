# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:04:08 2018

@author: Jahanzaib Malik
"""

import numpy as np
import pandas as pd
import socket
import struct

#Defining Converter functions
def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))



#Importing Dataset
dataset = pd.read_csv('DOS2012.csv')
dataset = np.array(dataset)
#making DataFrame just to check data in case from variable explorer
dataset_in_PD = pd.DataFrame(dataset)

#Calculating Rows and Columns
rows = len(dataset)
columns = len(dataset[0])


#Parsing 4th Column of ip 
for x in range(0,rows):
    dataset[x][5] = ip2int(dataset[x][5])

#Parsing 6th Column of ip 
for x in range(0,rows):
    dataset[x][8] = ip2int(dataset[x][8])


#making DataFrame just to check data in case from variable explorer
dataset_in_PD = pd.DataFrame(dataset)


#Saving File Now 
dataset_in_PD.to_csv('DOS2012.csv', index=False) 








