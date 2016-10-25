import movie
import fresh_tomatoes

Dark_knight = movie.Movie("Dark Knight 1", "How Batman turn out to save Gotham",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                            "https://youtu.be/EXeTwQWrcwY")

avatar = movie.Movie("Avatar",
                     "About a paralyzed soilder on planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-",
                     "https://youtu.be/5PSNL1qE6VY")

perks_of_being_a_wallflower = movie.Movie("Perks of Being a Wallflower",
                                          " About a boy who is socially different",
                                          "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg/215px-The_Perks_of_Being_a_Wallflower_Poster.jpg",
                                          "https://youtu.be/n5rh7O4IDc0")

three_idiots = movie.Movie("3 Idiots",
                        "About life of three friends in a esteemed engineering college",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",
                        "https://youtu.be/K0eDlFX9GMc")
movies = [Dark_knight, avatar, perks_of_being_a_wallflower, three_idiots]
fresh_tomatoes.open_movies_page(movies)