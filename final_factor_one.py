#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 01:22:19 2018

@author: vicky
"""

import csv
import random
from pymongo import MongoClient
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

def generate_customer_count(complaint_count):
    if complaint_count>=500 and complaint_count<1000:
        return random.randint(3000,5000)
    else:
        x=complaint_count//1000
        return random.randint(5*x*1000,7*(x+1)*1000)

with open('Company_Complaint_Count.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    final_data = []
    for line in csv_reader:
        if(int(line[1])>=500):
            total_customer = generate_customer_count(int(line[1]))
            complaint_ratio = (int(line[1])/total_customer)*100
            final_data.append([line[0],total_customer,line[1],complaint_ratio])
    
    print(final_data)
        
    with open('Customer_Count_of_Companies_with_complaint_ratio.csv','w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['Company','Customer_Count','Complaint_Count','Complaint_Ratio'])
        for data in final_data:    
            csv_writer.writerow(data)

client = MongoClient('localhost')
db = client['Consumer_Complaints_Analysis']
collection = db['Company_Complaint_Ratio']
collection.drop()
for data in final_data:
    collection.insert_one({'Company':data[0],'Customer_Count':data[1],'Complaint_Count':data[2],'Complaint_Ratio':data[3]})


company_complaint_ratio = dict()
for data in final_data:
    company_complaint_ratio[data[0]] = data[3]
    
plt.bar(range(len(company_complaint_ratio)),company_complaint_ratio.values(),align='center')
plt.xticks(range(len(company_complaint_ratio)),list(company_complaint_ratio.keys()))
plt.title('Company Complaint Ratio Analysis')
plt.xlabel('Company')
plt.ylabel('Complaint Ratio')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
plt.gcf().savefig('company_complaint_ratio')
        

