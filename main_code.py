#!/usr/bin/env python

# import module movie to use the object Movie
import movie

# import fresh_tomatoes to display the python code as a web page
import fresh_tomatoes

# A new object is created of Movie from the imported movie module
Dark_knight = movie.Movie("Dark Knight 1",
                          "How Batman turn out to save Gotham",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",   # noqa
                          "https://youtu.be/EXeTwQWrcwY")

avatar = movie.Movie("Avatar",
                     "About a paralyzed soilder on planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-",  # noqa
                     "https://youtu.be/5PSNL1qE6VY")

perks_of_being_a_wallflower = movie.Movie("Perks of Being a Wallflower",
                                          " About a boy who is socially different",  # noqa
                                          "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg/215px-The_Perks_of_Being_a_Wallflower_Poster.jpg",   # noqa
                                          "https://youtu.be/n5rh7O4IDc0")

three_idiots = movie.Movie("3 Idiots",
                           "About life of three friends in a esteemed engineering college",   # noqa
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",   # noqa
                           "https://youtu.be/K0eDlFX9GMc")

# Names of the movies are stored in a list
movies = [Dark_knight, avatar, perks_of_being_a_wallflower, three_idiots]

# List is passed on to the function in frest_tomatoes so that they can be displayed as a web page  # noqa
fresh_tomatoes.open_movies_page(movies)
