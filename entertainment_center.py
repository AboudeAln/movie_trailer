import media
import fresh_tomatoes

""" The entertainment_center file will create instances of the Movie class with certain attributes:
    1. Movie Title
    2. Movie Storyline
    3. Movie Box Art
    4. Movie Trailer Youtube URL
"""


# Create Toy Story instance of class Movie:
toy_story = media.Movie("Toy Story", "a story of a boy and his toys that come to life,",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Create Avatar instance of class Movie:
avatar = media.Movie("Avatar", "Alien,",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Create School of Rock instance of class Movie:
school_of_rock = media.Movie("School of Rock", "Rock and Roll,",
                              "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                              "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Create The Hunger Games instance of class Movie:
hunger_games = media.Movie("Hunger Games", "Only one survives!,",
                            "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")

# Create The Departed instance of class Movie:
the_departed = media.Movie("The Departed", "Only one survives!,",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                            "https://youtu.be/SGWvwjZ0eDc")

# Create The Godfather instance of class Movie:
the_godfather = media.Movie("The Godfather", "Only one survives!,",
                             "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                             "https://youtu.be/sY1S34973zA")


# Store the Movie objects in a list through and Array:
movie_list = [toy_story, avatar, school_of_rock, hunger_games, the_departed, the_godfather]


# Display the list of movies in web browser using the open_movies_page from the fresh tomatoes file:
fresh_tomatoes.open_movies_page(movie_list)
