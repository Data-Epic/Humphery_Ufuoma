# Repository on projects done with Data Epic <br/>

### -*- coding: utf-8 -*-
### """
### Created on Mon Oct 16 15:12:29 2023 <br/>
### @author: Humphery_Ufuoma <br/>
### Project : getting data from github repositories(through selenium library) and 
### sending to google spreadsheet with gspread package
### """

## This Project Utilizes the Gspread Package to push data/datasets to a Google SpreadSheet <br/>
-> Requirements to accomplish this project are in the requirements.txt file <br/>

## input data is gotten from github repo : https://github.com/Humphery7?tab=repositories <br/>

## Process <br/>
 -> It is required to authenticate python script by doing the following <br/>
### Enable API Access for a Project <br/>
1. Head to Google Developers Console and create a new project (or select the one you already have).<br/>
2. In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.<br/>
3. In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.<br/>
4. Using Service Account (A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs [sic]).Since it’s a separate account, by default it does not have access to any spreadsheet until you share it with this account. Just like any other Google account. <br/>

Here’s how to get one: <br/>
1. Enable API Access for a Project if you haven’t done it yet. <br/>
2. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”. <br/>
3. Fill out the form <br/>
4. Click “Create” and “Done”. <br/>
5. Press “Manage service accounts” above Service Accounts.<br/>
6. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”. <br/>
7. Select JSON key type and press “Create”. <br/>
8. You will automatically download a JSON file with credentials.<br/>
9. Very important! Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access this spreadsheet from your application or a script.<br/>
With this you are set up!

-> The Script uses the selenium library to get data from Github user account, data gotten are listed<br/>
1. Repository names<br/>
2. Language used<br/>
3. Description of repository<br/>
4. Datetime Repository was posted/last updated<br/>

-> After sucessfully obtaining the data from github, the data are used to create a pandas dataframe and are updated on a Google SpreadSheet using Gspread Package <br/>

## output result on spreadsheet is on : https://docs.google.com/spreadsheets/d/1omeaygKjly8K47I58mUb1hlRgU80wyXQ1iBSI1bPsdw/edit#gid=0



# Creating Test Script For Gspread_code <br/>

### -*- coding: utf-8 -*-
### """Created on Tue Oct 24 12:25:03 2023 """<br/>
### @author: Humphery_Ufuoma <br/>
### Project : creating test_code with pytest library for gspread_code which gets data using selenium from github repo and updates on google spreadsheet
### """

## This Project Utilizes the Pytest library to create a test_script for gspread_code <br/>
-> Requirements to accomplish this project are in the requirements.txt file <br/>

### No input data is required for creating the test script <br/>

## Process <br/>
 -> It is required install the pytest package using pip install pytest <br/>
 -> Test file must contain the name test either before or after : example test_gspread_code.py, cause this is how pytest automatically identifies it <br/>
    With this you are set up!

-> The Script uses the pytest library and unittest which is inbuilt in python to create test cases for gspread_code<br/>
-> The Following tests are created
1. test_getting_data : to test if data is sucessfully updated on list variables<br/>
2. test_populating_dictionary : to test if function to populate dictionary does so appropriately <br/>
3. test_creating_dataframe : test to check if dataframe is created successfully when given appropriate data and if the ValueError is raised when the data is not appropriate<br/>
4. test_worksheet_update : test to check if dictionary variable github_repo is succesfully being populated<br/>

-> After sucessfully obtaining the data from github, the data are used to create a pandas dataframe and are updated on a Google SpreadSheet using Gspread Package <br/>

## To run test navigate to directory where test file and main code file is and run the command pytest