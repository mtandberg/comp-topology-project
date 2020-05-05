import sys
import numpy
from PIL import Image, ImageDraw

def readoutput():
    output = open("../../tda/output.txt", "r")
    lines = output.readlines()

    data_by_days = []

    current_day = 0
    one_day = []
    for line in lines:
        contents = line.split('_')
        simplex = contents[3]
        simplex_dim = len(contents[3].split(','))-1

        #day, simplex dim, Lat and long
        data = [int(contents[1]), int(simplex_dim), float(contents[7]), float(contents[8].replace('\n',''))]

        

        #check if new day
        if(int(data[0]) == current_day):
            one_day.append(data)
        else:
            current_day = int(data[0])
            data_by_days.append(one_day)
            one_day = []
            one_day.append(data)


    return data_by_days
            

if __name__ == '__main__':
    #img = Image.open('background.jpg')
    WIDTH = 1000 
    HEIGHT = 1000 

    img = Image.new('RGB', (WIDTH,HEIGHT))

    data = readoutput()
    name = '../imgs/virusmap'
    print('Number of days = ', len(data))
    for count, day in enumerate(data):
        filename = name + str(count)
        print(filename)
        new_img = img.resize((WIDTH,HEIGHT))

        draw = ImageDraw.Draw(new_img)
        idx = 0
        while idx < len(day):


            #Draw 0 simplicies
            if(day[idx][1] == 0):
                draw.point(((day[idx][3]+180)*WIDTH/360,HEIGHT-(day[idx][2]+90)*HEIGHT/180), fill='red')

            #Remove Comment for addition of 1 simplicies
            #'''
            if(day[idx][1] == 1):
                #print(idx, day[idx])
                draw.line(
                        [
                            ((day[idx][3]+180)*WIDTH/360,HEIGHT-(day[idx][2]+90)*HEIGHT/180),
                            ((day[idx+1][3]+180)*WIDTH/360,HEIGHT-(day[idx+1][2]+90)*HEIGHT/180)
                            ], fill='blue', width = 0)
                idx=idx+1
            #'''


            idx = idx+1
        del draw
        #new_img.show()
        new_img.save(filename, 'jpeg')

            
        
