"""Assume we have a social network which supports 5 activities
(upload photo, upload video, comment on photo, vote on videos, and update profile page)
 - and we plan to suggest each user one of the activities as daily suggested activity -
 how will you write a system that suggests each user one recommended activity?
 What you suggest the user does not do on a particular day -
 how will you change recommendation for particular user/or your system based on this feedback?"""

"""Summarizing:There are basically two "Recommendation Techniques:-
1.Content Based And 
2.Collaborative"

Content based will be used if we are just starting from scratch i.e. each User is a new user 
and we will recommend acording to his "OWN" activities.
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Collaborative recommend:
Supposing that the data is in dataframe format with 'n' users as row having some 'userid' 
and 5 different columns of(upload_photo, upload_video, comment_on_photo, vote_on_videos, 
and update_profile_page)
"""
"""finding similarity between various actions using "cosine_similarity" an inbuilt library function in python:"
from sklearn.metrics.pairwise import cosine_similarity
action_simmilarity=cosine_similarity(socialMatrix.T)"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#creating file User.py to get the user entry passed
class User:
    def __init__(self,name,newUser):
        self.name = name
        self.isNewUser = newUser

        print(f"heloo User:{name}")

from User import User #importing file "User.py"
import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
class Recommend:
    def  __init__(self):
        self.dict={"upload_pic":1, "upload_vid":1, "comment_photo":1,"vote_video":1, "update_profile":1}
        self.df = pd.DataFrame()
        self.list_username = []

    # the first thing we will recommend is "Update_profile" if "newUser"
    def recommend_main(self,isNewUser,name):
            self.list_username.append(name)
            if isNewUser== True :#the first recommendation will be of Update_Profile
                print("your recommended activity today : ")
                self.recommend("update_profile")
            param = random.choice(list(self.dict.keys()))
            obj = Collaborative_Reco(self.df,self.dict)
            obj.recommend_ACTION(param,self.dict,self.list_username,name)

    def recommend(self,param):
        print(f"\n We suggest you to :{param}")
        char=input("Enter your choice : Y/N ")
        if char== 'Y' or char== 'y':
            for ke,val in self.dict.items():

                if ke==param:
                    value = self.dict.get(ke)
                    self.dict[ke]=value+1
                    self.dict.update()
                    # print(self.dict)
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)

class Collaborative_Reco:
    def __init__(self,df,dict):
        column_names = ["upload_pic", "upload_vid", "comment_photo", "vote_video", "update_profile"]
        self.df =df
        self.dict=dict

    # the first thing we will recommend is "Update_profile" if "newUser"
    def recommend_ACTION(self,param,dict,list,username):
        self.dict=dict
        self.list_user=list
        print(f"\n We suggest you to :{param}")
        char = input("Enter your choice : Y/N ")
        if char == 'Y' or char == 'y':
            print("Using Action_based_Collaborative_Filtering ")
            for ke, val in self.dict.items():

                if ke == param:
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.dict.update()
                    self.df = pd.DataFrame(self.dict, index=self.list_user)
                    print(self.df)

                    # finding corelation between various actions as ITEM/ACTION_BASED_COLLABORATIVE_FILTERING

                    similar_action = self.df.drop(labels=param, axis=1).corrwith(self.df[param])
                    # similar_action = self.df.corrwith(user_vote)
                    update_action_table = pd.DataFrame(similar_action, columns=['Correlation'])
                    recomm = update_action_table.sort_values('Correlation', ascending=False).head(1)

                    self.recommend_ACTION(recomm.index[0],self.dict,self.list_user,username)  # calling recommend() again based on recommended_action value "recomm"

##What you suggest the user does not do on a particular day -
#how will you change recommendation for particular user/or your system based on this feedback?
        elif char == 'N' or char == 'n':
            print("Doing User_based_Collaborative_Filtering using corrwith() function")

            self.df = pd.DataFrame(self.dict, index=self.list_user)
            self.df_trans = self.df.T
            similar_user = self.df_trans.corrwith(self.df_trans[username])
            update_user_table = pd.DataFrame(similar_user, columns=['Correlation'])
            recom_user = update_user_table.sort_values('Correlation', ascending=False).head(1)
            rec_action=self.df_trans[recom_user.index[0]].sort_values(ascending=False).head(1)
            self.recommend_ACTION(rec_action.index[0], self.dict, self.list_user, username)

objU= User("Sapna",True)
objR= Recommend()
objR.recommend_main(objU.isNewUser,objU.name)
