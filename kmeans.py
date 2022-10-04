import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('C:/Users/Arka Rutvik/Downloads/kmeans.jpeg',1)

def var(p1,p2):
    k = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return k


def Kmeans(k,img):
    p,q,r = img.shape
    i=0
    n=0
    c =[]
    img = img.reshape(-1,3)
    while(i<k):
        n = np.random.randint(0,img.shape[0])
        c.append(n)
        i = i+1
    cent = []
    for i in c:
        cent.append(img[i])
    z = 0
    iter = 10
    while(z< iter):
        print(1)
        fin = []
        for i in range(img.shape[0]):
            d =[]
            for j in range(k):
                d.append(var(img[i],cent[j]))
            min = d[0]
            for i in range(k):
                if (min > d[i]) :
                    min = d[i]
            for i in range(k):
                if (min == d[i]):
                    fin.append(i)
        cent = []
        i= 0
        while(i<k):
            r=0
            g=0
            b=0
            l =0
            for b in range(img.shape[0]):
                if (fin[b] == i):
                    r = r+ img[b][2]
                    g = g+ img[b][1]
                    b = b+ img[b][0]
                    l = l+1
            if (l==0):
                cent.append([0,0,0])
            else:
                cent.append([(b/l),(g/l),(r/l)])
            i = i+1
        z = z+1
        print(2)
    i=0
    print('No of clusters ',k)
    print('Color of clusters')
    while(i<k):
        print('Color of Cluster ',i+1, ' - ',cent[i])
        i = i+1
    a=0
    i=0
    for i in range(img.shape[0]):
        a = fin[i]
        img[i] = cent[a]
    
    img = img.reshape(467,700,3)
    plt.imshow(img)
        
Kmeans(5,img)