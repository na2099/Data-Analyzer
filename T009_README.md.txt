T099 Data Analyzer Version 1.0 17/06/2022

The project can be reached at:
Voice: 613-262-2822
Email: nabeelazard@cmail.carleton.ca

Description:
------------

- This project contains an interactive program that prompts a user to change or manipulate several movies in a dictionary containing a list of movies
  sorted by their category. First and foremost, the file chosen by the user must be loaded using the load command when prompted. Once the file is
  successfully loaded, the user can add movies, remove movies, get movies by title, rate, director, cast or category, get all categories for a movie title, and sort 
  movies by title, rate, director, or release year. After the execution of every command, the result of that command will be displayed. The user will be
  prompted to enter a command until they decide to quit the program.

- The project is made up of several files. These are:
  T009_P5_load_data.py                           A single Python script
  T009_P4_moviesUI.py                            A single Python script
  T009_P3_sorting_fun.py                         A single Python script
  T009_P2_add_remove_search_dataset.py           A single Python script

that allows a user to enter a CSV file. Several commands
  are presented to the user where they

Installation:
-------------

Python 3.7.4 or later must be installed
Only built-in Python modules are used. No external modules must be loaded.

Usage:
------

> python T009_data_analyzer.py

When promted, load a file using "L" or "l". Then, enter a command of your choice from the list of commands. For some
commands, a sub-command would also have to be entered. To quit the program, enter "Q" or "q". If you enter something that is
not in the given list of commands, "No such command will be displayed".

Credits:
----------

Muhammed Nabeel Azard (101152007) - Recorded as author for movie_category_dictionary_list, get_movies_by_category, get_movie_by_rate, sort_movies_title, dictionary_to_list, Case 4 (sort movies and its sub-commands), testing for get_movies_by_category; get_movie_by_rate, testing for sort_movies_ release_year 

K.C. Barnard - Recorded as author for movie_dictionary_director_list, add_movie, remove_movie, sort_movies_ascending_rate, dictionary_to_list, Case 3 (get movies by cast and category and get all categories for movie title), testing for add_movie; remove_movie, testing for sort_movies_director

Chrismon Charli - Recorded as author for movie_list_dictionary, get_movies_by_title, get_movies_by_director, sort_movies_ release_year, dictionary_to_list, Case 2 (get movies by title, rate, and director), testing for get_movies_by_title; get_movies_by_director, testing for sort_movies_title

Spencer McKeown - Recorded as author for movie_tuple_dictionary, get_movies_by_cast, get_all_categories_for_movie_title, sort_movies_director, dictionary_to_list, Case 1 (add and remove movie), testing for get_movies_by_cast; get_all_categories_for_movie_title, testing for sort_movies_ascending_rate

Copyright 2022 Muhammed Nabeel Azard, K.C. Barnard, Chrismon Charli, Spencer McKeown 