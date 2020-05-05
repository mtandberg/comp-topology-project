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
    whatday = 0

    h0_birth = []
    h0_death = []

    h1_birth = []
    h1_death = []

    h0_days = []
    h1_days = []

    for line in output:
        data = line.split("_")
        if data[0] == "Day":
            day_ctr = int(data[1])+1
            day_ctr_arr.append(day_ctr)
            #zero_homology.append(zero_homology_ctr)
            #one_homology.append(one_homology_ctr)
            zero_homology_ctr = 0
            one_homology_ctr = 0


            h0_days.append(h0_birth.copy())
            h0_days.append(h0_death.copy())

            h0_birth = []
            h0_death = []

            h1_days.append(h1_birth.copy())
            h1_days.append(h1_death.copy())

            h1_birth = []
            h1_death = []


            whatday = whatday+1

        else:
            #print(data[0][1])
            if int(data[0][1]) == 0:
                '''
                    if data[4] == "inf":
                            zero_homology_ctr = 1+zero_homology_ctr
                '''
                if(str(data[2]) == 'inf'):
                    h0_birth.append(1200000)
                else:
                    h0_birth.append(float(data[2]))


                if(str(data[4]) == 'inf'):
                    h0_death.append(1200000)
                else:
                    h0_death.append(float(data[4]))
                

            elif int(data[0][1]) == 1:
                '''
                    if data[4] == "inf":
                            one_homology_ctr = 1+one_homology_ctr
                '''
                if(str(data[2]) == 'inf'):
                    h1_birth.append(1200000)
                else:
                    h1_birth.append(float(data[2]))


                if(str(data[4]) == 'inf'):
                    h1_death.append(1200000)
                else:
                    h1_death.append(float(data[4]))

            else:
                print("n>1-homology found")

    #print(zero_homology)
    #print(one_homology)
    h0_days.append(h0_birth.copy())
    h0_days.append(h0_death.copy())

    h0_birth = []
    h0_death = []

    h1_days.append(h1_birth.copy())
    h1_days.append(h1_death.copy())

    h1_birth = []
    h1_death = []
    '''
    plt.xticks = (day_ctr_arr, 10)
    plt.bar(day_ctr_arr, zero_homology, align='center', alpha=0.5, color='g', label="Connected Components")
    plt.bar(day_ctr_arr, one_homology, align='center', alpha=0.5, color='b', label="Cycles")
    '''
    name = './plots/persistence'
    for day in range(int(len(h0_days)/2)):
        filename = name + str(day)
         
        plt.plot([1, 1000000], [1, 1000000])
        plt.scatter(h0_days[2*day],h0_days[2*day+1],color = 'b',label='H0')
        plt.scatter(h1_days[2*day],h1_days[2*day+1],color = 'g', label='H1')
        plt.xlabel("Radius of birth")
        plt.ylabel("Radius of death")
        plt.legend()
        plt.title("0- and 1- Homology persistence diagram for day" + str(day))
        plt.savefig(filename)
        plt.clf()

        #plt.show()
