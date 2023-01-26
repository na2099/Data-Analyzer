# ECOR 1042 Project Milestone 1 (Task 4)

#Muhammed Nabeel Azard 101152007 (Author of the code for case 1 made in the individual submission)
#K.C. Barnard 101223587 (Reviewed the code)
#Spencer-Nieman McKeown 101155117 (Reviewed the code)
#Chrismon Charli 101239397 (Reviewed the code)

# 17/06/2022: Version 1.0

import csv

def movie_category_dictionary_list (filename: str)-> dict:
    """
    Returns a dictionary where the movie categories are the keys, and the values
    associated with each key is a list containing all the movies and their information specific to each category. Precondition: filename must be a .csv file
    
    >>> movie_category_dictionary_list("netflix_movies.csv")
    movie_dictionary = {
    " Adventure":[ {"title": "The Sum of All Fears",
                    "director": "Phil Alden Robinson",
                    "cast": “Ben Affleck, Morgan Freeman, Bridget Moynahan, James Cromwell, Liev Schreiber, Michael Byrne, Colm Feore, Alan Bates, Ron Rifkin, CiarÃ¡n Hinds, Bruce McGill, Richard Marner, Philip Baker Hall",
                    "country": “United States, Germany, Canada”,
                    "date_added": " 7/1/2021",
                    "release_year": 2002,
                    "rating": “PG-13”,
                    "duration": 124,
                    },
            {another element},
                    …
                    ],
    "Children":[ {"title": " The Magic School Bus Rides Again In the Zone",
                  "director": " Richard Weston",
                  "cast": “Mikaela Blake, Gabby Clarke, Roman Lutterotti, Leke Maceda-Rustecki, Matthew Mucci, Lynsey Pham, Kaden Stephen, Lights",
                  "country": “Canada”,
                  "date_added": " 12/26/2020",
                  "release_year": 2020,
                  "rating": “TV-Y”,
                  "duration": 46},
                  {another element},
                  …],
    ….
    }
    """
    file = open(filename)
    csvreader = csv.reader(file)
    header = next(csvreader)
    movie_dictionary = {}
    for row in csvreader:
        key = row[8]
        if not (row[8] in movie_dictionary):
            movie_dictionary[key] = []
            
        movie = {}
        
        movie[header[0]] = row[0]
        movie[header[1]] = row[1]
        movie[header[2]] = row[2]
        movie[header[3]] = row[3] 
        movie[header[4]] = row[4] 
        movie[header[5]] = row[5]   
        movie[header[6]] = row[6]
        movie[header[7]] = row[7]
        movie_dictionary[key].append(movie)
    file.close()
    x = set()
    for category in movie_dictionary.keys():
        for movie in movie_dictionary[category]:
            t = (movie["title"], category)
            if t not in x:
                x.add(t)
            else:
                movie_dictionary[category].remove(movie)
    #print(len(x))
    return movie_dictionary
        
#movie_dictionary = movie_category_dictionary_list("netflix_movies.csv")
#print(movie_dictionary)