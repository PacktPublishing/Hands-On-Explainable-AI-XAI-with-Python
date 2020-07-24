#k-means clustering
#Copyright 2020 Denis Rothman MIT License. See LICENSE.
#KNN
#Denis Rothman copyright 2020, MIT License
from sklearn.cluster import KMeans  
import pandas as pd
import pickle
import numpy as np

#I.Training the dataset 
dataset = pd.read_csv('data_age_education.csv')
print (dataset.head())
print(dataset)

#creating the classifier
k = 2
kmeans = KMeans(n_clusters=k)

#running K-means clustering algorithm
kmeans = kmeans.fit(dataset)         #Computing k-means clustering
gcenters = kmeans.cluster_centers_   # the geometric centers or centroids
print("The geometric centers or centroids:")
print(gcenters)

#save model
filename="kmc_model.sav"
pickle.dump(kmeans, open(filename, 'wb'))
print("model saved")

#II.Testing the dataset
#dataset = pd.read_csv('data.csv')
kmeans = pickle.load(open('kmc_model.sav', 'rb'))
   
#making and saving the predictions
kmcpred=np.zeros((32563, 3)) 
predict=1
if predict==1:
    for i in range(0,32560):
        xf1=dataset.at[i,'age'];xf2=dataset.at[i,'numed'];
        X_DL = [[xf1,xf2]]
        prediction = kmeans.predict(X_DL)
        #print (i+1,"The prediction for",X_DL," is:",str(prediction).strip('[]'))
        #print (i+1,"The prediction for",str(X_DL).strip('[]')," is:",str(prediction).strip('[]'))
        p=str(prediction).strip('[]')
        p=int(p)
        kmcpred[i][0]=int(xf1);kmcpred[i][1]=int(xf2);kmcpred[i][2]=p;
np.savetxt('ckmc.csv', kmcpred, delimiter=',', fmt='%d')
print("predictions saved")
