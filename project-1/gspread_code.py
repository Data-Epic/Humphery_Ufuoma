import os
import logging 
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.DEBUG, 
                    format="%(levelname)s (%(asctime)s) : %(message)s (%(lineno)d)")
 
current_working_directory = os.getcwd()
#project_json is the credential file for the service account created
project_json = "spartan-figure-402211-2241d0349aab.json"
path = os.path.join(current_working_directory,project_json)

#url for github repo stored in variable github_url
github_url = "https://github.com/Humphery7?tab=repositories"

def update_spreadsheet(spreadsheet = "Gspread SpreadSheet",worksheet="Sheet1"):
    
    ''' authenticates python script to passed-in spreadsheet, 
        gets data from github repo and updates the chosen worksheet of the spreadsheet
        with the data to ''' 
        
    
    #loading credentials and authorizing gspread
    client = gspread.service_account(filename=path)
    worksheet = client.open(spreadsheet).worksheet(worksheet)
    #clearning worksheet on each run of program
    worksheet.clear() 
    
    
        
    options = webdriver.ChromeOptions() 
    #instantiate driver
    driver = webdriver.Chrome(options=options) 
    driver.set_window_size(1120,1000)
    driver.get(github_url) 
    #waiting for data to be available implicitly
    driver.implicitly_wait(30) 
    
    #dictionary to hold features and values of github data
    github_repo = {}
    #list variable holding repository names
    RepoName = [] 
    #list variable holding language used
    Language = [] 
    #list variable holding Description of each repo
    Description = [] 
    #list variable holding datetime when repo was las updated/posted
    Datetime_Posted = []  

    #Getting Repository names from github repo  with selenium
    RepoName += [name.text for name in driver.find_elements(by=By.CSS_SELECTOR,value='a[itemprop="name codeRepository"]')]
    #Getting Language used for each repo from github repo  with selenium
    Language += [language.text for language in driver.find_elements(by=By.CSS_SELECTOR,value='span[itemprop="programmingLanguage"]')]
    #Getting Description of each repo from github repo  with selenium
    Description += [desc.text for desc in driver.find_elements(by=By.CSS_SELECTOR, value='p[itemprop="description"]')]
    #Getting Datetime when repo was posted or last updated from github repo  with selenium
    Datetime_Posted += [time.text for time in driver.find_elements(by=By.CSS_SELECTOR,value='relative-time[class="no-wrap"]')] 
        
    #populating dictionary github_repo which will be used to create pandas dataframe
    github_repo["RepoName"] = RepoName
    github_repo["Language"] = Language
    github_repo["Description"]= Description
    github_repo['Datetime_posted'] = Datetime_Posted
    
    #attempting to create pandas dataframe and assigning to data variable
    try:
        data =  pd.DataFrame(github_repo).reset_index(drop=True)
    except Exception as e:
        logging.critical("one or more elements were not found", e)
        exit(0)
        
    #updating to spreadsheet
    worksheet.update([data.columns.tolist()] + data.values.tolist()) 


update_spreadsheet()