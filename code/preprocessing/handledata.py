# Imports


import math
import random
import pandas as pd
import csv


'''
This class deals with reading in all of the data and storing it in a format we can work with - the pandas dataframe.
'''


class Handledata:
    def __init__(self):
        print("Doing nothing in constructor woo")

    #Takes in the default dataframe and converts it to a format we want
    def preprocess_data(self, raw_data):
        print("In preprocess function")

    def read_raw_data(self):
        with open('../../data/data.csv','rt')as f:
            data = csv.reader(f)
            column_names = next(data)
            data_frame = pd.read_csv('../../data/data.csv', names=column_names)
                
                    
            return data_frame.drop(0)

        
        



if __name__ == '__main__':
    print('Running COVID-19 Preprocessor...')

    preprocess_impl = Handledata()

    corona_data_frame = preprocess_impl.read_raw_data()

    '''
    for column_label, column_values in corona_data_frame.items():
        print(column_label, column_values[1])
    '''


    print(corona_data_frame)

     #turn the data into 1's (if number is greater than 50) or a 0 (if number is less than 50)
    for column_labels, column_values in corona_data_frame.items():
        row_num = 0
        if (column_labels != 'Province/State') and (column_labels !='Country/Region') and (column_labels !='Lat') and (column_labels !='Long'):
            for col_val in column_values:
                x = corona_data_frame.loc[row_num+1, column_labels]

                if int(col_val) <= 50:
                    corona_data_frame.loc[row_num+1, column_labels] = 0
                else:
                    corona_data_frame.loc[row_num+1, column_labels] = 1
                row_num = row_num + 1
    
    print(corona_data_frame)

#OUTPUT: Pandas dataframe with rows going from 1 to n, each representing a geographic area and its time evolution of coronavirus cases over time. 





