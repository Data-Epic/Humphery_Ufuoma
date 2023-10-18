# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:12:29 2023

@author: computer world

Project : getting data from github repositories(through selenium library) and 
sending to google spreadsheet with gspread package
"""

import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "documents/datasets_for_data_science/gspread_project/spartan-figure-402211-2241d0349aab.json"

def update_spreadsheet(spreadsheet = "Gspread SpreadSheet",worksheet="Sheet1"):
    
    client = gspread.service_account(filename=path)
    worksheet = client.open(spreadsheet).worksheet(worksheet)
    worksheet.clear() #clearning worksheet on each run of program
    
    def github_data(url = "https://github.com/Humphery7?tab=repositories"):
        
        options = webdriver.ChromeOptions() 
        driver = webdriver.Chrome(options=options) #instantiate driver
        driver.set_window_size(1120,1000)
        driver.get(url) 
        driver.implicitly_wait(30) #waiting for data to be available implicitly
        
        github_repo = {} #dictionary to hold features and values of github data
        RepoName = [] #list variable holding repository names
        Language = [] #list variable holding language used
        Description = [] #list variable holding Description of each repo
        Datetime_Posted = [] #list variable holding datetime when repo was las updated/posted 
        
        try:
            #Start Scapping from github repo with selenium
            RepoName += [name.text for name in driver.find_elements(by=By.CSS_SELECTOR,value='a[itemprop="name codeRepository"]')]
            Language += [language.text for language in driver.find_elements(by=By.CSS_SELECTOR,value='span[itemprop="programmingLanguage"]')]
            Description += [desc.text for desc in driver.find_elements(by=By.CSS_SELECTOR, value='p[itemprop="description"]')]
            Datetime_Posted += [time.text for time in driver.find_elements(by=By.CSS_SELECTOR,value='relative-time[class="no-wrap"]')] 
        except Exception as e:
            print("one or more of elements not found", e)
            
        #populating dictionary github_repo which will be used to create pandas dataframe
        github_repo["RepoName"] = RepoName
        github_repo["Language"] = Language
        github_repo["Description"]= Description
        github_repo['Datetime_posted'] = Datetime_Posted
        
        return pd.DataFrame(github_repo).reset_index(drop=True)

    data = github_data() #calling github_data function and assigning output to data

    worksheet.update([data.columns.tolist()] + data.values.tolist()) #updating to spreadsheet
    

update_spreadsheet()