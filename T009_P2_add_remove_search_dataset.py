# ECOR 1042 Project Milestone 1 lab 2 (Task 3)

# Muhammed Nabeel Azard 101152007 
# K.C. Barnard 101223587 
# Spencer-Nieman McKeown 101155117 
# Chrismon Charli 101239397 

# 17/06/2022: Version 1.0


#from T009_P1_load_data import movie_category_dictionary_list
from T009_P5_load_data import movie_category_dictionary_list

# Function 1 by Chrismon Charli
def add_movie(movies: dict, new_movie: tuple) -> dict:
    """ Returns the updated dictionary and prints the message stating that "The 
    movie has been added correctly or "There was an error adding the movie".
    >>> The movie has been added correctly
        {'Adventure': [{'title': 'Birth of the Dragon', 'director': 'George Nolfi', 'cast': 'Billy Magnussen, Ron Yuan, Qu Jingjing,
         Terry Chen, Vanness Wu, Jin Xing, Philip Ng, Xia Yu, Yu Xia', 'country': 'China, Canada, United States', 'date_added': '16-Sep-21', 'release_year': '2017', 'rating': 'PG-13', 'duration': '96 min..... and so on.
    """    
    category=new_movie[8]
    new_movie_dict = dict(
        title=new_movie[0],
        director=new_movie[1],
        cast=new_movie[2],
        country=new_movie[3],
        date_added=new_movie[4],
        release_year=new_movie[5],
        rating=new_movie[6],
        duration=new_movie[7]
    )

    # check for a movie of the same title in the same category
    found_same_title = False
    for movie in movies[category]:
        if movie['title'] == new_movie_dict['title']:
            found_same_title = True
    
    # don't let the title be the same
    if found_same_title:
        print("There was an error adding the movie.")
    else:
        movies[category].append(new_movie_dict)
        print("The movie has been added correctly.") 
    
    return movies

# Function 2 by Chrismon Charli
def remove_movie(movies: dict, title: str, category: str):
    """ Returns the the updated dictionary and will remove a movie. It will print out a message stating, 
    "The movie has been removed correctly" or "There was an error removing the movie. Book not found". 
    
    >>>remove_movie( "Total Controllll","Crime", dictionary)
    There is an error removing the movie. movie is not found.
       {'Adventure': [{'title': 'Birth of the Dragon', 'director': 'George Nolfi', 'cast': 'Billy Magnussen, Ron Yuan, Qu Jingjing,
         Terry Chen, Vanness Wu, Jin Xing, Philip Ng, Xia Yu, Yu Xia', 'country': 'China, Canada, United States', 'date_added': '16-Sep-21', 'release_year': '2017', 'rating': 'PG-13', 'duration': '96 min..... and so on.
    
    >>>remove_movie( "Total Control","Crime", dictionary)
    The movie has been removed correctly
    
    """    
    if category not in movies:
        print("There was an error removing the movie. Movie not found.")
        return movies
    else:
        # find the index of the movie to remove (-1 if not)
        found_ind = -1
        for i, movie in enumerate(movies[category]):
            if movie['title'] == title:
                found_ind = i
                break
        
        if found_ind == -1:
            print("There was an error removing the movie. Movie not found.")
        else:
            print("The movie had been removed correctly.")
            movies[category].pop(found_ind)

        return movies
    
# Function 3 by Spencer-Nieman McKeown
def get_movies_by_category(movies: dict, category:str) -> int:
    """
    This function takes two inout parameters, the dictionary from which data is pulled and the category of a movie and returns the number of movies in said ategory

    >>>get_movies_by_category(adventure)
    The category adventure has 100000 movies. This is the list of movies:
    Movie 1: "Title" by "Director"
    Movie 2: "Title" by "Director"
    etc
    
    >>>get_movies_by_category(dramas)
    The category dramas has 0 movies. This is the list of movies:
    
    >>>get_movies_by_category(action)
    The category action has 2 movies. This is the list of movies:
    Movie 1: "Braven" by "Lin Oeding"
    Movie 2: "Birth of the dragon" by "George Nolfi"
    """
    
    num_movies = len(movies[category])
    print('The category', category, 'has', str(num_movies) + '. This is the list of movies:')
    i = 1
    for movie in movies[category]:
        print('Movie', str(i) + ': "' + movie['title'] + '" by "' + movie['director'] + '"')
        i += 1
    return num_movies

# Function 4 by Spencer-Nieman McKeown
def get_movie_by_rate(movies: dict, rate: str) -> int:
    """
    This function takes the dictionary from which data is being read and the rate of the desired movies and returns all movies having suhc a rating and the director associated
    
    >>>get_movie_by_rate(PG-13)
    There are999 movies whose rate is PG-13. This is the list of movies:
    Movie 1: "Birth of the dragon" by "George Nolfi"

    
    >>>get_movie_by_rate(TV-Y)
    There are 100 movies whose rate is TV-Y. This is the list of movies:
    Movie 1: "The Magic School Bus Rides Again In the Zone" by "Richard Weston"

    
    >>>get_movie_by_rate(R)
    There are 55 movies whose rate is R. This is the list of movies:
    Movie 1: "case 39" by "Christian Alvart"
    """
    
    movies_with_rate = set()

    for movie_list in movies.values():
        for movie in movie_list:
            if movie['rating'] == rate:
                movie_tuple = (movie['title'], movie['director'])
                movies_with_rate.add(movie_tuple)

    rating_length = len(movies_with_rate)
    print('There are', rating_length, 'movies whose rate is', rate + '. This is the list of movies:')

    i = 1
    for movie in movies_with_rate:
        print('Movie', str(i) + ': "' + movie[0] + '" by "' + movie[1] + '"')
        i += 1

    return rating_length



# Function 5 by Muhammed Nabeel Azard

def get_movies_by_title(dictionary: dict, movie_title: str) -> bool:
    '''
    Returns True or False after checking whether the input movie title is in the dictionary, where all the movies are stored.
    
    >>> get_movies_by_title(movie_dictionary, "Extraction")
    True
    >>> get_movies_by_title(movie_dictionary, "Iron Man")
    False
    >>> get_movies_by_title(movie_dictionary, "#Roxy")
    True
    '''
    
    for category in dictionary:
        movie_list = dictionary.get(category)
        for movie in movie_list:
            if movie['title'] == movie_title:
                print("The movie has been found")
                return(True)
    print("The movie has NOT been found")
    return (False)
    
# Function 6 by Muhammed Nabeel Azard 

def get_movies_by_director(dictionary: dict, director: str) -> int:
    '''
    Returns the number of movies directed by a given director after checking all the movies in the given dictionary. Precondition: The director's full name must be given.
    
    >>> get_movies_by_director(movie_dictionary, 'Sarik Andreasyan')
    1
    >>> get_movies_by_director(movie_dictionary, 'Barry Avrich')
    1
    >>> get_movies_by_director(movie_dictionary, 'Atom Egoyan')
    2
    >>> get_movies_by_director(movie_dictionary, 'George Clooney')
    0
    '''
    movies_by_director = []
    title = []
    rate = []
    for category in dictionary:
        movies_list = dictionary.get(category)
        for movie in movies_list:
            if not (movie in movies_by_director):
                if movie['director'] == director:
                    movies_by_director.append(movie)
                    title.append(movie["title"])
                    rate.append(movie["rating"])
    print("The director",director,"has published the following movies:")
    for i in range(len(title)):
        print("Movie",i+1,":",title[i],",","rate:", rate[i])
    return(len(movies_by_director))
    
# Function 7 by K.C. Barnard
def get_movies_by_cast (movie_dictionary: dict, actor: str) -> int:
    """
    >>> get_movies_by_cast (netflix_movies, Sarah Troyer)
    The actor Sarah Troyer has acted in the following movies:
    Movie 1: "Hometown Holiday" by "Justin G. Dyck"
    >>> get_movies_by_cast (netflix_movies, Morgan Neundorf)
    The actor Morgan Neundorf has acted in the following movies:
    Movie 1: "A Witches' Ball" by "Justin G. Dyck"
    >>> get_movies_by_cast
    The actor Laurence Fishburne has acted in the following movies:
    Movie 1: "The Ice Road" by "Jonathan Hensleigh"
    Movie 2: "Standoff" by "Adam Alleca"
    """
    count = 0
    movie_titles = []
    print ("The actor", actor, "has acted in the following movies:")
    for movie_list in movie_dictionary.values():
        for movie in movie_list:
            if actor in movie["cast"]:
                if movie['title'] not in movie_titles:
                    count += 1
                    print ("Movie", str(count)+":", '"'+ movie["title"]+ '"', "by", '"' + movie["director"]+'"')
                    movie_titles.append(movie['title'])
                
    return count            
    
# Funtion 8 K.C. Barnard
def get_all_categories_for_movie_title (movie_dictionary: dict, movie_title: str) -> int:
    """
    >>> get_all_categories_for_movie_title (netflix_movies, Birth of the Dragon)
    The movie title Birth of the Dragon belongs to the following categories:
    Category 1: "Adventure"
    Category 2: "Action"
    Category 3: "Dramas"
    >>> get_all_categories_for_movie_title (netflix_movies, Case 39)
    The movie title Case 39 belongs to the following categories:
    Category 1: "Thrillers"
    Category 2: "Horror Movies"
    >>> get_all_categories_for_movie_title (netflix_movies, Prom Night)
    The movie title Prom Night belongs to the following categories:
    Category 1: "Horror Movies"
    
    """
    count = 0
    print ("The movie title", movie_title , "belongs to the following categories:")
    for category in movie_dictionary:
        for movie in movie_dictionary[category]:
            if movie_title == movie["title"]:
                count += 1
                print ("Category", str(count)+":", '"'+ category +'"')
    return count        

# ----------------------------------------------------- UNIT TESTING -------------------------------------------------------------------

def check_equal(description: str, outcome, expected) -> bool:
    """
    Unit testing function provided by professor.
    Returns a boolean of whether the test passed or not.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
      #They are not required to use this formating
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
             "but outcome ({3}) has type {4}".
                format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        test_pass = False
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
            format(description, expected, outcome))
        test_pass = False
    else:
        print("{0} PASSED".format(description))
        test_pass = True
    print("------")
    return test_pass

# Unit testing for function 1 by K.C. Barnard
def test_add_movie():
    """
    Adds a movie to the dictionary, verifies that the movie has been added and returns the updated dictionary.
    """

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    # add a new movie that is not within the category adventure
    movie_to_add = ("KC: A biography", "KC", "KC Herself", "Canada", "16-Sept-21", "2001", "PG-13", "1hr", "Adventure")
    length_before = len(movie_dictionary["Adventure"])
    updated_movie_dictionary = add_movie(movie_dictionary, movie_to_add)
    length_after = len(updated_movie_dictionary["Adventure"])

    test_1 = check_equal("Testing adding new movie", length_after, length_before+1)

    # try to add the same movie again to the category adventure
    length_before = len(movie_dictionary["Adventure"])
    updated_movie_dictionary = add_movie(movie_dictionary, movie_to_add)
    length_after = len(updated_movie_dictionary["Adventure"])

    test_2 = check_equal("Testing adding new movie", length_after, length_before)

    if test_1 and test_2:
        return True
    else:
        return False

# Unit testing for function 2 by K.C. Barnard
def test_remove_movie():
    """
    Removes movies from the dictionary and returns the updated version of the dictionary.
    """
    
    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    # add a new movie that is not within the category adventure
    length_before = len(movie_dictionary["Adventure"])
    updated_movie_dictionary = remove_movie(movie_dictionary, "Birth of the Dragon", "Adventure")
    length_after = len(updated_movie_dictionary["Adventure"])

    test1 = check_equal("Testing removing movie", length_after, length_before-1)

    # try to add the same movie again to the category adventure
    length_before = len(movie_dictionary["Adventure"])
    updated_movie_dictionary = remove_movie(movie_dictionary, "Birth of the Dragon", "Adventure")
    length_after = len(updated_movie_dictionary["Adventure"])

    test2 = check_equal("Testing removing movie", length_after, length_before)

    if test1 and test2:
        return True
    else:
        return False

# Unit testing for function 3 by Muhammed Nabeel Azard

def test_get_movies_by_category():
    '''
    Returns the number of movies there are in the given dictionary in a given category.
    '''

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")
    test_1 = check_equal("get_movies_by_category(movie_dictionary, 'Adventure')", get_movies_by_category(movie_dictionary, "Adventure"), 19)
    test_2 = check_equal("get_movies_by_category(movie_dictionary, 'Romantic Movies')", get_movies_by_category(movie_dictionary, "Romantic Movies"), 8)
    test_3 = check_equal("get_movies_by_category(movie_dictionary, 'Sci-Fi')", get_movies_by_category(movie_dictionary, 'Sci-Fi'), 3)

    if test_1 and test_2 and test_3:
        return True
    else:
        return False

# Unit testing for function 4 by Muhammed Nabeel Azard

def test_get_movie_by_rate():
    '''
    Returns the number of movies there are for a given rate. No duplicates.
    '''

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")
    test1 = check_equal("get_movie_by_rate(movie_dictionary, 'PG-13')", get_movie_by_rate(movie_dictionary, "PG-13"), 15)
    test2 = check_equal("get_movie_by_rate(movie_dictionary, 'TV-MA')", get_movie_by_rate(movie_dictionary, "TV-MA"), 17)
    test3 = check_equal("get_movie_by_rate(movie_dictionary, 'A')", get_movie_by_rate(movie_dictionary, 'A'), 0)

    if test1 and test2 and test3:
        return True
    else:
        return False

# Unit testing for function 5 by Chrismon Charli
def test_get_movies_by_title():
    """
    Returns a boolean. returns true if the title exists in the dictionary, false if it does not.
    """

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    test_1 = check_equal("get_movies_by_title(movie_dictionary, 'Birth of the Dragon')", get_movies_by_title(movie_dictionary, "Birth of the Dragon"), True)
    test_2 = check_equal("get_movies_by_title(movie_dictionary, 'The Ice Road')", get_movies_by_title(movie_dictionary, "The Ice Road"), True)
    test_3 = check_equal("get_movies_by_title(movie_dictionary, 'Jack')", get_movies_by_title(movie_dictionary, "Jack"), False)

    if test_1 and test_2 and test_3:
        return True
    else:
        return False

# Unit testing for function 6 by Chrismon Charli
def test_get_movies_by_director():
    """
    Returns the number of movies produced by the director. no duplicates.
    """
    
    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    test1 = check_equal("get_movies_by_director(movie_dictionary, 'George Nolfi')", get_movies_by_director(movie_dictionary, "George Nolfi"), 1)
    test2 = check_equal("get_movies_by_director(movie_dictionary, 'Steven C. Miller')", get_movies_by_director(movie_dictionary, "Steven C. Miller"), 3)
    test3 = check_equal("get_movies_by_director(movie_dictionary, 'Chris')", get_movies_by_director(movie_dictionary, "Chris"), 0)

    if test1 and test2 and test3:
        return True
    else:
        return False

# Unit testing for function 7 by Spencer-Nieman McKeown
def test_get_movies_by_cast():
    """
    Returns the number of movies for the given actor's. no duplicates.
    """

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    test_1 = check_equal("get_movies_by_cast(movie_dictionary, 'Tom Hanks')", get_movies_by_cast(movie_dictionary, "Tom Hanks"), 1)
    test_2 = check_equal("get_movies_by_cast(movie_dictionary, 'Ron Yuan')", get_movies_by_cast(movie_dictionary, "Ron Yuan"), 1)
    test_3 = check_equal("get_movies_by_cast(movie_dictionary, 'Tom Cruise')", get_movies_by_cast(movie_dictionary, "Tom Cruise"), 0)

    if test_1 and test_2 and test_3:
        return True
    else:
        return False

# Unit testing for function 8 by Spencer-Nieman McKeown
def test_get_all_categories_for_movie_title():
    """
    Returns the number of categories associated with the given movie.
    """

    movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")

    test1 = check_equal("get_all_categories_for_movie_title(movie_dictionary, 'Birth of the Dragon')", get_all_categories_for_movie_title(movie_dictionary, "Birth of the Dragon"), 3)
    test2 = check_equal("get_all_categories_for_movie_title(movie_dictionary, 'The Ice Road')", get_all_categories_for_movie_title(movie_dictionary, "The Ice Road"), 2)
    test3 = check_equal("get_all_categories_for_movie_title(movie_dictionary, 'N/A')", get_all_categories_for_movie_title(movie_dictionary, "N/A"), 0)

    if test1 and test2 and test3:
        return True
    else:
        return False


if __name__ == '__main__':
    results = [
        test_add_movie(),
        test_remove_movie(),
        test_get_movies_by_category(),
        test_get_movie_by_rate(),
        test_get_movies_by_title(),
        test_get_movies_by_director(),
        test_get_movies_by_cast(),
        test_get_all_categories_for_movie_title()]

    passed = 0
    failed = 0
    for result in results:
        if result == True:
            passed += 1
        else:
            failed += 1

    print('The number of tests that passed was:', passed)
    print('The number of tests that failed was:', failed)