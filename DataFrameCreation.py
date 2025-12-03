import pandas as pd
import numpy as np

class DataFrame():
    def __init__(self):
        self.data = pd.read_csv('imdb_top_movies.csv')
    
    def get_movies_by_genre(self, genre):
        try:
            genre = str(genre)
        except ValueError:
            print("Invalid genre value. Please enter a valid genre.")
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Genres'].str.contains(genre, case=False, na=False)]
    def get_movies_by_rating(self, min_rating):
        try:
            min_rating = float(min_rating)
        except ValueError:
            print ("Invalid rating value. Please enter a number.")  
            return pd.DataFrame(columns=self.data.columns)
        if min_rating < 0 or min_rating > 10:
            print("Rating must be between 0 and 10.")
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Rating'] >= min_rating]
    def get_movies_by_certificate(self, certificate):
        if certificate not in self.data['Certificate'].values:
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Certificate'].str.contains(certificate, case=False, na=False)]
    def get_movies_by_year(self, year):
        try:
            year = int(year)
        except ValueError:
            print ("Invalid year value. Please enter a valid year.")
            return pd.DataFrame(columns=self.data.columns)
        if year not in self.data['Year'].values:
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Year'] == int(year)]
        
    def get_movies_by_title(self, title):
        if title not in self.data['Title'].values:
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Title'].str.contains(title, case=False, na=False)]
    def get_movies_by_rank(self, rank):
        try:
            rank = int(rank)
        except ValueError:
            print ("Invalid rank value. Please enter a valid rank.")
            return pd.DataFrame(columns=self.data.columns)
        if rank not in self.data['Rank'].values:
            return pd.DataFrame(columns=self.data.columns)
        return self.data[self.data['Rank'] == int(rank)]
    def get_dataframe(self):
        return self.data 
    def display_formatted(self, df=None, columns=None): 
        if columns:
            df = df[columns]
        
        if df.empty:
            print("No movies found matching the criteria.")
            return
        print(df.to_string(index=False)) 

    