#!/usr/bin/env python
import webbrowser


class Movie():
    """
    Class Movie defines the movie block shown on the website.
    It defines the information that the website holds for the particular movie
    like Name of the movie, stroyline in brief ,corresponding image followed by the trailer url. # noqa
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # noqa
        """
        The constructor __init__ takes the parameters like Name of the movie,
        Brief storyline, the image url and later the trailer url .
        The values passed are used to initialize the variables inside the class
         """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This particular funtion is used to call the open function from the
        webbrowser module. This helps us to stream the trailer for the movie.
        """
        webbrowser.open(self.trailer_youtube_url)
