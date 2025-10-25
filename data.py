import pandas as pd
 

class Data:
    def __init__(self,name,rating=None,year=None,genre=None,time=None,actors=[]):
        import pandas as pd
        self.name=name
        self.rate=rating
        self.year=year
        self.genre=genre
        self.time=time
        self.actors=actors
        self.df = pd.DataFrame([{
            "title":name,
            "rating": rating,
            "year": year,
            "genres":genre,           # list allowed; cell will contain the list
            "length_minutes":time,
            "actors": actors            # list allowed
        }])

    def excel(self):
        import pandas as pd
        self.df.to_excel("movie.xlsx")
    def update(self):
        import pandas as pd
        data=pd.read_excel("movie.xlsx",index_col=False)
        new_data=pd.concat([data,self.df],ignore_index=True)
        new_data.to_excel("movie.xlsx",index=False) 
