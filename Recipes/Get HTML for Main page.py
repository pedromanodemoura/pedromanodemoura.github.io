# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:22:21 2021

@author: c20460
"""

import glob
import pandas as pd

files = glob.glob(r'C:\Users\c20460\Downloads\Recipes\HTML\*')

filepath = ['..' + x[33::].replace('\\','/') for x in files]

filenames = [x.split('\\')[-1].split('.')[0] for x in files]

files_df = pd.DataFrame({'File': filepath, 'File Name': filenames})

files_df['Meal Type']

for meal in range(0,len(files_df)):
    if 'CHICKEN' in files_df.loc[meal,'File Name'].upper():
        files_df.loc[meal,'Meal Type'] = 'Chicken'
    elif 'BEEF' in files_df.loc[meal,'File Name'].upper():
        files_df.loc[meal,'Meal Type'] = 'Beef'
    elif 'CARNE' in files_df.loc[meal,'File Name'].upper():
        files_df.loc[meal,'Meal Type'] = 'Beef'
    elif 'STEAK' in files_df.loc[meal,'File Name'].upper():
        files_df.loc[meal,'Meal Type'] = 'Beef'
    elif 'PORK' in files_df.loc[meal,'File Name'].upper():
        files_df.loc[meal,'Meal Type'] = 'Pork'
    else:
        files_df.loc[meal,'Meal Type'] = 'Other'
        
files_df = files_df.sort_values('File Name')        

text = ''

for meal in range(0,len(files_df)):
    div_meal =  '  ' + \
                '<div onclick="location.href=' + \
                "'" + \
                files_df.loc[meal,'File'] + \
                "'" + \
                ';" ' + \
                'class="filterDiv ' + \
                files_df.loc[meal,'Meal Type'] + \
                '">' + \
                files_df.loc[meal,'File Name'] + \
                '</div> \n'
                
    text = text + div_meal

files_json = files_df.to_json()

