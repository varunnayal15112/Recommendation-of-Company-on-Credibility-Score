#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:20:35 2018

@author: vicky
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
#from numpy import genfromtxt
import json
import pymongo
from pymongo import MongoClient

style.use('ggplot')

with open('Consumer_Complaints.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    state_list = []
    state_complaint_count_by_pincode = dict()
    state_complaint_count = dict()
    for line in csv_reader:
        state_name=str(line[5])
        if(state_name==""):
            state_name='others'
        if state_name not in state_list:
            state_list.append(state_name)
            state_complaint_count_by_pincode[state_name]=dict()
        state_complaint_count_by_pincode[state_name][line[6]]=state_complaint_count_by_pincode[state_name].get(line[6],0)+1
        state_complaint_count[state_name]=state_complaint_count.get(state_name,0)+1
        
    print(state_list)
    print(state_complaint_count_by_pincode)
    print(state_complaint_count)
    
#    with open('Product_Complaint.csv','w') as new_file:
#        csv_writer = csv.writer(new_file)
#        csv_writer.writerow(['product','Complaint_Count'])
#        for key,value in product_complaint_count.items():    
#            csv_writer.writerow([key,value])


#with open('state_complaint_count.json','w') as out_file:
#    json.dump(state_complaint_count,out_file)
    
    

#print("varun")

plt.bar(range(len(state_complaint_count)),state_complaint_count.values(),align='center')
plt.xticks(range(len(state_complaint_count)),list(state_complaint_count.keys()))
plt.title('State vs Number of Complaints Analysis')
plt.xlabel('Complaint in State ')
plt.ylabel('Counts of Complaint')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig('State_vs_complaintCount')

client = MongoClient('localhost')
db = client['Consumer_Complaints_Analysis']
collection = db['State_Complaint_Count_by_Pincode']
collection.drop()
collection.insert(state_complaint_count_by_pincode)


collection = db['State_Complaint_Count']
collection.drop()
collection.insert(state_complaint_count)
