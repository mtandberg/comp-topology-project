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

    print('Rips Filtration')
    n_skeleton = 2
    rips_stopping_radius = 1
    filtration_list = []
    counter = 0
    for infected_coords in point_data:
        print('Day ', counter, '...')
        f = d.fill_rips(infected_coords, n_skeleton, rips_stopping_radius)
        filtration_list.append(f)
        counter = counter +1
        print('Simplices in f')
        for simplex in f:
            print(simplex)





