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
    homology = open("homology.txt","w+")




    print('Rips Filtration')
    n_skeleton = 2
    rips_stopping_radius = 1000000 #Meters
    filtration_list = []
    counter = 0

    for infected_idx in range(0,point_data.size):
        if(infected_idx % 4 == 0):
            print('Day ', counter, '...')
            f = d.fill_rips(point_data[infected_idx], n_skeleton, rips_stopping_radius)
            f.sort()

            #filtration_list.append(f)

            
            #print('Simplices in rips filtration with sensitivity ', rips_stopping_radius)
            '''
            output.write('Simplices in rips filtration with sensitivity ')
            output.write(str(rips_stopping_radius))
            output.write('m\n')
            '''
            for simplex in f:
                
                for index in simplex:
                    '''
                    print('Simplex: ', simplex, 'Place: ', point_data[infected_idx+1][index],',', point_data[infected_idx+2][index])
                    '''
                    output.write('Day_' )
                    output.write(str(counter))
                    output.write('_Simplex_')
                    output.write(str(simplex))
                    output.write('_Place_')
                    output.write(point_data[infected_idx+1][index])
                    output.write('_')
                    output.write(str(point_data[infected_idx+2][index]))
                    output.write('_')
                    output.write(str(point_data[infected_idx+3][index][0]))
                    output.write('_')
                    output.write(str(point_data[infected_idx+3][index][1]))
                    output.write("\n")
                    
            print('Homology output')
            m = d.homology_persistence(f)
            homology.write("Day_")
            homology.write(str(counter))
            homology.write("\n")

            print(m)

            dgms = d.init_diagrams(m,f)
            #print(dgms)
            #homology.write(dgms)

            

            for l, dgm in enumerate(dgms):
                for pt in dgm:
                    if(l !=2):
                        #print(pt)
                        #print("Day: ", l, "Birth: ", pt.birth, "Death ", pt.death)
                        homology.write("H")
                        homology.write(str(l))
                        
                        homology.write("_Birth_")
                        homology.write(str(pt.birth))
                        homology.write("_Death_")
                        homology.write(str(pt.death))
                        homology.write("_Day_")
                        homology.write(str(counter))
                        #homology.write("_homologygroup_")
                        #homology.write(str(l))
                        homology.write('\n')
               

            '''
            for i,c in enumerate(m):
                if(len(c) != 0):
                    #print(i,c)
                    homology.write(str(f[i]))
                    #simps = str(f[i]).split(',')

                    #homology.write('_HomologyChain')
                    homology.write('_')
                    homology.write(str(c))
                    rep = str(c).split('+')

                    print(rep)
                    for element in rep:
                        #print(element)
                        place = element.split('*')
                        #print(place)
                        simplex = int(place[1])
                        homology.write('_')
                        print(f[simplex])
                        homology.write(str(f[simplex]))
                        #print(int(name))
                        #print('Day names: ', point_data[infected_idx+1])
                        #homology.write('_')
                        #homology.write(point_data[infected_idx+1][int(name)-1])
                        #homology.write('_')
                        #homology.write(str(point_data[infected_idx+2][int(name)-1]))
                    
                    homology.write("\n")
            '''




            
            counter = counter +1





