import numpy as np
from scipy import sparse
import csv
from sklearn import svm
from sklearn.neighbors.nearest_centroid import NearestCentroid

# gender
Y = []

# [height, weight, shoe_size]
X = []

# read CSV file
genderFile = open('gender.csv')
genderReader = csv.reader(genderFile)

# skip header
iter_genderReader = iter(genderReader)
next(iter_genderReader)

# populate lists
for row in iter_genderReader:
   Y.append(row[0])
   X.append(row[1:])

# close CSV file
genderFile.close()

# covert string values to numbers
X_len = len(X)
for row in range(X_len):
    X[row][0] = float(X[row][0])
    X[row][1] = float(X[row][1])
    X[row][2] = float(X[row][2])

# initialize classifier
clf = svm.LinearSVC()
clf2 = NearestCentroid()
clf3 = svm.SVC()

# train classifier using data set
clf = clf.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 = clf3.fit(X, Y)

# enter user values for classifier
height = input('What is your height? (cm)')
weight = input('What is your weight? (kg)')
shoe_size = input('What is your shoe size? (eu)')

# catch string inputs
try:
    height = float(height)
    weight = float(weight)
    shoe_size = float(shoe_size)
except ValueError:
    print("Invalid input entered")
    exit()
# catch negative and zero inputs
if height <= 0.0 or weight <= 0.0 or shoe_size <= 0.0:
    print('Invalid number entered')
    exit()
    
# classifier prediction
prediction = clf.predict([[height, weight, shoe_size]])
prediction2 = clf2.predict([[height, weight, shoe_size]])
prediction3 = clf3.predict([[height, weight, shoe_size]])

# display predictions
gender = prediction[0]
gender2 = prediction2[0]
gender3 = prediction3[0]

print("Linear Support Vector - " + gender)
print("Nearest Centroid - " + gender2)
print("C-Support Vector - " + gender3)

# determine final prediction
result = ''
if gender == gender2 or gender == gender3:
    result = gender
else:
    result = gender3

# determine gender that is not prediction
anti_result = ''
if result == 'Male':
    anti_result = 'Female'
else:
    anti_result = 'Male'

# write user values to data set
validation = input('Is ' + result + ' correct? (y/n)')
if validation == "y":
    genderFile = open('gender.csv','a',newline='')
    genderWriter = csv.writer(genderFile)
    genderWriter.writerow([result,height,weight,shoe_size])
    genderFile.close()
elif validation == "n":
    genderFile = open('gender.csv','a',newline='')
    genderWriter = csv.writer(genderFile)
    genderWriter.writerow([anti_result,height,weight,shoe_size])
    genderFile.close()
else:
    exit()




