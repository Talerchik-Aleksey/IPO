#   MODEL
from collections import Counter # https://pythonworld.ru/moduli/modul-collections.html

def hash_validator_main(): 
    error_check_dist = {
            'tag not start in #': 0,
            'more then 1 elmement in tag': 0,
            'more then one tag': 0,
            'more then five tags': 0,
            'one tag have more then 20 elemnts': 0
        } 
    return error_check_dist
    
def input_hash_tags(): #    INPUT
    hash_tags = input().split()
    check_for_mistake(hash_tags, hash_validator_main())
    
def check_for_mistake(hash_tags, error_check_dist): #  CHECK FOR MISTAKE
    sort_how_much = Counter(hash_tags) # from collections import Counter
    sort_how_much.most_common() # sorted str

    for key in hash_tags:
        flag_error_check = False # flag for error_check_list
        
        if '#' not in key: 
            error_check_dist['tag not start in #'] += 1
            flag_error_check = True
        if (len(key) == 1) and ('#' in key): # if key == '#'
            error_check_dist['more then 1 elmement in tag'] += 1
            flag_error_check = True
        if sort_how_much[key] != 1: # if for search key = {another key}
            error_check_dist['more then one tag'] += 1
            flag_error_check = True
        if len(hash_tags) > 5: # less then five tags
            error_check_dist['more then five tags'] = 1
            flag_error_check = True
        if len(key) > 20: # one key must be less than 20 elements
            error_check_dist['one tag have more then 20 elemnts'] += 1
            flag_error_check = True

    #   OUTPUT
    return print(error_check_dist) if flag_error_check else print('+') # if {true} print error_check_dist, else print('+')
    
input_hash_tags() # start main function
