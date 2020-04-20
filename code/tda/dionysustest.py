import dionysus as d
import numpy as np


if __name__ == '__main__':

    print('Testing a TDA output for Dionysus...')

    vertex1 = 0
    vertex2 = 1
    vertex3 = 2

    print('Making simplex from verts: ', vertex1, vertex2, vertex3)


    s=d.Simplex([vertex1,vertex2,vertex3])
    print("Here is the simplex: ", s)

    print("Its dimension is: ", s.dimension())

    print("And its boundary...")
    for sb in s.boundary():
        print(sb)

    


    print("Great - So we can work with simplecies, but we can also work with points")
    print("Here is an array (Must be numpy)")
    points = np.array([[0.0,1.0],[2.0,0.0],[0.0,0.0]])
    print(points)

    #Computes rips filtration up to 2 skeleton and up to radius 5
    f = d.fill_rips(points, 2, 5)
    print("Here is the Rips filtration of the points: ", f)
    for x in f:
        print("Simplex :", x)

