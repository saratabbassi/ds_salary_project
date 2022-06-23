# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:26:41 2022

@author: sarat
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/sarat/Documents/ds_salary_project/chromedriver.exe"

df= gs.get_jobs('data scientist', 15,False,path,15)
df.to_csv('glassdoor_jobs.csv', index = False)