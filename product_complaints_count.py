#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:49:44 2018

@author: vicky
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
#from numpy import genfromtxt

style.use('ggplot')

with open('Consumer_Complaints.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    product_list = []
    product_complaint_count = dict()
    for line in csv_reader:
        if line[1] not in product_list:
            product_list.append(line[1])
        product_complaint_count[line[1]]=product_complaint_count.get(line[1],0)+1
    
#    print(product_list)
#    print(product_complaint_count)
        
    with open('Product_Complaint.csv','w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['product','Complaint_Count'])
        for key,value in product_complaint_count.items():    
            csv_writer.writerow([key,value])

plt.bar(range(len(product_complaint_count)),product_complaint_count.values(),align='center')
plt.xticks(range(len(product_complaint_count)),list(product_complaint_count.keys()))
plt.title('Product vs Number of Complaints Analysis')
plt.xlabel('Complaint Against Product')
plt.ylabel('Counts of Complaint')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig('Product_vs_complaintCount')
        