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
# =============================================================================

# loading credentials and authorizing gspread
# client = gspread.service_account(filename = path)
# # =============================================================================
# #         spreadsheet = client.create(self.spreadsheet)
# #         spreadsheet.share("faradayotuoniyo@gmail.com",perm_type="user",role="writer",email_message="Here is your spreadsheet")
# #         worksheet = spreadsheet.add_worksheet(self.worksheet, 100,20)
# # =============================================================================
# spreadsheet = client.open("Gspread Spreadsheet")
# worksheet = spreadsheet.worksheet("Sheet1")
# worksheet.clear() 

options = webdriver.ChromeOptions() 
#instantiate driver
driver = webdriver.Chrome(options=options) 
driver.set_window_size(1120,1000)
# driver.get(github_url) 
#waiting for data to be available implicitly
# driver.implicitly_wait(30) 



class UpdateSpreadSheet():
    
    def __init__(self):
        
        #dictionary to hold features and values of github data
        self.github_repo = {}
        #list variable holding repository names
        self.RepoName = [] 
        #list variable holding language used
        self.Language = [] 
        #list variable holding Description of each repo
        self.Description = [] 
        #list variable holding datetime when repo was las updated/posted
        self.Datetime_Posted = []  
    
    def getting_data(self):
  
        #Getting Repository names from github repo  with selenium
        self.RepoName += [name.text if isinstance(name,webdriver.remote.webelement.WebElement) is True else name for name in driver.find_elements(by=By.CSS_SELECTOR,value='a[itemprop="name codeRepository"]')]
        #Getting Language used for each repo from github repo  with selenium
        self.Language += [language.text if isinstance(language,webdriver.remote.webelement.WebElement) is True else language for language in driver.find_elements(by=By.CSS_SELECTOR,value='span[itemprop="programmingLanguage"]')]
        #Getting Description of each repo from github repo  with selenium
        self.Description += [desc.text if isinstance(desc,webdriver.remote.webelement.WebElement) is True else desc for desc in driver.find_elements(by=By.CSS_SELECTOR, value='p[itemprop="description"]')]
        #Getting Datetime when repo was posted or last updated from github repo  with selenium
        self.Datetime_Posted += [datetime.text if isinstance(datetime,webdriver.remote.webelement.WebElement) is True else datetime for datetime in driver.find_elements(by=By.CSS_SELECTOR,value='relative-time[class="no-wrap"]')] 
        
    
    def populating_dictionary(self):
        #populating dictionary github_repo which will be used to create pandas dataframe
        self.github_repo["RepoName"] = self.RepoName
        self.github_repo["Language"] = self.Language
        self.github_repo["Description"]= self.Description
        self.github_repo['Datetime_posted'] = self.Datetime_Posted
    
    
    def create_dataframe(self):
        #attempting to create pandas dataframe and assigning to data variable
        try:
            self.data =  pd.DataFrame(self.github_repo).reset_index(drop=True)
        except Exception as e:
            raise ValueError("All arrays must be of the same length",e)
            
    def worksheet_update(self):
        #updating to spreadsheet
        self.worksheet.update([self.data.columns.tolist()] + self.data.values.tolist()) 