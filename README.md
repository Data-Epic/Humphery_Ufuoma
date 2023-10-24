# Repository on projects done with Data Epic <br/>

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