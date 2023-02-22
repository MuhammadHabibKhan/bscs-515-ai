# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five

old_list = ['TENET', 'OPPENHEIMER', 'INTERSTELLAR', 'CARS']
new_list = [movies.lower() for movies in old_list if len(movies) > 5]
print(new_list)