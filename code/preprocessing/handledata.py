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


#OUTPUT: Pandas dataframe with rows going from 1 to n, each representing a geographic area and its time evolution of coronavirus cases over time. 





