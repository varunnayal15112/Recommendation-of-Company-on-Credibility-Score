#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:10:03 2018

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
import string

style.use('ggplot')

with open('Consumer_Complaints.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    company_list = []
    company_complaint_count = dict()
    for line in csv_reader:
        company_name=str(line[10])
        if '.' in company_name:
            company_name=company_name.replace('.','_')
        if company_name not in company_list:
            company_list.append(company_name)
            company_complaint_count[company_name]=dict()
        company_complaint_count[company_name][line[1]]=company_complaint_count[company_name].get(line[1],0)+1
    
    print(company_list)
    print(company_complaint_count)
        
#    with open('Product_Complaint.csv','w') as new_file:
#        csv_writer = csv.writer(new_file)
#        csv_writer.writerow(['product','Complaint_Count'])
#        for key,value in product_complaint_count.items():    
#            csv_writer.writerow([key,value])

with open('complaint_count.json','w') as out_file:
    json.dump(company_complaint_count,out_file)

client = MongoClient('localhost')
db = client['Consumer_Complaints_Analysis']
collection = db['Company_Wise_Complaints']
collection.insert(company_complaint_count)
#plt.bar(range(len(product_complaint_count)),product_complaint_count.values(),align='center')
#plt.xticks(range(len(product_complaint_count)),list(product_complaint_count.keys()))
#plt.title('Product vs Number of Complaints Analysis')
#plt.xlabel('Complaint Against Product')
#plt.ylabel('Counts of Complaint')
#plt.legend()
#plt.show()
        