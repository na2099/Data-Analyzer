# ECOR 1042 Project Milestone 2 (Lab 3, Task 2)

# Muhammed Nabeel Azard, 101152007
# K.C. Barnard, 101223587
# Spencer McKeown, 101155117
# Chrismon Charli, 101239397

# 17/06/2022: Version 1.0

# imports

import csv
#from T009_P1_load_data import movie_category_dictionary_list
from T009_P5_load_data import movie_category_dictionary_list

# The four functions from P3 – Task 1 (and extra function that arise from refactoring)

# Function 1 by Muhammed Nabeel Azard

def sort_movies_title(dictionary: dict) -> list:
    '''
    Returns a list, where all the movies are sorted by their title alphabetically, and where each list element is a dictionary where all the movie data
    for each movie is stored.
    
    >>> sort_movies_title(movie_dictionary)
    [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min', 'category': ['Comedies', 'Romantic Movies']}, {'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min', 'category': ['Dramas']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']},...]
    '''
    movies_list = dictionary_to_list(dictionary)
    n = len(movies_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if (movies_list[j]['title']) > (movies_list[j+1]['title']):
                movies_list[j], movies_list[j+1] = movies_list[j+1], movies_list[j]
    return (movies_list)


# Function 2 by Spencer McKeown

def sort_movies_director(dictionary: dict) -> list:
    '''
    Returns a sorted list of all movies from a director in alphabetical order.
    
    >>> {"director": "Georgoe Nolfi ",
    "Title": "Birth of the dragoni",
    " cast": “Billy Magnussen, Ron Yuan, Qu Jingjing, Terry Chen, Vanness Wu, Jin Xing, Philip Ng, Xia Yu, Yu Xia",
    "country": “China, Canada, United States”,
    "date_added": " 9/16/2021",
    "release_year": 2017,
    "rating": “PG-13”,
    "duration": 96,
    "category": [“Adventure”]}
    
    >>>{"Director": " Georgoe Nolfi ",
    "titke ": "zzzzz",
    " cast": “Patrick Wilson, Rose Byrne, Lin Shaye, Ty Simpkins, Barbara Hershey, Leigh Whannell, Angus Sampson, Andrew Astor, Joseph Bishara",
    "country": “United States, Canada”,
    "date_added": " 4/1/2021",
    "release_year": 2010,
    "rating": “PG-13”,
    "duration": 103,
    "category": [“Horror Movies”]}
    
    >>> {"director": " George nolfi ",
    "title": "title zzzzz",
    " cast": “Ben Affleck, Morgan Freeman, Bridget Moynahan, James Cromwell, Liev
    Schreiber, Michael Byrne, Colm Feore, Alan Bates, Ron Rifkin, CiarÃ¡n
    Hinds, Bruce McGill, Richard Marner, Philip Baker Hall",
    "country": “United States, Germany, Canada”,
    "date_added": " 7/1/2021",
    "release_year": 2002,
    "rating": “PG-13”,
    "duration": 124,
    "category": [“Adventure”, “Action”]}
    '''
    movies_list = dictionary_to_list(dictionary)

    n = len(movies_list)
 
    for i in range(n): 
        for j in range(i+1, n): #bubble sort
            if movies_list[i]['director'] > movies_list[j]['director']: #sort by director
                movies_list[i], movies_list[j] = movies_list[j], movies_list[i] #sort by director
            elif movies_list[i]['director'] == movies_list[j]['director'] and movies_list[i]['title'] > movies_list[j]['title']: #sort titles alphabtetically 
                movies_list[i], movies_list[j] = movies_list[j], movies_list[i]
                
    return movies_list

# Function 3 by Chrismon Charli

from T009_P1_load_data import movie_category_dictionary_list

def sort_movies_release_year(dictionary: dict) -> list:
    '''
    Returns a list with the movie data stored as a dictionary where the movies are sorted by their release_year in ascending order. Movies with the same
    release year will be sorted alphabetically by their title.
    
    >>> sort_movies_release_year(movie_dictionary)
    [{'title': 'One Last Shot', 'director': 'Mike Clattenburg', 'cast': 'Robb Wells, John Paul Tremblay, John Dunsworth', 'country': 'Canada', 'date_added': '24-Aug-18', 'release_year': '1998', 'rating': 'TV-MA', 'duration': '31 min', 'category': ['Comedies']}, {'title': 'Double Jeopardy', 'director': 'Bruce Beresford', 'cast': 'Tommy Lee Jones, Ashley Judd, Bruce Greenwood, Annabeth Gish, Roma Maffia, Jay Brazeau, Michael Gaston, Daniel Lapaine', 'country': 'United States, Germany, Canada', 'date_added': '01-Jul-20', 'release_year': '1999', 'rating': 'R', 'duration': '105 min', 'category': ['Thrillers']}, {'title': 'The Art of War', 'director': 'Christian Duguay', 'cast': 'Wesley Snipes, Anne Archer, Maury Chaykin, Marie Matiko, Cary-Hiroyuki Tagawa, Michael Biehn, Donald Sutherland, Liliana Komorowska, James Hong', 'country': 'United States, Canada', 'date_added': '01-Jul-20', 'release_year': '2000', 'rating': 'R', 'duration': '117 min', 'category': ['Adventure', 'Action']}, ...]
    '''
    #dictionary = movie_category_dictionary_list('netflix_movies.csv')
    result = dictionary_to_list(dictionary)

    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j].get('release_year') > result[j+1].get('release_year'):
                result[j], result[j+1] = result[j+1], result[j]
        for i in range(len(result)):
            for j in range(len(result) - i - 1):
                if result[j].get('release_year') == result[j+1].get('release_year') and result[j].get('title') > result[j+1].get('title'):
                    result[j], result[j+1] = result[j+1], result[j]            
    
    
                        
    return result

# Function 4 by K.C. Barnard

def sort_movies_ascending_rate(dictionary: dict) -> list:
    '''
    Returns a list with the movie data stored as a dictionary where the movies are sorted by their rating in ascending order (beginning with NR). Movies with the same
    rating will be sorted alphabetically by their title.
    
    >>> {"title": " Birth of the Dragon ",
    "director": "George Nolfi",
    " cast": “Billy Magnussen, Ron Yuan, Qu Jingjing, Terry Chen, Vanness Wu, Jin Xing, Philip Ng, Xia Yu, Yu Xia",
    "country": “China, Canada, United States”,
    "date_added": " 9/16/2021",
    "release_year": 2017,
    "rating": “PG-13”,
    "duration": 96,
    "category": [“Adventure”]}
    
    >>>{"title": " Insidious ",
    "director": "James Wan",
    " cast": “Patrick Wilson, Rose Byrne, Lin Shaye, Ty Simpkins, Barbara Hershey, Leigh Whannell, Angus Sampson, Andrew Astor, Joseph Bishara",
    "country": “United States, Canada”,
    "date_added": " 4/1/2021",
    "release_year": 2010,
    "rating": “PG-13”,
    "duration": 103,
    "category": [“Horror Movies”]}
    
    >>> {"title": " The Sum of All Fears ",
    "director": "Phil Alden Robinson",
    " cast": “Ben Affleck, Morgan Freeman, Bridget Moynahan, James Cromwell, Liev
    Schreiber, Michael Byrne, Colm Feore, Alan Bates, Ron Rifkin, CiarÃ¡n
    Hinds, Bruce McGill, Richard Marner, Philip Baker Hall",
    "country": “United States, Germany, Canada”,
    "date_added": " 7/1/2021",
    "release_year": 2002,
    "rating": “PG-13”,
    "duration": 124,
    "category": [“Adventure”, “Action”]}
    '''
    movies_list = dictionary_to_list(dictionary)

    n = len(movies_list)
 
    for i in range(n):
        for j in range(i+1, n):
            if movies_list[i]['rating'] > movies_list[j]['rating']:
                movies_list[i], movies_list[j] = movies_list[j], movies_list[i]

    for i in range(n):
        for j in range(i+1, n):
            if movies_list[i]['rating'] == movies_list[j]['rating'] and movies_list[i]['title'] > movies_list[j]['title']:
                movies_list[i], movies_list[j] = movies_list[j], movies_list[i]

    return movies_list

# Function 5 (Extra function that arose from refactoring)

def dictionary_to_list(dictionary: dict) -> list:
    '''
    Takes a dictionary of movies and turns it into a list. Also, creates a category key with the value of that being a list containing all the categories
    a movie falls under.
    '''
    result_list = []
    
    for category in dictionary:
        for movie in dictionary[category]:

            found_same_movie = False
            for result in result_list:
                if result['title'] == movie['title']:

                    if category not in result['category']:
                        result['category'].append(category)

                    found_same_movie = True
                    break
            
            if not found_same_movie:
                movie['category'] = [category]
                result_list.append(movie)

    return result_list 

# Main Script

#if __name__ == "__main__":

def check_equal(description: str, outcome, expected) -> bool:
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
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

# Function 1 test by Chrismon Charli

def test_sort_movies_title() -> int:
    '''
    Returns a list (contains no duplicates), where all the movies are sorted by their title alphabetically, and where each list element is a dictionary where all the movie data
    for each movie is stored.
   
    >>> test_sort_movies_title(test_dictionary1)
    [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min', 'category': ['Comedies', 'Romantic Movies']}, {'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min', 'category': ['Dramas']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}]
    '''   
    
    test_dictionary1 = {'Comedies': [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min'}], 'Romantic Movies': [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min'}], 'Dramas':[{'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min'}], 'Family Movies':[{'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 
    'rating': 'PG', 'duration': '91 min'}]}    

    total_tests_passed = 0
    
    test1 = check_equal("sort_movies_title(test_dictionary1)", sort_movies_title(test_dictionary1), [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min', 'category': ['Comedies', 'Romantic Movies']}, {'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min', 'category': ['Dramas']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}])
   
    if test1 == True:
        total_tests_passed += 1     
    return total_tests_passed

total_tests_passed = test_sort_movies_title() # The function call

print ("Total Tests passed for Function 1: ", total_tests_passed)
print ("Total Tests failed for Function 1: ", (1 - total_tests_passed))


# Function 2 test by K.C. Barnard

def test_sort_movies_director() -> int:
    '''
    The function returns a list with the movie data stored as a dictionary movie where the movie where the movies are sorted by their release_year in ascending order.
    
    >>> test_sort_movies_title(test_dictionary2)
    [{'title': "Molly's Game", 'director': 'Aaron Sorkin', 'cast': "Jessica Chastain, Idris Elba, Kevin Costner, Michael Cera, Jeremy Strong, Chris O'Dowd, J.C. MacKenzie, Brian d'Arcy James, Bill Camp, Graham Greene, Justin Kirk, Brian dâ€™Arcy James", 'country': 'China, Canada, United States', 'date_added': '01-Apr-20', 'release_year': '2017', 'rating': 'R', 'duration': '141 min', 'category': ['Dramas']}, {'title': 'Standoff', 'director': 'Adam Alleca', 'cast': 'Thomas Jane, Laurence Fishburne, Joanna Douglas, John Tench, Ted Atherton, Jim Watson, Ella Ballentine', 'country': 'Canada', 'date_added': '11-Dec-18', 'release_year': '2015', 'rating': 'R', 'duration': '86 min', 'category': ['Adventure', 'Action']}, {'title': 'For the Love of Spock', 'director': 'Adam Nimoy', 'cast': 'Leonard Nimoy, William Shatner, George Takei, Nichelle Nichols, Chris Pine, Zachary Quinto, Simon Pegg, Zoe Saldana, Jim Parsons, Jason Alexander, Neil deGrasse Tyson, J.J. Abrams', 'country': 'Canada, United States', 'date_added': '02-Dec-16', 'release_year': '2016', 'rating': 'TV-14', 'duration': '112 min', 'category': ['Documentaries']}, {'title': 'Gridlocked', 'director': 'Allan Ungar', 'cast': 'Dominic Purcell, Cody Hackman, Stephen Lang, Trish Stratus, Danny Glover, Vinnie Jones, Saul Rubinek, Richard Gunn, Steve Byers, James A. Woods', 'country': 'Canada', 'date_added': '14-Jul-16', 'release_year': '2015', 'rating': 'R', 'duration': '114 min', 'category': ['Adventure', 'Action']}]
    '''
    total_tests_passed = 0
   
    test_dictionary2 = {'Adventure': [{'title': 'Gridlocked', 'director': 'Allan Ungar', 'cast': 'Dominic Purcell, Cody Hackman, Stephen Lang, Trish Stratus, Danny Glover, Vinnie Jones, Saul Rubinek, Richard Gunn, Steve Byers, James A. Woods', 'country': 'Canada', 'date_added': '14-Jul-16', 'release_year': '2015', 'rating': 'R', 'duration': '114 min'}, {'title': 'Standoff', 'director': 'Adam Alleca', 'cast': 'Thomas Jane, Laurence Fishburne, Joanna Douglas, John Tench, Ted Atherton, Jim Watson, Ella Ballentine', 'country': 'Canada', 'date_added': '11-Dec-18', 'release_year': '2015', 'rating': 'R', 'duration': '86 min'}], 'Action': [{'title': 'Gridlocked', 'director': 'Allan Ungar', 'cast': 'Dominic Purcell, Cody Hackman, Stephen Lang, Trish Stratus, Danny Glover, Vinnie Jones, Saul Rubinek, Richard Gunn, Steve Byers, James A. Woods', 'country': 'Canada', 'date_added': '14-Jul-16', 'release_year': '2015', 'rating': 'R', 'duration': '114 min'}, {'title': 'Standoff', 'director': 'Adam Alleca', 'cast': 'Thomas Jane, Laurence Fishburne, Joanna Douglas, John Tench, Ted Atherton, Jim Watson, Ella Ballentine', 'country': 'Canada', 'date_added': '11-Dec-18', 'release_year': '2015', 'rating': 'R', 'duration': '86 min'}], 'Dramas': [{'title': "Molly's Game", 'director': 'Aaron Sorkin', 'cast': "Jessica Chastain, Idris Elba, Kevin Costner, Michael Cera, Jeremy Strong, Chris O'Dowd, J.C. MacKenzie, Brian d'Arcy James, Bill Camp, Graham Greene, Justin Kirk, Brian dâ€™Arcy James", 'country': 'China, Canada, United States', 'date_added': '01-Apr-20', 'release_year': '2017', 'rating': 'R', 'duration': '141 min'}], 'Documentaries': [{'title': 'For the Love of Spock', 'director': 'Adam Nimoy', 'cast': 'Leonard Nimoy, William Shatner, George Takei, Nichelle Nichols, Chris Pine, Zachary Quinto, Simon Pegg, Zoe Saldana, Jim Parsons, Jason Alexander, Neil deGrasse Tyson, J.J. Abrams', 'country': 'Canada, United States', 'date_added': '02-Dec-16', 'release_year': '2016', 'rating': 'TV-14', 'duration': '112 min'}]}
   
   
    test2 = check_equal("sort_movies_director(test_dictionary2)", sort_movies_director(test_dictionary2), [{'title': "Molly's Game", 'director': 'Aaron Sorkin', 'cast': "Jessica Chastain, Idris Elba, Kevin Costner, Michael Cera, Jeremy Strong, Chris O'Dowd, J.C. MacKenzie, Brian d'Arcy James, Bill Camp, Graham Greene, Justin Kirk, Brian dâ€™Arcy James", 'country': 'China, Canada, United States', 'date_added': '01-Apr-20', 'release_year': '2017', 'rating': 'R', 'duration': '141 min', 'category': ['Dramas']}, {'title': 'Standoff', 'director': 'Adam Alleca', 'cast': 'Thomas Jane, Laurence Fishburne, Joanna Douglas, John Tench, Ted Atherton, Jim Watson, Ella Ballentine', 'country': 'Canada', 'date_added': '11-Dec-18', 'release_year': '2015', 'rating': 'R', 'duration': '86 min', 'category': ['Adventure', 'Action']}, {'title': 'For the Love of Spock', 'director': 'Adam Nimoy', 'cast': 'Leonard Nimoy, William Shatner, George Takei, Nichelle Nichols, Chris Pine, Zachary Quinto, Simon Pegg, Zoe Saldana, Jim Parsons, Jason Alexander, Neil deGrasse Tyson, J.J. Abrams', 'country': 'Canada, United States', 'date_added': '02-Dec-16', 'release_year': '2016', 'rating': 'TV-14', 'duration': '112 min', 'category': ['Documentaries']}, {'title': 'Gridlocked', 'director': 'Allan Ungar', 'cast': 'Dominic Purcell, Cody Hackman, Stephen Lang, Trish Stratus, Danny Glover, Vinnie Jones, Saul Rubinek, Richard Gunn, Steve Byers, James A. Woods', 'country': 'Canada', 'date_added': '14-Jul-16', 'release_year': '2015', 'rating': 'R', 'duration': '114 min', 'category': ['Adventure', 'Action']}])

    if test2 == True:
        total_tests_passed += 1     
    return total_tests_passed

total_tests_passed = test_sort_movies_director() # The function call

print ("Total Tests passed for Function 2: ", total_tests_passed)
print ("Total Tests failed for Function 2: ", (1 - total_tests_passed))

# Function 3 test by Muhammed Nabeel Azard

def test_sort_movies_release_year() -> int:
    '''
    The function returns a list with the movie data stored as a dictionary movie where the movie where the movies are sorted by their release_year in ascending order.
    
    >>> test_sort_movies_title(test_dictionary3)
    [{'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min', 'category': ['Dramas']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}, {'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min', 'category': ['Comedies', 'Romantic Movies']}]
    '''
    total_tests_passed = 0
   
    test_dictionary3 = {'Comedies': [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min'}], 'Romantic Movies': [{'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min'}], 'Dramas':[{'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min'}], 'Family Movies':[{'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 
   'rating': 'PG', 'duration': '91 min'}]}
   
    test3 = check_equal("sort_movies_release_year(test_dictionary3)", sort_movies_release_year(test_dictionary3), [{'title': 'A Family Man', 'director': 'Mark Williams', 'cast': 'Gerard Butler, Gretchen Mol, Alison Brie, Willem Dafoe, Alfred Molina, Maxwell Jenkins, Anupam Kher, Dustin Milligan', 'country': 'Canada, United States', 'date_added': '15-Dec-19', 'release_year': '2016', 'rating': 'R', 'duration': '110 min', 'category': ['Dramas']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}, {'title': '#Roxy', 'director': 'Michael Kennedy', 'cast': 'Jake Short, Sarah Fisher, Booboo Stewart, Danny Trejo, Pippa Mackie, Jake Smith, Patricia Zentilli, Carter Thicke', 'country': 'Canada', 'date_added': '10-Apr-19', 'release_year': '2018', 'rating': 'TV-14', 'duration': '105 min', 'category': ['Comedies', 'Romantic Movies']}])
                        
    if test3 == True:
        total_tests_passed += 1     
    return total_tests_passed

total_tests_passed = test_sort_movies_release_year() # The function call

print ("Total Tests passed for Function 3: ", total_tests_passed)
print ("Total Tests failed for Function 3: ", (1 - total_tests_passed))

# Function 4 test by Spencer McKeown    

def test_sort_movies_ascending_rate() -> int:
    '''
    The function returns a list with the movie data stored as a dictionary movie where the movie where the movies are sorted by their release_year in ascending order.
    
    >>> test_sort_movies_title(test_dictionary4)
    [{'title': 'Adventures in Public School', 'director': 'Kyle Rideout', 'cast': 'Daniel Doheny, Judy Greer, Siobhan Williams, Russell Peters, Grace Park, Andrew McNee, Alex Barima, Andrew Herr, Eva Day, Josh Epstein', 'country': 'Canada, United States', 'date_added': '15-Aug-18', 'release_year': '2018', 'rating': 'NR', 'duration': '86 min', 'category': ['Comedies']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}, {'title': 'Elliot the Littlest Reindeer', 'director': 'Jennifer Westcott', 'cast': 'Josh Hutcherson, Samantha Bee, Martin Short, Morena Baccarin, Jeff Dunham, John Cleese', 'country': 'Canada', 'date_added': '01-Nov-20', 'release_year': '2018', 'rating': 'PG', 'duration': '90 min', 'category': ['Children', 'Family Movies']}]
    '''
    total_tests_passed = 0
   
    test_dictionary4 = {'Children': [{'title': 'Elliot the Littlest Reindeer', 'director': 'Jennifer Westcott', 'cast': 'Josh Hutcherson, Samantha Bee, Martin Short, Morena Baccarin, Jeff Dunham, John Cleese', 'country': 'Canada', 'date_added': '01-Nov-20', 'release_year': '2018', 'rating': 'PG', 'duration': '90 min'}], 'Comedies': [{'title': 'Adventures in Public School', 'director': 'Kyle Rideout', 'cast': 'Daniel Doheny, Judy Greer, Siobhan Williams, Russell Peters, Grace Park, Andrew McNee, Alex Barima, Andrew Herr, Eva Day, Josh Epstein', 'country': 'Canada, United States', 'date_added': '15-Aug-18', 'release_year': '2018', 'rating': 'NR', 'duration': '86 min'}], 'Family Movies': [{'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min'}, {'title': 'Elliot the Littlest Reindeer', 'director': 'Jennifer Westcott', 'cast': 'Josh Hutcherson, Samantha Bee, Martin Short, Morena Baccarin, Jeff Dunham, John Cleese', 'country': 'Canada', 'date_added': '01-Nov-20', 'release_year': '2018', 'rating': 'PG', 'duration': '90 min'}]}
   
    test4 = check_equal("sort_movies_ascending_rate(test_dictionary4)", sort_movies_ascending_rate(test_dictionary4), [{'title': 'Adventures in Public School', 'director': 'Kyle Rideout', 'cast': 'Daniel Doheny, Judy Greer, Siobhan Williams, Russell Peters, Grace Park, Andrew McNee, Alex Barima, Andrew Herr, Eva Day, Josh Epstein', 'country': 'Canada, United States', 'date_added': '15-Aug-18', 'release_year': '2018', 'rating': 'NR', 'duration': '86 min', 'category': ['Comedies']}, {'title': "A Witches' Ball", 'director': 'Justin G. Dyck', 'cast': 'Morgan Neundorf, Karen Slater, Loukia Ioannou, Will Ennis, Renee Stein, Keith Cooper, Paul Mason, Lisa Scenna, Ashley Rogan', 'country': 'Canada', 'date_added': '01-Oct-18', 'release_year': '2017', 'rating': 'PG', 'duration': '91 min', 'category': ['Family Movies']}, {'title': 'Elliot the Littlest Reindeer', 'director': 'Jennifer Westcott', 'cast': 'Josh Hutcherson, Samantha Bee, Martin Short, Morena Baccarin, Jeff Dunham, John Cleese', 'country': 'Canada', 'date_added': '01-Nov-20', 'release_year': '2018', 'rating': 'PG', 'duration': '90 min', 'category': ['Children', 'Family Movies']}])

    if test4 == True:
        total_tests_passed += 1     
    return total_tests_passed

total_tests_passed = test_sort_movies_ascending_rate() # The function call

print ("Total Tests passed for Function 4: ", total_tests_passed)
print ("Total Tests failed for Function 4: ", (1 - total_tests_passed))