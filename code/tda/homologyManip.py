import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

if __name__ == '__main__':
    output = open("homology.txt", "r")
    day_ctr = 0 #will let us only grab one entry per 1-simplex
    day_ctr_arr = [] #used in graphing
    zero_homology = []
    one_homology = []
    zero_homology_ctr = 0
    one_homology_ctr = 0


    for line in output:
        data = line.split("_")
        if data[0] == "Day":
            day_ctr = int(data[1])+1
            day_ctr_arr.append(day_ctr)
            zero_homology.append(zero_homology_ctr)
            one_homology.append(one_homology_ctr)
            zero_homology_ctr = 0
            one_homology_ctr = 0
        else:
            #print(data[0][1])
            if int(data[0][1]) == 0:
                    if data[4] == "inf":
                            zero_homology_ctr = 1+zero_homology_ctr

            elif int(data[0][1]) == 1:
                    if data[4] == "inf":
                            one_homology_ctr = 1+one_homology_ctr

            else:
                print("n>1-homology found")

    #print(zero_homology)
    #print(one_homology)
    plt.xticks = (day_ctr_arr, 10)
    plt.bar(day_ctr_arr, zero_homology, align='center', alpha=0.5, color='g', label="Connected Components")
    plt.bar(day_ctr_arr, one_homology, align='center', alpha=0.5, color='b', label="Cycles")
    plt.xlabel("Day")
    plt.ylabel("Number of Instances")
    plt.legend()
    plt.title("0- and 1- Homology groups per day at r=1,000KM")
    plt.show()
