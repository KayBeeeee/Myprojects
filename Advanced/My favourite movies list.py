# This App  allow us to create a beautiful website that lists our top 10 films of all time. As we watch more movies, 
# we can always update our list and keep track of which movies to recommend people.


import requests
from tmdbv3api import TMDb, Movie
import json

# Initialize TMDb
tmdb = TMDb()
tmdb.api_key = 'your_tmdb_api_key'  # Replace with your actual TMDb API key

# File to store the movie list
MOVIE_LIST_FILE = 'movie_list.json'


# Load movies from the file
def load_movies():
    try:
        with open(MOVIE_LIST_FILE, 'r') as file:
            movies = json.load(file)
            return movies
    except FileNotFoundError:
        return []


# Save the current movie list to the file
def save_movies(movies):
    with open(MOVIE_LIST_FILE, 'w') as file:
        json.dump(movies, file, indent=4)


# Add a new movie to the list
def add_movie(title, director, rating):
    movies = load_movies()
    movie = {
        'title': title,
        'director': director,
        'rating': rating
    }
    movies.append(movie)
    # Ensure that we only have the top 10 movies
    if len(movies) > 10:
        movies = movies[:10]
    save_movies(movies)


# Search for a movie on TMDb
def search_movie(title):
    movie_api = Movie()
    results = movie_api.search(title)
    return results


# Display the top 10 movies
def display_movies():
    movies = load_movies()
    if not movies:
        print("No movies added yet.")
    else:
        print("Top 10 Movies:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie['title']} - Rating: {movie['rating']} - Director: {movie['director']}")


# Main menu to interact with the user
def main():
    while True:
        print("\nMovie Tracker")
        print("1. View Top 10 Movies")
        print("2. Add a Movie")
        print("3. Search for a Movie on TMDb")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_movies()
        elif choice == '2':
            title = input("Enter the movie title: ")
            director = input("Enter the director's name: ")
            rating = input("Enter the movie rating (out of 10): ")
            add_movie(title, director, rating)
            print("Movie added successfully!")
        elif choice == '3':
            search_term = input("Enter movie title to search: ")
            results = search_movie(search_term)
            if results:
                print(f"Search Results for '{search_term}':")
                for idx, result in enumerate(results, start=1):
                    print(f"{idx}. {result.title} ({result.release_date})")
            else:
                print("No results found.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()











