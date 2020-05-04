import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    output = open("output.txt", "r")
    day_ctr = 1 #will let us only grab one entry per 1-simplex

    #arrays to hold data on 0-, 1-, and 2-simplices
    zero_simplex = []
    one_simplex = []
    two_simplex = []

    #counters to hold data to be appended
    a=0
    zero_simplex_ctr = 0
    one_simplex_ctr = 0
    two_simplex_ctr = 0
    day_ctr_arr = [] #used in graphing
    for line in output:
        if a != 0: #handles multiple entries for every 1- ad 2-simplex
            a = a-1
        else:
            data = line.split('_')
            #if the day goes up one, add the previous day's data, reset
            #holders to zero/blank, and continue
            if int(data[1]) != int(day_ctr):
                zero_simplex.append(zero_simplex_ctr)
                one_simplex.append(one_simplex_ctr)
                two_simplex.append(two_simplex_ctr)
                day_ctr_arr.append(day_ctr)
                day_ctr = 1+day_ctr
                zero_simplex_ctr = 0
                one_simplex_ctr = 0
                two_simplex_ctr = 0
            #gather data from input file
            simplex_from_data = data[3]
            end = simplex_from_data.find(">")
            simplex = simplex_from_data[0: end+1]
            points_in_simplex = simplex.split(",")

            #determine if 0-, 1-, or 2-simplex
            if len(points_in_simplex) == 1:
                zero_simplex_ctr = 1+ zero_simplex_ctr
            elif len(points_in_simplex) == 2:
                one_simplex_ctr = 1+ one_simplex_ctr
                a = 1
            elif len(points_in_simplex) == 3:
                two_simplex_ctr == 1 + two_simplex_ctr
                a=2

    #plot data in a bar graph
    plt.bar(day_ctr_arr, zero_simplex, align='center', alpha = 0.5, color = 'b', label = "zero-simplices")
    plt.bar(day_ctr_arr, one_simplex, align='center', alpha = 0.5, color = 'g', label = "one-simplicies")
    plt.xlabel("Day")
    plt.ylabel("Number of Simplicies")
    plt.legend()
    plt.title('Number of 0- and 1- Simplicies per Day at 1,000km Sensitivity')
    plt.show()
