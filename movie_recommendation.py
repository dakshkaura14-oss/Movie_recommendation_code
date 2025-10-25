import pandas as pd 
import ast

movies_data=pd.read_excel("movie.xlsx")
print(movies_data)

class Movie_recommend():
    def __init__(self,movie_watched):
        self.watched=movie_watched

    def data_movies(self):
        self.movies_data_watched=pd.DataFrame([])
        for names in self.watched:
            if self.movies_data_watched.empty==True:
                self.movies_data_watched=movies_data[movies_data["title"]==names]
            else:
                self.movies_data_watched=pd.concat([self.movies_data_watched,movies_data[movies_data["title"]==names]],ignore_index=True)
    
    def prefered_genre(self):
        self.pref_genre=self.movies_data_watched["genres"].values
        self.genre_list=[]
        for i in self.pref_genre:
            lst = ast.literal_eval(i)
            for x in lst:
                self.genre_list.append(x)
        # print(self.genre_list)
        from collections import Counter
        counts=Counter(self.genre_list)
        duplicates = {item:cnt for item, cnt in counts.items() if cnt > 1}
        duplicates_list=[]
        for key in duplicates.keys(): # This is now a list of (genre, count) tuples
            duplicates_list.append(key)
        if duplicates_list==[]:
            duplicates_list=self.genre_list
        # print(duplicates_list)
        self.data_frame=pd.DataFrame([])
        for categories in duplicates_list:
            if self.data_frame.empty==True:
                genre_data=[]
                j=0
                for i in movies_data["genres"]:
                    if ((categories in i)==True ):
                        genre_data.append(j)
                        j=j+1
                    else:
                        j=j+1
                        continue
                self.data_frame=movies_data.take(genre_data)
            else:
                genre_data=[]
                j=0
                for i in movies_data["genres"]:
                    if ((categories in i)==True ):
                        genre_data.append(j)
                        j=j+1
                    else:
                        j=j+1
                        continue
                data_frame_copy=movies_data.take(genre_data)
                self.data_frame=pd.concat([self.data_frame,data_frame_copy],ignore_index=True)
        print(self.data_frame)
        for i in self.watched:
            self.data_frame=self.data_frame[self.data_frame["title"] != i]
        self.data_frame.drop_duplicates(inplace=True)
        return self.data_frame
    
    def prefered_actor(self):
        self.pref_actor=self.movies_data_watched["actors"].values
        self.actors_list=[]
        for i in self.pref_actor:
            lst = ast.literal_eval(i)
            for x in lst:
                self.actors_list.append(x)
        print(self.actors_list)
        from collections import Counter
        count=Counter(self.actors_list)
        duplicate={item:cnt for item,cnt in count.items() if cnt>1}
        duplicate_list=[]
        for key in duplicate.keys():
            duplicate_list.append(key)
        if duplicate_list==[]:
            return None
        print(duplicate_list)
        self.actors_dataframe=pd.DataFrame([])
        for categories in duplicate_list:
            if self.actors_dataframe.empty==True:
                actors_data=[]
                j=0
                for i in movies_data["actors"]:
                    if ((categories in i)==True ):
                        actors_data.append(j)
                        j=j+1
                    else:
                        j=j+1
                        continue
                self.actors_dataframe=movies_data.take(actors_data)
            else:
                actor_data=[]
                j=0
                for i in movies_data["actors"]:
                    if ((categories in i)==True ):
                        actor_data.append(j)
                        j=j+1
                    else:
                        j=j+1
                        continue
                actors_dataframe_copy=movies_data.take(actor_data)
                self.actors_dataframe=pd.concat([self.actors_dataframe,actors_dataframe_copy],ignore_index=True)
        print(self.actors_dataframe)
        for i in self.watched:
            self.actors_dataframe=self.actors_dataframe[self.actors_dataframe["actors"] != i]
        self.actors_dataframe.drop_duplicates(inplace=True)
        return self.actors_dataframe
    
    def movie_recommended(self):
        genre_pref=self.prefered_genre()
        actor_pref=self.prefered_actor()
        pref_dataframe=pd.concat([genre_pref,actor_pref])
        pref_dataframe.sort_values(by="rating",ascending=False,inplace=True)
        print(pref_dataframe.head(10))



movie_watch=list(input("Enter the movies you watched recently :").split(","))
movie=Movie_recommend(movie_watch)
movie.data_movies()
movie.movie_recommended()


