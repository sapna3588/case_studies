# from ques1 import Recommend
import pandas as pd

class Collaborative_Reco:
    def __init__(self,df):
        column_names = ["upload_pic", "upload_vid", "comment_photo", "vote_video", "update_profile"]
        # df = pd.read_csv('xyz', sep=',', names=column_names)
        # "finding similarity between various actions using "cosine_similarity"
        # self.socialMatrix =self.df.pivot_table(index='user_id', columns=column_names, values='votes')
        self.socialMatrix =df
        # self.dict=Recommend.dict

        # from sklearn.metrics.pairwise import cosine_similarity
        # action_simmilarity = cosine_similarity(socialMatrix.T)

    # the first thing we will recommend is "Update_profile" if "newUser"
    def recommend_ACTION(self,param,dict,list):
        # print(dict.keys())
        self.dict=dict
        self.list_username=list
        print(f"\n We suggest you to :{param}")
        char = input("Enter your choice : Y/N ")
        if char == 'Y' or char == 'y':
            for ke, val in self.dict.items():
                flag = True
                if ke == param == 'update_profile':
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.dict.update()
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)

                    # finding corelation between various actions as ITEM/ACTION_BASED_COLLABORATIVE_FILTERING
                    update_profile_user_vote = self.socialMatrix['update_profile']
                    similar_to_update_profile = self.socialMatrix.corrwith(update_profile_user_vote)
                    update_profile_table = pd.DataFrame(similar_to_update_profile, columns=['Correlation'])
                    recomm = update_profile_table.sort_values('Correlation', ascending=False).head(1)

                    self.recommend_ACTION(recomm,self.dict,self.list_username)  # calling recommend() again based on recommended_action value "recomm"

                elif ke == param== 'upload_pic':
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)

                    upload_pic_user_vote = self.socialMatrix['upload_pic']
                    similar_to_upload_pic = self.socialMatrix.corrwith(upload_pic_user_vote)
                    upload_pic_table = pd.DataFrame(similar_to_upload_pic, columns=['Correlation'])
                    recomm = upload_pic_table.sort_values('Correlation', ascending=False).head(1)
                    print(recomm)
                    self.recommend_ACTION(recomm,self.dict,self.list_username)  # calling recommend() again based on recommended_action value "recomm"

                elif ke == 'upload_vid':
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)

                    upload_vid_user_vote = self.socialMatrix['upload_vid']
                    similar_to_upload_vid = self.socialMatrix.corrwith(upload_vid_user_vote)
                    upload_vid_table = pd.DataFrame(similar_to_upload_vid, columns=['Correlation'])
                    recomm = upload_vid_table.sort_values('Correlation', ascending=False).head(1)

                    self.recommend_ACTION(recomm,self.dict,self.list_username)  # calling recommend() again based on recommended_action value "recomm"

                elif ke == param== 'comment_photo':
                    # we can do content based "Sentiment Analysis" for the entered text and if it is a positive comment
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)

                    comment_photo_user_vote = self.socialMatrix['comment_photo']
                    similar_to_comment_photo = self.socialMatrix.corrwith(comment_photo_user_vote)
                    comment_photo_table = pd.DataFrame(similar_to_comment_photo, columns=['Correlation'])
                    recomm = comment_photo_table.sort_values('Correlation', ascending=False).head(1)

                    self.recommend_ACTION(recomm,self.dict,self.list_username)  # calling recommend() again based on recommended_action value "recomm"

                elif ke == param== 'vote_video':
                    value = self.dict.get(ke)
                    self.dict[ke] = value + 1
                    self.df = pd.DataFrame(self.dict, index=self.list_username)
                    print(self.df)
                    vote_video_user_vote = self.socialMatrix['vote_video']
                    similar_to_vote_video = self.socialMatrix.corrwith(vote_video_user_vote)
                    vote_video_table = pd.DataFrame(similar_to_vote_video, columns=['Correlation'])
                    recomm = vote_video_table.sort_values('Correlation', ascending=False).head(1)

                    self.recommend_ACTION(recomm,self.dict,self.list_username)  # calling recommend() again based on recommended_action value "recomm"

                else:
                    print("Too Busy...as You have not done any activities today")
                    self.recommend_Similar_User_based()

    def recommend_Similar_User_based(self):
        pass
        """
        we can do the same above by "User_based_Collaborative_Filtering" i.e. finding the "User_Simmilarity"
        between various users(by cosine_similarity matrix) present and suggest based on the action of the 
        Simmilar user having highest correlated activity. """
