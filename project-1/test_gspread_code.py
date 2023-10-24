# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:25:03 2023

@author: computer world
"""

import pytest
from gspread_code import UpdateSpreadSheet
from unittest.mock import patch
import pandas as pd


class TestUpdateSpreadSheet():
   
    def test_getting_data(self):
        '''test to check that the data is being added to the list
         variables successfully'''

        #creating instance of class UpdateSpreadSheet
        self.inst = UpdateSpreadSheet()
        #mocking selenium driver attribute for checks if code syntax is accurate
        with patch('gspread_code.driver.find_elements') as mocked_get:
            
            #mocked attribute driver.find_elements is assigned to list to check
            mocked_get.return_value = ['textID','yes']
            #calling getting_data function which begins to get the data from selenium
            self.inst.getting_data()
            #asserting all list variables were updated with first round of data gotten
            assert self.inst.RepoName == ['textID','yes']
            assert self.inst.Language == ['textID','yes']
            assert self.inst.Description == ['textID','yes']
            assert self.inst.Datetime_Posted == ['textID','yes']

            #assigning new data 
            mocked_get.return_value = [1,2]
            self.inst.getting_data()
            #checking all list variables retained previous data and have added new data
            assert self.inst.RepoName == ['textID','yes',1,2]
            assert self.inst.Language == ['textID','yes',1,2]
            assert self.inst.Description == ['textID','yes',1,2]
            assert self.inst.Datetime_Posted == ['textID','yes',1,2]

    def test_populating_dictionary(self):
        """test to check if dictionary variable
           github_repo is succesfully being populated"""
        
        #calling class
        self.inst = UpdateSpreadSheet()
        #populating list variables wiith values
        self.inst.RepoName = [1]
        self.inst.Language = [1,2]
        self.inst.Description = [1,2]
        self.inst.Datetime_Posted = [1,2]
        #calling function to populate dictionary
        self.inst.populating_dictionary()
        #asserting keys of dictionary are same as the number of list variables
        assert len(self.inst.github_repo.keys()) == 4
        #asserting values of dictionaries are identical to combination of values contained in list variables
        assert list(self.inst.github_repo.values()) == [[1],[1,2],[1,2],[1,2]]
        


    def test_creating_dataframe(self):
        """test to check if dataframe is created successfully
           when given appropriate data and if the ValueError
           is raised when the data is not appropriate"""
        
        #calling class
        self.inst = UpdateSpreadSheet()
        #populating dictionary variable github_repo with appropriate data
        self.inst.github_repo = {'test1':[2,'3'],'test2':['5','4']}
        #calling create data_frame function which creates a dataframe with dictionary github_repo
        self.inst.create_dataframe()
        #asserting data variable which holds the dataframe created from github_repo is equal expected dataframe
        assert self.inst.data.equals(pd.DataFrame({'test1':[2,'3'],'test2':['5','4']}))

        #populating github_repo variable with inappropriate data
        self.inst.github_repo = {'test1':[2,'3'],'test2':[5]}
        #asserting that ValueError is raised when an attempt to create a dataframe with this data is made
        with pytest.raises(ValueError):
            self.inst.create_dataframe()



    def test_worksheet_update(self):
        """test to check if the values passed in to
           update worksheet is accurate"""
        
        #calling class
        self.inst = UpdateSpreadSheet()
        #populating github_repo variable
        self.inst.github_repo = {'test1':[2,'3'],'test2':['5','4']}
        #creating dataframe from github_repo
        self.inst.create_dataframe()

        #asserting dataframe created contains expected columns
        assert self.inst.data.columns.tolist() == ['test1','test2']
        #asserting dataframe created contains expected values
        assert self.inst.data.values.tolist() == [[2,'5'],['3','4']]
