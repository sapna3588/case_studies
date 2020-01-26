"""We want to build a system where user is shown score of whether changing a job is right one or not
 for user. Whenever user changes job the satisfaction level goes lower because new people,
 new tools, new place to commute but if the new job is better than previous job
 then the later satisfaction level gains make up for this temporary loss -
 if the new job is very similar or worse then the satisfaction level never makes up
 and so user is better off not changing the job.
 How will you model (give high level ideas) to consider for the long term effect
 and immediate effect while making the decision?"""


"""For this problem we can use DECISION TREE as the model.The system is to make decision whether to
choose change_of_job or not.Some of the conditions I"ve taken into consideration is:
 ('Salary_hike','Easy_Commute','work_life_balance','project_type') where "new people, 
 new tools, new place" always creates lower satisfaction level so not taking into consideration """

#categoriesed the various columns as per some basic criteria:
# Salary_hike=['<30%','30-50%','>50%']
# Easy_Commute=['YES','NO']
# work_life_balance=['YES','NO']
# project_type=['easy','hard','average']

import pandas as pd
import numpy as np
#predifined data from various users/survey
# load the data
df = pd.DataFrame({"Salary_hike":["<30%","<30%","30-50%","30-50%","30-50%","30-50%","<30%","<30%",">50%",">50%"],
                     "Easy_Commute":["YES","YES","NO","YES","YES","YES","NO","NO","YES","NO"],
                     "work_life_balance":["YES","YES","YES","YES","YES","YES","NO","YES","YES","YES"],
                     "project_type":["easy","average","hard","average","average","easy","hard","hard","easy","easy"],
                     "Job_Change": ["YES", "NO", "NO", "YES", "NO", "YES", "YES", "NO", "YES", "YES"]
                   },
                    columns=['Salary_hike','Easy_Commute','work_life_balance','project_type','Job_Change'])

#we can take take dataframe manually also:
#df = pd.read_csv('/home/Job_change_Decision_tree.csv')

# split the data into x and y
x = df.iloc[:, 0:4].values #features:('Salary_hike','Easy_Commute','work_life_balance','project_type')
y = df.iloc[:, 4].values#target:Column in dataframe with Job_change=0 for "NO" and Job_change=0 for "YES"

# replace the Categorial values of columns with numerical values
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x[:, 0] = encoder.fit_transform(x[:, 0])
print(x[:, 0])#[1 1 0 0 0 0 1 1 2 2]
x[:, 1] = encoder.fit_transform(x[:, 1])
print(x[:, 1])#[1 1 0 1 1 1 0 0 1 0]
x[:, 2] = encoder.fit_transform(x[:, 2])
print(x[:, 2])#[1 1 1 1 1 1 0 1 1 1]
x[:, 3] = encoder.fit_transform(x[:, 3])
print(x[:, 3])#[1 0 2 0 0 1 2 2 1 1]
y = encoder.fit_transform(y)
print(y)#[1 0 0 1 0 1 1 0 1 1]


# train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=12345)

# get the model built
from sklearn.tree import DecisionTreeClassifier
#the Gini_index decides
classifier = DecisionTreeClassifier(max_depth=5,min_samples_split=2,criterion="gini")#can be criterion="entropy"
classifier = classifier.fit(x_train, y_train)


#getting input from user
Salary_hike=int(input("Enter salary hike range i.e for ['<30%'=1,'30-50%'=0,'>50%'=2]"))
Easy_Commute=int(input("Enter if you wish Commute Easy or it is not necessary :['Yes'=1,'No'=0]"))
work_life_balance=int(input("Enter if you wish work_life_balance or it is not necessary by ['Yes'=1,'No'=0]"))
project_type=int(input("Enter your wish of your project_type to be: ['easy'=1,'hard'=0,'average'=2]"))

x_test=[Salary_hike,Easy_Commute,work_life_balance,project_type]
# x_test.reshape(0, 1)
predictions = classifier.predict([x_test])
print(predictions[0])
print(y_test)
#To get the accuracy of the system we can use the below code by uncommenting it:
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, predictions)
# print(cm)
# accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
# per_accuracy=accuracy*100
# print(f"accuracy = {accuracy * 100} %")

#getting the predicted value by DECISION TREE CLASSIFIER and the accuracy of our system
if predictions[0]==1: #and per_accuracy>75:
    print("Yes it is definitive you should change your job")
else:
    print("No you should not change your job")















