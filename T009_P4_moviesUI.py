# ECOR 1042 Milestone 2 (Lab 2, Task 2)

# Muhammed Nabeel Azard, 101152007
# K.C. Barnard, 101223587
# Spencer McKeown, 101155117
# Chrismon Charli, 101239397

# 17/06/2022: Version 1.0


#from T009_P1_load_data import movie_category_dictionary_list
from T009_P5_load_data import movie_category_dictionary_list
from T009_P2_add_remove_search_dataset import *
from T009_P3_sorting_fun import *

given_commands = "The available commands are: \n1- L)oad data\n2- A)dd movie\n3- R)emove movie\n4- G)et movies\n       -  T)itle  R)ate  D)irector  C)ast  Ca)tegory\n5- GCT) Get all Categories for movie Title\n6- S)ort movies\n       -  T)itle  R)ate  D)irector  RE)lease year\n7- Q)uit\n\nPlease type your command: "

movies_dict = movie_category_dictionary_list("netflix_movies.csv")

valid_commands = ["L", "G", "GCT", "Q"]
movies_dataset = None

def command1() -> dict:
    load_input = input("Please enter a file: ")
    #if filename == 'netflix_movies.csv':
        #movie_dictionary = movie_category_dictionary_list(filename)
        #print(movie_dictionary)
        #file_loaded = True
    #else:
        #print("File not found")        
    
    movies_dataset = movie_category_dictionary_list(load_input)
    print(movies_dataset)
    return movies_dataset

def command2():
    input_title = input("Please provide a title for the movie you want to add: ")
    input_director = input("Please provide an director for the movie you want to add: ")
    input_cast = input("Please provide a cast for the movie you want to add: ")
    input_country = input("Please provide a country for the movie you want to add: ")
    input_date_added = input("Please provide a date added for the movie you want to add: ")
    input_release_year = input("Please provide a relase year for the movie you want to add: ")
    input_rating = input("Please provide a rating for the movie you want to add: ")
    input_duration = input("Please provide a duration for the movie you want to add: ")
    input_category = input("Please provide a category for the movie you want to add: ")

    new_movie = (input_title, input_director, input_cast, input_country, input_date_added, input_release_year, input_rating, input_duration, input_category, )
    add_movie(movies_dataset, new_movie)

def command3 ():
    input_title = input ("Please provide the title of the movie you wish to remove: ")
    input_category = input("Please provide the category of the movie you wish to remove: ")
    remove_movie(movies_dataset, input_title, input_category)

def command4():
    subcommand_input = input("Please provide a sub-command: ")
    subcommand_input = subcommand_input.lower()
    
    if subcommand_input == "t":
        input_title = input("Please provide the title of the movies you wish to find: ")
        get_movies_by_title(movies_dataset, str(input_title))
        
    elif subcommand_input == "r":
        input_rate = input("Please provide the rate of the movies you wish to find: ")
        get_movie_by_rate(movies_dataset, str(input_rate))
        
    elif subcommand_input == "d":
        input_director = input("Please provide the name of the director you wish to find movies for: ")
        get_movies_by_director(movies_dataset, str(input_director))
        
    elif subcommand_input == "c":
        input_cast = input("Please provide the Cast of the movies you wish to find: ")
        get_movies_by_cast(movies_dataset, str(input_cast))
        
    elif subcommand_input == "ca":
        input_category = input("Please provide the Category of the movie you wish to find: ")
        get_movies_by_category(movies_dataset, input_category)
    else:
        print("That was not a valid command")

def command5():
    input_title = input("Please provide the title of the movie you wish to see the categories for: ")
    get_all_categories_for_movie_title(movies_dataset, input_title)

def command6():
    subcommand_input = input("Please provide a subcommand: ")
    subcommand_input = subcommand_input.lower()

    if subcommand_input == "t":
        print(sort_movies_title(movies_dataset))
    elif subcommand_input == "r":
        print(sort_movies_ascending_rate(movies_dataset))
    elif subcommand_input == "d":
        print(sort_movies_director(movies_dataset))
    elif subcommand_input == "re":
        print(sort_movies_release_year(movies_dataset))
    else:
        print("No such command")

while True:
            
    command = input(given_commands)
    command = command.upper()
               
    # command 7
    if command == "Q":
        break
            
    # command 1
    if command == "L":
        movies_dataset = command1()  # we changed this line    
       
    elif movies_dataset is not None:
        # command 2
        if command == "A":
            command2()

        # command 3
        elif command == "R":
            command3()        
    
        # command 4
        elif command == "G":
            command4 ()
            
        # command 5
        elif command == "GCT":
            command5 ()
                    
        # command 6
        elif command == "S":
            command6 ()   
            
    elif command not in valid_commands:
        print("No such command")
                
    elif movies_dataset is None:
        print("No file loaded")