from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt

# Initialising kmeans 

k = KMeans(n_clusters = 5, max_iter = 300,tol = 0.0001,n_init = 10)

# Importing the image

img = cv2.imread('C:/Users/Arka Rutvik/Downloads/kmeans.jpeg',1)

# Reshaping it into 2-d array where each row has 3 values(b,g,r) corresponding to a particular pixel

img =  img.reshape(-1,3)

# Performing Kmeans

out = k.fit_predict(img)

# Checking the label of each pixel (the cluster it is assigned to) and then changing the color of it to it's centroid color accordingly

a=0
for i in range(img.shape[0]):
    a = out[i]
    img[i] = k.cluster_centers_[a]

# Reshaping it to original shape

img = img.reshape(467,700,3)

plt.imshow(img)
    