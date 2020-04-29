import dionysus as d
import numpy as np

import sys
sys.path.append('../preprocessing')
from handledata import Handledata



if __name__ == '__main__':
    print('Running experiment...')

    print('Reading in data ...')
    preprocess_impl = Handledata()
    corona_data_frame = preprocess_impl.read_raw_data()

    print('Converting to 3D coordinates...')
    corona_data_frame = preprocess_impl.ones(corona_data_frame)
    point_data = preprocess_impl.tosphere(corona_data_frame)


    print('Writing to output file: output.txt')
    output= open("output.txt","w+")




    print('Rips Filtration')
    n_skeleton = 2
    rips_stopping_radius = 1000000 #Meters
    filtration_list = []
    counter = 0

    for infected_idx in range(0,point_data.size):
        if(infected_idx % 3 == 0):
            print('Day ', counter, '...')
            f = d.fill_rips(point_data[infected_idx], n_skeleton, rips_stopping_radius)

            filtration_list.append(f)

            counter = counter +1
            print('Simplices in rips filtration with sensitivity ', rips_stopping_radius)
            output.write('Simplices in rips filtration with sensitivity ')
            output.write(str(rips_stopping_radius))
            output.write('m\n')
            for simplex in f:
                
                for index in simplex:
                    '''
                    print('Simplex: ', simplex, 'Place: ', point_data[infected_idx+1][index],',', point_data[infected_idx+2][index])
                    '''
                    output.write('Day: ' )
                    output.write(str(counter))
                    output.write(' Simplex: ')
                    output.write(str(simplex))
                    output.write(' Place: ')
                    output.write(point_data[infected_idx+1][index])
                    output.write(',')
                    output.write(str(point_data[infected_idx+2][index]))
                    output.write("\n")
                    


            





