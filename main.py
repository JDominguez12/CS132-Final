import pandas as pd
from IPython.display import display
from DataFrameCreation import DataFrame
def query():
    
    while True:
        print("============================")
        print("IMDb Movie Query System")
        print("1. See all Movies (Top 250)")
        print("2. Search Movie by Genre")
        print("3. Search Movie by rating")
        print("4. Search Movie by Movie certification")
        print("5. Search Movie by Year")
        print("6. Search Movie by title")
        print("7. Search Movie by rank")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            print("Displaying all movies...")
            db = DataFrame()
            all_movies = db.get_dataframe()
            db.display_formatted(all_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '2':
            genre = input("Enter genre to search: ")
            print(f"Searching movies in genre: {genre}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_genre(genre)
            db.display_formatted(filtered_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '3':
            rating = input("Enter minimum rating to search: ")
            print(f"Searching movies with rating >= {rating}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_rating((rating))
            db.display_formatted(filtered_movies, columns = ['Rank', 'Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '4':
            certification = input("Enter movie certification to search: ")
            print(f"Searching movies with certification: {certification}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_certificate(certification)
            db.display_formatted(filtered_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '5':
            year = input("Enter release year to search: ")
            print(f"Searching movies released in year: {year}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_year((year))
            db.display_formatted(filtered_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '6':
            title = input("Enter movie title to search: ")
            print(f"Searching movies with title containing: {title}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_title(title)
            db.display_formatted(filtered_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])
        elif choice == '7':
            rank = input("Enter movie rank from 1 to 250 to search: ")
            print(f"Searching movies with rank: {rank}")
            db = DataFrame()
            filtered_movies = db.get_movies_by_rank(rank)
            db.display_formatted(filtered_movies, columns = ['Rank','Title', 'Year', 'Rating', 'Duration', 'Genres', 'Certificate'])

        if choice == '8':
            print("Exiting... Goodbye!")
            break
        print("============================")
def main():
    query()


if __name__ == "__main__":
    main()

