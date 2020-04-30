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
    img = Image.new('RGB', (256, 256))

    data = readoutput()
    name = '../imgs/virusmap'
    print('Number of days = ', len(data))
    for count, day in enumerate(data):
        filename = name + str(count)
        print(filename)
        WIDTH = 256
        HEIGHT = 256
        new_img = img.resize((WIDTH,HEIGHT))

        draw = ImageDraw.Draw(new_img)
        idx = 0
        while idx < len(day):
            if(day[idx][1] == 0):
                draw.point(((day[idx][2]+180)*WIDTH/360,(day[idx][3]+90)*HEIGHT/180), fill='red')
            if(day[idx][1] == 1):
                print(idx, day[idx])
                draw.line(
                        [
                            ((day[idx][2]+180)*WIDTH/360,(day[idx][3]+90)*HEIGHT/180),
                            ((day[idx+1][2]+180)*WIDTH/360,(day[idx+1][3]+90)*HEIGHT/180)
                            ], fill='red', width = 5)
                idx=idx+1
                print(idx)
        del draw
        #new_img.show()
        new_img.save(filename, 'jpeg')

            
        
