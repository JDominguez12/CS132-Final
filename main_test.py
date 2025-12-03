import main

def test_main1():
    db = main.DataFrame()
    df = db.get_dataframe()
    expected_columns = ['Rank', 'Title', 'Year', 'Rating', 'Duration', 'Certificate', 'Genres', 'Description', 'Image URL', 'Movie URL']
    for col in expected_columns:
        assert col in df.columns, f"Expected column '{col}' not found in DataFrame"
def test_main2():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_genre("Action")
    assert not filtered_movies.empty, "Expected non-empty DataFrame for genre 'Action'"
def test_main3():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_rating(8.5)
    assert not filtered_movies.empty, "Expected non-empty DataFrame for rating >= 8.5"
def test_main4():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_certificate("PG-13")
    assert not filtered_movies.empty, "Expected non-empty DataFrame for certificate 'PG-13'"
def test_main5():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_year(1994)
    assert not filtered_movies.empty, "Expected non-empty DataFrame for year 1994"
def test_main6():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_title("The Shawshank Redemption")
    assert not filtered_movies.empty, "Expected non-empty DataFrame for title 'The Shawshank Redemption'"
def test_main7():
    db = main.DataFrame()
    filtered_movies = db.get_movies_by_rank(1)
    assert not filtered_movies.empty, "Expected non-empty DataFrame for rank 1"
def test_main8():
    db = main.DataFrame()
    all_movies = db.get_dataframe()
    assert len(all_movies) == 250, "Expected 250 movies in the DataFrame"