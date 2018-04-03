import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toy that comw to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School_Of_Rock",
                             "Using Rock Music to Learn",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

iron_man = media.Movie("Iron Man",
                       "Suit of iron",
                       "https://en.wikipedia.org/wiki/Iron_Man_(2008_film)#/media/File:Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

gone_girl = media.Movie("Gone Girl",
                        "Gharelu Hinsa",
                        "https://en.wikipedia.org/wiki/Gone_Girl_(film)#/media/File:Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=QZsF7IRTgMQ")

harry_potter = media.Movie("Harry Potter",
                           "Story Of Wizards",
                           "https://en.wikipedia.org/wiki/Harry_Potter_(film_series)#/media/File:Harry-film-logo.png",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")

movies = [toy_story, avatar, school_of_rock, iron_man, gone_girl, harry_potter]
fresh_tomatoes.open_movies_page(movies)
