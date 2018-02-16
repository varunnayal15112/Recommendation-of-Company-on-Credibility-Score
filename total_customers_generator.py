#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 01:44:44 2018

@author: vicky
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random
#from numpy import genfromtxt

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
    final_company_list = []
    company_customer_count = dict()
    for line in csv_reader:
        if(int(line[1])>=500):
            if line[0] not in final_company_list:
                final_company_list.append(line[0])
            company_customer_count[line[0]]=generate_customer_count(int(line[1]))
    
    print(final_company_list)
    print(company_customer_count)
        
    with open('Customer_Count_of_Companies.csv','w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['Company','Customer_Count'])
        for key,value in company_customer_count.items():    
            csv_writer.writerow([key,value])
        